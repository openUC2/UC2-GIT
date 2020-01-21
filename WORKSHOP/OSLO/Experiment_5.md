## Experiment – 4 Examination of the Time-Lapse Series
Process long-time series with Software of choice

The over-night measurements using the incubator microscope can be processed using e.g. Fiji or Phyton. Try to connect to the microscope using a "SSH" tool (e.g. [WinSCP for Windows](https://winscp.net/eng/index.php) or [Cyber Duck for MAC](https://cyberduck.io/)

Connect to the device with an IP-address of either
```
21.3.2.102 - setup 9

21.3.2.112

21.3.2.122

21.3.2.132

21.3.2.142
```

The files can be found in the folder ```/home/uc2/UC2/UC2-GUI/data/20200120/```. Take the newest date (not necessarily the actual date) and look through the ```expt_0**```folders. The one with many images can be copied on your local machine (takes some time). 

**ALTERNATIVE:** You can also copy the files using a USB drive (takes even longer).


## STEPS: 

1. Import an image sequence using the Fiji Import command
2. Split the color channels and use only the green one
3. Bin the pixels by a factor of 6
4. Export the stack as a ```.tiff```-file 

The result could look like this here (30 minutes of MDCK-cells prepared by Edna and Kay):

<p align="center">
<img src="./IMAGES/SAMPLE.gif" width="500">
</p>


5. Process the data with your prefered image processing pipe-line (e.g. tracking, segmentation, etc.)
6. Publish the result somewhere :) 

