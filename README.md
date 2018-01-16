# Twitter Back Surgery

The key word for search is #backsurgery

The application get more data every 3 hours.
The first time will acquire data is not time 0 but rather at 3 hours....

Usage:
1. Install python anaconda from https://anaconda.org/anaconda/python
2. create a folder and name it what you want
3. download these files and unzip them
4. copy the files to the folder you Created
5. From the command line cd into the folder you created (example: cd /Documents/to/path)
6. when you are in the folder, create an anaconda environment by typing in the terminal: conda env create -f environment.yml  
7. activate the anaconda environement from the command line by typing: source activate twitter or activate twitter (depend on operating system)
8. run the file from terminal: python TwitterSchedule.py
9. when enough data is collected the file data.txt you can stop the application by doing control C
