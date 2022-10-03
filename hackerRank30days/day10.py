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
            binn.insert(0, str(n % 2))
            b = n // 2
            if b:
                binn.insert(0, str(b))
            break
    
        binn.insert(0, str(n % 2))
        n //= 2
    
    ones = map(len, ''.join(binn).split('0'))

    print(max(ones))
