from distutils.core import setup


setup(
    name='pycom',
    version='0.0.1',
    packages=['test', 'pycom'],
    url='https://github.com/agile4you/pycom',
    license='GLPv3',
    author='Papavassiliou Vassilis',
    author_email='vpapavasil@gmail.com',
    description='Python development toolkit',
    extras_require={
        'test': ['pytest'],
    }
)
