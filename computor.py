#!/usr/bin/python3

import sys

class Polynomial:

    all_terms = {}
    degree = 0

    def __init__(self, sign, coefficient, variable, exponent, inverse=False):
        """Example -- '+', '5', 'X', '0'"""
        try:
            self.coefficient = float(sign + coefficient)
        except:
            self.coefficient = float(coefficient)
        self.variable = variable
        self.exponent = int(exponent)
        if inverse:
            self.coefficient *= -1
    
    def __str__(self):
        num = abs(self.coefficient)
        if num % 1 == 0:
            num = int(num)
        return f"{num} * {self.variable}^{self.exponent}"
            
    
    @classmethod
    def get_terms(cls, equation):

        def proceed(terms, inverse):
            for i in range(0, len(terms), 4):
                variable, exponent = terms[i+3].split("^")
                term = Polynomial(terms[i], terms[i+1], variable, exponent, inverse=inverse)
                if term.exponent in cls.all_terms:
                    cls.all_terms[term.exponent].coefficient += term.coefficient
                else:
                    cls.all_terms[term.exponent] = term

        left, right = equation.split("=")
        terms = ["+"] + left.split()
        if not (terms[1] == '0' and len(terms) == 2):
            proceed(terms, inverse=False)
        terms = ["+"] + right.split()
        if not (terms[1] == '0' and len(terms) == 2):
            proceed(terms, inverse=True)
    
    @classmethod
    def print_reduced_form(cls):
        print("Reduced form: ", end="")
        try:
            term = cls.all_terms[0]
            if term.coefficient < 0:
                print(f"-{term}", end="")
            else:
                print(term, end="")
        except:
            pass
        for i in range(1, len(cls.all_terms)):
            try:
                term = cls.all_terms[i]
                if term.coefficient > 0:
                    sign = " +"
                else:
                    sign = " -"
                print(sign, term, end="")
            except:
                pass
        print(" = 0")
    
    @classmethod
    def print_degree(cls):
        terms = cls.all_terms
        try:
            exponents = [terms[t].exponent for t in terms.keys() if terms[t].coefficient != 0]
            cls.degree = max(exponents)
        except:
            cls.degree = 0
        print("Polynomial degree: ", cls.degree)
    
    @classmethod
    def solve(cls):
        """Solve Linear and Quadratic equations."""

        if cls.degree > 2:
            sys.exit("The polynomial degree is strictly greater than 2, I can't solve.")
        
        if cls.degree == 0:
            """n * X^0"""
            
            n = cls.all_terms[0].coefficient
            if n != 0:
                sys.exit("The eqution has no solution")
            print("Every real number is a solution")

        elif cls.degree == 1:
            """b * X^0 + a * X^1 = 0"""

            a = cls.all_terms[1].coefficient
            b = cls.all_terms[0].coefficient
            linear_formula(a, b)

        elif cls.degree == 2:
            """c * X^0 + b * X^1 + a * X^2 = 0"""

            a = cls.all_terms[2].coefficient
            b = cls.all_terms[1].coefficient
            c = cls.all_terms[0].coefficient
            discriminant = (b ** 2) - (4 * a * c)
            two_a = 2 * a

            if discriminant == 0:
                print("\033[1mDiscriminant is 0\033[0m")
                linear_formula(two_a, b)
            else:
                print("\nQuadratic Formula:")
                print(quadratic_formula.__doc__)
                print("a = ", a)
                print("b = ", b)
                print("c = ", c)
                print("2a = ", two_a)
                print("discriminant (b^2 - 4ac) = ", discriminant)
                if discriminant > 0:
                    print("\n\033[1mDiscriminant is strictly positive.\033[0m")
                    quadratic_formula(two_a, b, discriminant)
                else:
                    print("\n\033[1mDiscriminant is strictly negative.\033[0m",
                          "\nSo we would have to calculate complex solutions",
                          "with real and imaginary parts")
                    quadratic_formula(two_a, b, discriminant, simple=False)


def linear_formula(a, b):
    """x = -b / a"""

    print("The solution is:")
    if b == 0 and a == 0:
        print("Every real number is a solution")
    elif a == 0:
        sys.exit("The eqution has no solution")
    elif b == 0:
        print(0)
    else:
        print(-b / a)
    
def quadratic_formula(two_a, b, discriminant, simple=True):
    """
        -b +- sqrt(b^2 - 4ac)
    x = —————————————————————
                2a
    """
    if simple:
        sqrt = discriminant ** 0.5
        print("sqrt (discriminant ** 0.5) =", sqrt)
        x1 = (-b - sqrt) / two_a
        x2 = (-b + sqrt) / two_a
        print("\nThe two solutions are:")
        print("x1 (-b - sqrt) / 2a =\033[1m", round(x1, 6), "\033[0m")
        print("x2 (-b + sqrt) / 2a =\033[1m", round(x2, 6), "\033[0m")
    else:
        discriminant *= -1
        print(f"\n=> convert discriminant (b^2 - 4ac) to positive = {discriminant}")
        sqrt = discriminant ** 0.5
        print("=> calculate sqrt (discriminant ** 0.5) =", sqrt)
        real = -b / two_a
        print("=> calculate real part (-b / two_a) = ", real)
        imaginary = sqrt / two_a
        print("=> calculate imaginary part (sqrt / 2a) = ", imaginary)
        print("\nThe two complex solutions are:")
        print(f"real - imaginary = \033[1m{round(real, 6)} - {round(imaginary, 6)}i\033[0m")
        print(f"real + imaginary = \033[1m{round(real, 6)} + {round(imaginary, 6)}i\033[0m")


def main():
    if len(sys.argv) != 2:
        sys.exit('Usage: ./computor.py "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"')
    Polynomial.get_terms(sys.argv[1])
    Polynomial.print_reduced_form()
    Polynomial.print_degree()
    Polynomial.solve()

if __name__ == "__main__":
    main()