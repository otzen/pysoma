import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="test-pysoma",
    version="0.0.1",
    author="Wazombi Labs",
    author_email="labs@wazombi.com",
    description="A simple package for controlling SOMA devices",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ratsept/pysoma",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Home Automation",
    ],
)
