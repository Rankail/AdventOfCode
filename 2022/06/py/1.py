data = open("i.txt").read()

n=4
for i in range(0,len(data)-n):
    if len(set(data[i:i+n])) == n:
        print(i+n)
        break