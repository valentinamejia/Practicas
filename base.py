largest = None
smallest = None
list =[]
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    try:
        num = int(num)
        list.append(num)
    except:
        print('invalid input')
        continue

list.sort()
print('The largest element is: ', list[-1])
print('The smallest element is: ', list[0])


