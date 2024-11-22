# coding: utf-8

"""
    SDK

    算想云对开发者提供的API

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "sxwl-client"
VERSION = "1.0.2"
PYTHON_REQUIRES = ">= 3.8"
REQUIRES = [
    "urllib3 >= 1.25.3, < 3.0.0",
    "python-dateutil >= 2.8.2",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="SDK",
    author="OpenAPI Generator community",
    author_email="team@openapitools.org",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "SDK"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description="""\
    算想云对开发者提供的API
    """,  # noqa: E501
    package_data={"sxwl_client": ["py.typed"]},
)
