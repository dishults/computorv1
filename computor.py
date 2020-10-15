#!/usr/bin/python3

import sys

class Polynomial:

    all_terms = {}
    degree = 0

    def __init__(self, sign, coefficient, variable, exponent, inverse=False):
        """Example -- '+', '5', 'X', '0'"""
        self.coefficient = float(sign + coefficient)
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
        proceed(terms, inverse=False)
        terms = ["+"] + right.split()
        proceed(terms, inverse=True)
    
    @classmethod
    def print_reduced_form(cls):
        print("Reduced form: ", end="")
        term = cls.all_terms[0]
        print(term, end="")
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
        if cls.degree > 2:
            sys.exit("The polynomial degree is strictly greater than 2, I can't solve.")


def main():
    Polynomial.get_terms(sys.argv[1])
    Polynomial.print_reduced_form()
    Polynomial.print_degree()

if __name__ == "__main__":
    main()