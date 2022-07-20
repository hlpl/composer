#! /usr/bin/python
from setuptools  import setup
import os
import sys
import platform
import configparser

from io import open
# to install type:
# python setup.py install --root=/
LONG_DESCRIPTION=open('README.md','r',encoding='utf8').read()        
        
if sys.version_info[0] < 3:
    raise Exception(
        'You are tying to install ChatterBot on Python version {}.\n'
        'Please install ChatterBot in Python 3 instead.'.format(
            platform.python_version()
        )
    )
 
REQUIREMENTS = []

"""
with open('requirements.txt') as requirements:
    for requirement in requirements.readlines():
        REQUIREMENTS.append(requirement)"""
            
config = configparser.ConfigParser()
current_directory = os.path.dirname(os.path.abspath(__file__))
config_file_path = os.path.join(current_directory, 'hlpl_composer/setup.cfg')
config.read(config_file_path)

VERSION = config['hlpl_composer']['version']
AUTHOR = config['hlpl_composer']['author']
AUTHOR_EMAIL = config['hlpl_composer']['email']
URL = config['hlpl_composer']['url']


projects_urls={}
for i in range(4,len(list(config['hlpl_composer'].keys()))):
    x=list(config['hlpl_composer'].keys())[i]
    y=x
    if i>3:
       y=y[0:len(y)-4]
    projects_urls[y]=config['hlpl_composer'][x]
    

setup (name='hlpl_composer', version=VERSION,
      description='Text composer and analyser',
      long_description_content_type='text/markdown',  
      long_description = LONG_DESCRIPTION,       
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      url=URL,
      download_url=URL+'/download/',
      project_urls=projects_urls,      
      python_requires='>=3, <3.9',
      license='MIT',
      platform="OS independent",
      keywords=['hlpl_composer', 'hlpl composer', 'hlpl-composer', 'text composer', 'text analyser', 'hlpl'],
      package_dir={'hlpl_composer': 'hlpl_composer',},
      packages=['hlpl_composer'],
      install_requires=REQUIREMENTS,         
      include_package_data=True,
      entry_points ={
        'console_scripts': [
                'hlpl_composer = hlpl_composer.hlpl_composer:main',
            ]},   
      classifiers=[
          'Framework :: Robot Framework',
          'Framework :: Robot Framework :: Library',
          'Framework :: Robot Framework :: Tool',
          'Natural Language :: Arabic',
          'Natural Language :: English',
          ],
                  
    );
