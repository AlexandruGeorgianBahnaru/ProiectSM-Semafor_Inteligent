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
