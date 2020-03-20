import time
import serial

class xyStepper:
    mycurrentposition = 0
    max_steps = 100
    mystepper = 'x'
    backlash = 0
    '''
    X -> backwards
    x -> forwards
    '''

    def __init__(self, myserial, mycurrentposition=0, mystepper='x', backlash=0):
        self.mycurrentposition = mycurrentposition
        self.mystepper = mystepper
        self.myserial = myserial
        self.backlash = backlash
        print('Initializing XY-stepper: ' + self.mystepper)

    def go_to(self, nextposition):
        if ((nextposition <= self.max_steps) and  (nextposition >= 0)):
            self.mystepstogo = nextposition - self.mycurrentposition
            self.mycurrentposition = nextposition

            mycmd = ' '
            if (self.mystepstogo > 0):
                # fwd
                if (self.mystepper == 'x'):
                    mycmd = 'x' + str(abs(self.mystepstogo))
                if (self.mystepper == 'y'):
                    mycmd = 'y' + str(abs(self.mystepstogo))

            if (self.mystepstogo < 0):
                # vwd
                if (self.mystepper == 'x'):
                    mycmd = 'X' + str(abs(self.mystepstogo))
                if (self.mystepper == 'y'):
                    mycmd = 'Y' + str(abs(self.mystepstogo))

            print('Steps to go: ' + str(self.mystepstogo) + ' using command: '+mycmd)
            self.myserial.write(str.encode(mycmd))
            time.sleep(abs(self.mystepstogo)*.01+1)

    def reset_pos(self):
        print('Reset the position of ' + self.mystepper + '-stepper with backlash; '+str(str(self.backlash)))

        self.mycurrentposition = 0
        if (self.mystepper == 'x'):
            mycmd = 'X' + str(self.max_steps)
            self.myserial.write(str.encode(mycmd))
            time.sleep(4)
            mycmd = 'x' + str(self.backlash) # backlash
        if (self.mystepper == 'y'):
            mycmd = 'Y' + str(self.max_steps)
            self.myserial.write(str.encode(mycmd))
            time.sleep(4)
            mycmd = 'y' + str(self.backlash) # backlash

        self.myserial.write(str.encode(mycmd))
        time.sleep(1)
