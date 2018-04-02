"""
Created at: 02-04-2018
Author: Vubon Roy
Arithmetic Sequence ..

Example: Find 35th term value following series
3, 9, 15, 21, .........

Rules: finding term = first term + (n - 1) different between consecutive numbers

Here n is the finding term

user should send a list of consecutive numbers
"""


def arithmetic_sequence(terms, finding_term):
    difference = terms[1] - terms[0]
    first_term = terms[0]
    finding_term = finding_term

    return first_term + (finding_term - 1) * difference
