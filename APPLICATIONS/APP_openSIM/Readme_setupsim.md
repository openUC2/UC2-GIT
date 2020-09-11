# Setup opensIM


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

