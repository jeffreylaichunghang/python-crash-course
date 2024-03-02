# indentation defines scope
""" if 3 > 4:
    print('correct result')
elif 2 < 1:
    print('other result')
elif 0 == 0 and 5 > 1:
    print('and statement')
    if len([1,2,3]) > 2:
        print('list is long enough')
else:
    print('incorrect result')
print('test') """

# while loop
""" counter = 0
while counter <= 10:
    print(counter)
    counter += 1
    if counter == 5:
        print('counter is 5')
print('while loop is finished') """

# for loop
""" test_list = [1,2,3,4,5]
test_dict = {1:2, 3:4, 5:6}
for x in test_list:
    print(x)
for x,y in test_dict.items():
    print(x)
    print(y) """

# true and false
if [] or '':
    print('truthy')
else:
    print('falsy')
