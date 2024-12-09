from setuptools import setup, find_packages
setup(
    name="wrogn", 
    version="0.2.1",     
    author="gagandeep",
    author_email="kgagandeepvirat@example.com",
    description="A simple demonstration package",
    long_description="A derivative measures how a function changes as its input changes. It represents the rate of change or slope of the function at a particular point. In simple terms, the derivative tells us how fast something is changing. For example, in physics, the derivative of a position function gives the velocity",
    packages=find_packages(), 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)