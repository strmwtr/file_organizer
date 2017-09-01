import os
import re
import sys

def prep_fldr():
    '''Asks user for abs path to directory, then checks if directory exists, if
    directory does not exist, creates directory'''
    print 'Provide empty directory to store output of script'
    fldr = raw_input('Empty Output directory: ')
    if os.path.exists(fldr):
        pass
    else:
        os.mkdir(fldr)
    return fldr

def get_names():
    ''' Asks user for list, creates subdirectories in directory provided in 
    prep_fldr()'''
    print "Provide list of names separated by commas"
    print "ex: Basketball, Softball, Hiking"
    #Replace removes all blank spaces in string
    name_string = raw_input().replace(' ','')
    #Split creates list bases on string with commas as breakpoints
    name_list = name_string.split(',')

    #creates empty list to hold directory names
    dir_names = []
    #for each of the names in name_list
    for name_provided in name_list:
        #Append the name stripped of non-alphanumeic characters to dir_names
        dir_names.append(re.sub('\W', '', name_provided))
    return dir_names

def make_dirs():
    ''' Creates directory tree based on prep_fldr and get_names'''
    root = prep_fldr()
    dirs = get_names()
    #for each dir_name in dirs
    for dir_name in dirs:
        #Absolute path is root\\dir_name
        full_path = root + '\\' + dir_name
        '''If the subdirectory already exists, abort script. This avoids issues
        in file_organizer.py. We don't want to change anything other than the 
        intended files'''
        if os.path.exists(full_path):
            print "Output directory provided is not empty. Aborting script"
            sys.exit()
        else:
            os.mkdir(full_path)

make_dirs()
