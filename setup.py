#!/usr/bin/env python

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [ 'requests>=2.0.1' ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Mario Falcao",
    author_email='mario@bitsiders.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="Thin Python 3 wrapper for the InvoiceXpress REST API",
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    include_package_data=True,
    keywords='invoicexpress_api',
    name='invoicexpress_api',
    packages=find_packages(include=['invoicexpress_api']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/bitmario/invoicexpress-api-python',
    version='0.1.2',
    zip_safe=False,
)
