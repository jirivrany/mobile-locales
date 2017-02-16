#!/bin/sh
virtualenv env
./env/bin/pip install requests
./env/bin/pip install pandas
source env/bin/activate
python downloader.py
