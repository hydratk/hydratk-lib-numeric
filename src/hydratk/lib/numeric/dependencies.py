# -*- coding: utf-8 -*-
"""Library module dependency definitions
.. module:: lib.numeric.dependencies
   :platform: Unix
   :synopsis: Library core module dependency definitions
.. moduleauthor:: Petr Rašek <bowman@hydratk.org>
"""

dep_modules = {
  'hydratk'    : {
                  'min-version' : '0.4.0',
                  'package'     : 'hydratk'
                 },    
  'matplotlib' : {
                  'min-version' : '2.0.0',
                  'package'     : 'matplotlib'
                 },  
  'numpy'      : {
                  'min-version' : '1.12.1',
                  'package'     : 'numpy'
                 },  
  'scipy'      : {
                  'min-version' : '0.19.0',
                  'package'     : 'scipy'
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
    
    return dep_modules 