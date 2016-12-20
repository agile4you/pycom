from distutils.core import setup
from pycom import __version__

setup(
    name='pycom',
    version=__version__,
    packages=['pycom'],
    url='https://github.com/agile4you/pycom',
    license='GLPv3',
    author='Papavassiliou Vassilis',
    author_email='vpapavasil@gmail.com',
    description='Python development toolkit',
    extras_require={
        'test': ['pytest'],
    }
)
