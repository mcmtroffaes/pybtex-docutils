# -*- coding: utf-8 -*-

from setuptools import setup
import codecs


def readfile(filename):
    with codecs.open(filename, encoding="utf-8") as stream:
        return stream.read().split("\n")

doclines = readfile("README.rst")
requires = readfile("requirements.txt")
version = readfile("VERSION")[0].strip()

setup(
    name='pybtex-docutils',
    version=version,
    url='https://github.com/mcmtroffaes/pybtex-docutils',
    download_url='http://pypi.python.org/pypi/pybtex-docutils',
    license='MIT',
    author='Matthias C. M. Troffaes',
    author_email='matthias.troffaes@gmail.com',
    description=doclines[0],
    long_description="\n".join(doclines[2:]),
    zip_safe=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Text Editors :: Text Processing',
        'Topic :: Text Processing :: Markup :: XML'
    ],
    platforms='any',
    py_modules=['pybtex_docutils'],
    install_requires=requires,
    use_2to3=True,
    entry_points={
        'pybtex.backends': [
            'docutils = pybtex_docutils:Backend',
        ]
    },
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
)
