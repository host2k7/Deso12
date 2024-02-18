import os

os.chdir("./btboiduong/Deso12/Giai_ma")

fi = open("giaima.inp")
inp = fi.readlines()
n = list(map(int, inp[0].split()))[0]

encrypt = {
    "a" : 1,
    "b" : 2,
    "cc" : 3,
    "bbc" : 4,
    "cbc" : 5,
    "abc" : 6,
    "bac" : 7,
    "aac" : 8,
    "cac" : 9
}

for i in range(1, len(inp)):
    s = list(map(str, inp[i].split()))[0]
    count = ""
    i = 0
    while i < len(s):
        h = False
        lst = []
        for z in encrypt:
            if s[i] == z[0]:
                lst.append(z)
        
        check = s[i]
        for j in range(i+1, len(s)):
            check += s[j]
            
            for z in lst:
                if z not in check and check not in z:
                    lst.remove(z)
                
                if s[i] == "a" or s[i] == "b":
                    if len(lst) == 2:
                        if z == check:
                            i += len(check)
                            count += str(encrypt[check])
                            h = True
                            break
                if s[i] == "c":
                    if z == check:
                        i += len(check)
                        count += str(encrypt[check])
                        h = True
                        break
        if not h:
            count += str(encrypt[s[i]])
            i += 1
    print(count)