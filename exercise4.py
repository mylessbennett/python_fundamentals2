my_string = "Hello"
result = None

def less_than_eight(my_string):
    if len(my_string) < 8:
        result = False
    else:
        result = True
    return result

result = less_than_eight(my_string)
print(result)
