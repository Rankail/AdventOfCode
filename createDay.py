import os
import datetime

year = int(input("Year: "))
if year < 2015 or year > datetime.datetime.now().year:
    print("invalid year")
    exit()
day = int(input("Day: "))
if 25 < day or 0 > day:
    print("invalid day")
    exit()
p = f"C:/dev/AdventOfCode/{year}/{day:02}"
if not os.path.isdir(p):
    os.mkdir(p)
    open(p+"/i.txt", "x")
    open(p+"/i2.txt", "x")
    os.mkdir(p+"/py")
    with open(p+"/py/1.py", "x") as f:
        f.write("data = open(\"i.txt\").read()\n\n")
    open(p+"/py/2.py", "x")