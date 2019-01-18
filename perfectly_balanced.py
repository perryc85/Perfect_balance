# Bonus 
# get input
user_input = input('Enter a string : ')

counts = dict()
for chars in user_input:
    counts[chars] = counts.get(chars,0) + 1

value_count = []
for value in counts.values():
    value_count.append(value)

if value_count[1:] == value_count[:-1]:
    print('true')
else:
    print('false')