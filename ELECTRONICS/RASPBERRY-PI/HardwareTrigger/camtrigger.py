import os
import sys
from glob import glob
from gpiozero import Button
from picamera import PiCamera
from signal import pause
from datetime import datetime
from subprocess import check_output, CalledProcessError

def get_usb_devices():
    sdb_devices = map(os.path.realpath, glob('/sys/block/sd*'))
    usb_devices = (dev for dev in sdb_devices if 'usb' in dev.split('/')[5])
    return dict((os.path.basename(dev), dev) for dev in usb_devices)

def get_mount_points(devices=None):
    devices = devices or get_usb_devices()
    output = check_output(['mount']).splitlines()
    is_usb = lambda path: any(dev in path for dev in devices)
    usb_info = (line for line in output if is_usb(line.split()[0]))
    return [(info.split()[0], info.split()[2]) for info in usb_info]

def take_picture_with_camera():

    mounts = get_mount_points()
    subfolder = '/DIHM/'
    imgpath = None

    if not mounts:
        mounts = None
        imgpath = os.path.dirname(os.path.abspath(__file__)) + subfolder
        print('No mount points found.')
    else:
        imgpath = mounts[0][1] + subfolder
        print('Found USB Storage.')

    if not os.path.isdir(imgpath):
        os.makedirs(imgpath)

    print('Image will be saved at ' + imgpath)
    mydatetime = datetime.now()
    date = mydatetime.strftime('%Y-%m-%d')
    time = mydatetime.strftime('%H-%M-%S')
    imgfile = imgpath + 'IMG_' + date + '_' + time + '.jpg'
    camera.capture(imgfile)
    print('Took photo')

camera = PiCamera()
id = 'camtrigger.py: '
print(id + 'Script is running')

button = Button(4)
button.when_pressed = take_picture_with_camera

pause()
