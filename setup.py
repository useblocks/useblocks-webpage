"""
useblocks webpage
=================
"""
from setuptools import setup, find_packages
import re
import ast

_version_re = re.compile(r'__version__\s+=\s+(.*)')
with open('useblocks_webpage/version.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    name='useblocks webpage',
    version=version,
    url='http://useblocks webpage.readthedocs.org',
    license='MIT license',
    author='team useblocks',
    author_email='info@useblocks.com',
    description="Package for hosting groundwork apps and plugins like useblocks_webpage_app or useblocks_webpage_plugin.",
    long_description=__doc__,
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    platforms='any',
    setup_requires=['groundwork', 'groundwork_web', 'pytest-runner', 'sphinx', 'gitpython'],
    tests_require=['pytest', 'pytest-flake8'],
    install_requires=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    entry_points={
        'console_scripts': ["useblocks_webpage = "
                            "useblocks_webpage.applications.useblocks_webpage_app:start_app"],
        'groundwork.plugin': ["useblocks_webpage_introduction_plugin = "
                              "useblocks_webpage.plugins.ub_webpage_introduction.ubwebpageintroduction:"
                              "UbWebpageIntroduction"],
    }
)
