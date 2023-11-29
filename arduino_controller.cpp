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

void	loop()
{
	
  delay(1000);
}