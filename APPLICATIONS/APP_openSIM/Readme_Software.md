## Software  

Using the PCB, setting up the module is again straight forward. After setting up the Raspberry Pi operating system, the *I2C* registers have to be set in order to display a fullscreen image on the DMD at a true resolution of *640x360* pixels. The raspbian version we applied on the raspberry pi is 10.0. MQTT package is not pre-installed and need to install with ```python3 -m pip install paho-mqtt```

This can be done from remote through SSH (e.g. ```ssh pi@192.168.178.39```) or using a secondary screen.
Opening a terminal connection one need to enter the following commands:

```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install mplayer

```

To edit the *I2C* settings the following is requiered:

Edit the entry at boot by typing ```nano /etc/rc.local``` and add (make sure the number after ```-y``` matches your I2C device by listing ```ls /dev/``` (e.g. ```/dev/i2c-11```)
Don't use ```sudo``` for ```i2cset```!!

```
i2cset -y 11 0x1b 0x0b 0x00 0x00 0x00 0x00 i
i2cset -y 11 0x1b 0x0c 0x00 0x00 0x00 0x1b i
# export DISPLAY=:0 (use this to access the screen from a remote SSH session)
```

In order to keep this after a reboot this can be added to the boot-config.txt.


Another thing before it starts working is to set the timings of the video-display.
Therefore type the following:

```nano /boot/config.txt```

and enter the following text:

```
# and your display can output without overscan
disable_overscan=1

# Enable audio (loads snd_bcm2835)
dtparam=audio=on

# Add support for software i2c on gpio pins
dtoverlay=i2c-gpio,i2c_gpio_sda=23,i2c_gpio_scl=24,i2c_gpio_delay_us=2

# DPI Video Setup
dtoverlay=dpi18
overscan_left=0
overscan_right=0
overscan_top=0
overscan_bottom=0
framebuffer_width=640
framebuffer_height=360
enable_dpi_lcd=1
display_default_lcd=1
dpi_group=2
dpi_mode=87

dpi_output_format=458773
hdmi_timings=640 0 14 4 12 360 0 2 3 9 0 0 0 60 0 32000000 3

```


Once you have created a proper video-file which contains the RAW-frames (e.g. ```ABC.avi```) you can start the video on the screen remotely by typing the following:

```mplayer -fs -loop 0 ./Desktop/ABS.avi```


## Additional infos 


For windows you can download ```WinSCP```+ ```Putty``` for connecting to the Pi through SSH. 
For mac you can use the Terminal + Filezilla for connecting to the Pi .

## Start Jetson

Start the camera by typing the following into the TERMINAL

```
cd ~./Downloads/Vimba_v3.1_ARM64/Vimba_3_1/Tools/Viewer/Bin/arm_64bit/
./VimbaViewer
```

The vimba viewer GUI will appear and you can control the camera features with live-stream and continious capture



## Start Raspberry Pi 

Turn on the wifi Hotspot with 

```
SSID: Blynk
Password: 12345678
```

Turn on the Raspberry Pi and wait until it connects. Note the IP Address of the pi (in our case ```192.168.43.9```

Connect to the pi with SSH on you computer using the following line: 


```
ssh pi@192.168.43.9
```

The password is: ```raspberrz``` (eventhough default is ```raspberry```). 

Now we need to activate the external display by typing the following in the Terminal on your computer

```
export DISPLAY=:0
```

Now the pi displays anything you want to have on the DMD. 


### Start Video on the Pi

Inside the home-folder of the pi there is a pre-generated SIM-pattern video with 3 phases and 3 orientations. You can start it by typing:

```
mplayer -fs -loop 0 SIM_360_640_9_1.avi 
```

It will start the video in fullscreen mode at an infinity loop.


```
Opening video decoder: [raw] RAW Uncompressed Video
Could not find matching colorspace - retrying with -vf scale...
Opening video filter: [scale]
Movie-Aspect is undefined - no prescaling applied.
[swscaler @ 0x768c9418]bicubic scaler, from pal8 to bgra using C
[swscaler @ 0x768c9418]using unscaled pal8 -> bgra special converter
VO: [x11] 640x360 => 640x360 BGRA  [fs] [flip]
Selected video codec: [rawbgr8flip] vfm: raw (RAW BGR8)
==========================================================================
Load subtitles in ./
Audio: no sound
Starting playback...
V:  21.0  22/ 22  0%  0%  0.0% 0 0 
```

You end the infinite loop with typing ```Ctrl+c``` in the Terminal on your computer. 

**IMPORTANT:** The video-player interpolates the frames, which means, that there is a black border and no true pixel-to-pixel relationship. **Not useful for SIM**. It's better to use a python programm with pygame instead! 


### Uploading/Downloading files to the PI using FileZilla

Download Filezilla for Mac, Windows and Linux. 

Add a new server (protocol: SFTP, Server: 192.168.43.9, Port: 22, user: pi, password: raspberrz) and connect to the Pi using the IP-address and user/password and browse the filesystem (need to accept the SSH-key first):	


### Video generation

#### Fiji Plugin

For generating the frames we suggest to use the freely available pattern-generation software which is part of the ***fairSIM*** project by Marcel Müller et al. This can generate patterns using the following GUI:


<p align="center">
<img src="./IMAGES/fairSIM_configuration.png" width="200">
</p>

The created stack (i.e. TIF) need to be imported and saved as an uncompressed 8-Bit monochromatic AVI-file in order to get displayed using mplayer on the Raspberry Pi.

The plugin is available from Marcel Müller on his [Repo](https://github.com/fairSIM/fastSIM-GratingSearch/releases). Download the file ```SLM_GratingSearch.jar``` and add it to the plugin directory. 

#### Matlab Programm

The Matlab based version of the SLM Pattern generation can be found in our [fastSIM Repository](https://github.com/nanoimaging/fastSIM_GratingSearchforSLM).

#### Java Programm

There is also a Java implementation for CUDA enabled graphic cards available from the University Bielefeld [here](https://github.com/biophotonics-bielefeld/coherent-dmd-sim-simulator).

## Further reading

- [DATASHEET DMD](https://www.digikey.at/de/product-highlight/t/texas-instruments/dlp-lightcrafter-display-2000-eval-module)
- [DMD for Photo-Lithography](https://hackaday.io/project/25260/gallery#f8c0a842e59a10156db102aedcd8b790)
- [Hands-on and review of DMD module](https://www.element14.com/community/roadTestReviews/2662/l/dlp-pico-display-projector-evm-beaglebone-black-review)
- [Alternative fiber-coupled laser](https://de.aliexpress.com/item/32880918252.html)
- [Deeper Reading into the I2C settings](https://mikrokontroler.pl/2019/01/02/projektor-dlp-z-wykorzystaniem-raspberry-pi-3-oraz-modulu-ti-lightcrafter-display-2000/2/)
- [Datasheet DLP2000](http://www.ti.com/lit/ds/symlink/dlp2000.pdf)
- [Display Timinigs on Raspi](https://www.raspberrypi.org/documentation/hardware/raspberrypi/dpi/)
- [Flickering Problem on DLP](https://e2e.ti.com/support/dlp/f/94/t/700072?DLPDLCR2000EVM-Screen-Jitter-Glitch-on-Output-of-DLP-Lightcrafter-2000)

