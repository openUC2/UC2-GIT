<p align="left">
<a href="#logo" name="logo"><img src="./IMAGES/UC2_logo_text.png" width="400"></a>
</p>

# **UC2 - Open and Modular Optical Toolbox**

---

**New**: :boom: **UC2_v3 is now released!** :boom: [Watch how much time the IM cubes can save!](https://www.youtube.com/watch?v=M_oqieogAOo&feature=youtu.be&ab_channel=openUC2)   
*We are working on making the IM Cubes and Puzzles available for sale, but we are not able to offer a 'BUY' button yet. If you are interested in buying some components, contact us via email info@useetoo.org*

**New**: The Pre-print of "UCsim2: 2D Structured Illumination Microscopy using UC2" is available on [Biorxiv](https://www.biorxiv.org/content/10.1101/2021.01.08.425840v1)  [![DOI:10.1101/2021.01.08.425840](http://img.shields.io/badge/DOI-10.1101/2021.01.08.425840-B31B1B.svg)](https://doi.org/10.1101/2021.01.08.425840)

**New**: The UC2 paper is out in Nature Communications! [A versatile and customizable low-cost 3D-printed open standard for microscopic imaging](https://www.nature.com/articles/s41467-020-19447-9) [![DOI:10.1038/s41467-020-19447-9](http://img.shields.io/badge/DOI-10.1038/s41467_020_19447_9-000000.svg)](https://doi.org/10.1038/s41467-020-19447-9)



[<img src="./IMAGES/sitemap.png" height=50 align="right">](./SITEMAP.md)

[<img src="./IMAGES/UC2_Logo.png" height=40>](https://www.useetoo.org) [<img src="./IMAGES/icon_git.png" width=40>](https://github.com/bionanoimaging/UC2-GIT) [<img src="./IMAGES/icon_UC2Software.png" height=40>](https://github.com/bionanoimaging/UC2-Software-GIT) [<img src="./IMAGES/icon_tw.png" width=40>](https://twitter.com/openuc2)  [<img src="./IMAGES/icon_yt.png" width=40>](https://www.youtube.com/channel/UCcHFzXTdC1Ro0OMnHS_54UA) [![Open Source Love](https://badges.frapsoft.com/os/v3/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)


Cite this repository: [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4041339.svg)](https://doi.org/10.5281/zenodo.4041339)

---

# <a href="#icon01" name="icon01"><img src="./IMAGES/signpost.png" width=30></a> Start here! Everything is open-source - simply join!

## Steps to reproduce and use the toolbox:
<p align="center">
 <a href="https://github.com/bionanoimaging/UC2-GIT/tree/master/TUTORIALS"><img src="./IMAGES/UC2_Reproduce_Scheme.png" width="800"></a>
</p>

## Too many new things? Follow our tutorials [<img src="./IMAGES/BtP.png" width="60"> From a Beginner to a Professional](./TUTORIALS)!

## Already familiar? Click here if you are looking for...
TheBOX | General toolbox  | Specific setup |Workshops
:------:|:------:|:------:|:------:
[<img src="./IMAGES/UC2_theBox.jpg" height="150" hspace="20">](./TheBOX)|[<img src="./IMAGES/UC2_Cube_Store.jpg" height="150">](./CAD)|[<img src="./IMAGES/UC2_application.jpg" height="150">](./APPLICATIONS)|[<img src="./IMAGES/UC2_workshop.jpg" height="150">](./WORKSHOP)
[Choose a version and build your own BOX.](./TheBOX) | [Explore the toolbox and its applications.](./CAD) | [Alternatives for many Microscopy methods... and more.](./APPLICATIONS) | [Host or join a UC2 workshop.](./WORKSHOP)

## [Get Involved! Contribute to the project!](CONTRIBUTING.md)

## ... or keep on reading to learn more!

---

## Making **open-science** great again!

**UC2** is a general-purpose modular framework for making interactive (electro)-optical projects. Most optical systems such as microscopes follow a simple **4f** or Fourier-optical principle, where lenses are aligned such that focal-planes of adjacent components overlap to limit the amount of aberrations as much as possible and to be able to predict the system-behavior easily using Fourier-transforms.

Following this idea, a microscope as shown in **Fig 1** creates an angular magnification depending on the focal lenghts of the objective f<sub>obj</sub> and tube lens f<sub>tube</sub>:

***M<sub>4f</sub>=  f<sub>tube</sub>/f<sub>obj</sub>***

<p align="center">
<img src="./IMAGES/UC2_simplemicroscope.png" width="800">
<br> Fig. 1: Fourier-Optical Setup; Koehler Illumination where the illumination plane is conjugate to the objective pupil plane (BFP)
</p>

Besides optical components, the **UC2** building blocks can also host electronics such as **Arduinos** or **ESP32s** to create ''smart'' functions like LED array illumination, Z-stages, et cetera. Communication can be granted through the wired **I²** BUS or the wireless **MQTT** protocol.

**UC2** is in active development. It is meant to be used not only by beginners, but also for professionals dealing with optical setups on a daily basis. Its magnetic click-and-go concept simplifies the process of aligning and adjusting the parts giving new tools acting as rapid-prototyping devices. It also comes with a series of open-source workshops (in the future) explaining the theory behind optics.

People are also encouraged to share their work. We are curious what the community is doing with our little blocks. All necessary details to modify the design of the blocks are given in the sub-folders of the specific folders. Share your ideas through our [@openUC2-Twitter account](https://twitter.com/openuc2).

With the version UC2_v3 we introduced an **injection moulded (IM) cube**. This makes the assembly easier becuase no screws or magnets are needed for the Base Cube. But there is also a **3D-printed (3DP) cube** that is alternative to the IM one an it is fully compatible - the cubes and baseplates can be arbitrarily combined.   
Find out more about the two different Cube designs in [ASSEMBLY_CUBE_Base](./CAD/ASSEMBLY_CUBE_Base) and more about the baseplate puzzles in [ASSEMBLY_Baseplate](./CAD/ASSEMBLY_Baseplate).

*We are working on making the IM Cubes and Puzzles available for sale, but we are not able to offer a 'BUY' button yet. If you are interested in buying some components, contact us via email info@useetoo.org*

A full cube + base-plate looks like that:
<p align="center">
<img src="./IMAGES/Assembly_Cube_IM_explosion.png" height="300">
<img src="./IMAGES/Assembly_Cube_3DP_explosion.png" height="300">
<br> Fig. 2: Assembly of the cube + base-plate; <br>
LEFT: IM Cube - Two identical halves of the Cube are pressed together, the Cube connects to the baseplate via lego-like pins; <br>
RIGHT: 3DP Cube - A set of ferro-magnetic screws hold the lid and base-cube in place and connect to four 5mm Neodym ballmagnets sitting in the baseplate, and extra set of M5 screws further fixes the cube to the baseplate and supports the alignment; Optical components find their place inside the cube.
</p>

:grey_exclamation: If you are still working with the v2 version of the cube, you find the documentation in the [UC2_v2 branch](https://github.com/bionanoimaging/UC2-GIT/tree/UC2_v2). Check out the Modular Developer Kit to learn about the [UC2 version history](./MDK#uc2-version-history).

**UC2** can be used with cameras from the Raspberry Pi world, but creates even more beautiful images with your cellphone. Thus making cutting edge-research not only affordable, but also available.
A more in-detail project description can be found in the [UC2 White-Paper](./TUTORIALS/DOCUMENTS/UC2_Whitepaper.pdf)

## UC2 as an "open-standard"

The idea is to use **UC2** as an open-standard or bridge to external hardware components and devices such as cameras or lenses. An already existing or customized adapter/insert creates the link to the **UC2** eco-system. A variety of ready-to-use adapters can be found in the folder [CAD](./CAD).

<p align="center">
<img src="./IMAGES/MDK.jpg" width="550">
<br> Fig. 3: The structure of any UC2 assembly follows the green lines; A basic cube can hold an insert thus adapting to different components (i.e. lenses, etc.); A number of assembled cube-modules can form a complex optical system here called application
</p>

A more in-detail description of the **MDK** (**M**odular **D**eveloper **K**it) which explains how ***your idea*** can be adapted to the module system can be found in the [MDK](./MDK)-folder. There you also found an explanation about the UC2 version history, if you found some confusing information through the repository.

If you have a new part, we are eager to see it. Please feel free to share it on available websites like Twitter, Thingiverse, Github or any other platform of choice!

### Read more about the project in our papers:
The UC2 paper: A versatile and customizable low-cost 3D-printed open standard for microscopic imaging is available on [Nature Communications](https://www.nature.com/articles/s41467-020-19447-9) [![DOI:10.1038/s41467-020-19447-9](http://img.shields.io/badge/DOI-10.1038/s41467_020_19447_9-000000.svg)](https://doi.org/10.1038/s41467-020-19447-9)
All data from the paper is available in [Zenodo](https://doi.org/10.5281/zenodo.4018965) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4018965.svg)](https://doi.org/10.5281/zenodo.4018965)  
The Pre-print of the SIM+ISM paper is available on [Biorxiv](https://www.biorxiv.org/content/10.1101/2021.01.08.425840v1)  [![DOI:10.1101/2021.01.08.425840](http://img.shields.io/badge/DOI-10.1101/2021.01.08.425840-B31B1B.svg)](https://doi.org/10.1101/2021.01.08.425840)  
The COSI conference paper is out on [OSA](https://www.osapublishing.org/abstract.cfm?uri=ISA-2019-ITh3B.5)  [![DOI:10.1364/ISA.2019.ITh3B.5](http://img.shields.io/badge/DOI-10.1364/ISA.2019.ITh3B.5-36449F.svg)](https://doi.org/10.1364/ISA.2019.ITh3B.5)


Where next? [<img src="./IMAGES/sitemap.png" height=50>](./SITEMAP.md)

### Complete overview of setups, modules, parts to buy and parts to print
Find a complete shopping'n'printing list including estimated prices for all modules and setups in this [BILL OF MATERIALS](https://docs.google.com/spreadsheets/d/1U1MndGKRCs0LKE5W8VGreCv9DJbQVQv7O6kgLlB6ZmE/edit?usp=sharing)!

### List of available Setups

Our goal is to make as many setups as possible available, so that people can play with it. Basically everything's possible, you just need to think in blocks! Please have a look in the [APPLICATIONS](./APPLICATIONS/Readme.md) folder for the up to date list of the setups.

<p align="center">
<img src="./IMAGES/UC2_Holography.png" width="300">
<br> Fig. 4: In-line holographic microscope
</p>

### Repositories

Currently, **UC2** consists of the following repositories:

 - [UC2 Hardware Repo (core)](https://github.com/bionanoimaging/UC2-GIT/) (this repository) - [SITEMAP](./SITEMAP.md)
 - [UC2 Software Control Repo](https://github.com/bionanoimaging/UC2-Software-GIT)
 - [UC2+ImJoy Image Processing Repo](https://github.com/bionanoimaging/UC2-ImJoy-Plugins)

### Software

There is a GitHub repository dedicated for the UC2 software. It can be found [here](https://github.com/bionanoimaging/UC2-Software-GIT).
It supports you with controller APPS for the Raspberry Pi and Android Cellphones.

### Workshops

The documented workshops can be found in the folder [WORKSHOP](./WORKSHOP) and give a step-by-step introduction into the system. We have done multiple workshops together with the HHMI Janelia Farm, UiO Oslo, Lichtwerkstatt Jena and Leibniz IPHT Jena e.V.  
If you're interested we are happy to host one near you!

## Get Involved

This project is open so that anyone can get involved. You don't even have to learn CAD designing or programming. Find ways you can contribute in  [CONTRIBUTING](CONTRIBUTING.md)


## Kits, License and Collaboration

This project is open-source and is released under the CERN open hardware license. Our aim is to make the kits commercially available.
We encourage everyone who is using our Toolbox to share their results and ideas, so that the Toolbox keeps improving. It should serve as a easy-to-use and easy-to-access general purpose building block solution for the area of STEAM education. All the design files are generally for free, but we would like to hear from you how is it going.

You're free to fork the project and enhance it. If you have any suggestions to improve it or add any additional functions make a pull-request or file an issue.

Please find the type of licenses [here](./License.md)

REMARK: All files have been designed using Autodesk Inventor 2019 (EDUCATION)

## Showcase

This is the mess you can end up during Fourier-optics session using UC2 components. Pure-fun! :-)

<p align="center">
<img src="./IMAGES/UC2_workshop.jpg" width="400">
</p>

## Credits
If you find this project useful, please like this repository, follow us on Twitter and cite the webpage! :-)

*B. Diederich, R. Lachmann, B. Marsikova, E. Bingöl, S. Carlstedt, X. Uwurukundo, H. Wang, R. Heintzmann, Lichtwerkstatt, IPHT Jena, HHMI Janelia Farm, UiO Oslo, NorMic  and many more*
