#include <Stepper.h>

const int step_360 = 2058;// 360 number of steps per/rev
const int nsteps = 1000;
// initialize the stepper library on pins 2-5 n 8-11
Stepper stepperX(step_360, 2, 4, 3, 5);
Stepper stepperY(step_360, 6, 8, 7, 9);
Stepper stepperZ(step_360, 10, 12, 11, 13);

void setup()
{
  // set the speed at 60 rpm:
  stepperX.setSpeed(8);//left
  stepperY.setSpeed(8);//right
  stepperZ.setSpeed(8);//right
  // initialize the serial port:
  Serial.begin(9600);
}
void loop()
{
  // run around..
  Serial.println("Run X+");
  run_X(1000);
  delay(1000);
  Serial.println("Run X-");
  run_X(-1000);
  delay(1000);

  Serial.println("Run Y");
  run_Y(1000);
  delay(1000);
  Serial.println("Run Y-");
  run_Y(-1000);
  delay(1000);

  Serial.println("Run Z");
  run_Z(1000);
  delay(1000);
  Serial.println("Run Z-");
  run_Z(-1000);
  delay(1000);
  // step one revolution  in one direction:

}


void run_X(int nsteps) {
  // Runn two motors to move the back/forth
  int mydir = -1;
  if (nsteps > 0){mydir = 1;}

  for (int steps = 0; steps < abs(nsteps); steps++)
  {
    stepperX.step(mydir);
    stepperY.step(mydir);
  }
}

void run_Y(int nsteps) {
  // Runn two motors to move the left/right
  int mydir = -1;
  if (nsteps > 0){mydir = 1;}
  
  for (int steps = 0; steps < abs(nsteps); steps++)
  {
    stepperY.step(mydir);
    stepperZ.step(mydir);
  }
}


void run_Z(int nsteps) {
  // Runn all motors to move the stage up/down
  int mydir = -1;
  if (nsteps > 0){mydir = 1;}

  for (int steps = 0; steps < abs(nsteps); steps++)
  {
    stepperX.step(mydir);
    stepperY.step(mydir);
    stepperZ.step(mydir);
  }
}
