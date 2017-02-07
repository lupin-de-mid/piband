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
    install_requires=[
        'gattlib==0.20150805',
    ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: System :: Hardware :: Hardware Drivers',
        'Operating System :: POSIX :: Linux'
    ],
    zip_safe=False)
