# get input
user_input = input('Enter a string of only x\'s and y\'s: ')

# count the number of x's and y's
x_count = user_input.count('x')
y_count = user_input.count('y')

isBalance = x_count == y_count

def check_balance():
    if isBalance:
        return True
    else:
        return False

result = check_balance()
print(result)