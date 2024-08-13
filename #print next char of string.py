#print next char of string
s='abcdz'
s = 'abcdz'
next_chars = []

for i in range(len(s)):
    current_char = s[i]
    
    if current_char == 'z':
        next_char = 'a'
    else:
        next_char = chr(ord(current_char) + 1)
    
    next_chars.append(next_char)

next_string = ''.join(next_chars)

print(next_string)
