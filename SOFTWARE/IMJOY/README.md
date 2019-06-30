# ImJoy Project Template
This is a template for project layout we propose for projects supporting ImJoy plugins. The overall organization is standard and your code can very well be use without ImJoy. Two additional elements allow the direct use with ImJoy:

0. Folder **`imjoy-plugins`**: contains the ImJoy plugin files (extension 'imjoy.html'). 
1. File **`manifest.imjoy.json`**: specifies how your ImJoy plugins will be shown in the ImJoy plugin import menu

## Creating url to automatically install your plugins
The ImJoy plugin files can be used to [generate a url](http://imjoy.io/docs/index.html#/development?id=distributing-your-plugin-with-url) which automatically opens ImJoy and installs your plugin with all dependencies. 

This example install the template plugin: [Template Plugin](https://imjoy.io/#/app?plugin=https://raw.githubusercontent.com/oeway/ImJoy-project-template/master/imjoy-plugins/templatePlugin.imjoy.html)

Once the plugin is installed, click `Template Plugin` in the plugin menu and follow the instructions in the dialog to install the Python Plugin Engine. You can then execute the plugin. 

### Using tags
ImJoy plugins can have different **[tags](http://imjoy.io/docs/index.html#/development?id=plugins-and-tags)** determining how the plugin is shown in the interface and how it is executed, e.g. to allow processing either on a CPU or GPU. These tags can be set in the url, and you can provide different options to the user.  





