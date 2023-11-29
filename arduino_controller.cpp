#include <Arduino.h>
#include <Servo.h>

#define LED1 3
#define LED2 5
#define LED3 9
#define SERVO 6
#define POT A0
#define HEARTBEAT 13

Servo	servo1;


void	setup() {
	Serial.begin(9600);
	pinMode(LED1, OUTPUT);
	pinMode(LED2, OUTPUT);
	pinMode(LED3, OUTPUT);
	pinMode(HEARTBEAT, OUTPUT);
	pinMode(POT, INPUT);
	servo1.attach(SERVO);
}


int	check_header(byte *command)
{
	// undefined = x00, potent = x01, servo = x02, heartbeat = x03, led = x04
	if (command[0] == 0x00)
		return NULL;
	else if (command[0] == 0x01)
		return (POT);
	else if (command[0] == 0x02)
		return (SERVO);
	else if (command[0] == 0x03)
		return (HEARTBEAT);
	else if (command[0] == 0x04)
		if (command[2] == 0x01)
			return (LED1);
		else if (command[2] == 0x02)
			return (LED2);
		else if (command[2] == 0x03)
			return (LED3);
	else
		return ("undefined");
}


void	loop()
{
	int	potentiometerValue = analogRead(POT);
	Serial.println(potentiometerValue);
	if (Serial.available()) 
	{
		// receive as byte array
		byte *command = Serial.readBytes();
		// check header
		int header = check_header(command);
		// in case led
		if (header == LED1 || header == LED2 || header == LED3)
		{
			digitalWrite(header, digitalRead(header) == HIGH ? LOW : HIGH);
		}
		// in case servo
		else if (header == SERVO)
		{
			int servoAngle = command[2];
			servo1.write(servoAngle);
		}
		// in case heartbeat
		else if (header == HEARTBEAT)
		{
			digitalWrite(HEARTBEAT, digitalRead(HEARTBEAT) == HIGH ? LOW : HIGH);
		}
			
	}	
}
