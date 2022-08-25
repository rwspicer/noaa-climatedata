"""
setup script
"""
from setuptools import setup,find_packages
import climatedata

config = {
    'description': (
        'Python interface for accessing Noaa climatedata API'
    ),
    'author': 'Rawser Spicer',
    'url': climatedata.__url__,
    'download_url': climatedata.__url__,
    'author_email': 'rwspicer@alaska.edu',
    'version': climatedata.__version__,
    'install_requires': [
        'pandas',
        'validators',
        'requests',
  
    ],
    'packages': find_packages(),
    'scripts': [],
    'package_data': {},
    'name': 'NOAA-climatedata'
}

setup(**config)
