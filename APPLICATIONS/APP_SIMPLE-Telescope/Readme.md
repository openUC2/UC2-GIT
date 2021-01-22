# Simple Telescopes

([TUT05 of TUTORIALS](../../TUTORIALS))

We developed a very easy-to-use setup to help you understand how a telescope works. It guides you through different optical designs, all with one goal: magnifying far-away objects.

<p align="center">
<img src="./IMAGES/Application_Telescopes_v3.png" width="400">
</p>

### Schemes of the telescopes
<p align="center">
<img src=".\IMAGES\UC2_Setups_6_telescopes.png"
width="600">
<br> L1: f' = +100 mm; L2: f' = +40 mm; L3: f' = -50 mm
</p>

## <img src="./IMAGES/D.png" width="40">Parts
The [Bill of Materials](https://docs.google.com/spreadsheets/d/1U1MndGKRCs0LKE5W8VGreCv9DJbQVQv7O6kgLlB6ZmE/edit?usp=sharing) is always the most up-to-date version!

### Modules for this setup

|  Name | Properties  |  Price | Link  | # |
|---|---|---|---|---|
|  Baseplate puzzle| - | 5€  | [Base-plate](../../CAD/ASSEMBLY_Baseplate/)  | 8|
|  Module: Lens Cube | -  | 20 €  | [Lens](../../CAD/ASSEMBLY_CUBE_Lens)  | 4|

### <img src="./IMAGES/P.png" width="40"> 3D-printing
To acquire the STL-files use the [UC2-Configurator](https://uc2configurator.netlify.app/). The files themselves are in the [RAW](../../RAW/STL) folder. The module can be built using injection-moulded (IM) or 3D-printed (3DP) cubes.

When using a lens of your choice, please follow our [Tutorial: Design your own Lens Holder](../../CAD/ASSEMBLY_CUBE_Lens/OPENSCAD).

## <img src="./IMAGES/B.png" width="40"> Additional components
* Check out the [RESOURCES](../../TUTORIALS/RESOURCES) for more information!
* 1× planoconvex lens, *f'* = +100 mm, diameter 25,4 mm (Artikel 2004) [🢂](https://optikbaukasten.de/)
* 2× planoconvex lens, *f'* = +40 mm, diameter 25,4 mm, (Artikel 2120) [🢂](https://optikbaukasten.de/)
* 1× planoconcave lens, *f'* = -50 mm, diameter 25,4 mm [🢂](https://www.thorlabs.com/thorproduct.cfm?partnumber=LC1259)
* 32× 5mm Ball magnets [🢂](https://www.magnetmax.de/Neodym-Kugelmagnete/Magnetkugel-Kugelmagnet-O-5-0-mm-Neodym-vernickelt-N40-haelt-400-g::158.html)
* 16× - 32× Screws DIN912 ISO 4762 M3×12 mm [🢂](https://eshop.wuerth.de/Zylinderschraube-mit-Innensechskant-SHR-ZYL-ISO4762-88-IS25-A2K-M3X12/00843%20%2012.sku/de/DE/EUR/)

## <img src="./IMAGES/A.png" width="40"> Assembly
For assembly instructions of the respective modules refer to the links in Modules for this setup.

In the end they look like this:
<p align="center">
<img src="./IMAGES/Telescope_Galileo.jpg" width="300">
<img src="./IMAGES/Telescope_Kepler.jpg" width="300">
<br>Left: Galilean telescope, Right: Keplerian telescope. 
</p>


## Alignment

Pre-align the telescope by putting every lens holder roughly in the center of the cube. Then look through it on some far away object (rather out of the window then across the table) and shift the eyepiece lens until you see a sharp magnified image.

The mutual position of the lenses is crucial for the working principle of the telescope. Read more about how the telescopes work and align them properly :-)

## Behind the telescope

A refracting telescope (also called a refractor) is a type of optical telescope that uses lenses to form an image. Refractors were the earliest type of optical telescope. The first practical refracting telescopes appeared in the Netherlands about 1608. All refracting telescopes use the same principles. The combination of an objective lens and eyepiece lens is used to gather more light than the human eye is able to collect on its own, focus it, and present the viewer with a brighter, clearer, and magnified virtual image.

The magnification of such a simple telescope is given by  
***M =  f<sub>1</sub> / |f<sub>2</sub>|***

### Galilean Telescope
<p align="center">
<img src="./IMAGES/UC2_Galileo.png" width="500">
</p>

The design Galileo Galilei used in 1609 is commonly called a Galilean telescope. It used a convergent (plano-convex) objective lens and a divergent (plano-concave) eyepiece lens [Galileo, 1610].  In a Galilean telescope, the image is non-inverted, since the design has no intermediary focus.

Galileo’s best telescope magnified objects about 30 times. Because of flaws in its design, such as the shape of the lens and the narrow field of view, the images were blurry and distorted. Despite these flaws, the telescope was still good enough for Galileo to explore the sky. The Galilean telescope could view the phases of Venus, and was able to see craters on the Moon and four moons orbiting Jupiter.  

The concave lens L<sub>2</sub> serves as an eyepiece and is placed in front of the focal plane of the objective lens L<sub>1</sub> in such a way that the back focal point F<sub>1</sub>‘ of L<sub>1</sub> coincides with the focal point F<sub>2</sub> of L<sub>2</sub>. The distance between the principle planes of objective and eyepiece is f<sub>1</sub> - │f<sub>2</sub>│.  

We then observe a virtual non-inverted magnified image of the observed object.

### Keplerian Telescope
<p align="center">
<img src="./IMAGES/UC2_Kepler.png" width="500">
</p>

The Keplerian telescope, invented by Johannes Kepler in 1611, is an improvement on Galileo's design. It uses a convex lens as the eyepiece instead of Galileo's concave one. The advantage of this arrangement is that the rays of light emerging from the eyepiece are converging. This allows for a much wider field of view and greater eye relief, but the image for the viewer is inverted. Considerably higher magnifications can be reached with this design, but to overcome aberrations the simple objective lens needs to have a very high ratio of focal distances (Johannes Hevelius built one with a 46-metre  focal length, and even longer tubeless "aerial telescopes" were constructed).  

Keplerian telescope is composed of two convex lenses. The objective lens L<sub>1</sub>, focal distance f<sub>1</sub>, creates an image which is then observed through the eyepiece lens L<sub>2</sub> with focal distance f<sub>2</sub>. The distance between the principle planes of objective and eyepiece is f<sub>1</sub> + f<sub>2</sub> .

We then observe a virtual inverted magnified image of the observed object.

### Terrestrial telescope

<p align="center">
<img src="./IMAGES/UC2_terrestrial.png" width="500">
</p>

A terrestrial telescope is a telescope which, unlike most telescopes used for astronomical purposes, contains an arrangement of lenses presenting a non-inverted image to the observer, suitable for observation of objects on the Earth's surface.

A terrestrial telescope is, in a way, just a Keplerian telescope modified for terrestrial observation. An inverting lens is placed between the objective and the eyepiece and it inverts the image in the focal plane of the objective, so it’s flipped when viewed through the eyepiece.

The inverting lens doesn’t contribute to the magnification and the magnification is calculated the same way as in a Keplerian telescope.

Source of information for the above text:  [1](https://en.wikipedia.org/wiki/Refracting_telescope)  [2](https://en.wiktionary.org/wiki/terrestrial_telescope)

Where next?  
The telescopes are also a part of the [SimpleBOX](../../TheBOX/SimpleBOX). Find out more about in the [SimpleBOX manuals](../../../TheBOX/SimpleBOX/DOCUMENTS)    
Or return to the [TUTORIALS](../../../TUTORIALS)

## <img src="./IMAGES/E.png" width="40"> Results
None yet. Be the first to share yours!

## <img src="./IMAGES/S.png" width="40"> Participate!

Do you want to show your own results? Do you have ideas for improvements? Let us know!
