import time
import serial

class xyStepper:
    mycurrentposition = 0
    max_steps = 100
    mystepper = 'x'
    backlash = 0
    highspeed = 2500
    lowspeed = 2500
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

            # set high speed
            mycmd = 'S'
            self.myserial.write(str.encode(mycmd))
            time.sleep(1)

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

            #print('Steps to go: ' + str(self.mystepstogo) + ' using command: '+mycmd)
            self.myserial.write(str.encode(mycmd))
            time.sleep(abs(self.mystepstogo)*.01+.5)

    def reset_pos(self):
        print('Reset the position of ' + self.mystepper + '-stepper with backlash; '+str(str(self.backlash)))
        self.mycurrentposition = 0

        print("Setting slow-speed")
        mycmd = 'L'
        self.myserial.write(str.encode(mycmd))
        time.sleep(1)

        if (self.mystepper == 'x'):
            #for ix in range(8):
            print("Resetting X")
            mycmd = 'X' + str(80)
            self.myserial.write(str.encode(mycmd))
            time.sleep(4)

            mycmd = 'x' + str(self.backlash) # backlash

        if (self.mystepper == 'y'):
            #for iy in range(8):
            print("Resetting Y")
            mycmd = 'Y' + str(80)
            self.myserial.write(str.encode(mycmd))
            time.sleep(4)

        # set high speed
        mycmd = 'S'
        self.myserial.write(str.encode(mycmd))
        time.sleep(1)

        mycmd = self.mystepper + str(self.backlash) # backlash
        self.myserial.write(str.encode(mycmd))
        time.sleep(1)

