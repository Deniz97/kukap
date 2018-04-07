
n = int(input())
lst = [0] *n

# lstElement -> [solNoktaSayisi, sagNoktaSayisi, solKatsayi, sagKatsayi]

def calcDuration(i1, i2):
    return lst[i1][0] * lst[i1][1] * lst[i2][1]

# i1 -> index of left one, i2 -> index of right one
def calcYorgunluk(i1, i2):
    return lst[i1][3] * lst[i2][2]

if __name__ == '__main__':

    for i in range(n):
        lst.append([int x for x in input().split()])




