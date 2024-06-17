#!/usr/bin/env python3
# factor_quadratic.py


<<<<<<< HEAD
def factor_quadratic(J, K, L):  # define the factor function, takes in quadratic
    # coeffs ints.
    print("Given the quadratic:")
    print(f" {J}x^2 + {K}x + {L} = 0")
    print("The factors are:")
=======
def factor_quadratic(J, K, L):
    print("Given the quadratic:", end=" ")
    print(f"{J}x^2 + {K}x + {L}")
>>>>>>> 8714fac53a740147291686210ad82b687caf566b

    for a in range(1, J + 1):  # we want to include J in the list of numbers
        # iterated over
        if J % a == 0:  # i.e. is 'a' a factor of 'J'?
            c = J // a  # "//" integer division: rounds down
            for b in range(1, L + 1):  # similar process for b
                if L % b == 0:
                    d = L // b
<<<<<<< HEAD
                    if a * d + b * c == K:  # check that a and b (and hence
                        # c and d) yield K
                        print(f" ({a}x + {b})" f"({c}x + {d})")


def main():
    factor_quadratic(115425, 3254121, 379020)  # function has j,k,l integer inputs
    # and is executable from the command line
=======
                    if a * d + b * c == K:
                        print("The factors are:", end=" ")
                        print(f"({a}x + {b})" f"({c}x + {d})")


def main():
    factor_quadratic(115425, 3254121, 379020)
>>>>>>> 8714fac53a740147291686210ad82b687caf566b


if __name__ == "__main__":
    main()
