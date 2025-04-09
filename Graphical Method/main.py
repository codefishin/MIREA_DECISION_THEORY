class main_function:
    def __init__(self, x1, x2):
        self.x1 = x1
        self.x2 = x2
        self.equation = str(x1) + 'x1 + ' + str(x2) + 'x2'
        self.diff_equation = str(x1) + ' + ' + str(x2)
        self.grad = '(' + str(x1) + ';' + str(x2) + ')'
        self.anti_grad = '(-' + str(x1) + ';-' + str(x2) + ')'

    def print(self):
        print('f(x) =', self.equation,
              "f(x)' =", self.diff_equation,
              'grad =', self.grad,
              'anti-grad =', self.anti_grad, end='\n'+'*'*50+'\n')

    # todo: odr


class other_functions:
    def __init__(self):
        self.eq1 = '3x1 + 8x2 <= 28'
        self.eq2 = '7x1 + 4x2 <= 42'
        self.eq3 = 'x1,x2 >= 0'

    def print(self):
        print(self.eq1, self.eq2, self.eq3, sep='\n')

    def process(self):
        self.eq1 = self.eq1.replace('<=', '==')
        self.eq1 = self.eq1.replace('>=', '==')
        self.eq2 = self.eq2.replace('<=', '==')
        self.eq2 = self.eq2.replace('>=', '==')
        self.eq3 = self.eq3.replace('<=', '==')
        self.eq3 = self.eq3.replace('>=', '==')


def main():
    equation = main_function(3, 5)
    other = other_functions()
    equation.print()
    other.print()
    other.process()
    other.print()

if __name__ == "__main__":
    main()
