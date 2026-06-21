# Installs python packages, launch files, config files, package.xml, 

from setuptools import setup
from glob import glob

package_name = 'localization'

setup(
name=package_name,
version='0.1.0',
packages=[package_name],

```
data_files=[
    ('share/ament_index/resource_index/packages',
     ['resource/' + package_name]),

    ('share/' + package_name,
     ['package.xml']),

    ('share/' + package_name + '/launch',
     glob('launch/*.py')),

    ('share/' + package_name + '/config',
     glob('config/*')),
],

install_requires=['setuptools'],

zip_safe=True,

maintainer='Rory O'Brien',
maintainer_email='rpobrien@tudelft.nl',

description='Localization package for MIRTE master tetris assembly robot',

license='MIT',

tests_require=['pytest'],

entry_points={
    'console_scripts': [
        'localization_node = localization.localization_node:main',
    ],
},
```

)
