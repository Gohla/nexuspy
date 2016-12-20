from setuptools import setup

dependencies = [
  'requests'
]

setup(
  name='nexuspy',
  version='0.1.0',
  description='Wrapper for (parts of) the Nexus Repository API',
  url='http://github.com/Gohla/nexuspy',
  author='Gabriel Konat',
  author_email='g.d.p.konat@tudelft.nl',
  license='Apache 2.0',
  packages=['nexuspy'],
  install_requires=dependencies,
  test_suite='nose.collector',
  tests_require=['nose>=1.3.7'] + dependencies
)
