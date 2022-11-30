import os

def createAndWrite(path: str, text: str = ""):
    with open(path, "x") as f:
        f.write(text)


for i in range (1, 26):
    path = f"2022/{i:02}"
    if not os.path.isdir(path):
        os.mkdir(path)
        createAndWrite(f"{path}/1.py", "with open(\"i.txt\") as f:")
        createAndWrite(f"{path}/2.py", "with open(\"i2.txt\") as f:")
        createAndWrite(f"{path}/i.txt")
        createAndWrite(f"{path}/i2.txt")
