# encoding: utf-8
from distutils.core import setup,Extension
import sys, glob

define_macros=[('EIGEN_DONT_ALIGN',None)]
if sys.platform=='win32':
	libraries=['boost_python-mgw47-mt-1_51']
	library_dirs=[r'c:\src\boost_1_51_0\stage\lib']
	include_dirs=[r'c:\src\boost_1_51_0',r'c:\src\eigen-3.1.1']
	# SSE2 might cause DLL load error (ImportError: DLL load failed with error code -1073741795).
	# Until it is determined for sure, disable vectorization here. See also:
	# * http://matplotlib.1069221.n5.nabble.com/Problem-with-Basemap-and-Python-2-6-under-Windows-XP-td777.html
	# * https://bugs.launchpad.net/panda3d/+bug/919237
	define_macros+=[('EIGEN_DONT_VECTORIZE',None)]
else:
	libraries=['boost_python']
	library_dirs=[]
	include_dirs=['/usr/include/eigen3','minieigen']

setup(name='minieigen',
	version='0.4-1',
	author='Václav Šmilauer',
	author_email='eu@doxos.eu',
	url='http://www.launchpad.net/minieigen',
	description='Wrap parts of Eigen3, c++ library for basic math and geometry.',
	long_description='''
A small wrapper for core parts of Eigen (http://eigen.tuxfamily.org), c++ library for linear algebra. It is mainly useful for inspecting c++ code which already uses eigen and boost::python. Supported types are Vectors (2,3,6 and dynamic-sized with integer, floating-point and complex values), Matrices (3x3, 6x6 and dynamic-sized with floating-point and complex values), Quaternions and 2d and 3d aligned boxes. Numerous methods are wrapped and the original API of Eigen is followed. The code compiles with a c++99 compiler. The documentation is at http://flux.doxos.eu/minieigen .
''',
	classifiers=[
		'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
		'Programming Language :: Python',
		'Programming Language :: Python :: 3',
		'Operating System :: OS Independent',
		'Topic :: Scientific/Engineering :: Mathematics',
		'Intended Audience :: Science/Research',
		'Development Status :: 4 - Beta'
	],
	ext_modules=[Extension('minieigen',
		sources=['minieigen/minieigen.cpp',
			'minieigen/expose-boxes.cpp',
			'minieigen/expose-complex.cpp',
			'minieigen/expose-converters.cpp',
			'minieigen/expose-matrices.cpp',
			'minieigen/expose-quaternion.cpp',
			'minieigen/expose-vectors.cpp',
			'minieigen/double-conversion/bignum.cc',
			'minieigen/double-conversion/bignum-dtoa.cc',
			'minieigen/double-conversion/cached-powers.cc',
			'minieigen/double-conversion/diy-fp.cc',
			'minieigen/double-conversion/double-conversion.cc',
			'minieigen/double-conversion/fast-dtoa.cc',
			'minieigen/double-conversion/fixed-dtoa.cc',
			'minieigen/double-conversion/strtod.cc'
		],
		libraries=libraries,
		library_dirs=library_dirs,
		include_dirs=['minieigen']+include_dirs,
		define_macros=define_macros
	)],
)

