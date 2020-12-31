from setuptools import setup, find_packages

setup(
    name='botlistawrapper',
    author='ivall',
    author_email='ivallpl@gmail.com',
    install_requires=['requests'],
    version='1.0',
    description='Simple botlista.pl api wrapper in python.',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ivall/botlista-wrapper",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
