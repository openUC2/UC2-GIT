#include <StepMotor.h>

StepMotor STP_X = StepMotor(6, 7, 8, 9, 9600);
StepMotor STP_Y = StepMotor(10,11,12,13, 9600);

void setup()
{
  STP_X.SetSpeed(8);
  STP_Y.SetSpeed(8);
}
void loop()
{
  STP_X.Move(800);
  delay(100);
  STP_X.Move(-800);
  delay(100);

  STP_Y.Move(800);
  delay(100);
  STP_Y.Move(-800);
  delay(100);
}
