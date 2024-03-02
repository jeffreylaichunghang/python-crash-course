# Tuple, List, Dictionary, Set

a_tuple = (1, 2, 3, 'a', 'b', 'c') # list of items
a_list = [1, 3, 3, 'a string'] # similar to array
a_list.append('another word')
# print(a_list)
a_set = {1, 2, 2, 3}
# print(a_set)
# print(set(a_list))
# print(list(a_set))
a_dictionary = {
    'key': 'value',
    123: [1,2,3]
}
# print(a_dictionary)


""" TO GET VALUES FROM CONTAINER """
user_list = ['Lisa', 'Bob', 'Alex', 'Anna', 'John']
print(user_list[0: 3: 2])
print(a_dictionary['key'])
