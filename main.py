from math import sqrt, atan, pi, cos, sin
import sys

class vector_v0():
    def __init__(self):
        self.x = 1.0
        self.y = 0.0

def atan_calculation(i):
    return [atan(2**-i) for i in range(i)]

def CORDIC_gain(i):
    val = 1.0
    for i in range(i):
        exp_2i = -2 * i
        val *= 1 / sqrt(1 + 2 ** (exp_2i))
    return val

def CORDIC(theta):
    i = 50
    v = vector_v0()
    K = CORDIC_gain(i)
    x = v.x * K
    y = v.y * K

    atan_calc = atan_calculation(i)
    for iation in range(i):
        shift = 1 if theta >= 0 else -1
        xn = x - shift * y * (2 ** -iation)
        yn = y + shift * x * (2 ** -iation)
        theta_n = theta - shift * atan_calc[iation]
        x, y, theta = xn, yn, theta_n
    return x, y

def main(RED, GREEN, RESET):
    try:
        try:
            theta_input = int(input("pi / "))
            print()
            theta = pi / theta_input

        except ValueError:
            print(f"{RED}\nInvalid Value\n{RESET}")
            return
        else: 
            print(f"{RED}Invalid input{RESET}")
            
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
