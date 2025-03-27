import pandas as pd
import numpy

class PlayerData:
    def __init__(self, elo: float, kd: float, elo_diff: float,
                 loss_in_30: float, name):
        self.elo = elo
        self.kd = kd
        self.elo_diff = elo_diff
        self.loss30 = loss_in_30
        self.name = name


player_list = []
player_dict = {'Alias': [],
               'ELO': [],
               'ELO diff': [],
               'K/D': [],
               'Losses in the last 30': []}
arr = numpy.zeros((9, 9), dtype=object)


def addToList(e: float, kd: float,
              ed: float, loss: float, name) -> None:
    player = PlayerData(e, kd, ed, loss, name)
    player_dict['Alias'].append(player.name)
    player_dict['ELO'].append(player.elo)
    player_dict['ELO diff'].append(player.elo_diff)
    player_dict['K/D'].append(player.kd)
    player_dict['Losses in the last 30'].append(str(player.loss30) + " losses")
    player_list.append(player)


def autoListFromTask() -> None:
    addToList(3318, 1.14, -216, 11,  "sinitza7")  # 1
    addToList(2473, 1.04, 629, 14, "neverWMD")  # 2
    addToList(2244, 1.08, 858, 19,  "xStaipy")  # 3
    addToList(2448, 1.10, 654, 18,  "Ness1z")  # 4
    addToList(1978, 1.24, 1124, 15,  "-efemeral")  # 5
    addToList(2342, 0.96, 760, 17,  "bishUP_me")  # 6
    addToList(3002, 1.26, 100, 11,  "orstedo")  # 7
    addToList(1766, 1.09, 1336, 13,  "yourhate")  # 8
    addToList(2608, 1.11, 494, 14, "senz")  # 9


def userAddToList(length: int) -> None:  # for fun
    for i in range(0, length):
        addToList(float(input("Enter elo")),
                  float(input("Enter k/d")),
                  float(input("Enter elo diff")),
                  float(input("Enter loss/30")),
                  str(input("Enter alias")))


def calc_p_n_d(index1: int, index2: int, *, printable=False):
    p = 0
    n = 0
    output_p = "P" + str(index1) + str(index2)
    output_n = "N" + str(index1) + str(index2)
    output_d = "D" + str(index1) + str(index2) + " = " + output_p + '/' + output_n + ' = '
    player1 = player_list[index1 - 1]
    player2 = player_list[index2 - 1]
    output_p += " = "
    output_n += " = "

    if player1.elo == player2.elo:
        output_p += "0 + "
        output_n += "0 + "
    elif player1.elo > player2.elo:
        output_p += "5 + "
        output_n += "0 + "
        p += 5
    else:
        output_p += "0 + "
        output_n += "5 + "
        n += 5

    if player1.elo_diff == player2.elo_diff:
        output_p += "0 + "
        output_n += "0 + "
    elif player1.elo_diff < player2.elo_diff:
        output_p += "5 + "
        output_n += "0 + "
        p += 5
    else:
        output_p += "0 + "
        output_n += "5 + "
        n += 5

    if player1.kd == player2.kd:
        output_p += "0 + "
        output_n += "0 + "
    elif player1.kd > player2.kd:
        output_p += "3 + "
        output_n += "0 + "
        p += 3
    else:
        output_p += "0 + "
        output_n += "3 + "
        n += 3

    if player1.loss30 == player2.loss30:
        output_p += "0 ="
        output_n += "0 ="
    elif player1.loss30 < player2.loss30:
        output_p += "1 ="
        output_n += "0 ="
        p += 1
    else:
        output_p += "0 ="
        output_n += "1 ="
        n += 1

    if printable is True:
        print(output_p, p, '\b;')
        print(output_n, n, '\b;')
    output_d += str(p) + '/' + str(n) + " ="

    if n != 0:
        d = p / n
        if printable is True:
            if d > 1:
                print(output_d, d, '> 1 - принимаем;')
            else:
                print(output_d, d, '< 1 - отбрасываем;')
    else:
        d = numpy.inf
        if printable is True:
            print(output_d, d, '> 1 - принимаем;')
    return d


def get_alts_connections() -> None:
    for i in range(9):
        connection = 0
        connected = 0
        for j in range(9):
            if i == j:
                continue
            if arr[i, j] != '':
                connection += 1
            if arr[j, i] != '':
                connected += 1
        print(f'A{i + 1} ({connection}, {connected})')


def gen_electre_list(*, c = 1, can_print=False) -> None:
    for i in range(9):
        for j in range(9):
            if i == j:
                arr[i, j] = 'X'
            if i == j or i > j:
                continue
            if can_print is True:
                print(f"Рассмотрим альтернативы {i + 1} и {j + 1} (i = {i + 1}, j = {j + 1})")
            r1 = calc_p_n_d(i + 1, j + 1, printable=can_print)
            r2 = calc_p_n_d(j + 1, i + 1, printable=can_print)
            if r1 > c:
                arr[i, j] = r1
            else:
                arr[i, j] = ''
            if r2 > c:
                arr[j, i] = r2
            else:
                arr[j, i] = ''

            if can_print is True:
                print('\n')
    d = pd.DataFrame(arr)
    d.index += 1
    d.columns += 1
    print(d, '\n')
    get_alts_connections()


def main() -> None:
    autoListFromTask()  # switchable with userAddToList(10)

    gen_electre_list()


if __name__ == "__main__":
    main()
