#!/usr/bin/python3
# Int list and  list comprehension
# list1 = [1,4,5,7,9,15, 21, 30]
# list2 = [num for num in list1 if num%3 ==0 and num%5==0]
# print(list2)

# #kes and values in dictionary
# my_dict = {"name": "Ashish", "age": 41, "city": "Kathmandu"}
# print(my_dict.keys())
# print(my_dict.values())    

# key = []
# value = []
# for k,v in my_dict.items():
#     key.append(k)
#     value.append(v)
# print(key)
# print(value)    

# #zip function
# keys = ["name", "age", "city"]
# values = ["Ashish", 41, "Kathmandu"]
# my_dict =dict(zip(keys, values))
# print(my_dict)

# tup1 = ("name", "age", "city")
# tup2 = ("Ashish", 41, "Kathmandu", "Test")
# my_dict = dict(zip(tup1, tup2))
# print(my_dict)  
# names, ages = zip(*my_dict.items())
# print(names)

#ars and kwargs
def test(*numbers):
    result = 0
    for num in  numbers:
        result = result+num
    return result

print(test(10,20,30, 40));  

def kwargs_test(**kwargs):
    keys = [];
    values = [];
    for k,v in kwargs.items():
        keys.append(k)
        values.append(v)
    return keys, values

result =kwargs_test(name="Asri", age=7, city="Kathmandu")
print(result[0])
print(result[1])   

#lambda function
add = lambda x,y:x+y
print(add(10,20))   