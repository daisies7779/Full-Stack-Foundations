# Removes created db so that it is possible to start everything from scratch
# this script works
import os
files = []
files.append("restaurantmenu.db")
files.append("database_setup.pyc")
for file in files:
    os.remove(file)

# works but glob could keep one file per iteration
# should investigate what glob is, not enought knowledge
'''
import glob
import os
files = glob.glob("restaurantmenu.db")
files = glob.glob("database_setup.pyc")

for fl in files:
    #Do what you want with the file
    os.remove(fl)
'''


'''
import glob
import os


for fl in glob.glob("restaurantmenu.db"):
    #Do what you want with the file
    os.remove(fl)
'''