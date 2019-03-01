from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("search_c.pyx")
)

# rm -R __pycache__

# python setup.py build_ext --inplace