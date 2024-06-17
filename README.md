# Proiect-semafor
# Universitatea Tehnică „Gheorghe Asachi” Iași
# Facultatea de Automatică și Calculatoare Iași
# Sisteme cu microprocesoare
Contribuitori
  - Archir Maria-Mirabela (1307B) -
  - Bahnaru Alexandru-Georgian (1307B) -
  - Bulgaru Vlad-Andrei (1307B) - 



# Descrierea proiectului

Proiectul prezintă un sistem de control al unui semafor inteligent, care combină elemente de software și hardware pentru a gestiona iluminarea LED-urilor și a primi comenzi din exterior. Sistemul utilizează un microcontroller Raspberry Pi, care rulează un cod Python pentru a controla LED-urile și a comunica cu exteriorul prin intermediul unui modul Bluetooth.

În ceea ce privește partea de hardware, sistemul utilizează mai multe componente, inclusiv LED-uri bi-color (roșu și verde), un modul Bluetooth pentru comunicarea cu exteriorul și un microcontroller Raspberry Pi care gestionează întregul sistem.

Partea de software, scrisă în Python, gestionează iluminarea LED-urilor, controlul LED-urilor și primirea comenzilor prin Bluetooth. Sistemul permite utilizatorilor să trimită comenzi textuale de la telefon către Raspberry Pi prin conexiunea Bluetooth, pentru a controla funcționalitatea semaforului.

În general, proiectul demonstrează cum se poate combina software-ul cu hardware-ul pentru a crea un sistem inteligent și interactiv, care poate fi utilizat în diverse aplicații, cum ar fi simularea unui semafor de trafic sau controlul unui sistem de iluminat.

# Arhitectura sistemului

Sistemul este construit pe baza a două componente principale: hardware și software.

# Componentele hardware folosite în acest proiect sunt:

Breadboard
Raspberry Pi Pico H (microcontroller)
Modulul Bluetooth HC-05
LED-uri (roșu, galben și verde)
Senzor infraroșu TCRT5000
Cablu de alimentare și fire de conexiune
Rezistențe de 330/220 Ω, 1kΩ

# Componentele software folosite în acest proiect sunt:

Codul Python care rulează pe Raspberry Pi Pico H
Funcționalități software, cum ar fi configurarea pinilor GPIO, controlul semaforului și comunicarea Bluetooth

# Software necesar:

Programul Thonny pentru editarea codului și testare, disponibil pentru descărcare la link-ul acesta: https://thonny.org/

Aplicația pentru Android, Serial Bluetooth Terminal, pentru a putea primi și transmite mesaje de la și spre semafor: https://play.google.com/store/apps/details?id=de.kai_morich.serial_bluetooth_terminal

# Funcționalitatea

Sistemul inteligent și interactiv a fost creat pentru a simula funcționalitatea unui semafor real. Funcționalitatea sistemului este împărțită în trei componente principale: controlul LED-urilor, comunicarea Bluetooth și controlul senzorului infraroșu.

Controlul LED-urilor: Sistemul utilizează trei LED-uri bi-color (roșu, galben și verde) care sunt controlate de microcontrollerul Raspberry Pi. LED-urile sunt conectate la pini GPIO diferiți pentru a controla starea lor. Funcția update_lights() gestionează starea LED-urilor în funcție de starea curentă a semaforului.

Comunicarea Bluetooth: Sistemul utilizează un modul Bluetooth pentru a primi comenzi externe. Comenzile sunt primite prin intermediul aplicației Serial Bluetooth Terminal și sunt procesate de microcontrollerul Raspberry Pi. Funcția control_lights() gestionează comenzile primite și controlează pornirea și oprirea semaforului.



Configurare pini GPIO:
    
    LED-uri:
  	-LED roșu:
	  	Anod: Conectat la rezistență de 330Ω, apoi la GPIO 15 al Raspberry Pi	
	  	Catod: Conectat la GND
  	LED rosu 2:
	  	Anod: Conectat la rezistență de 330Ω, apoi la GPIO 18 al Raspberry Pi
	  	Catod: Conectat la GND
	  LED verde:
	  	Anod: Conectat la rezistență de 330Ω, apoi la GPIO 13 al Raspberry Pi
  		Catod: Conectat la GND
  	LED verde 2:
	   	Anod: Conectat la rezistență de 330Ω, apoi la GPIO 20 al Raspberry Pi
	  	Catod: Conectat la GND
    Modulul Bluetooth HC-05:
	  	VCC: Conectat la VBUS al Raspberry Pi
	  	GND: Conectat la GND al Raspberry Pi
	 	TXD: Conectat la GPIO 1 al Raspberry Pi
	  	RXD: Conectat la GPIO 0 al Raspberry Pi
