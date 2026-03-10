from math import sqrt, atan, pi, cos, sin, radians
import sys

#the margin of error
epsilon = 1e-9

RED = "\033[0;31m"
GREEN = "\033[0;32m"
RESET = '\033[0m'

class v_v0():
    def __init__(self):
        self.x = 1.0
        self.y = 0.0

def ATAN_CALC(itr):
    return [atan(2**-i) for i in range(itr)]

def C_GAIN(itr):
    val = 1.0
    for i in range(itr):
        exp_2i = -2 * i
        val *= 1 / sqrt(1 + 2 ** (exp_2i))
    return val

def CORDIC(theta):
    itr = 40
    v = v_v0()
    K = C_GAIN(itr)
    x = v.x * K
    y = v.y * K

    atan_calc = ATAN_CALC(itr)
    for i in range(itr):
        shift = 1 if theta >= 0 else -1
        xn = x - shift * y * (2 ** -i)
        yn = y + shift * x * (2 ** -i)
        tn = theta - shift * atan_calc[i]
        x, y, theta = xn, yn, tn
    return x, y

def absolute_value(n):
    if (n * -1) >= 0: return n * -1
    else: return n

#limit values so smaller than epsilon is just zero
def epsilon_clamp(n):
    if absolute_value(n) <= epsilon:
        return 0.0
    return n

def main():
    try:
        degree = float(input("Enter Angle In Degrees: "))
        theta = degree * (pi / 180)
        cordic_cos, cordic_sin = CORDIC(theta)

        cordic_cos = epsilon_clamp(cordic_cos)
        cordic_sin = epsilon_clamp(cordic_sin)

        print(f"{GREEN}CORDIC Algorithm Values{RESET}")
        print(f"CORDIC -> Cosine : {cordic_cos}")
        print(f"CORDIC -> Sine : {cordic_sin}\n")

        print(f"{GREEN}Math Library Function{RESET}")
        print(f"Math Library -> Cosine : {epsilon_clamp(cos(theta))}")
        print(f"Math Library -> Sine : {epsilon_clamp(sin(theta))}\n")

    except ValueError:
        print(f"{RED}\nInvalid Value\n{RESET}")
        return

if __name__ == "__main__":
    print(f"{GREEN}CORDIC Algorithm{RESET}")
    while True:
        try: 
            main()
        except KeyboardInterrupt: 
            print(f"\n{RED}KeyboardInterrupt{RESET}")
            sys.exit(0)