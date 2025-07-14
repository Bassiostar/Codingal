def sum (n):
    return n*(n+1) // 2 

def arraysum(a):
    total=0
    for i in a:
        total +=i
    return total
a=[12,3,4,15]
arraysum(a)

def summ(n):
    if n<=0:
        return 0
    return n+summ(n-1)

