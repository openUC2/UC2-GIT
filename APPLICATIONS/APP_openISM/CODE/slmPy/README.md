# slmPy
A simple Python module based on wxPython to interact with spatial light modulators handled as secondary monitors.

## What is it for?

Most Spatial Light Modulators (SLMs) are controlled via an analog (VGA) or digital (HDMI/DVI) monitor standard communication protocol. In other words, you plug it to your computer and it is recognized as a monitor display. There is usually no useful tool or API provided with the device to dynamically control the SLM. I present here a way to do this using Python.

## A short explanation
You can skip this part if you just want to get a working code, I want to briefly comment how I wrote this code and why.

Displaying an image on an SLM is not harder than displaying an image on a screen. We can for example simply drag a window on the SLM "screen". However, we want to be sure to control what happen on each pixel of the SLM and avoid any interpolation that occurs when an image is resized. We then need a full screen window in which we display an image of the same resolution as the screen. My first idea was to search in the video games oriented modules, like Pygame and Pyglet. It turns out that Pygame does not support multiple screens and while Pyglet is supposed to handle them, I was only able to make it work when all the screens had the same resolution. I then searched into modules for building graphic user interfaces. Tkinter and wxPython seem to be the most popular ones. I chose wxPython, but I know it would be possible with Tkinter too.

The **SLMdisplay** class of the slmpy module creates a frame (window) that is constantly refreshed in a loop. As we want to be able to send an image to display from an external code, this loop is run in a separate thread (using the Python module thread included in the standard distributions). I was largely inspired by this tutorial http://wiki.wxpython.org/MainLoopAsThread.

## Requirements

* A Python distribution under Linux or Windows (I did not test Mac OS, there may be issues),
* The wxPython module available from [here](http://www.wxpython.org/),
* An SLM with a VGA/HDMI/DVI cable,

## Usage

### A simple example
First, we import the **slmpy** module

```python
import slmpy
```

We also need the numpy module, since we send the images to display as numpy arrays, and the time module.

```python
import numpy as np
import time
```

We then create the object that handles the SLM array.

```python
slm = slmpy.SLMdisplay()
```

By default, slmpy uses the second monitor for displaying images. If you have more that one monitor in addition to the SLM, you may want to specify which monitor is the SLM.

```python
slm = slmpy.SLMdisplay(monitor = x)
```

with x the id of the SLM display as set up in the operating system. 0 correspond to the primary screen. By default, monitor is set to 1.

We then retreive the size of the SLM display. These values correspond to the ones set up in you operating system, make sure they are set to the native resolution of your device. 

```python
resX, resY = slm.getSize()
```

We then generate a test image to display. Note that the image has to be converted to 8-bit integers, be careful to have integers between 0 and 255.

```python
X,Y = np.meshgrid(np.linspace(0,resX,resX),np.linspace(0,resY,resY))
testIMG = np.round((2**8-1)*(0.5+0.5*np.sin(2*np.pi*X/50))).astype('uint8'))
```

We can then display the image on the SLM 

```python
slm.updateArray(testIMG)
```

and close the window once finished.

```python
slm.close()
```
 

### Image resolution and SLM resolution

In the previous example we were careful to create an image with the same resolution as the SLM. Thus, one pixel of the image correspond to one pixel of the SLM. However, if one send am image of any given resolution, it will be deformed to fit the SLM array. This can be usefull when one does not need a high resolution image, for example, one can send a 400x300 image on a 800x600 screen, one pixel of the image will correspond to exactly 4 pixels of the SLM. This is faster that generating a 800x600 image with 2x2 squares of the same color as the software handles arrays 4 times smaller. However, if the image resolution is not a sub-mulitple of the SLM resolution, the interpolation could lead to dramatic effects, for example when one want to display a grating or if the SLM is DMD (binary) modulator.


#### Image lock

In SLM experiments, it is common to display images in a loop. What will happen if the mage does not have the time to be displayed between two iterations of the loop? In some cases, you want to be sure that the image is sent usin updateArray() before going further, in order to measure its effect for example, but in some cases, you do not want to loose sync, even if it means skipping images. You can control that with the imageLock parameter.

```python
slm = slmpy.SLMdisplay(isImageLock = True)
```

If isImageLock is set to True, the program will wait for the image to be displayed before returning from the updateArray() function. If it is set to False, it will not. By default, isImageLock is True.

Check the following example with isImageLock = True or IsImageLock = False. The code sent 100 times the same blank image on the screen, the image does not change not to spend too much computational time treating the data array. You will notice that the time spent in the loop without the image can be faster than the actual refresh rate of the monitor if isImageLock is set to False.

```python
import slmpy
import time
slm = slmpy.SLMdisplay(isImageLock = False)
resX, resY = slm.getSize()
testIMG = np.zeros([resY,resX]).astype('uint8')
t0 = time.time()
for i in range(100):
  slm.updateArray(testIMG)
print time.time() - t0
slm.close()
```

### Color layers

The module can display monochromatic or color images. A standard monitor display is controlled using three 8-bit color layers (red, green and blue). For most SLMs, there is 256 or less values possible for the phase or amplitude of the pixels. The array is controlled by only one 8-bit color channel. We can then only display black and white images.

However, there exists 16-bit SLMs which uses two 8-bit color channels to encode the information. For those devices, it is needed to display "color images", i.e. to control the three color layers independently (while it would still be used with a monochromatic illumination). The **updateArray()** function automatically detects if the array sent is a 2 or 3 dimensional one.

Here is an example of how to show a color image. On the green layer we display sine oscillation and nothing on the other layer. If you use a secondary monitor to test, you will see green fringes.

```python
slm = slmpy.SLMdisplay(isImageLock = False)
resX, resY = slm.getSize()
X,Y = np.meshgrid(np.linspace(0,resX,resX),np.linspace(0,resY,resY))
# The image we want on the green layer
greenIMG = np.round((2**8-1)*(0.5+0.5*np.sin(2*np.pi*X/50)))
# We need a third dimension corresponding to the color layer
greenIMG.shape = greenIMG.shape[0], greenIMG.shape[1], 1
# The two other layers are blank arrays
blankImage = np.zeros([greenIMG.shape[0], greenIMG.shape[1], 1])
# We merge the three layers in a (resY,resX,3) color array
color_array = np.concatenate((blankImage,greenIMG,blankImage), axis=2).astype('uint8')
# The image is sent to the slm
slm.updateArray(color_array)
# Wait 10 seconds
time.sleep(10)
# Close the window
slm.close
```

## A dynamic example

As a final example, the following code generated moving fringes. The resolution of the images is set to half the one of the SLM.

```python
import slmpy
import time
import numpy as np
slm = slmpy.SLMdisplay(isImageLock = True)
resX, resY = slm.getSize()
# We use images twice smaller than the resolution of the slm
ImgResX = resX//2
ImgResY = resY//2
X,Y = np.meshgrid(np.linspace(0,ImgResX,ImgResX),np.linspace(0,ImgResY,ImgResY))
for i in range(100):
  testIMG = np.round((2**8-1)*(0.5+0.5*np.sin(2*np.pi*X/50+1.0*i/10*np.pi))).astype('uint8')
  slm.updateArray(testIMG)
  time.sleep(0.05)
slm.close()
```

## Other example

[**python-SLM**](https://github.com/totesalaz/python-SLM), written by Luis [José Salazar-Serrano](http://www.opensourcelab.salazarserrano.com/), is good example of the use of this **slmPy** to generate the phase masks to create Laguerre Gauss beams with a SLM. 
