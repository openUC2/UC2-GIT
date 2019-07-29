#ifndef StepMotor_h
#define StepMotor_h

class StepMotor {
public:
	StepMotor(int ino_OUT1, int ino_OUT2, int ino_OUT3, int ino_OUT4);
	StepMotor(int ino_OUT1, int ino_OUT2, int ino_OUT3, int ino_OUT4, int reqSpeed);

	void Init(int ino_OUT1, int ino_OUT2, int ino_OUT3, int ino_OUT4);
	void SetSpeed(int reqSpeed);
	void SetNumberOfSteps(int reqStepsFullrot);
	void Move(int nsteps);
	void IncrementPhase(int rotationDirection);
	void Step(int reqPhase);

private:

	boolean phases1[8] = { 0, 0, 0, 0, 0, 1, 1, 1 };
	boolean phases2[8] = { 0, 0, 0, 1, 1, 1, 0, 0 };
	boolean phases3[8] = { 0, 1, 1, 1, 0, 0, 0, 0 };
	boolean phases4[8] = { 1, 1, 0, 0, 0, 0, 0, 1 };

	int direction;					// Direction of rotation
	long step_delay;		            // delay between steps, in ms, based on speed
	int nStepsFullrot;				// total number of steps this motor can take
	int phase;

	// motor pin numbers:
	int motor_IN1;
	int motor_IN2;
	int motor_IN3;
	int motor_IN4;

};

#endif

