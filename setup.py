from setuptools import setup
setup(
	name='mics',
	version='0.01',
	author='Buys de Barbanson',
	author_email='code@buysdb.nl',
	description='Python module to read MICS-4514 MICS-6814 metal oxide sensors ',
	url='https://github.com/BuysDB/MICS-Python',
	py_modules=['mics'],
	install_requires=['Adafruit_ADS1x15']
)
