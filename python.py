k,n = [int(i) for i in input().split()]
a = [i for i in range(k)]
print(*a)

def one(a, k, n):
    for i in range(k-1, -1, -1):
        if a[i] < (n-1) - (k-1-i):
            a[i] += 1
            for j in range(i+1,k):
                a[j] = a[j - 1] + 1
            print(*a)
            one(a, k, n)
one(a, k, n)




Нужно сгенерировать все возможные k-сочетания из n элементов.

Формат входных данных:
Два числа k и n через пробел. Для них гарантированно выполняется условие: 0≤𝑘≤𝑛

. 

Формат выходных данных:
Необходимое число строк, в каждой из которых содержится k чисел из диапазона от 0 до n-1 включительно, разделенных пробелом. 


Sample Input 1:

2 3

Sample Output 1:

0 1
0 2
1 2

Sample Input 2:

1 1

Sample Output 2:

0
