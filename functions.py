# create a function
def print_x_times(parameters = 'loop', loop_amount = 5):
    counter = 0
    print(global_var)
    while counter <= loop_amount:
        print(counter, parameters)
        counter += 1
    return loop_amount

# global variable
global_var = 'global variable'
# call the function
test = print_x_times()
print(test)
