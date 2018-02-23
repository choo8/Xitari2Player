from distutils.core import setup, Extension
import os.path, sys

xitari_c_lib = 'xitari_python_interface/libxitari_c.so'
if not os.path.isfile(xitari_c_lib):
  print('ERROR: Unable to find required library: %s. Please ensure you\'ve '\
    'built Xitari using CMake.'%(xitari_c_lib))
  sys.exit()

module1 = Extension('xtari_python_interface.xitari_c_wrapper',
                    libraries = ['xitari_c'],
                    include_dirs = ['agents', 'common', 'controllers', 'emucore', 'environment', 'games', 'os_dependent', 'zlib', './'],
                    library_dirs = ['xitari_python_interface'],
                    extra_compile_args=['-D__STDC_CONSTANT_MACROS', '-std=c++11'],
                    sources=['xitari_python_interface/xitari_c_wrapper.cc'])
setup(name = 'xitari_python_interface',
      version='0.4',
      description = 'Xitari (fork of Arcade Learning Environment v0.4) Python Interface',
      url='https://github.com/choo8/Xitari2Player',
      author='Joshua Choo',
      license='GPL',
      ext_modules = [module1],
      packages=['xitari_python_interface'],
      package_dir={'xitari_python_interface': 'xitari_python_interface'},
      package_data={'xitari_python_interface': ['libxitari_c.so']})