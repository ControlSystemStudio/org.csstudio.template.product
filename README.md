# org.csstudio.template.product
A template product which can be used to create your own site specific product

The goal is to simplify the creation of a new site specific product.

## Quick start

* Clone the template product repository

>> git clone https://github.com/ControlSystemStudio/org.csstudio.template.product.git

* Refactor the name renaming "template" with site name

While refactoring one has to be careful to refactor all pom.xml and MANIFEST files

* Building the product

>> mvn clean verify 

## Understanding the architecture

The main components required for creating your own product are
The product definition file (.product), this is the file which defines the list of features that are to be included into your project.
(optional) a feature which contains configuration files like the plugin_customization.ini, authorization.conf
(optional) additional plugins and features that are site specific

Directory Structure:
The top level maven project for your product
```
|----[+]  features: The features module for all your site specific features.
|      |---- The feature containing the customization and configuration files.
|      |---- (optional) Additional features to be included in your product
|----[+]  (optional) plugins: The plugins module will contain all your site specific plugins.
|
|----[+] repository: The repository module which contains product definition file
```
