# z = a +bi
# a is the real and the bi is the imaginary part

# z^2 -2z +6 = 0  equation of degree 2
import math
import cmath

def func():
    a = input("Enter a value for A: ")
    b = input("Enter a value for B: ")
    c = input("Enter a value for C: ")
    b4ac = (b ** 2 - 4 * a * c)
    if (b4ac > 0):
        sqr = math.sqrt(b4ac)
        z1 = (-b + sqr) / (2 * a)
        z2 = (-b - sqr) / (2 * a)
    else:
        b4ac = b4ac * -1
        sqr = math.sqrt(b4ac) * -1
        z1 = (-b + complex(0, sqr)) / (2 * a)
        z2 = (-b - complex(0, sqr)) / (2 * a)
        
    print(z1.real)
    print(z1.imag)
    print(z2.real)
    print(z2.imag)
    print ("The value for the z_1 is :=> {0:.3f}" .format(z1))    
    print ("The value for the z_2 is :=> {0:.3f}" .format(z2))    

if __name__ == "__main__":
    func()