def find_linear_equation(x1, y1, x2, y2):
    
    a = (y2 - y1) // (x2 - x1) 
    

    b = y1 - a * x1
    
    return a, b

def main():
   
    num_cases = int(input())
    results = []

    for _ in range(num_cases):
        
        x1, y1, x2, y2 = map(int, input().split())
        
       
        a, b = find_linear_equation(x1, y1, x2, y2)
        
        
        results.append(f"({a} {b})")
    
   
    print(" ".join(results))


main()
