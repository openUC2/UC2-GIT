# Contribute to UC2

This project is open so that anyone can get involved. We welcome all community contributions to the UC2 project. Every contribution is meaningful, whether you catch bugs, make performance improvements, and help with documentation. We appreciate your time and effort to make open-science great!

When contributing to our project, please first discuss the change you wish to make via issue, email *info@useetoo.org*, or any other method with the maintainers of this repository before making a change. The following lines are mostly guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request.

Please follow our [Code of Conduct](./CODE_OF_CONDUCT.md) when making a contribution.

## Contributing for the first time
It's always hard the first time you do something. Everything new is scary. But we'd like to encourage you to join our project because every contribution, huge or tiny, helps us to improve. You don't even have to learn CAD designing or programming, there are other ways of contributing.

Where to start? Have a look at our [TUTORIALS](./TUTORIALS), especially at the [First steps with GitHub](./TUTORIALS#github). There you find links to guidelines tp GitHub contributions for beginners.

## How can I contribute? :muscle:
Things in need of attention are currently described in issues so have a look there if you'd like to work on something but aren't sure what.

### Become a UC2 builder :construction_worker:
* The UC2 toolbox or its parts could be useful in your work? Give it a try!
* Share your results - setups you've built or things you've seen with them - on Twitter using [#openUc2](https://twitter.com/search?q=%23openUc2&src=typed_query)
* Fork it, and make pull requests - documentation improvements are every bit as useful as a new design or software improvement
* Propose adding your results to the APP's README in a pull request - [Issue #27](https://github.com/bionanoimaging/UC2-GIT/issues/27)
  * Include: the image of the setup you've build, an image of what you've seen with it, your name and institution (if relevant)
* You've built your setup following the [TUTORIALS](./TUTORIALS)? Suggest an improvement there - [Issue #26](https://github.com/bionanoimaging/UC2-GIT/issues/26)

### Documentation :pencil:
* Get involved in discussions in the [ISSUE-section](https://github.com/bionanoimaging/UC2-GIT/issues).
* Raise an issue if you spot something that's wrong, or something that could be improved. This includes the instructions/documentation.
  * Improve assembly tutorial if you found out there's an important of anyhow useful information missing
  * Create alignment tutorial with images of a setup that you've built and doesn't have a detailed tutorial yet
  * Suggest better text or images for the instructions

### Hardware :hammer:
* We support you with the basic CAD design files, so that you can develop specific hardware-function which can fit in our cubes.
* We provide a brief tutorial on how to design an insert which adapts any part to the UC2 system. Please find it [here](./CAD/ASSEMBLY_CUBE_Base_v2/#tutorial-on-how-to-design-an-insert-in-inventor) on how to design an insert in Inventor.
* Improve the design of parts. STL files or descriptions of changes are helpful, even if you don't use OpenSCAD or Inventor.

### Software :computer:
* Our software-oriented [UC2-SOFTWARE-GIT](https://github.com/bionanoimaging/UC2-Software-GIT) provides you with all the different programs that you need to automate your blocks
* Run our GUI on [RasPi](https://github.com/bionanoimaging/UC2-Software-GIT/tree/master/GUI/RASPBERRY_PI/RASPIapp_py3) or [Android-Phone](https://github.com/bionanoimaging/UC2-Software-GIT/tree/master/GUI/Android/UC2-TheBox)
  * Report bugs or other issues
* Setup your [Arduino](https://github.com/bionanoimaging/UC2-Software-GIT/tree/master/HARDWARE_CONTROL/ARDUINO) or [ESP32](https://github.com/bionanoimaging/UC2-Software-GIT/tree/master/HARDWARE_CONTROL/ESP32)
* We want to generalize our Software to integrate even more with community standards and have an overall compatibility with different Operating Systems. Get **INVOLVED** by:
  * switching to a new browser-based GUI
  * improving our MQTT based connection routines and trying to improve the necessary hardware-flashes
  * adding totally unknown functions
  * making our Software as modular as possible
