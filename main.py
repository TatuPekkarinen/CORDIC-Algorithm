from math import sqrt, atan, pi, cos, sin
import matplotlib.pyplot as plt
import numpy as np
import sys

#the margin of error as epsilon
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
    itr = 30
    v = v_v0()
    K = C_GAIN(itr)
    x = v.x * K
    y = v.y * K

    atan_calc = ATAN_CALC(itr)

    for i in range(itr):
        direction = 1 if theta >= 0 else -1
        xn = x - direction * y * (2 ** -i)
        yn = y + direction * x * (2 ** -i)
        tn = theta - direction * atan_calc[i]
        x, y, theta = xn, yn, tn
    return epsilon_round(x), epsilon_round(y)

#limit values so smaller than epsilon is just zero
def epsilon_round(n):
    if abs(n) <= epsilon:
        return 0.0
    return n

def plot(angle, ccos_val, csin_val):
    plt.figure(figsize=(10,6))
    plt.plot(angle, ccos_val, label="CORDIC.cos")
    plt.plot(angle, csin_val, label="CORDIC.sin")
    plt.legend()
    plt.title("CORDIC-Algorithm")
    plt.xlabel("(rad)")
    plt.ylabel("(val)")

    plt.grid(True)
    plt.show()

def main():
    try:
        angle = np.linspace(0, 4*pi, 500)

        ccos_val = []
        csin_val = []

        for theta in angle:
            theta = theta % (2 * pi)
            cos_quad, sin_quad = 1, 1

            if 0 <= theta <= pi / 2:
                theta_0 = theta

            elif pi / 2 < theta <= pi:
                theta_0 = pi - theta
                cos_quad, sin_quad = -1, 1

            elif pi < theta <= 3 * pi / 2:
                theta_0 = theta - pi
                cos_quad, sin_quad = -1, -1

            else:
                theta_0 = 2 * pi - theta
                cos_quad, sin_quad = 1, -1

            cordic_cos, cordic_sin = CORDIC(theta_0)

            cordic_cos *= cos_quad
            cordic_sin *= sin_quad

            lib_cos = epsilon_round(cos(theta))
            lib_sin = epsilon_round(sin(theta))

            ccos_val.append(cordic_cos)
            csin_val.append(cordic_sin)

        print(f"{RED}MARGIN OF ERROR{RESET} (cos) -> {abs(cordic_cos - lib_cos)}")
        print(f"{RED}MARGIN OF ERROR{RESET} (sin) -> {abs(cordic_sin - lib_sin)}")
        plot(angle, ccos_val, csin_val)

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