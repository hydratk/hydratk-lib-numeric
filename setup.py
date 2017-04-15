# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from sys import argv, version_info
import hydratk.lib.install.task as task

with open("README.rst", "r") as f:
    readme = f.read()
    
classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Environment :: Console",
    "Environment :: Other Environment",
    "Intended Audience :: Developers",
    "License :: Freely Distributable",
    "Operating System :: OS Independent",   
    "License :: OSI Approved :: BSD License",
    "Programming Language :: Python",    
    "Programming Language :: Python :: 2.6",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: Implementation",
    "Programming Language :: Python :: Implementation :: CPython", 
    "Programming Language :: Python :: Implementation :: PyPy",
    "Topic :: Software Development :: Libraries :: Application Frameworks",
    "Topic :: Utilities"
]     

def version_update(cfg):
    
    major = version_info[0]
    
    if (major == 3):
        cfg['libs']['matplotlib>=2.0.0']['apt-get'][0] = 'python3-tk'
        cfg['libs']['matplotlib>=2.0.0']['yum'][0] = 'python3-tkinter'

config = {
  'pre_tasks' : [
                 version_update,
                 task.install_libs,                 
                 task.install_modules
                ],
          
  'modules' : [   
               'hydratk',
               'numpy>=1.12.1',
               'matplotlib>=2.0.0',
               'scipy>=0.19.0',
               'sympy>=1.0'                                      
              ],
          
  'libs' : {
            'matplotlib>=2.0.0' : {
                                   'apt-get' : [
                                                'python-tk'
                                               ],
                                   'yum'     : [
                                                'tkinter'
                                               ]
                                  }
           }                                   
}    
    
task.run_pre_install(argv, config)                          
          
setup(
      name='hydratk-lib-numeric',
      version='0.1.0a.dev0',
      description='Libraries for numerical computing, data analysis',
      long_description=readme,
      author='Petr Rašek, HydraTK team',
      author_email='bowman@hydratk.org, team@hydratk.org',
      url='http://libraries.hydratk.org/numeric',
      license='BSD',
      packages=find_packages('src'),
      package_dir={'' : 'src'},
      classifiers=classifiers,
      zip_safe=False,
      keywords='hydratk,numerical computing,data analysis',
      requires_python='>=2.6,!=3.0.*,!=3.1.*,!=3.2.*',
      platforms='Linux'
     )        