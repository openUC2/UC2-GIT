# Digital In-Line Hologram

This ImageJ / Fiji command (plugin) written in Java computes an in-line hologram of an sufficiently coherent captured image by reconstructing the corresponding phases via [Huygens-Fresnel](https://en.wikipedia.org/wiki/Huygens–Fresnel_principle) backpropagation.

## Getting Started

* Download the free image analysis and processing tool [ImageJ / Fiji](https://imagej.net/Fiji/Downloads)
* Browse to Fiji installation folder. Enter plugin folder.
* Place repository file DIHM-0.1.jar (located in target folder) into Fiji plugin folder
* Run Fiji and open any (suitable) RGB-image file from your local disk (if grayscale, make sure it has 3 channels anyway)
* Plugin will take automatically the slice of the blue channel (hardcoded)
* In the Fiji menu run: Plugins >> DIHM
* Plugin will automatically crop maximum square with sidelenths of the next power of 2 from the image center
* Computation will take approx. 1m depending on loaded image size and machine
* Result is an image stack consisting of 70 images in which each slice corresponds to a phase distribution at a given position along optical axis (on object-side)

### Built With

* [Eclipse](http://www.eclipse.org/downloads/packages/) - IDE
* [Maven](https://maven.apache.org/) - Dependency Management

