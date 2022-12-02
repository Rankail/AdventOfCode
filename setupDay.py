import subprocess
import webbrowser
import sys

day = int(input("Day: "))
if 25 < day or 0 > day:
    print("error day")
    exit()

with open(".vscode/launch.json", "w") as f:
    f.write(f"""{{
    "version": "0.2.0",
    "configurations": [
        {{
            "name": "Python: AoC",
            "type": "python",
            "request": "launch",
            "program": "${{workspaceFolder}}/2022/{day:02}/1.py",
            "console": "integratedTerminal",
            "justMyCode": true,
            "cwd": "${{workspaceFolder}}/2022/{day:02}"
        }}
    ]
}}""")

webbrowser.open("https://adventofcode.com/")
subprocess.Popen(["code", "C:/dev/AdventOfCode"], shell=True)
quit()