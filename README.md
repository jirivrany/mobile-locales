# mobile-locales
Python Tool for generating locales string files for Android an iOS developers.

## Requirements
Python 2.7.x
requests
pandas

## Usage
This tool generates locales for Android and iOS projects from one sigle source. This source can be 
sheet in Google Docs or local csv file. 

First row of the spreadsheet must contain header with lang codes and platform keys. Check out the [sample document](https://docs.google.com/spreadsheets/d/14L6Xrcwvs_DiLb0H3NApgwSrHf0BGgttuBlq1YsFmBQ) and generated outputs in the android an ios dirs. 

If you need to use the values only at one of the platforms, just put the NOT_EXIST as the key value for ommited platform.
