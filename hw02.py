

#Violet McAuliffe, CSC110, HW02
# Task 1.1:
#  Complete the function "read_two_ints" below:
def read_two_ints():
    # using doc string to make a plan
    '''
    -create a line that requests an input: input(...)
    -concert input to integers: int(...)
    -return both integers at the same time: return ...
    '''
    x = input("give me x: ")
    x = int(x)
    y = input("give me y: ")
    y = int(y)
    return x,y
 

# Task 2.1:
#  Complete the function "compute_multadd" below:
def compute_multadd(a, b):
    # using docstring to make a plan
    '''
    -verify it accepts a and b (it does)
    -assign numerator, a*b, to a variable
    -print result using f string
    -assign denominator, a+b, to a variable
    -print result using f string
    -find result dividing numerator by denominator
    '''
    mult = a * b
    print(f"mult result: {mult}")
    add = a + b
    print(f"add result: {add}")
    mult_add = mult/add
    return mult_add
    
    
# Task 3.1:
#  Complete the function "print_fancy" below:
def print_fancy(a, b, ab_multadd):
    #using doc string to make a plan
    '''
    -verify it accepts three given variable: it does
    -print stars
    -use fstring to print a, then b, then mult add
    -print equal signs
    '''
    print("*"*16)
    print("RESULTS: \n first number")
    print(f"first number: {a}")
    print(f"second number: {b}")
    print(f"multadd result: {ab_multadd}")
    print("="*16)
    

def main ():
    #1.2: calling the read_two_ints() function, making x and y global variables
    x,y = read_two_ints()
    
    # Task 2.2: calling the compute_multadd function, making output a global variable
    xy_multadd = compute_multadd(x, y)

    # Task 3.2: I call the print)fancy, with the global variables I obtained from calling the other two functions. 
    print_fancy(x, y, xy_multadd)
    
    print("The End")

# Do not modify these two lines
if __name__ == "__main__":
    main()
