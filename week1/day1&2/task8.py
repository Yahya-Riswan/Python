my_list = [1,2,4,5,6,7,8]

my_tuple = tuple(my_list);

try:
    my_tuple[1] = 0;
except TypeError as e:
    print("error ", e)