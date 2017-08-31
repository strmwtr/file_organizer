import os

def rename_files():
    ''' Takes the output file from directory_creator.py and renames files to 
    reflect subdirectory names'''
    #Provide the same file provided in directory_creator.py
    dirs = raw_input('File provided to directory_creator.py: ')

    #Setup counter
    counter = 0
    
    #List subdirectories of dirs
    for dir in os.listdir(dirs):
        #Create absolute path to subdirectory
        subdir = os.path.join(dirs,dir)
        #For the files in each subdirector of dirs
        for old_file_name in os.listdir(subdir):
            #New filename is <subdirectory>__<counter>
            new_file_name = os.path.basename(subdir)+ '__{}'.format(counter) 
            #Gets the file extension
            file_ext = old_file_name.split('.')[-1]
            #Combines subdirectory with new_file_name and file_ext,
            #forms absolute path name of new file
            new_file_path = os.path.join(subdir,new_file_name + '.' + file_ext)
            #Gets the existing path name
            old_file_path = os.path.join(subdir,old_file_name)
            #Replaces existing pathname with updated path name
            os.rename(old_file_path, new_file_path)
            #Increases counter by 1
            counter += 1
            
rename_files()