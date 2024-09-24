from setuptools import setup, find_packages
import sys

if sys.platform != 'darwin':
    raise OSError("This package is only supported on macOS.")

setup(
    name="silica",
    version="0.0.4",
    description="Python GUI library for writing MacOS native apps using pyObjC and Cocoa",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/oliver408i/silica",
    install_requires=["pyobjc"],
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: MacOS :: MacOS X',
        'Intended Audience :: Developers',
        'Topic :: GUI :: MacOS',
    ],
)