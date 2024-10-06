
def find_unique(numbers):
    
    count = {}
    
    for number in numbers:
        if number in count:
            count[number] += 1
        else:
            count[number] = 1
            

    for number, cnt in count.items():
        if cnt == 1:
            return number


print(find_unique([3, 3, 3, 7, 3, 3])) 
print(find_unique([0, 0, 0.77, 0, 0])) 
print(find_unique([0, 1, 1, 1, 1, 1, 1, 1])) 
