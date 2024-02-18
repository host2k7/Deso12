import os

os.chdir("./btboiduong/Deso12/Day_so")

fi = open("dayso.inp")
inp = fi.readlines()

n = list(map(int, inp[0].split()))[0]
check_list = set()

def day_so(x, i, t, check_list):
    if t > 486:
        return 0
    if i == 0:
        for j in range(1, 10):
            x[i] = str(j)
            day_so(x, i+1, t, check_list)
    else:
        for j in range(0, 10):
            x[i] = str(j)
            if i == t - 1:
                check = ""
                c2 = 0
                for z in x:
                    check += z
                    c2 += int(z)**2
                if int(check) % t == 0 and c2 == t:
                    check_list.add(check)
                    if check == "999999":
                        return check_list
            else:
                day_so(x, i+1, t, check_list)

for i in range(1, n+ 1):
    t = list(map(int, inp[i].split()))[0]
    x = t * [0]
    print(day_so(x, 0, t, check_list))