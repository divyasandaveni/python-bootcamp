#check whether num is magical or not
'''''''''
N=1729
step1:sum of digits 
s2:reverse s1
s3:mul s1 and s2
s4:check s4 ,if ans is same as ip leave
s5:if same magical else not magical
'''''''''


n=int(input())
sum=0
while n>0:
    rem=n%10
    sum=sum+rem
    rem
    n=n//10
print('the sum is:',sum)    