from setuptools import setup, find_packages

setup(
	name="Tidal-Client",
	version="Alpha-1",
	packages=find_packages()
	
	install_requires=['tidal-api','ffmpeg-python'],
	
	author="Joe0400",
	author_email="joseph_scannell@student.uml.edu",
	classifiers=["WTFPL"]
	#TODO add GIT URL
)

