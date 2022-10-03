"""
Task
Given a base-10 integer, n, convert it to binary (base-2). Then find and print the base-10 integer denoting the maximum number of consecutive 1's in n's binary representation. When working with different bases, it is common to show the base as a subscript.
"""

# SOLUTION

if __name__ == '__main__':
    n = int(input().strip())
    
    binn = []
    
    while True: 
        if n <= 2:
            binn.insert(0, n % 2)
            b = n // 2
            if b:
                binn.insert(0, b)
            break
    
        binn.insert(0, n % 2)
        n //= 2
    
    bigger = 0
    current = 0
    for i in binn:
        if i == 1:
            current +=1 
        elif i == 0:
            if current > bigger:
                bigger = current
            current = 0

    print(bigger)
