from decimal import Decimal
from numpy import transpose


class PrioritySet:
    def __init__(self, priority_set):
        self.priority_set = priority_set

    def redefine_set(self, new_set):
        self.priority_set = new_set

    def __get_v_num(self, div=1):
        result = 1
        for element in self.priority_set:
            result = element * result
        return pow(result, 1/div)

    def __get_w_num(self, e__v, div=1):
        if e__v is None or e__v == 0:
            e__v = 1
        return self.__get_v_num(div) / e__v

    def get_v(self, div=1):
        return float(f"{Decimal(self.__get_v_num(div)):.4}")

    def get_w(self, e__v, div=1):
        return float(f"{Decimal(self.__get_w_num(e__v, div)):.3}")


class ProcessPriorities:
    def __init__(self):
        self.prioritiesK = [
            [1, 1, 5, 3],
            [1, 1, 5, 3],
            [1 / 5, 1 / 5, 1, 3],
            [1 / 3, 1 / 3, 1 / 3, 1]
        ]
        self.prioritiesK1 = [
            [1, 1, 3, 5, 5],
            [1, 1, 5, 5, 5],
            [1 / 3, 1 / 5, 1, 3, 5],
            [1 / 5, 1 / 5, 1 / 5, 1, 5],
            [1 / 5, 1 / 5, 1 / 5, 1 / 5, 1]
        ]
        self.prioritiesK2 = [
            [1, 3, 5, 7, 7],
            [1 / 3, 1, 3, 5, 5],
            [1 / 5, 1 / 3, 1, 3, 5],
            [1 / 7, 1 / 5, 1 / 3, 1, 1],
            [1 / 5, 1 / 5, 1 / 5, 1, 1]
        ]
        self.prioritiesK3 = [
            [1, 1 / 3, 1, 3, 3],
            [3, 1, 3, 5, 5],
            [1, 1 / 3, 1, 3, 3],
            [1 / 3, 1 / 5, 1 / 3, 1, 1],
            [1 / 3, 1 / 5, 1 / 3, 1, 1]
        ]
        self.prioritiesK4 = [
            [1, 1, 3, 3, 5],
            [1, 1, 3, 3, 5],
            [1 / 3, 1 / 3, 1, 1, 3],
            [1 / 3, 1 / 3, 1, 1, 3],
            [1 / 5, 1 / 5, 1 / 3, 1 / 3, 1]
        ]


    def process_v_w(self, priorities):
        e_vi = 0
        for i in range(0, len(priorities)):
            obj = PrioritySet(priorities[i])
            e_vi += obj.get_v(div=len(priorities))
            print(obj.get_v(div=len(priorities)))

        print('*' * 50)
        print('e_vi=', e_vi, sep='', end='\n' + '*' * 50 + '\n')

        for i in range(0, len(priorities)):
            obj = PrioritySet(priorities[i])
            print(obj.get_w(e_vi, div=len(priorities)))

    def get_processed_w(self, priorities):
        e_vi = 0
        for i in range(0, len(priorities)):
            obj = PrioritySet(priorities[i])
            e_vi += obj.get_v(div=len(priorities))

        r = []

        for i in range(0, len(priorities)):
            obj = PrioritySet(priorities[i])
            r.append(obj.get_w(e_vi, div=len(priorities)))
        return r

    def launch(self):
        print('---PROPERTY K---')
        self.process_v_w(self.prioritiesK)
        print('---PROPERTY K1---')
        self.process_v_w(self.prioritiesK1)
        print('---PROPERTY K2---')
        self.process_v_w(self.prioritiesK2)
        print('---PROPERTY K3---')
        self.process_v_w(self.prioritiesK3)
        print('---PROPERTY K4---')
        self.process_v_w(self.prioritiesK4)


class SMatrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.lambdaMax = 0
        self.SI = 1.12


    def process_matrix(self,priority):  # P, IS, OS
        r = self.get_S()
        obj = ProcessPriorities()
        w = obj.get_processed_w(priority)  # danger
        result = []
        for i in range(0, len(r)):
            print(f'{r[i]} * {w[i]} = {r[i]*w[i]}')
            result.append(r[i]*w[i])
        self.lambdaMax = sum(result)
        print('IS:', self.get_IS())
        print('OS:', self.get_OS(), '\nlambdaMax:')
        return self.lambdaMax

    def get_S(self):
        m = transpose(self.matrix)
        result = []
        for i in range(0,len(m)):
            result.append(float(sum(m[i])))
        return result

    def get_IS(self):
        p1 = self.lambdaMax - len(self.matrix[0])
        p2 = len(self.matrix[0]) - 1
        return p1/p2

    def get_OS(self):
        return self.get_IS() / self.SI


def process_all_matrix(m, priority):
    matrix = SMatrix(m)
    print(matrix.get_S())
    print(matrix.process_matrix(priority))


matrixK = [  # for S, P, OS, IS
    [1, 1, 3, 5],
    [1, 1, 3, 5],
    [1 / 3, 1 / 3, 1, 3],
    [1 / 5, 1 / 5, 1 / 3, 1]
]
matrixK1 = [
    [1, 3, 3, 7, 7],
    [1 / 3, 1, 3, 3, 3],
    [1 / 3, 1 / 3, 1, 1, 3],
    [1 / 7, 1 / 3, 1, 1, 3],
    [1 / 7, 1 / 5, 1 / 3, 1 / 3, 1]
]
matrixK2 = [
    [1, 3, 5, 7, 7],
    [1 / 3, 1, 3, 5, 5],
    [1 / 5, 1 / 3, 1, 1, 3],
    [1 / 7, 1 / 5, 1, 1, 3],
    [1 / 7, 1 / 5, 1 / 3, 1 / 3, 1]
]
matrixK3 = [
    [1, 1 / 3, 1, 3, 3],
    [3, 1, 3, 5, 5],
    [1, 1 / 3, 1, 1, 1],
    [1 / 3, 1 / 5, 1, 1, 1],
    [1 / 3, 1 / 5, 1, 1, 1]
]
matrixK4 = [
    [1, 1, 4, 4, 5],
    [1, 1, 4, 4, 5],
    [1 / 4, 1 / 4, 1, 1, 2],
    [1 / 4, 1 / 4, 1, 1, 2],
    [1 / 5, 1 / 5, 1 / 2, 1 / 2, 1]
]


def calc_w(w2, w31, w32, w33, w34):
    w1r = w2[0] * w31[0] + w2[1] * w32[0] + w2[2] * w33[0] + w2[3] * w34[0]
    w2r =w2[0] * w31[1] + w2[1] * w32[1] + w2[2] * w33[1] + w2[3] * w34[1]
    w3r = w2[0] * w31[2] + w2[1] * w32[2] + w2[2] * w33[2] + w2[3] * w34[2]
    w4r = w2[0] * w31[3] + w2[1] * w32[3] + w2[2] * w33[3] + w2[3] * w34[3]
    w5r = w2[0] * w31[4] + w2[1] * w32[4] + w2[2] * w33[4] + w2[3] * w34[4]

    print(f'W1 -> {w2[0]} * {w31[0]} + {w2[1]} * {w32[0]}'
          f' + {w2[2]} * {w33[0]} + {w2[3]} * {w34[0]} = {w1r}')

    print(f'W2 -> {w2[0]} * {w31[1]} + {w2[1]} * {w32[1]}'
          f' + {w2[2]} * {w33[1]} + {w2[3]} * {w34[1]} = {w2r}')

    print(f'W3 -> {w2[0]} * {w31[2]} + {w2[1]} * {w32[2]}'
          f' + {w2[2]} * {w33[2]} + {w2[3]} * {w34[2]} = {w3r}')

    print(f'W4 -> {w2[0]} * {w31[3]} + {w2[1]} * {w32[3]}'
          f' + {w2[2]} * {w33[3]} + {w2[3]} * {w34[3]} = {w4r}')

    print(f'W5 -> {w2[0]} * {w31[4]} + {w2[1]} * {w32[4]}'
          f' + {w2[2]} * {w33[4]} + {w2[3]} * {w34[4]} = {w5r}')

    variables = {w1r:'1',
                 w2r:'2',
                 w3r:'3',
                 w4r:'4',
                 w5r:'5'}
    print(f'best choice: {variables.get(max(variables))}')



def main():
    priorities = ProcessPriorities()
    priorities.launch()
    process_all_matrix(matrixK, priorities.prioritiesK)
    process_all_matrix(matrixK1, priorities.prioritiesK1)
    process_all_matrix(matrixK2, priorities.prioritiesK2)
    process_all_matrix(matrixK3, priorities.prioritiesK3)
    process_all_matrix(matrixK4, priorities.prioritiesK4)
    calc_w(
        priorities.get_processed_w(priorities.prioritiesK),
        priorities.get_processed_w(priorities.prioritiesK1),
        priorities.get_processed_w(priorities.prioritiesK2),
        priorities.get_processed_w(priorities.prioritiesK3),
        priorities.get_processed_w(priorities.prioritiesK4)
    )


if __name__ == '__main__':
    main()
