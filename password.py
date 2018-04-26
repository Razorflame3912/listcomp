def value(char):
    numbers = '1234567890'
    specials = ',.!@#$%^&*();[]<>?~+-_/|:'
    caps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if(char in numbers):
        return 2.0
    elif(char in caps):
        return 3.0
    elif(char in specials):
        return 4.0
    else:
        return 1.0

def passwordgrade(passcode):
    print passcode + " scored:"
    scorelist = [value(char) for char in passcode]
    #print scorelist
    total = 0
    for i in scorelist:
        total += i
    #print total
    avg = total/len(scorelist)
    #print avg
    score = (avg * 2.5) * (len(scorelist)/15.0)
    return score


print passwordgrade('hello')
print passwordgrade('1234')
print passwordgrade('HeLlO!')
print passwordgrade('SeCRETpass478!!')
print passwordgrade('*&^$@#@!%!!.?-+')
