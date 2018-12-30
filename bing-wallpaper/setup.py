# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2018-12-30 15:22:17
# @Last Modified time: 2018-12-30 20:13:40
import setuptools
import pkg_resources
import sys
import os

try:
    if int(pkg_resources.get_distribution("pip").version.split('.')[0]) < 6:
        print('pip older than 6.0 not supported, please upgrade pip with:\n\n'
              '    pip install -U pip')
        sys.exit(-1)
except pkg_resources.DistributionNotFound:
    pass

this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

version = sys.version_info[:2]
if version < (2, 7):
    print('bing-wallpaper requires Python version 2.7 or later' +
          ' ({}.{} detected).'.format(*version))
    sys.exit(-1)
elif (3, 0) < version < (3, 4):
    print('bing-wallpaper requires Python version 3.4 or later' +
          ' ({}.{} detected).'.format(*version))
    sys.exit(-1)

install_requires = ['requests']
VERSION = '1.0.0'


setuptools.setup(
    name='BingWallpaper',
    version=VERSION,
    description="A python script which can download bing's beautiful images and set the image to your computer wallpaper.",
    long_description_content_type='text/markdown',
    author='LogicJake',
    author_email='chenyangshi1996@gamil.com',
    url='https://github.com/LogicJake/some-scripts/tree/master/bing-wallpaper',
    long_description=long_description,
    install_requires=install_requires,
    packages=setuptools.find_packages(),
    zip_safe=False,
    license='MIT',
    entry_points={'console_scripts': ['wallpaper = wallpaper.main:main']}
)
