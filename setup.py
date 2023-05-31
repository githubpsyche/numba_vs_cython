from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy

package = Extension('operations', ['operations.pyx'], include_dirs=[numpy.get_include()])
setup(ext_modules=cythonize([package]))