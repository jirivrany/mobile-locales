"""
@Author - Jiri Vrany <jiri.vrany@gmail.com>
@License - MIT
"""

from StringIO import StringIO  
import requests
import pandas as pd
import os

LANGS = ['fr', 'en', 'de', 'it', 'sk', 'cs', 'es', 'pt', 'ja']

def create_dir_ifnotexis(mpath):
    try:
        os.mkdir(mpath)
    except OSError:
        pass    

def get_dataframe_from_google(murl):

    r = requests.get(murl)
    data = r.content
    return pd.read_csv(StringIO(data))

def write_android_files(df):


    android = df[df['android_key'] != 'NOT_EXISTS']
    android = android.drop_duplicates()

    create_dir_ifnotexis('./android-output')

    android_head = """<?xml version="1.0" encoding="utf-8"?>\n<resources xmlns:tools="http://schemas.android.com/tools">\n"""

    android_foot = "</resources>\n"
    android_row = '<string name="{}">{}</string>\n' 


    for lang in LANGS:
        colname = "{}_value".format(lang)
        mpath = './android-output/values-{}'.format(lang)
        fpath = mpath + "/strings.xml"
        print fpath
        create_dir_ifnotexis(mpath)
        with open(fpath, 'w+') as f:
            f.write(android_head)
            for index, row in android.iterrows():
                f.write(android_row.format(row['android_key'], row[colname]))

            f.write(android_foot)    
        
def write_ios_files(df):
    ios = df[df['ios_key'] != 'NOT_EXISTS']
    ios_dir = './ios-output'    
    create_dir_ifnotexis(ios_dir)
    ios_row = '"{}" = "{}";\n'
    #normal rows
    for lang in LANGS:
        colname = "{}_value".format(lang)
        mpath = ios_dir + '/{}.lproj'.format(lang)
        fpath = mpath + "/Localizable.strings"
        print fpath
        create_dir_ifnotexis(mpath)
        with open(fpath, 'w+') as f:
            for index, row in ios.iterrows():
                f.write(ios_row.format(row['ios_key'], row[colname]))

    #base project
    colname = "en_value"
    mpath = ios_dir + '/Base.lproj'
    fpath = mpath + "/Localizable.strings"
    print fpath
    create_dir_ifnotexis(mpath)
    with open(fpath, 'w+') as f:
        for index, row in ios.iterrows():
            f.write(ios_row.format(row['ios_key'], row[colname]))            

if __name__ == '__main__':
    MURL = 'https://docs.google.com/spreadsheets/d/14L6Xrcwvs_DiLb0H3NApgwSrHf0BGgttuBlq1YsFmBQ/edit?usp=sharing'
    df = get_dataframe_from_google(MURL)
    write_android_files(df)
    write_ios_files(df)