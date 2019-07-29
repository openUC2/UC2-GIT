from I2CDevice import I2CDevice
from I2CBus import I2CBus
import time

ledarr = I2CDevice(0x07)
ledarr.announce()
# response = ledarr.sendCommand("CLEAR")
# print(response)
# time.sleep(1)
ledarr.sendCommand("NA+4")
for i in range(50):
    response = ledarr.sendCommand("CLEAR")
    cmd = "RECT+2+2+5+5+0+255+255+" + str(i % 2)
    response = ledarr.sendCommand(cmd)
    print(response)

time.sleep(3)
response = ledarr.sendCommand("CLEAR")
print(response)
