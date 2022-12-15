data = open("i.txt").read()

# Testcases
# data = "C200B40A82" # (1+2) -> 3
# data = "04005AC33890" # (6*9) -> 54
# data = "880086C3E88112" # (min(7,8,9)) -> 7
# data = "CE00C43D881120" # (max(7,8,9)) -> 9
# data = "D8005AC2A8F0" # (5<15) -> 1
# data = "F600BC2D8F" # (5>15) -> 0
# data = "9C005AC2F8F0" # (5==15) -> 0
# data = "9C0141080250320F1802104A08" ((1+3)==(2*2)) -> 1

def binToInt(b: str):
    n = 0
    for c in b:
        n *= 2
        if c == "1": n += 1
    return n

def operate(typeId: str, nums: list[int]):
    if typeId == "000":
        return sum(nums)
    elif typeId == "001":
        res = 1
        for n in nums:
            res *= n
        return res
    elif typeId == "010":
        return min(nums)
    elif typeId == "011":
        return max(nums)
    elif typeId == "101":
        return 1 if nums[0] > nums[1] else 0
    elif typeId == "110":
        return 1 if nums[0] < nums[1] else 0
    elif typeId == "111":
        return 1 if nums[0] == nums[1] else 0
    print("Error")

def packet(s: str, cnt: int = -1):
    i = 0
    c = 0
    nums = []
    while i < len(s)-1 and (cnt == -1 or cnt > c):
        if len(s)-i < 11: return i, nums
        typeId = s[i+3:i+6]
        i += 6
        if typeId == "100":
            num = ""
            while s[i] == "1":
                num += s[i+1:i+5]
                i += 5
            num += s[i+1:i+5]
            i += 5
            nums.append(binToInt(num))
        elif s[i] == "0":
            i += 1
            num = s[i:i+15]
            i += 15
            j, ns = packet(s[i:i+binToInt(num)])
            i += j
            res = operate(typeId, ns)
            nums.append(res)
        elif s[i] == "1":
            i += 1
            num = s[i:i+11]
            i += 11
            j, ns = packet(s[i:], binToInt(num))
            i += j
            res = operate(typeId, ns)
            nums.append(res)
        
        c+=1
    return i, nums

d = ""
for c in data:
    n = ord(c)-55 if ord(c)>=65 else int(c)
    p = ""
    while n > 0:
        p = str(n%2) + p
        n //= 2
    d +=  "0"*(4-len(p))+p
    

print(packet(d)[1][0])
# 1264857437203