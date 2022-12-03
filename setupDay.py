import subprocess
import webbrowser
import sys
import os

day = int(input("Day: "))
if 25 < day or 0 > day:
    print("error day")
    exit()
p = f"C:/dev/AdventOfCode/2022/{day:02}"
if not os.path.isdir(p):
    os.mkdir(p)
    open(p+"/i.txt", "x")
    open(p+"/i2.txt", "x")
    os.mkdir(p+"/py")
    os.mkdir(p+"/js")
    os.mkdir(p+"/java")
    open(p+"/py/1.py", "x")
    open(p+"/py/2.py", "x")

webbrowser.open("https://adventofcode.com/")
subprocess.Popen(["code", "C:/dev/AdventOfCode"], shell=True)
quit()