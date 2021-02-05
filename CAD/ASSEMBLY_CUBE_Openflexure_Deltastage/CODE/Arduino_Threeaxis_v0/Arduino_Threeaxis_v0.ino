#include <Stepper.h>

const int step_360 = 2058;// 360 number of steps per/rev  
const int nsteps = 10000;                            
// initialize the stepper library on pins 2-5 n 8-11
Stepper stepperZ(step_360, 2, 4, 3, 5);
Stepper stepperY(step_360,6,8,7,9);      
Stepper stepperX(step_360,10,12,11,13);      

int myspeed = 10;
void setup()
{
 // set the speed at 60 rpm:
 stepperZ.setSpeed(myspeed);//left
 stepperY.setSpeed(myspeed);//right
 stepperX.setSpeed(myspeed);//right
 // initialize the serial port:
 Serial.begin(9600);
}
void loop()
{

// step one revolution  in one direction:
 Serial.println("clockwise");
 


 for(int s=0; s<nsteps; s++)
{
  stepperZ.step(-1);
  stepperY.step(-1);
  stepperX.step(-1);
}
 for(int s=0; s<nsteps; s++)
{
  stepperZ.step(1);
  stepperY.step(1);
  stepperX.step(1);
}
}
