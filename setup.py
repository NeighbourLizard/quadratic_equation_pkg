import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="quadratic_equation_giarts",
    version="0.0.4",
    author="Giorgi Artsivadze",
    author_email="giarts@taltech.ee",
    description="Quadratic Equation Solver",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NeighbourLizard/quadratic_equation_pkg",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
