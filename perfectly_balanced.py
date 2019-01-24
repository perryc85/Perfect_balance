def Dict(inputString):
    counts = dict()
    for chars in inputString:
        counts[chars] = counts.get(chars,0) + 1
    return counts
    
def isTrueOrFalse(counts):
    prev_val = None
    for value in counts.values():
        if prev_val != None and prev_val != value:
            return False
        prev_val = value
    return True

# Bonus 
# get input
user_input = input('Enter a string: ')

print(isTrueOrFalse(Dict(user_input)))