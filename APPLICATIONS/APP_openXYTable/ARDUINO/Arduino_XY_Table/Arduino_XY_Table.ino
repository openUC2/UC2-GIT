#include <AccelStepper.h>
#define HALFSTEP 8

// motor pins
#define motorPin1  2     // IN1 on the ULN2003 driver 1
#define motorPin2  3     // IN2 on the ULN2003 driver 1
#define motorPin3  4     // IN3 on the ULN2003 driver 1
#define motorPin4  5     // IN4 on the ULN2003 driver 1

#define motorPin5  6     // IN1 on the ULN2003 driver 2
#define motorPin6  7     // IN2 on the ULN2003 driver 2
#define motorPin7  8    // IN3 on the ULN2003 driver 2
#define motorPin8  9    // IN4 on the ULN2003 driver 2

// Initialize with pin sequence IN1-IN3-IN2-IN4 for using the AccelStepper with 28BYJ-48
AccelStepper stepper1(HALFSTEP, motorPin1, motorPin3, motorPin2, motorPin4);
AccelStepper stepper2(HALFSTEP, motorPin5, motorPin7, motorPin6, motorPin8);

// variables
int turnSteps = 2100; // number of steps for a 90 degree turn
int lineSteps = -6600; //number of steps to drive straight
int stepperSpeed = 1000; //speed of the stepper (steps per second)
int steps1 = 0; // keep track of the step count for motor 1
int steps2 = 0; // keep track of the step count for motor 2

boolean turn1 = false; //keep track if we are turning or going straight next
boolean turn2 = false; //keep track if we are turning or going straight next

void setup() {
  delay(3000); //sime time to put the robot down after swithing it on

  stepper1.setMaxSpeed(2000.0);
  stepper1.move(1);  // I found this necessary
  stepper1.setSpeed(stepperSpeed);

  stepper2.setMaxSpeed(2000.0);
  stepper2.move(-1);  // I found this necessary
  stepper2.setSpeed(stepperSpeed);

}
void loop() {

  if (steps1 == 0) {
    int target = 0;
    if (turn1 == true) {
      target = turnSteps;
    }

    else {
      target = lineSteps;
    }

    stepper1.move(target);
    stepper1.setSpeed(stepperSpeed);
    turn1 = !turn1;
  }

  if (steps2 == 0) {
    int target = 0;
    if (turn2 == true) {
      target = turnSteps;
    }

    else {
      target = -lineSteps;
    }

    stepper2.move(target);
    stepper2.setSpeed(stepperSpeed);
    turn2 = !turn2;
  }

  steps1 = stepper1.distanceToGo();
  steps2 = stepper2.distanceToGo();

  stepper1.runSpeedToPosition();
  stepper2.runSpeedToPosition();
}
