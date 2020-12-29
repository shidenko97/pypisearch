import setuptools

from pypisearch import __version__ as version


with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

setuptools.setup(
    name="pypisearch",
    version=version,
    author="Serhii Hidenko",
    author_email="shidenko97@gmail.com",
    description="Replacement of temporarily deprecated pip search command",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shidenko97/pypisearch",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
