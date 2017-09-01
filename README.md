# file_organizer

Objective:
Tool created to help organize files. Created with photos in mind, but any stand alone file could be reorganized with this script. 

Overview:
directory_creator.py creates directory tree based on list of names and location provided by user. </n>
User then manually places files into appropriate folders created by directory_creator.py. </n>
file_organizer.py then renames each file in the folder with the structure [directory_name]__[counter].[extension]


Requirements:

Python 2.7

Windows OS 

Instructions:

1: Download repo via github

2: CD to repo

3: python directory_creator.py

4: provide name to directory to store output. ie - C:\Users\username\Desktop\StructurePhotos
    directory does not have to exist, but must be empty if an existing directory is provided

5: provide list of directories to create, separated by commas. ie - site 1, site 2, site 3

6: manually place photos into corresponding directories

7: python file_organizer.py

8: provide same file path as in step 4

