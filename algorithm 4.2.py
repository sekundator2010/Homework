import math
import time
start = time.time()
n = 500
a = [0] * n
for i in range(n):
    a[i] = i
a[1] = 0

m = 2
while m < n:
    if a[m] != 0:
        j = m * 2
        while j < n:
            a[j] = 0
            j = j + m
    m += 1
b = []
for i in a:
    if a[i] != 0:
        b.append(a[i])
del a
print(b)

print(time.time() - start)

# Вторым вариантом нахождения простых чисел выбрал сито Аткина.
start_1 = time.time()
def sieveOfAtkin(limit):
    P = [2,3]
    sieve=[False]*(limit+1)
    for x in range(1,int(math.sqrt(limit))+1):
        for y in range(1,int(math.sqrt(limit))+1):
            n = 4*x**2 + y**2
            if n<=limit and (n%12==1 or n%12==5) : sieve[n] = not sieve[n]
            n = 3*x**2+y**2
            if n<= limit and n%12==7 : sieve[n] = not sieve[n]
            n = 3*x**2 - y**2
            if x>y and n<=limit and n%12==11 : sieve[n] = not sieve[n]
    for x in range(5,int(math.sqrt(limit))):
        if sieve[x]:
            for y in range(x**2,limit+1,x**2):
                sieve[y] = False
    for p in range(5,limit):
        if sieve[p] : P.append(p)
    return P

print(sieveOfAtkin(500))
print(time.time() - start_1)

# Испытуемые были поставлены в равные условия, им было условлено найти простые числа до 500.
# Судя по времени работы, решето Эратосфена с лёгкостью выигрывает у сита  Аткина. Так же решето более простое
# и понятное в решении. Следовательно, первое решение является более оптимальным со всех точек зрения.

