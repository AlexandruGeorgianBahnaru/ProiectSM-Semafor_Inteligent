from machine import UART, Pin
  from time import sleep
  import _thread

  # Define the GPIO pins for the LEDs
  red_led = Pin(15, Pin.OUT)
  green_led = Pin(13, Pin.OUT)
  green_led1 = Pin(20, Pin.OUT)
  red_led1 = Pin(18, Pin.OUT)

  # Initialize the UART for Bluetooth communication
  uart = UART(0, baudrate=9600)

  # Initialize states
  states = ["g1r1", "r1r1", "g0r0", "r1r1"]
  current_state_index = 0
  running = False

  def update_lights():
      global current_state_index
      state = states[current_state_index]

      if state == "r1r1":
          red_led.value(1)
          green_led.value(0)
          red_led1.value(1)
          green_led1.value(0)
      elif state == "g1r1":
          red_led.value(0)
          green_led.value(1)
          red_led1.value(1)
          green_led1.value(0)
      elif state == "g0r0":
          red_led.value(1)
          green_led.value(0)
          red_led1.value(0)
          green_led1.value(1)
          
   def cycle_states():
      global running
      while running:
          next_state()
          sleep(4)  # Adjust the sleep time to control the duration of each state

  def control_lights(val):
      global running
      print(f"Control lights with val: {val}")
      if 'start' in val:
          if not running:
              running = True
              _thread.start_new_thread(cycle_states, ())
          uart.write("Semafor start\n")
      elif 'stop' in val:
          running = False
          current_state_index = 0
          update_lights()
          uart.write("stop\n")
          sleep(4)


buffer = ""
while True:
    if uart.any():
        msg = uart.read(1).decode('utf-8')  # Read one byte at a time
        if msg == '\n':  # End of message
            buffer = buffer.strip()  # Remove any surrounding whitespace
            if buffer:
                print(f"Received message: {buffer}")  # Debugging statement
                uart.write(buffer + "\n")  # Echo the received message for debugging

                if 'start' in buffer:
                    print("Start command received")  # Debugging statement
                    control_lights(buffer)
                elif 'stop' in buffer:
                    print("Stop command received")  # Debugging statement
                    control_lights(buffer)
                    uart.write("val 0\n")
            buffer = ""  # Clear the buffer for the next message
        else:
            buffer += msg  # Append byte to buffer
    else:
        sleep(0.1)  # Add a small delay to avoid busy-waiting
