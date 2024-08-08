#increment
def increment(arr):
    count=0
    for i in arr:
        if check(i):
            print(i)
            count+=1
            return count
        arr=[24,78,212,782,1001]
        print(increment(arr))