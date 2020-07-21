import setuptools

with open('README.md','r') as fh:
    long_description = fh.read()

setuptools.setup(
    name="lapymod",
    version="1.0.3",
    author="Lag",
    author_email="no@email.com",
    description="A simple wrapper for Labymod's API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lag/lapymod",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
