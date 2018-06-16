#Uses python2

import sys

def compare(a, b):
    return 1 if a + b > b + a else -1
            
def largest_number(a):
    return ''.join(sorted(a, cmp=compare, reverse=True))

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
