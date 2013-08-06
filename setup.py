# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import codecs


def readfile(filename):
    with codecs.open(filename, encoding="utf-8") as stream:
        return stream.read().split("\n")

doclines = readfile("README.rst")
version = readfile("VERSION")[0].strip()

setup(
    name='pybtex-docutils',
    version=version,
    url='https://github.com/mcmtroffaes/pybtex-docutils',
    download_url='http://pypi.python.org/pypi/pybtex-docutils',
    license='MIT',
    author="Matthias C. M. Troffaes",
    author_email='matthias.troffaes@gmail.com',
    description=doclines[0],
    long_description="\n".join(doclines[2:]),
    zip_safe=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Text Editors :: Text Processing',
        'Topic :: Text Processing :: Markup :: XML'
    ],
    platforms='any',
    packages=find_packages(),
    use_2to3=True,
    entry_points={
        'pybtex.backend': [
            'docutils = pybtex_docutils:Backend',
        ]
    },
)
