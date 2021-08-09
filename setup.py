import setuptools

from pypisearch import __version__ as version


with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

with open("requirements.txt", "r", encoding="utf-8") as file:
    requirements = file.read().splitlines()

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
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "pypisearch=pypisearch.__main__:main",
        ],
    },
)
