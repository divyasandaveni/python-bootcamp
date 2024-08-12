#uniquestring
s='hello world hello world good morning good afternoon'
words=s.split()
unique_words=[]

for word in words:
    if word not in unique_words:
        unique_words.append(word)

        unique_string=''.join(unique_words)
        print(unique_string)
