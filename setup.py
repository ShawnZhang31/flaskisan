'''
/*
 * @Author: Shawn Zhang 
 * @Date: 2019-09-09 00:24:12 
 * @Last Modified by: Shawn Zhang
 * @Last Modified time: 2019-09-09 00:26:11
 */
'''
import setuptools
with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'flaskisan',
    version = '0.0.1',
    author = 'Shawn Zhang',
    author_email = 'shawnzhang31@gmail.com',
    description = 'A mini flask skeleton framworks little like laravel',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/ShawnZhang31/flaskisan.git',
    packages = setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)