import os

os.chdir("./btboiduong/Deso12/Chiec_non_ki_dieu")

fi = open("magic.inp")
inp = fi.readlines()
n = list(map(int, inp[0].split()))[0]
vong_quay = [i for i in list(map(int, inp[1].split()))]
check  = []
point = vong_quay[0]
s = str(vong_quay[0]) + ""
for i in range(1, len(vong_quay)):
    if vong_quay[i] == point:
        check.append(s)
        s = ""
    s += str(vong_quay[i]) + ""

ans = check[0]
for i in range(1, len(check)):
    if check[i] != check[i-1]:
        ans += check[i]
    else:
        break
    
    check_again = ""
    for j in range(i + 1, len(check)):
        check_again += check[j]
    if ans in check_again:
        count = 0
        for z in range(len(ans)):
            if ans[z] == check_again[z]:
                count += 1
        if count == len(ans):
            break
        else:
            continue
'''        elif check_again in ans:
            count = 0
            for z in range(len(check_again)):
                if ans[z] == check_again[z]:
                    count += 1
            if count == len(check_again):
                break'''

print(len(ans))