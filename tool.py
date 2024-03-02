# f strings (similar is template literal)
""" user_name = 'Bob'
user_age = 10
user_information = 'Bob is 10 years old'
bad_approach = user_name + 'is 10 years old'
better_approach = f'{user_name} is {user_age} years old'
print(better_approach) """

# single line if statement
""" user_name = 'Bob'
user_age = 10
user_age = 15
user_status = 'adult' if user_age >= 18 else 'child'
# if user_age < 18:
#     user_status = 'child'
# else:
#     user_status = 'adult'
# print(user_status)
print(f'{user_name} is {user_age} years old so he is a {user_status}') """

# list comprehension
""" # simple_list = [0,1,2,3,4,5]
# for i in range(0, 10, 1):
#     simple_list.append(i)
simple_list = [f'{j}{i}' for i in range(0,11,1) for j in ('a', 'b', 'c') if j == 'a']
print(simple_list) """

# lambda functions (similar to arrow function, ie: one liner)
""" # def double_value(num):
#     return num * 2
double_value = lambda num: num * 2
print(double_value(10)) """

# function as argument
""" # random_list = [0,6,4,1,5,7]
random_list = [('Anna', 25), ('Paul', 24), ('Lisa', 10)]
sorted_list = sorted(random_list, key= lambda user_tuple: user_tuple[1])
print(sorted_list) """

# exercise - battleship record
# board = ['A1','A2','A3','A4','A5','B1','B2','B3','B4','B5','C1','C2','C3','C4','C5','D1','D2','D3','D4','D5','E1','E2','E3','E4','E5']
board_number = [f'{j}{i}' for j in ('A', 'B', 'C', 'D', 'E') for i in range(0,6,1) if f'{j}{i}' != 'C3']
print(board_number)
