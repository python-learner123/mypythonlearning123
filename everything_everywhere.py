#/usr/bin/python
import os
import fnmatch
import sys
# *  matches everything
# ? matches any single character
# [seq] matches any character in seq
# [!seq] matches any character not in seq

scriptname=sys.argv[0]
count=0
try:
	path=sys.argv[1]
	filematch=sys.argv[2] 
	
except IndexError as err:
	print("Please pass two argument as input for script, As example following:")
	print(f'{scriptname} "C:\3781\Projects\Production_file\" "*msi"')
    raise


for dir, dir_mid, files in os.walk(path):
        for filename in files:
            if fnmatch.fnmatch(filename, filematch):
             print(os.path.join(dir, filename))
             count=count+1
print(f"--------- Total {count} files available --------")
