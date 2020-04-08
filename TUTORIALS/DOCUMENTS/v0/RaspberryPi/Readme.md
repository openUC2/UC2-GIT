Setup for the Raspberry Pi Control Interface

V0, 24.08.2018

X. Uwurukundo

B. Diederich

Introduction
=============

The control interface is a Raspberry Pi 3, connected to the 7 inch
touchscreen baked into a 3D printed case. It acts as the acquisition
synchronization interface, controlling the I2C hardware, the camera and
manages the memory/connections.

<img src=".//media/image1.jpeg">

Components / Resources
======================

Below you’ll find a list with the basic ingredients for the control
interface to work

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Article                        Image                                                                                                                                                              Price/Link
  ------------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Raspberry Pi 3                 <img src=".//media/image2.jpeg">[Link](https://images-na.ssl-images-amazon.com/images/I/811dTOvynqL.\_SL1500\_.jpg)    35 €,

                                                                                                                                                                                                    <https://www.amazon.de/Raspberry-1373331-Pi-Modell-Mainboard/dp/B07BDR5PDW/ref=sr_1_1?ie=UTF8&qid=1534931804&sr=8-1&keywords=Raspberry+Pi>

  7 inch touchscreen             <img src=".//media/image3.jpeg">[Link](https://images-na.ssl-images-amazon.com/images/I/61-FECrrgaL.\_SL1024\_.jpg)   70 €,

                                                                                                                                                                                                    <https://www.amazon.de/Raspberry-Pi-7-inch-Screen-Display/dp/B014WKCFR4/ref=sr_1_3?ie=UTF8&qid=1534934546&sr=8-3&keywords=Raspberry+Pi+7+inch>

  SD Card, 64 GB                                                                                                                                                                                    10 €

  Logitech Keyboard + Trackpad   <img src=".//media/image4.jpeg">[Link](https://images-na.ssl-images-amazon.com/images/I/51mCYj7xUvL.\_SL1000\_.jpg)    35€,

                                                                                                                                                                                                    <https://www.amazon.de/Logitech-Wireless-Tastatur-Deutsches-Tastaturlayout/dp/B00VHHWNMI/ref=sr_1_3?ie=UTF8&qid=1534934623&sr=8-3&keywords=logitech+tastatur+touch>

  Pi Camera v 2.1                                                                                                                                                                                   15€

  Ribbon Cable 1m                                                                                                                                                                                   3€


  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Assembly
=========

It is recommended to buy/print a case for the Raspberry Pi and the 7
inch touchscreen. We made good experiences with the original Pi-Screen
though it’S more expensive. It ships with all necessary parts (screws,
mounting material). For an assembly guide please have a look here:

<https://thepihut.com/blogs/raspberry-pi-tutorials/45295044-raspberry-pi-7-touch-screen-assembly-guide>

For the I2C connection use the pins below (SDA/SCL):

![Bildergebnis fÃ¼r Raspberry Pi
pinout](.//media/image5.jpeg)

5V, Gnd also connects to the external components. The 5V power supply
can either be used through the USB-connector or the 5V input of the Pi
(take care it’s not fused!).

Soldering/Wiring/Camera connection
==================================

Install Stuff on Arduinos (I2C-Devices)
=======================================

Right now there are several examples to run with the U2C toolbox:

-   Light-Source

-   XYZ-Stage

-   Z-Stage

-   XY-Stage

-   LED Matrix

All of them are backed with an Arduino acting as the “communicator”. It
states the set of available functions with a hand-shake protocol at the
beginning and makes sure that the requested commands over I2C coming
from the master (Raspi) are executed. Each Device needs a specifc
Address which has to be set in the Arduino files (Arduino folder).

You can implement what-ever device you want. For further information
please have a look in the I2C guide.

To install the Arduino stuff, please download the Arduino IDE and flash
the .ino files to you Nano’s.

Install OS
===========

Download stable Raspbian Version and flash it on the SD-Card.

How-to setup the Raspberry Pi
=============================

**Step-by-Step Guide to Set-up Raspbian Stretch**

Disclaimer: Note that the Raspberry Pi Zero – although running Raspbian
Stretch as all other Raspberry Pi’s – is ARMv6 architecture in contrast
to the most common ARMv7 architecture as used on the Raspberry Pi 3.
However, all steps described in this guide should work on both and were
tested on a Raspberry Pi Zero W.

Before you begin, check your default python version with:

-   pi@raspberrypi:\~\$ python --version

This guide is written for python 2.7 and assumes it is the default
python-compiler on the target system. All steps were performed under
afore-mentioned conditions and systems only. Apart from this, it is
highly recommended that all **pip**-installs are run as follows:

-   Instead of: pi@raspberrypi:\~\$ ~~pip install numpy~~

-   Better run: pi@raspberrypi:\~\$ python -m pip install numpy

This will install the package more specific to your default-compiler and
showed advantages relating dependencies-setup.

1)  Browse to: <https://www.raspberrypi.org/downloads/raspbian/>

2)  Download Raspbian Stretch

3)  Flash it to Micro-SD-Card with at least 8GB capacity (e.g. with
    Etcher on Windows)

4)  Set up your WiFi-Connection if not already done

5)  *Optional*: First get packagelist with package size and then get rid
    of unnecessary packages in order to free some space on your SD-Card:

-   pi@raspberrypi:\~\$ dpkg-query -Wf
    '\${Installed-Size}\\t\${Package}\\n' | sort -n

-   pi@raspberrypi:\~\$ sudo apt-get remove --purge wolfram-engine

-   pi@raspberrypi:\~\$ sudo apt-get clean

-   pi@raspberrypi:\~\$ sudo apt-get autoremove

1)  Install Kivy for Raspbian Stretch ( according to
    <https://kivy.org/docs/installation/installation-rpi.html> ):

-   pi@raspberrypi:\~\$ sudo apt-get update

-   pi@raspberrypi:\~\$ sudo apt-get install libsdl2-dev
    libsdl2-image-dev libsdl2-mixer-dev

-   pi@raspberrypi:\~\$ sudo apt-get install libsdl2-ttf-dev pkg-config
    libgl1-mesa-dev

-   pi@raspberrypi:\~\$ sudo apt-get install libgles2-mesa-dev
    python-setuptools libgstreamer1.0-dev

-   pi@raspberrypi:\~\$ sudo apt-get install git-core
    gstreamer1.0-plugins-{bad,base,good,ugly}

-   pi@raspberrypi:\~\$ sudo apt-get install gstreamer1.0-{omx,alsa}
    python-dev libmtdev-dev

-   pi@raspberrypi:\~\$ sudo apt-get install xclip xsel

-   Install Kivy globally on your system but with the following command

1)  Install Cython 0.28.3 ( according to
    <https://kivy.org/docs/installation/installation-rpi.html> ):

-   pi@raspberrypi:\~\$ sudo python -m pip install -U Cython==0.28.3
    (takes approx. 2h on RasPi Zero)

1)  Install Kivy ( according to
    <https://kivy.org/docs/installation/installation-rpi.html> ):

-   pi@raspberrypi:\~\$: sudo pip install
    git+https://github.com/kivy/kivy.git@master

> (takes approx. 2h on RasPi Zero)

1)  Open RasPi Config and activate SSH:

-   pi@raspberrypi:\~\$ sudo raspi-config

-   Navigate to: Interfacing Options SSH Enable SSH Yes

1)  Connect to your Raspberry Pi using its IP-Address within your
    Network (e.g. with PuTTy on Windows

2)  Create Folder “Programming” in home directory. Change into that
    folder via SSH-Terminal

3)  Fetch FludiscopeApp from Benedict Diederichs Branch on GitLab:

-   pi@raspberrypi:\~\$ git clone -b developBD --single-branch
    git@gitlab.com:renerichter/PPS-app.git

1)  Browse to: \~/Programming/PPS-app/code/

2)  Run: python main.py

3)  Install all missing dependencies you are notified about to be
    missing (list may be incomplete):

-   pi@raspberrypi:\~\$: python -m pip install unipath

-   pi@raspberrypi:\~\$: python -m pip install ruamel.yaml

-   pi@raspberrypi:\~\$: sudo apt-get install libffi-dev

-   pi@raspberrypi:\~\$: python -m pip install cffi

-   pi@raspberrypi:\~\$: python -m pip install smbus-cffi

-   pi@raspberrypi:\~\$: python -m pip install pyusb

-   pi@raspberrypi:\~\$: python -m pip install safe-cast

1)  Install pre-compiled OpenCV 2.4.9.1 as described in order to save
    hours of compile-time as opposed to widespread conventional install.
    Get OpenCV-dependencies in advance. And check it installed correctly
    afterwards.

-   pi@raspberrypi:\~\$: sudo apt-get update

-   pi@raspberrypi:\~\$: sudo apt-get upgrade

-   pi@raspberrypi:\~\$ sudo apt-get install libtiff5-dev libjasper-dev
    libpng12-dev

-   pi@raspberrypi:\~\$ sudo apt-get install libjpeg-dev

-   pi@raspberrypi:\~\$ sudo apt-get install libavcodec-dev
    libavformat-dev libswscale-dev libv4l-dev

-   pi@raspberrypi:\~\$ sudo apt-get install libgtk2.0-dev

-   pi@raspberrypi:\~\$ sudo apt-get install libatlas-base-dev gfortran

-   pi@raspberrypi:\~\$ sudo apt-get install libopencv-dev python-opencv
    python-picamera

-   pi@raspberrypi:\~\$ python

-   &gt;&gt;&gt; cv2.\_\_version\_\_

1)  Enable I2C, Serial Communication and PiCamera:

-   pi@raspberrypi:\~\$: sudo raspi-config

1)  *Optional \[RasPi 3\]*: Install TeamViewer for remote maintenance:

-   pi@raspberrypi:\~\$: sudo apt-get update && sudo apt-get
    dist-upgrade

-   pi@raspberrypi:\~\$: wget
    <http://download.teamviewer.com/download/linux/version_11x/teamviewer-host_armhf.deb>

-   pi@raspberrypi:\~\$: sudo dpkg -i teamviewer-host\_armhf.deb (will
    throw some errors, that’s okay)

-   pi@raspberrypi:\~\$: sudo apt-get -f install (will fix previous
    errors)

1)  *Optional \[RasPi Zero W\]*: Install TeamViewer for remote
    maintenance:

    -   pi@raspberrypi:\~\$: sudo nano /etc/dphys-swapfile

2)  Install UC2 Software

    -   Git clone XXX –recursive

3)  Start Software

    -   python main.py

Software download
=================

For the future we want to release a ready-to-download image for the pi.
Please be patient

Troubleshooting
===============

Intentionally left blank.
