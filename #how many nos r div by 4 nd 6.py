#how many nos r div by 4 nd 6

1,36,9,24,4,2,12
#pass this arr as func parameter


def check(arr):
    count=0
    for i in arr:
        if i%4==0 and i%6==0:
            count+=1
            return count
        print(check(arr))