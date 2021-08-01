import numpy as np


vctr = np.array([8.218,
                 -9.341])
vctr1 = np.array([-1.129,
                  2.111])
pluss = vctr + vctr1
print('plus', pluss)

vctr2 = np.array([7.119,
                  8.215])
vctr3 = np.array([-8.223,
                  0.878])
minuss = vctr2 - vctr3
print('minus', minuss)

vctr4 = np.array([1.671, -1.012, -0.318])
scalar_multiply = 7.41 * np.array(vctr4)
print('Scalar Multiply', scalar_multiply)
