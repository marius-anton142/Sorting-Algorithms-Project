import random
import time

def merge(v1, v2):
    i = 0
    j = 0
    u = []
    while i < len(v1) and j < len(v2):
        if v1[i] < v2[j]:
            u.append(v1[i])
            i += 1
        else:
            u.append(v2[j])
            j += 1
    while i < len(v1):
        u.append(v1[i])
        i += 1
    while j < len(v2):
        u.append(v2[j])
        j += 1
    return u

def merge_sort(v):
    if len(v) <= 1:
        return v
    stanga = merge_sort(v[0:(len(v))//2])
    dreapta = merge_sort(v[(len(v))//2:len(v)])
    sortat = merge(stanga, dreapta)
    return sortat

def quick_sort(v):
    if len(v) <= 1:
        return v
    rand = random.randrange(len(v))
    p = v[rand]
    v.remove(p)
    s = []
    d = []
    for x in v:
        if x <= p:
            s.append(x)
        else:
            d.append(x)
    return quick_sort(s) + [p] + quick_sort(d)


def shell_sort(v):
    gap = len(v)//2
    while gap > 0:
        for i in range(gap, len(v)):
            if v[i-gap] > v[i]:
                v[i-gap], v[i] = v[i], v[i-gap]
            x = i
            while (x-gap > -1):
                if v[x] < v[x-gap]:
                    v[x], v[x-gap] = v[x-gap], v[x]
                x -= gap
        gap = gap//2
    return v

def counting_sort(v):
    u = [0]*10000000
    v2 = []
    maxx = v[0]
    for x in v:
        u[x] += 1
        if (x > maxx):
            maxx = x
    for i in range(maxx+1):
        for j in range(u[i]):
            v2.append(i)
    return v2

def radix_count(v, k):
    if v == []:
        return []
    u = []
    u0 = u1 = u2 = u3 = u4 = u5 = u6 = u7 = u8 = u9 = []
    for x in v:
        if (x//(10**(k-1))) == 0:
            u0.append(x)
        elif (x//(10**(k-1))) == 1:
            u1.append(x)
        elif (x//(10**(k-1))) == 2:
            u2.append(x)
        elif (x//(10**(k-1))) == 3:
            u3.append(x)
        elif (x//(10**(k-1))) == 4:
            u4.append(x)
        elif (x//(10**(k-1))) == 5:
            u5.append(x)
        elif (x//(10**(k-1))) == 6:
            u6.append(x)
        elif (x//(10**(k-1))) == 7:
            u7.append(x)
        elif (x//(10**(k-1))) == 8:
            u8.append(x)
        elif (x//(10**(k-1))) == 9:
            u9.append(x)
    if k == 1:
        return [u0] + [u1] + [u2] + [u3] + [u4] + [u5] + [u6] + [u7] + [u8] + [u9]
    else:
        return radix_count(u0, k-1) + radix_count(u1, k-1) + radix_count(u2, k-1) + radix_count(u3, k-1) + radix_count(u4, k-1) + radix_count(u5, k-1) + radix_count(u6, k-1) + radix_count(u7, k-1) + radix_count(u8, k-1) + radix_count(u9, k-1)

def radix_sort(v):
    maxx = v[0]
    v1 = v2 = v3 = v4 = v5 = v6 = v7 = v8 = []
    for x in v:
        if (x > maxx):
            maxx = x
        k = 0
        y = x
        while y > 0:
            k += 1
            y = y//10
        if k == 1:
            v1.append(x)
        elif k == 2:
            v2.append(x)
        elif k == 3:
            v3.append(x)
        elif k == 4:
            v4.append(x)
        elif k == 5:
            v5.append(x)
        elif k == 6:
            v6.append(x)
        elif k == 7:
            v7.append(x)
        elif k == 8:
            v8.append(x)
    return radix_count(v1, 1) + radix_count(v2, 2) + radix_count(v3, 3) + radix_count(v4, 4) + radix_count(v5, 5) + radix_count(v6, 6) + radix_count(v7, 7) + radix_count(v8, 8)

def test_sort(v):
    for i in range(len(v)-1):
        if v[i] > v[i+1]:
            return False
    return True

N = 1000
Max = 10000000
v = [0]*N
for i in range(N):
    v[i] = random.randrange(Max)
timp_start = time.time()
u = merge_sort(v)
timp_end = time.time()
print("merge_sort N = 1000 Max = 10000000 " + str(timp_end-timp_start) + " " + str(test_sort(u)))

N = 10000
Max = 1000
v = [0]*N
for i in range(N):
    v[i] = random.randrange(Max)
timp_start = time.time()
u = merge_sort(v)
timp_end = time.time()
print("merge_sort N = 10000 Max = 1000 " + str(timp_end-timp_start) + " " + str(test_sort(u)))

N = 100
Max = 10000000
v = [0]*N
for i in range(N):
    v[i] = random.randrange(Max)
timp_start = time.time()
u = merge_sort(v)
timp_end = time.time()
print("merge_sort N = 100 Max = 10000000 " + str(timp_end-timp_start) + " " + str(test_sort(u)))

N = 10
Max = 1000
v = [0]*N
for i in range(N):
    v[i] = random.randrange(Max)
timp_start = time.time()
u = merge_sort(v)
timp_end = time.time()
print("merge_sort N = 10 Max = 1000 " + str(timp_end-timp_start) + " " + str(test_sort(u)))

N = 100000
Max = 1000000
v = [0]*N
for i in range(N):
    v[i] = random.randrange(Max)
timp_start = time.time()
u = merge_sort(v)
timp_end = time.time()
print("merge_sort N = 100000 Max = 1000000 " + str(timp_end-timp_start) + " " + str(test_sort(u)))

N = 1000
Max = 10000000
v = [0]*N
for i in range(N):
    v[i] = random.randrange(Max)
timp_start = time.time()
u = quick_sort(v)
timp_end = time.time()
print("quick_sort N = 1000 Max = 10000000 " + str(timp_end-timp_start) + " " + str(test_sort(u)))

N = 10000
Max = 1000
v = [0]*N
for i in range(N):
    v[i] = random.randrange(Max)
timp_start = time.time()
u = quick_sort(v)
timp_end = time.time()
print("quick_sort N = 10000 Max = 1000 " + str(timp_end-timp_start) + " " + str(test_sort(u)))

N = 100
Max = 10000000
v = [0]*N
for i in range(N):
    v[i] = random.randrange(Max)
timp_start = time.time()
u = quick_sort(v)
timp_end = time.time()
print("quick_sort N = 100 Max = 10000000 " + str(timp_end-timp_start) + " " + str(test_sort(u)))

N = 10
Max = 1000
v = [0]*N
for i in range(N):
    v[i] = random.randrange(Max)
timp_start = time.time()
u = quick_sort(v)
timp_end = time.time()
print("quick_sort N = 10 Max = 1000 " + str(timp_end-timp_start) + " " + str(test_sort(u)))

N = 100000
Max = 1000000
v = [0]*N
for i in range(N):
    v[i] = random.randrange(Max)
timp_start = time.time()
u = quick_sort(v)
timp_end = time.time()
print("quick_sort N = 100000 Max = 1000000 " + str(timp_end-timp_start) + " " + str(test_sort(u)))

N = 1000
Max = 10000000
v = [0]*N
for i in range(N):
    v[i] = random.randrange(Max)
timp_start = time.time()
u = counting_sort(v)
timp_end = time.time()
print("counting_sort N = 1000 Max = 10000000 " + str(timp_end-timp_start) + " " + str(test_sort(u)))

N = 10000
Max = 1000
v = [0]*N
for i in range(N):
    v[i] = random.randrange(Max)
timp_start = time.time()
u = counting_sort(v)
timp_end = time.time()
print("counting_sort N = 10000 Max = 1000 " + str(timp_end-timp_start) + " " + str(test_sort(u)))

N = 100
Max = 10000000
v = [0]*N
for i in range(N):
    v[i] = random.randrange(Max)
timp_start = time.time()
u = counting_sort(v)
timp_end = time.time()
print("counting_sort N = 100 Max = 10000000 " + str(timp_end-timp_start) + " " + str(test_sort(u)))

N = 10
Max = 1000
v = [0]*N
for i in range(N):
    v[i] = random.randrange(Max)
timp_start = time.time()
u = counting_sort(v)
timp_end = time.time()
print("counting_sort N = 10 Max = 1000 " + str(timp_end-timp_start) + " " + str(test_sort(u)))

N = 100000
Max = 1000000
v = [0]*N
for i in range(N):
    v[i] = random.randrange(Max)
timp_start = time.time()
u = counting_sort(v)
timp_end = time.time()
print("counting_sort N = 100000 Max = 1000000 " + str(timp_end-timp_start) + " " + str(test_sort(u)))

N = 1000
Max = 10000000
v = [0]*N
for i in range(N):
    v[i] = random.randrange(Max)
timp_start = time.time()
u = shell_sort(v)
timp_end = time.time()
print("shell_sort N = 1000 Max = 10000000 " + str(timp_end-timp_start) + " " + str(test_sort(u)))

N = 10000
Max = 1000
v = [0]*N
for i in range(N):
    v[i] = random.randrange(Max)
timp_start = time.time()
u = shell_sort(v)
timp_end = time.time()
print("shell_sort N = 10000 Max = 1000 " + str(timp_end-timp_start) + " " + str(test_sort(u)))

N = 100
Max = 10000000
v = [0]*N
for i in range(N):
    v[i] = random.randrange(Max)
timp_start = time.time()
u = shell_sort(v)
timp_end = time.time()
print("shell_sort N = 100 Max = 10000000 " + str(timp_end-timp_start) + " " + str(test_sort(u)))

N = 10
Max = 1000
v = [0]*N
for i in range(N):
    v[i] = random.randrange(Max)
timp_start = time.time()
u = shell_sort(v)
timp_end = time.time()
print("shell_sort N = 10 Max = 1000 " + str(timp_end-timp_start) + " " + str(test_sort(u)))

N = 100
Max = 10000000
v = [0]*N
for i in range(N):
    v[i] = random.randrange(Max)
timp_start = time.time()
u = radix_sort(v)
timp_end = time.time()
print("radix_sort N = 100 Max = 10000000 " + str(timp_end-timp_start) + " " + str(test_sort(u)))

N = 10
Max = 1000
v = [0]*N
for i in range(N):
    v[i] = random.randrange(Max)
timp_start = time.time()
u = radix_sort(v)
timp_end = time.time()
print("radix_sort N = 10 Max = 1000 " + str(timp_end-timp_start) + " " + str(test_sort(u)))

N = 10000
Max = 1000
v = [0]*N
for i in range(N):
    v[i] = random.randrange(Max)
timp_start = time.time()
u = radix_sort(v)
timp_end = time.time()
print("radix_sort N = 10000 Max = 1000 " + str(timp_end-timp_start) + " " + str(test_sort(u)))

N = 1000
Max = 10000000
v = [0]*N
for i in range(N):
    v[i] = random.randrange(Max)
timp_start = time.time()
u = radix_sort(v)
timp_end = time.time()
print("radix_sort N = 1000 Max = 10000000 " + str(timp_end-timp_start) + " " + str(test_sort(u)))


N = 100000
Max = 1000000
v = [0]*N
for i in range(N):
    v[i] = random.randrange(Max)
timp_start = time.time()
u = radix_sort(v)
timp_end = time.time()
print("radix_sort N = 100000 Max = 1000000 " + str(timp_end-timp_start) + " " + str(test_sort(u)))
