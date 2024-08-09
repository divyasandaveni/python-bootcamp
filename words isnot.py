#how many words r there(is/isnot)

s='he is palying football but not crciket'

s=s.split()
print(s)

#length:

s='he is playing football but not cricket'
s=s.split()
print(len(s))

print(s.count('playing'))
print(s.count('he'))

s='he is playing football but not playing crciket'
s=s.split()
print(s.count('playing'))
print(s.count('he'))