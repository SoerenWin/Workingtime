# Workingtime

### Description of usage
This tool helps tracking your daily working time. You can choose between two different versions of this tool by switching the branch. You can either only store your data in .txt documents for each day or additionally upload the data to a MySql- or MariaDB-database. 

#### Standard version
In order to use the standard version, you just have to run the “main.py” file on your computer. Make sure to have a python3 interpreter installed. After running the file, it should ask you for your name and the point in time that you started working at today. After that you can choose what you want to do next by yourself. You can quit and rerun the program without any problems and loss of data at any point in time by simply typing in an “e” and pressing the return button on your keyboard. Your data will be saved in a .txt file with the title “workingtime_<today’s date>.txt” so you can always review your information or even change it within the text file. You can find this file in the same directory, you stored your “main.py” file in. After some time you will have a text file for every single day so you can always go back in time and look up your working time in the past. When you inserted all your information at the end of the day, you can “finish” your day. By doing that, your final working and break time will be calculated and saved but you can still change these afterwards if you like. For that you simply have to “finish” your day again. 

#### Database version
In this version you can not only store your information in a .txt file but also upload them to a MySql- or MariaDB database. For that you simply have to insert your database information into the source code once before running the program. The parts to be filled are marked with “<>” characters. Besides that, the program works just like the standard version. You just have to be careful that you really commit your changes to the database when you are asked to do so. Remember that this is only possible when you have already “finished” your day. You can overwrite your information in the database easily. Again it is just important that you remember to “finish” your day after changing some information.
Important: In order to use the database version, you need the required MySql-connector-package to be installed. For that navigate to the Script directory within your terminal or command prompt and type in the command 

    python -m pip install mysql-connector-python
