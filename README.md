gsrchDwn
========

Python script to download files via google search

Requirements
============

In order to use the script you need to install Python 2.7 from http://www.python.org/getit/ and the following packages:

- setuptools: https://pypi.python.org/pypi/setuptools#installation-instructions
- xgoogle: https://github.com/pkrumins/xgoogle

For each package just run:
```
py setup.py build
py setup.py install
```

Usage
=====
```
py gsrchDwn.py --query [query_text] [--ftype file_extension] [--cnt contine_result_number] [--dir download_dir]
```
