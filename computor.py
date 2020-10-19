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
        Polynomial.degree = max([self.exponent, Polynomial.degree])
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
        print("Polynomial degree: ", Polynomial.degree)
    
    @classmethod
    def solve(cls):
        """Solve Linear and Quadratic equations.

        Standard forms
            Linear:     ax + by = c
            Quadratic:  ax^2 + bx + c = 0
        
        Quadratic formula:
            -b +- sqrt(b^2 - 4ac)
        x = —————————————————————
                    2a
        """

        if cls.degree > 2:
            sys.exit("The polynomial degree is strictly greater than 2, I can't solve.")
        
        a, b, c = 0, 0, 0
        if cls.degree == 0:
            x = cls.all_terms[0].coefficient
            print(x)
        elif cls.degree == 1:
            a = cls.all_terms[1].coefficient
            b = cls.all_terms[0].coefficient
            print(f"The solution is:")
            if b == 0:
                print(0)
            else:
                try:
                    print(-b / a)
                except:
                    print("The eqution has no solution")
        elif cls.degree == 2:
            a = cls.all_terms[2].coefficient            
            b = cls.all_terms[1].coefficient
            c = cls.all_terms[0].coefficient
            discriminant = (b ** 2) - (4 * a * c)
            two_a = 2 * a

            if discriminant > 0:
                print("Discriminant is strictly positive, the two solutions are:")
            elif discriminant < 0:
                print("Discriminant is strictly negative, the two solutions are:")
            else:
                print(f"Discriminant is 0, the solution is:{-b / two_a}")
                sys.exit(0)

            sqrt = discriminant ** 0.5
            x1 = (-b - sqrt) / two_a
            x2 = (-b + sqrt) / two_a
            try:
                print(round(x1, 6))
                print(round(x2, 6))
            except:
                print("The eqution has no real solutions")


def main():
    Polynomial.get_terms(sys.argv[1])
    Polynomial.print_reduced_form()
    Polynomial.print_degree()
    Polynomial.solve()

if __name__ == "__main__":
    main()