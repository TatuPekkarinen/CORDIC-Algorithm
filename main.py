from math import sqrt, atan, pi, cos, sin
import matplotlib.pyplot as plt
import numpy as np
import sys

RED = "\033[0;31m"
GREEN = "\033[0;32m"
RESET = '\033[0m'

class v_v0():
    def __init__(self):
        self.x = 1.0
        self.y = 0.0

#iterations 
itr = 30

#the margin of error as epsilon
epsilon = 1e-9

#microsteps lookuptable as variable AC
def ATAN_CALC(itr):
    return [atan(2**-i) for i in range(itr)]

ATAN_TB = ATAN_CALC(itr)

#gain value as variable K
def C_GAIN(itr):
    val = 1.0
    for i in range(itr):
        exp_2i = -2 * i
        val *= 1 / sqrt(1 + 2 ** (exp_2i))
    return val

K = C_GAIN(itr)

def CORDIC(theta):
    v = v_v0()
    x = v.x * K
    y = v.y * K

    for i in range(itr):
        dir = 1 if theta >= 0 else -1
        xn = x - dir * y * (2 ** -i)
        yn = y + dir * x * (2 ** -i)
        tn = theta - dir * ATAN_TB[i]
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
        cos_error = []
        sin_error = []
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

            cos_error.append(abs(cordic_cos - lib_cos))
            sin_error.append(abs(cordic_sin - lib_sin))

            ccos_val.append(cordic_cos)
            csin_val.append(cordic_sin)

        print(f"{RED}MAX ERROR{RESET} (cos) -> {max(cos_error)}")
        print(f"{RED}MAX ERROR{RESET} (sin) -> {max(sin_error)}")

        print(f"{RED}LAST ANGLE ERROR{RESET} (cos) -> {abs(cordic_cos - lib_cos)}")
        print(f"{RED}LAST ANGLE ERROR{RESET} (sin) -> {abs(cordic_sin - lib_sin)}")

        plot(angle, ccos_val, csin_val)

    except ValueError:
        print(f"{RED}\nInvalid Value\n{RESET}")
        return

if __name__ == "__main__":
    print(f"\n{GREEN}CORDIC Algorithm{RESET}")
    try: 
        main()
    except KeyboardInterrupt: 
        print(f"\n{RED}KeyboardInterrupt{RESET}")
        sys.exit(0)