def sum_mix(arr):
    n = 0
    for i in arr:
        n+=int(i)
    return n

# print(sum_mix([9, 3, '7', '3']))


def bool_to_word(boolean):
    if boolean == True:
        return 'Yes'
    elif boolean == False:
        return 'No'


# bool_to_word(True)


def to_alternating_case(string):
    n = ''
    for i in string: 
        if i.isupper():
            n+=i.lower()
        elif i.isdigit():
            n+=i
        elif i.islower():
            n+=i.upper()
        else:
            n += i
    return n
print(to_alternating_case('String.prototype.toAlternatingCase'))