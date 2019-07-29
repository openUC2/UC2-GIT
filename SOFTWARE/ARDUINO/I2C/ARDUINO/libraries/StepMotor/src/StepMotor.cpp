#include "Arduino.h"
#include "StepMotor.h"


//Konstruktur mit Zuordnung zu jeweiligen Arduino-Pins
StepMotor::StepMotor(int ino_OUT1, int ino_OUT2, int ino_OUT3, int ino_OUT4)
{
	Init(ino_OUT1, ino_OUT2, ino_OUT3, ino_OUT4);
}

StepMotor::StepMotor(int ino_OUT1, int ino_OUT2, int ino_OUT3, int ino_OUT4, int reqSpeed)
{
	SetSpeed(reqSpeed);
	Init(ino_OUT1, ino_OUT2, ino_OUT3, ino_OUT4);
}

void StepMotor::Init(int ino_OUT1, int ino_OUT2, int ino_OUT3, int ino_OUT4)
{
	SetNumberOfSteps(4096);
	SetSpeed(12);

	this->phase = 0;
	this->direction = 0;

	this->motor_IN1 = ino_OUT1;
	this->motor_IN2 = ino_OUT2;
	this->motor_IN3 = ino_OUT3;
	this->motor_IN4 = ino_OUT4;

	pinMode(this->motor_IN1, OUTPUT);
	pinMode(this->motor_IN2, OUTPUT);
	pinMode(this->motor_IN3, OUTPUT);
	pinMode(this->motor_IN4, OUTPUT);

}

void StepMotor::SetNumberOfSteps(int reqStepsFullrot)
{
	int minSteps = 4; //to avoid division by zero and instability in calculation of step_delay
	if (reqStepsFullrot >= minSteps)
		this->nStepsFullrot = reqStepsFullrot;
}

void StepMotor::SetSpeed(int reqSpeed)
{
	int minSpeed = 1;
	if (reqSpeed >= minSpeed) {
		this->step_delay = 60L * 1000L / this->nStepsFullrot / reqSpeed;
		if (this->step_delay < 1) this->step_delay = 1;  //28BYJ-Motor-Driver does not support delays below 1ms
	}
}

void StepMotor::Move(int nsteps) //Motorcontrol. Sign of nsteps determines direction.
{
	this->direction = nsteps < 1 ? -1 : 1;
	nsteps *= this->direction;

	for (int i = 0; i < nsteps; i++)
	{
		Step(phase);
		IncrementPhase(this->direction);
		delay(step_delay);
	}
}

void StepMotor::Step(int reqPhase)
{
	digitalWrite(motor_IN1, phases1[reqPhase]); 
	digitalWrite(motor_IN2, phases2[reqPhase]);
	digitalWrite(motor_IN3, phases3[reqPhase]);
	digitalWrite(motor_IN4, phases4[reqPhase]);
}

void StepMotor::IncrementPhase(int rotationDirection)
{
	this->phase += 8;
	this->phase += rotationDirection;
	this->phase %= 8;
}
