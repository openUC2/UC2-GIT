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
* Result is an image stack in which each slice corresponds to a phase distribution at a given position along optical axis (on object-side)
 
## Development

### Prerequisites

What things you need to install the software and how to install them

```
Give examples
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

### Built With

* [Eclipse](http://www.eclipse.org/downloads/packages/) - IDE
* [Maven](https://maven.apache.org/) - Dependency Management

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system



## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

