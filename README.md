# file_organizer

Objective:
Tool created to help organize files. Created with photos in mind, but any stand alone file could be reorganized with this script. 

---

Overview:
directory_creator.py creates directory tree based on list of names and location provided by user. </n>
User then manually places files into appropriate folders created by directory_creator.py. </n>
file_organizer.py then renames each file in the folder with the structure [directory_name]__[counter].[extension]

---

Requirements:

Python 2.7

Windows OS 

---

Instructions:

1. Start with several unorganized standalone files


 ![file_organizer](https://github.com/strmwtr/file_organizer/blob/master/readme/example_files.PNG)


2. Open Command Prompt.


3. Change directory to where file_organizer folder is stored.


4. Run python script directory_creator.py


5. Provide path to where you want to store new photos at. New folder does not have to exist, but if an existing folder is provided it must be empty.


6. Provide groups to organize photos into, separated by commas.

 
 ![file_organizer](https://github.com/strmwtr/file_organizer/blob/master/readme/command_line_directory_creator.PNG)

 A screenshot of my command prompt window after running the script directory_creator.py


7. The script directory_creator.py will now create a new folder for each of the groups listed in the step above.

 ![file_organizer](https://github.com/strmwtr/file_organizer/blob/master/readme/directory_creator_output.png)
 
 Output of directory_creator.py

---


8. Drag and drop files into newly created folders

 ![file_organizer](https://github.com/strmwtr/file_organizer/blob/master/readme/pre_file_organizer_setup.PNG)
 
 My file structure after dragging and dropping the photos in appropriate folder

---


9. Run file_organizer.py . If you have not closed the command prompt from the above steps, simply run it from that window. If you have closed it, open the command line again and cd back to the folder file_organizer, then run the script.


10. Provide same path provided in directory_creator.py.

 ![file_organizer](https://github.com/strmwtr/file_organizer/blob/master/readme/command_line_file_organizer.PNG)
 
A screenshot of my command prompt window after running the script file_organizer.py


11. The script file_organizer.py will now rename each file in each folder with the structure [folder name]__[number].[extension].

 ![file_organizer](https://github.com/strmwtr/file_organizer/blob/master/readme/output_file_organizer.PNG)
 
 A screenshot of the result of running file_organizer.py

