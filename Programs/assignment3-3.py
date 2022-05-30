class complex_:
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im

    def get_re(self):
        return self.re

    def get_im(self):
        return self.im

    def __str__(self):
        g = lambda x:"+" if x >= 0 else ""
        return f"({self.re}{g(self.im)}{self.im}i)"

    def cadd(self, other):
        new_re = self.get_re() + other.get_re()
        new_im = self.get_im() + other.get_im()
        return complex_(new_re, new_im)

    def __add__(self, other):
        new_re = self.get_re() + other.get_re()
        new_im = self.get_im() + other.get_im()
        return complex_(new_re, new_im)
    
    def multiply(self,other):
        new_re = self.get_re() * other.get_re()
        new_im = self.get_im() * other.get_im()
        return complex(new_re, new_im)

if __name__ =='__main__':
    w = complex_(1,-3)
    x = complex_(-1,3)
    y = complex_(1,3)
    z = complex_(-1,-3)
    print(w)
    print(x)
    print(y)
    print(z)
    print(w.cadd(x).cadd(y).cadd(z))
    print((1-3j) + (-1+3j) + (1+3j) + (-1-3j))
    print(w + x + y + z)
    print(w.multiply(x))