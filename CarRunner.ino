/*
Author: Navjot Saroa

This is the arduino bit of the code that will run the car stuff.
For now it is just a servo and a stepper motor messing around.
There is a problem that the stepper motor does not turn backwards with this code but I 
am happy with the way it is working so I won't fret about it.
*/

#include <Servo.h>
#include <Stepper.h>
#define STEPS 100

Servo servo;
int angle = 10;
Stepper stepper(STEPS, 7, 6, 5, 4);

int previous = 0;

void setup() {
  // Initialize serial communication
  Serial.begin(9600);

  servo.attach(8);
  servo.write(angle);
  stepper.setSpeed(60);
}

void loop() {
  // Check if data is available to read

  if (Serial.available() > 0) {
    // Read the incoming integer
    int data = Serial.parseInt();
    
    switch(data) {
      case 0:
        for(angle = 10; angle < 100; angle++)  
        {                                  
          servo.write(angle);               
          delay(15);                   
        } 
        break;

      case 1:
        for(angle = 100; angle > 10; angle--)    
        {                                
          servo.write(angle);           
          delay(15);       
        } 
        break;

      case 2:
        int val = analogRead(0);
        stepper.step(val - previous);
        previous = val;
        break;

      case 3:
        val = analogRead(0);
        stepper.step(val + previous);
        previous = val;
        break;
    }
    delay(1000);
  }


}