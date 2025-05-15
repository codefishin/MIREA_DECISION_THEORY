import matplotlib.pyplot as plt
import numpy as np


class Gradient:
    def __init__(self, vector1, vector2):
        self.vector1 = vector1
        self.vector2 = vector2
        self.grad = f'({vector1}; {vector2})'
        self.anti_grad = f'(-{vector1}; -{vector2})'


class Setup:
    def __init__(self, x1, x2, gradient: Gradient):
        self.x1 = x1
        self.x2 = x2
        self.equation = f'{x1}x1 + {x2}x2'
        self.diff_equation = f'{x1} + {x2}'
        self.gradient = gradient

    def print(self):
        print('f(x) =', self.equation,
              "f(x)' =", self.diff_equation,
              'grad =', self.gradient.grad,
              'anti-grad =', self.gradient.anti_grad, end='\n'+'*'*50+'\n')


class Functions:
    def __init__(self, eqx1, eqx2, equality1,
                 eqx3, eqx4, equality2):
        self.eq1 = f'{eqx1}x1 + {eqx2}x2 <= {equality1}'
        self.eq2 = f'{eqx3}x1 + {eqx4}x2 <= {equality2}'
        self.eq3 = 'x1,x2 >= 0'
        self.y_func1 = f'{eqx2}y = {equality1} - {eqx1}x'
        self.y_func2 = f'{eqx4}y = {equality2} - {eqx3}x'
        self.eqx1 = eqx1
        self.eqx2 = eqx2
        self.eqx3 = eqx3
        self.eqx4 = eqx4
        self.equality1 = equality1
        self.equality2 = equality2

    def check_odr(self):
        print("ODR:")
        point_y_intercept = (0, self.equality1 / self.eqx2)
        checked_str = f'{self.eqx1} * {point_y_intercept[0]} + {self.eqx2} * {point_y_intercept[1]} == {self.equality1}'
        checked = self.eqx1 * point_y_intercept[0] + self.eqx2 * point_y_intercept[1] == self.equality1
        print(checked_str, checked, sep='\n')

        point_x_intercept = (self.equality1 / self.eqx1, 0)
        checked_str = f'{self.eqx1} * {point_x_intercept[0]} + {self.eqx2} * {point_x_intercept[1]} == {self.equality1}'
        checked = self.eqx1 * point_x_intercept[0] + self.eqx2 * point_x_intercept[1] == self.equality1
        print(checked_str, checked, sep='\n')

    def generate_graph(self):
        x = np.linspace(0, 10, 200)
        vec_limit = np.linspace(-3, 3, 200)
        vec_on_limit = np.linspace(0, 6.5, 200)
        draw_on_vec = np.linspace(0, 6, 200)
        y = (self.equality1 - self.eqx1 * x) / self.eqx2
        y2 = (self.equality2 - self.eqx2 * x) / self.eqx4
        vec1 = 5 * vec_limit / 3
        vec2 = -5 * vec_limit / 3

        plt.plot(x, y, label=self.y_func1)
        plt.plot(x, y2, label=self.y_func2)
        plt.plot(vec_limit, vec1, label='grad')
        plt.plot(vec_limit, vec2, label='anti-grad')
        plt.plot(vec_on_limit, y + vec2 + 2, label="")
        plt.plot(draw_on_vec, vec2 + 3.75)
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.legend(loc='best', title="Функции")
        plt.grid()
        plt.show()

    def print(self):
        print(self.eq1, self.eq2, self.eq3, self.y_func1, self.y_func2, sep='\n', end='\n'+'*'*50+'\n')

    def process(self):
        self.eq1 = self.eq1.replace('<=', '==')
        self.eq1 = self.eq1.replace('>=', '==')
        self.eq2 = self.eq2.replace('<=', '==')
        self.eq2 = self.eq2.replace('>=', '==')
        self.eq3 = self.eq3.replace('<=', '==')
        self.eq3 = self.eq3.replace('>=', '==')



def main():
    x1 = 3
    x2 = 5
    gradient = Gradient(x1, x2)
    equation = Setup(x1, x2, gradient)
    other = Functions(3, 8, 28, 7, 4, 42)
    equation.print()
    other.print()
    other.process()
    other.print()
    other.check_odr()
    other.generate_graph()

if __name__ == "__main__":
    main()
