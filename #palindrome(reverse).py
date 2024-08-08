#palindrome(reverse)

s='malayalam'
print=(s[5:])

s='python'
reversed(s[2:])

s='python'
s1='  '
for i in range(len(s)-1,-1,-1):
    s1+=s[i]        #output(rev)python

    if(s1==s):
        print('palindrome')
    else: 
        print('Not')