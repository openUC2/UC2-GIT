/*
 * Unipolar stepper motor speed and direction control with Arduino
 *   and joystick
 * This is a free software with NO WARRANTY.
 * https://simple-circuit.com/
 */
 
// include Arduino stepper motor library
#include <Stepper.h>
 
// define number of steps per revolution
#define STEPS 32
 
// define stepper motor control pins
#define INa1  2
#define INa2  4
#define INa3  3
#define INa4  5

#define INb1  6
#define INb2  8
#define INb3  7
#define INb4  9

// initialize stepper library
Stepper stepperA(STEPS, INa1, INa2, INa3, INa4);
Stepper stepperB(STEPS, INb1, INb2, INb3, INb4);
 
// joystick pot output is connected to Arduino A0
#define joystickA  A0
#define joystickB  A1
 
void setup()
{
  Serial.begin(19200);
  Serial.println("START");
}
 
void loop()
{
  // read analog value from the potentiometer
  int valA = analogRead(joystickA);
  int valB = analogRead(joystickB);

  // FOR Z-Stage 
  // if the joystic is in the middle ===> stop the motor
  if(  (valA > 500) && (valA < 523) ) 
  {
    digitalWrite(INa1, LOW);
    digitalWrite(INa2, LOW);
    digitalWrite(INa3, LOW);
    digitalWrite(INa4, LOW);

  }
  else
  {
    // move the motor in the first direction
    while (valA >= 523)
    {
      // map the speed between 5 and 500 rpm
      int speed_ = map(valA, 523, 1023, 5, 500);
      // set motor speed
      stepperA.setSpeed(speed_);
 
      // move the motor (1 step)
      stepperA.step(1);
 
      valA = analogRead(joystickA);
    }
 
    // move the motor in the other direction
    while (valA <= 500)
    {
      // map the speed between 5 and 500 rpm
      int speed_ = map(valA, 500, 0, 5, 500);
      // set motor speed
      stepperA.setSpeed(speed_);
 
      // move the motor (1 step)
      stepperA.step(-1);
 
      valA = analogRead(joystickA);
    }
 
  }



   // FOR S-Stage 
  // if the joystic is in the middle ===> stop the motor
  if(  (valB > 500) && (valB < 523) ) 
  {
    digitalWrite(INb1, LOW);
    digitalWrite(INb2, LOW);
    digitalWrite(INb3, LOW);
    digitalWrite(INb4, LOW);

  }
  else
  {
    // move the motor in the first direction
    while (valB >= 523)
    {
      // map the speed between 5 and 500 rpm
      int speed_ = map(valB, 523, 1023, 5, 500);
      // set motor speed
      stepperB.setSpeed(speed_);
 
      // move the motor (1 step)
      stepperB.step(1);
 
      valB = analogRead(joystickB);
    }
 
    // move the motor in the other direction
    while (valB <= 500)
    {
      // map the speed between 5 and 500 rpm
      int speed_ = map(valB, 500, 0, 5, 500);
      // set motor speed
      stepperB.setSpeed(speed_);
 
      // move the motor (1 step)
      stepperB.step(-1);
 
      valB = analogRead(joystickB);
    }
 
  }

}
