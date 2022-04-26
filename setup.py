from setuptools import find_packages
from setuptools import setup
import pathlib

here = pathlib.Path(__file__).parent
readme = (here/"README.md").read_text()

setup(
    name='deployingtestpack',
    version='2.0.0',
    description='deployingtestpack',
    long_description=readme,
    long_description_content_type = "text/markdown",
    url="https://github.com/Dlubal-Software/RFEM_Python_Client",
    author="Dlubal Software",
    author_email="info@dlubal.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9"
    ],
    packages="deployingtestpack",
    include_package_data=True,
    install_requires=["requests", "six", "suds-py3", "xmltodict", "pytest", "mock", "setuptools"],
    zip_safe = False
)