data = open("i.txt").read()

n=14
for i in range(1,len(data)-n):
    if len(set(data[i:i+n])) == n:
        print(i+n)
        break