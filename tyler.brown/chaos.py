__author__ = 'tyler.browngit'

# File: chaos.py
# A simple program illustrating chaotic behavior.

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    y = 1
    z = 2.0
    for i in range(20):
        x = z * x * (y - x)
        print(x)

main()
