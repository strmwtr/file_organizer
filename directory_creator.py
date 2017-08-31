import os
import re
import sys

def prep_fldr():
    print 'Provide empty directory to store output of script'
    fldr = raw_input('Empty Output directory: ')
    if os.path.exists(fldr):
        pass
    else:
        os.mkdir(fldr)
    return fldr

def get_names():
    print "Provide list of names separated by commas"
    print "ex: Basketball, Softball, Hiking"
    name_string = raw_input().replace(' ','')
    name_list = name_string.split(',')

    dir_names = []
    for name_provided in name_list:
        dir_names.append(re.sub('\W', '', name_provided))
    return dir_names

def make_dirs():
    root = prep_fldr()
    dirs = get_names()
    for dir_name in dirs:
        full_path = root + '\\' + dir_name
        if os.path.exists(full_path):
            print "Output directory provided is not empty. Aborting script"
            sys.exit()
        else:
            os.mkdir(full_path)

make_dirs()
