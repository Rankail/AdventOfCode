import subprocess
import webbrowser
import os

day = int(input("Day: "))
if 25 < day or 0 > day:
    print("invalid day")
    exit()
p = f"C:/dev/AdventOfCode/2022/{day:02}"
if not os.path.isdir(p):
    os.mkdir(p)
    open(p+"/i.txt", "x")
    open(p+"/i2.txt", "x")
    os.mkdir(p+"/py")
    with open(p+"/py/1.py", "x") as f:
        f.write("data = open(\"i.txt\").read().split(\"\\n\")\n\n")
    open(p+"/py/2.py", "x")

webbrowser.open("https://adventofcode.com/")
subprocess.Popen(["code", "C:/dev/AdventOfCode"], shell=True)
quit()