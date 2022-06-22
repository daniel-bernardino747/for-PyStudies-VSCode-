def sum(a, b):
    return a + b

def sub(a, b):
    return a - b

func = [sum, sub]

print(func[0](3, 5))
print(func[1](3, 5))
