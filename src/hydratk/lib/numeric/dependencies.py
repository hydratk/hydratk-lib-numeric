# -*- coding: utf-8 -*-
"""Library module dependency definitions
.. module:: lib.numeric.dependencies
   :platform: Unix
   :synopsis: Library core module dependency definitions
.. moduleauthor:: Petr Rašek <bowman@hydratk.org>
"""

from platform import python_implementation

dep_modules = {
  'hydratk'    : {
                  'min-version' : '0.4.0',
                  'package'     : 'hydratk'
                 },    
  'numpy'      : {
                  'min-version' : '1.12.1',
                  'package'     : 'numpy'
                 },   
  'sympy'      : {
                  'min-version' : '1.0',
                  'package'     : 'sympy'
                 }                                                                                                                                                                                                                                                                                                                
}

def get_dep_modules():
    """Method returns dependent modules
        
    Args:  
       none        
           
    Returns:
       dict          
                
    """ 
    
    if (python_implementation() != 'PyPy'):
        dep_modules['matplotlib'] = {'min-version' : '2.0.0',  'package' : 'matplotlib'}     
        dep_modules['scipy']      = {'min-version' : '0.19.0', 'package' : 'scipy'}     
    
    return dep_modules 