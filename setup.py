"""
	Recommender
	-----
	recommender is a recommendation application using either item-based or user-based approaches

	:copyright: (c) 2016 - 2019 by Tran Ly Vu. All Rights Reserved.
    :license: Apache License 2.0
"""


from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='recommender',
    version="1.1.0",
    author='Tran Ly Vu',
	author_email='vutransingapore@gmail.com',
	maintainer='Tran Ly Vu <vutransingapore@gmail.com>',
	maintainer_email='vutransingapore@gmail.com',
	description='A recommendation application using either item-based or user-based approaches',
	long_description=long_description,
	long_description_content_type="text/markdown",
	url='https://github.com/tranlyvu/recommender',
	packages=find_packages(where="recommender", exclude=['docs', 'tests*']),
    package_dir={'':'recommender'},
	license='Apache License 2.0',
  	download_url='https://github.com/tranlyvu/recommender/releases', 
    classifiers=[
    	'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
		"License :: OSI Approved :: Apache Software License ",
		"Operating System :: OS Independent",
		"Development Status :: 5 - Production/Stable",
		'Intended Audience :: Science/Research',
		"Natural Language :: English",
		"Environment :: Console",
		'Topic :: Scientific/Engineering :: Artificial Intelligence',
	],
	keywords=['recommender', "Artificial Intelligence"],
	project_urls={
	    'Source': 'https://github.com/tranlyvu/recommender',
	    'Tracker': 'https://github.com/tranlyvu/recommender/issues',
	    'Chat: Gitter': 'https://gitter.im/recommender/Lobby',
	    'CI: Travis': 'https://travis-ci.org/tranlyvu/recommender',
	    'Coverage: coveralls': 'https://coveralls.io/github/tranlyvu/recommender',
	},
	py_modules=["six"],
	python_requires='>=2.6, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*, <4',
	tests_require = [
    	'pytest',
    ]
)