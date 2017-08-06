#!/usr/share/env python3

import os
import glob

output_choice = "n"

def print_line():
    print(90 * "=")

print_line()
print("Bulk Trim Videos Python Script by Bhavin, Using ffmpeg")
print_line()

list_of_files = glob.glob("input/*.mp4")
#print list_of_files
if list_of_files == []:
    print("Input Directory is empty!")
else :
    output_choice = input("Do you want to create output directory?, if it exist it will give error, [y/N]  ")

if output_choice == "Y" or output_choice == "y":
    os.mkdir("output")
    
    
###### FFMPEG to all .mp4 files ######
for i in list_of_files:
    print_line()
    print("Trimming " + i)
    print_line()
    output_name = i.lstrip("input/")
    os.system('ffmpeg -ss 00:00:00.0 -i "' + i + '" -c copy -t 00:22:29.963 "output/' + output_name + '"')
    
