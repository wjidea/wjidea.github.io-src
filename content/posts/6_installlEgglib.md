Title: Compile Bio++ and install egglib on Ubuntu 14.04 LTS
Category: article
Date: 03-12-2016
Tags: python; bioinformatics; tutorials
Slug: installEgglib
Template: article
Status: published

I didn't find it difficult to install or compile the egglib module on Linux, when I first come to use egglib in python. However, things changed my mind when I was trying to use the internal function Align.polymorphismBPP(), which is a function that depends on the Bio++ library supoort. Somehow, I didn't install the C++ module correctly in the beginning, thus now I need to pay the price. 

Before we get into the installation, we need to make sure the pre-requisites by egglib and my local platform configuration.

####This tutorial was test on my platform:  
 
* Ubuntu Linux 14.04LTS
* [Bio-Linux](http://environmentalomics.org/bio-linux-installation/) installed
* Python 2.7.6
* GCC 4.8.2

#### Pre-requisites:

* cmake:  `sudo apt-get install cmake`
* doxygen:  `sudo apt-get install doxygen`
* [Bio++](http://biopp.univ-montp2.fr/wiki/index.php/Installation#Ubuntu.2FDebian_packages)'s install will be elaborated below

### Install dependencies
For egglib-cpp module, you will only need to the three libraries from Bio++: **bpp-core**, **bpp-seq**, and **bpp-popgen**. Keep this mind. I need to mention here, I downloaded everything in the download directory on my server. I am running all the code on an admin account, I ran everything using sudo to get root privilege. 

1.Update and upgrade system apps  
	
```sh
	sudo apt-get upgrade
	sudo apt-get update
```

2.Download installation files from Bio++

```sh
	mkdir ~/download/bpp
	cd ~/download/bpp
	wget http://biopp.univ-montp2.fr/repos/sources/bpp-core-2.2.0.tar.gz
	wget http://biopp.univ-montp2.fr/repos/sources/bpp-seq-2.2.0.tar.gz
	wget http://biopp.univ-montp2.fr/repos/sources/bpp-popgen-2.2.0.tar.gz
```

3.Unzip tar files:

```sh
	tar xzvf bpp-core-2.2.0.tar.gz  
	tar xzvf bpp-seq-2.2.0.tar.gz  
	tar xzvf bpp-popgen-2.2.0.tar.gz  
```

4.Compile each module. Make sure you don't have any errors when you try to run the make command

```sh
	cd ~/download/bpp/bpp-core-2.2.0
	cmake -DCMAKE_INSTALL_PREFIX=/usr/local
	make # make sure no errors, but warnings should be fine
	make install
	
	cd ../bpp-seq-2.2.0
	cmake -DCMAKE_INSTALL_PREFIX=/usr/local
	make
	make install
	
	cd ../bpp-pop-2.2.0
	cmake -DCMAKE_INSTALL_PREFIX=/usr/local
	make
	make install
```

5.Install linux dependencies for egglib-py. If you already installed the Bio-linux, most of the packages below should be already installed in your system. Just in case, I listed all the dependencies, install them as needed.

* gsl - GNU Scientific Library: `sudo apt-get install libgsl0ldbl`
* clustalw
* muscle
* paml
* phyml
* primer3
* phylip

### Install egglib
Obtain most recent version of egglib from [sourceforge-egglib](https://sourceforge.net/projects/egglib/). You will need download two files for this tutorial:

* egglib-cpp-2.x.xx.tar.gz
* egglib-py-2.x.xx.tar.gz

Compile the cpp package:

```sh
tar xvzf egglib-cpp-2.1.1.tar.gz
tar xvzf egglib-py-2.1.1.tar.gz
cd egglib-cpp-2.1.11
./configure
make
make install

cd ../egglib-py-2.1.11
sudo python setup.py build
sudo python setup.py install
```

### Test egglib installation
confirm your egglib was installed correctly

```sh
Python 2.7.6 (default, Jun 22 2015, 17:58:13)
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import egglib
>>> quit()
```

### References
This tutorial was built based on the resources available online:

[1]. [Building Bio++ and Egglib From Source](http://pmagwene.github.io/blog/2013/02/06/building-bio-plus-plus-and-egglib/) 

[2]. [tips on installing EggLib on linux](http://maojf.blogspot.com/2012/09/tips-on-installing-egglib-on-linux.html)






