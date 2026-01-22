from math import*
import sys


class vector_v0():
    def __init__(self):
        self.x = 1.0
        self.y = 0.0

def atan_calculation(iter):
    return [atan(2**-i) for i in range(iter)]

def CORDIC_gain(iter):
    val = 1.0
    for i in range(iter):
        exp_2i = -2 * i
        val *= 1 / sqrt(1 + 2 ** (exp_2i))
    return val

def CORDIC(theta):
    iter = 50
    v = vector_v0()
    K = CORDIC_gain(iter)
    x = v.x * K
    y = v.y * K

    atan_calc = atan_calculation(iter)
    for iteration in range(iter):
        shift = 1 if theta >= 0 else -1
        xn = x - shift * y * (2 ** -iteration)
        yn = y + shift * x * (2 ** -iteration)
        theta_n = theta - shift * atan_calc[iteration]
        x, y, theta = xn, yn, theta_n
    return x, y

def main(RED, GREEN, RESET):
    try:
        try:
            theta_input = int(input("pi / "))
            print()

        except ValueError:
            print(f"{RED}\nInvalid Value\n{RESET}")
            return

        if theta_input == int(theta_input):
            theta = pi / theta_input
        else: print(f"{RED}Invalid input{RESET}")
        cosine_theta, sine_theta = CORDIC(theta)

        print(f"{GREEN}CORDIC Algorithm Values{RESET}")
        print(f"CORDIC -> Cosine : {cosine_theta}")
        print(f"CORDIC -> Sine : {sine_theta}\n")

        print(f"{GREEN}Math Library Function Sanity Check{RESET}")
        print(f"Math Library -> cosine : {cos(theta)}")
        print(f"Math Library -> sine : {sin(theta)}\n")

    except KeyboardInterrupt:
        print(f"{RED}KeyboardInterrupt{RESET}")
        sys.exit(0)


if __name__ == "__main__":
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    RESET = '\033[0m'
    print(f"{GREEN}CORDIC Algorithm{RESET}")
    while True:
        main(RED, GREEN, RESET)