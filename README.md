# file_organizer

Objective:
Tool created to help organize photos taken during field assessments. 

Overview:
When performing field work it is commom to take photos of a site, then put them in a directory back at the office. 
This script helps organize these files. The example below will help illustrate what this script does.



Requirements:
Python 2.7
Written to refect windows file system \\

Instructions:
1: Download repo

At command line
2: CD to repo
3: python directory_creator.py
4: provide name to directory to store output. ie - C:\Users\username\Desktop\StructurePhotos
    directory does not have to exist, but must be empty if an existing directory is provided
5: provide list of directories to create, separated by commas. ie - site 1, site 2, site 3
--
6: manually place photos into corresponding directories
--
At command line
7: python file_organizer.py
8: provide same file path as in step 4

