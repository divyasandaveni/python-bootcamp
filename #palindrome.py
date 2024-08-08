#palindrome
def check(n):
    n=str(n)
    return len(n)>1 and n==n[::-1]

def increment(N):
    count=0
    for i in range(1,N+1):
        if check(i):
            print(i)
            count+=1
    return count
N=50
print(increment(N))

def check(ele):
    ele=str(ele)
    return ele==ele[::-1]

def increment(arr):
    count=0
    for i in arr:
        if check(i):
            print(i)
            count+=1
            return count
        arr=[24,78,212,782,1001]
        print(increment(arr))
