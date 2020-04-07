

def string_length(str1):
    """gives the length of the work or input"""
    count = 0
    for char in str1:
        count+= 1
    return count
print(string_length('nijaobao'))

# use function len()

print(len("nijaobao"))


choice = input(f' vamos a jugar piedra, papel o tijeras, ingresa tu elección: ')
print(choice.lower())

