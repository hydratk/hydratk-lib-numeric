.. install_lib_numeric:

Numeric
=======

You have 2 options how to install Numeric library.

Package
^^^^^^^

Install it via Python package managers PIP or easy_install.
Filename after PIP download contains version, adapt sample code.

  .. code-block:: bash
  
     $ sudo pip download hydratk-lib-numeric
     $ sudo pip install hydratk-lib-numeric.tar.gz 
     
  .. code-block:: bash
  
     $ sudo easy_install hydratk-lib-numeric
     
  .. note::
  
     Use PIP to install package from local file for correct installation.
     When installed from remote repository, PIP sometimes doesn't call setup.py.     

Source
^^^^^^

Download the source code from GitHub or PyPi and install it manually.
Full PyPi URL contains MD5 hash, adapt sample code.

  .. code-block:: bash
  
     $ git clone https://github.com/hydratk/hydratk-lib-numeric.git
     $ cd ./hydratk-lib-numeric
     $ sudo python setup.py install
     
  .. code-block:: bash
  
     $ wget https://pypi.python.org/pypi/hydratk-lib-numeric -O hydratk-lib-numeric.tar.gz
     $ tar -xf hydratk-lib-numeric.tar.gz
     $ cd ./hydratk-lib-numeric
     $ sudo python setup.py install
     
  .. note::
  
     Source is distributed with Sphinx (not installed automatically) documentation in directory doc. 
     Type make html to build local documentation however is it recommended to use up to date online documentation.     
     
Requirements
^^^^^^^^^^^^

Several python modules are used.
These modules will be installed automatically, if not installed yet.

* hydratk
* matplotlib
* numpy
* scipy
* sympy

Module matplotlib requires library which will be installed via Linux package managers, if not installed yet.

  .. note ::
     
     Installation for Python2.6 and 3.3 is not supported due to key module numpy.

  .. note ::
  
     Installation for Python3 has some differences.
     Library python3-tk or python3-tkinter is installed instead of python-tk or tkinter. 
     
  .. note ::
  
     Installation for PyPy has some differences.
     Modules matplotlib, scipy are not supported and installed.      

matplotlib

* apt-get: python-tk
* yum: tkinter 
    
Installation
^^^^^^^^^^^^

See installation example for Linux based on Debian distribution, Python 2.7. 

  .. note::
  
     The system is clean therefore external libraries will be also installed (several MBs will be downloaded)
     You can see strange log messages which are out of hydratk control. 
     
  .. code-block:: bash
  
     **************************************
     *     Running pre-install tasks      *
     **************************************

     *** Running task: version_update ***

     *** Running task: install_libs ***

     Installing package python-tk

     *** Running task: install_modules ***

     Installing module hydratk
     Installing module numpy>=1.12.1
     Installing module matplotlib>=2.0.0
     Installing module scipy>=0.19.0
     Installing module sympy>=1.0
     running install
     running bdist_egg
     running egg_info
     creating src/hydratk_lib_numeric.egg-info

     Installed /usr/local/app/venv/p27/lib/python2.7/site-packages/hydratk_lib_numeric-0.1.0-py2.7.egg
     Processing dependencies for hydratk-lib-numeric==0.1.0
     Finished processing dependencies for hydratk-lib-numeric==0.1.0           
        
Run
^^^

When installation is finished you can run the application.

Check hydratk-lib-numeric module is installed.

  .. code-block:: bash
  
     $ pip list | grep hydratk-lib-numeric

     hydratk-lib-numeric (0.1.0)    
     
Upgrade
=======

Use same procedure as for installation. Command options --upgrade (pip, easy_install) or --force (setup.py) are not necessary.

Uninstall
=========    

Run command htkuninstall numeric.          