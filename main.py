from math import sqrt, atan, pi, cos, sin
import sys

class vector_v0():
    def __init__(self):
        self.x = 1.0
        self.y = 0.0

def atan_calculation(iters):
    return [atan(2**-i) for i in range(iters)]

def CORDIC_gain(iters):
    val = 1.0
    for i in range(iters):
        exp_2i = -2 * i
        val *= 1 / sqrt(1 + 2 ** (exp_2i))
    return val

def CORDIC(theta):
    iters = 50
    v = vector_v0()
    K = CORDIC_gain(iters)
    x = v.x * K
    y = v.y * K

    atan_calc = atan_calculation(iters)
    for i in range(iters):
        shift = 1 if theta >= 0 else -1
        xn = x - shift * y * (2 ** -i)
        yn = y + shift * x * (2 ** -i)
        tn = theta - shift * atan_calc[i]
        x, y, theta = xn, yn, tn
    return x, y

def quit_program():
    sys.exit(0)
    return

def main(RED, GREEN, RESET):
    try:
        theta_degrees = float(input("Enter angle in degrees: "))
        theta = theta_degrees * pi / 180
        theta = ((theta + pi) % (2 * pi)) - pi
        cosine_theta, sine_theta = CORDIC(theta)

        print(f"{GREEN}CORDIC Algorithm Values{RESET}")
        print(f"CORDIC -> Cosine : {cosine_theta}")
        print(f"CORDIC -> Sine : {sine_theta}\n")

        print(f"{GREEN}Math Library Function Sanity Check{RESET}")
        print(f"Math Library -> cosine : {cos(theta)}")
        print(f"Math Library -> sine : {sin(theta)}\n")

    except ValueError:
        print(f"{RED}\nInvalid Value\n{RESET}")
        return


if __name__ == "__main__":
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    RESET = '\033[0m'

    print(f"{GREEN}CORDIC Algorithm{RESET}")
    while True:
        try: main(RED, GREEN, RESET)
        except KeyboardInterrupt: 
            print(f"\n{RED}KeyboardInterrupt{RESET}")
            quit_program()
