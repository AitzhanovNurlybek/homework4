def rotate_list(elements):
    if len(elements) == 0:
        return elements 
    

    rotated = [elements[-1]] + elements[:-1]
    return rotated


elements = [1, 2, 3, 4, 5]

result = rotate_list(elements)

print(result)
