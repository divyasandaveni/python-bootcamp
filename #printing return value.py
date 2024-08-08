#printing return value
def greetings():
    return('hello good morning')
print(greetings())
print(greetings())
print(greetings())

def greetings(branch):
    return('hello good morning',branch)
print(greetings('cse'))
print(greetings('ece'))
print(greetings('it'))
