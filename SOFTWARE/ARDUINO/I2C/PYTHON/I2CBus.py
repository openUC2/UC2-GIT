import smbus
import time
import errno
# import pigpio
import os


class I2CBus(object):

    addr_space = range(int(0x04), int(0x77))
    defaultBus = smbus.SMBus(1)

    def __init__(self, address):
        self.name = ""

    @staticmethod
    def scanBus():
        address_list = []
        for address in I2CBus.addr_space:
            try:
                I2CBus.defaultBus.write_byte(address, 0)
                address_list.append(address)
                print("Device found at {0}".format(hex(address)))
            except IOError as e:
                if e.errno != errno.EREMOTEIO:
                    print("Error: {0} on address {1}".format(e, hex(address)))
            except Exception as e:  # exception if read_byte fails
                print("Unknown error: {0} on address {1}".format(
                    e, hex(address)))
        return address_list
