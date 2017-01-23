from distutils.core import setup

from setuptools import find_packages

setup(
    name='piband',
    version='0.0.1',
    packages=find_packages(),
    url='https://github.com/lupin-de-mid/piband',
    license='GPL-3',
    author='Demid Lupin',
    author_email='lupin@demid.su',
    description='Python interface for mi band ',
    long_description='Python interface to interact with Xiaomi mi band fitness tracker',
    keywords='bluetooth low-energy ble miband xiaomi',
)
