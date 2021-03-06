#!/usr/bin/env python


from setuptools import setup, find_packages

long_description = """
Small package with scripts to process Direct Readout Suomi NPP/VIIRS data from
RDR (level-0) to SDR (level-1). Uses the CSPP package from SSEC, Wisconsin, and
expects messages in pytroll format from the reception station telling when a
file is being dispatched to the server.
""" 

setup(name='npp_lvl1proc',
      description="Run scripts for Suomi NPP RDR to SDR processing",
      author="Adam Dybbroe",
      author_email="adam.dybbroe@smhi.se",
      url='',
      long_description=long_description,
      license='GPLv3',
      version='0.1',
      #packages = find_packages(),
      scripts = ['npp_dr_runner.sh', 'npp_dr_runner.py'],
      py_modules=['npp_dr_runner', 'cspp2pps', 'pre_cspp'],
      
      # Project should use reStructuredText, so ensure that the docutils get
      # installed or upgraded on the target machine
      install_requires = ['docutils>=0.3', 
                          'posttroll',
                          'numpy',
                          'pyorbital'
                          ],

      data_files=[('etc', ['etc/npp_dr_config.cfg'])],
      test_suite="nose.collector",
      tests_require=[],
      zip_safe=False
      )
