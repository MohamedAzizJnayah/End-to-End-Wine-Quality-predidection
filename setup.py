from setuptools import setup, find_packages
import setuptools

setup(
    name="ML_Project",
    version="0.1",
    author="Mohamed Aziz Jnayah",
    author_email="mohamedazizjnayah@gmail.com",
    description="Un projet de machine learning",
    url="https://github.com/MohamedAzizJnayah/End-to-End-Wine-Quality-predidection",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
    
)
