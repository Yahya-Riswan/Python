n = 3

try:
    print(n/0)
except ZeroDivisionError as e:
    print("ERROR : ",e)
else:
    print(n);
finally:
    print("ALL COMPLETED")
    

    