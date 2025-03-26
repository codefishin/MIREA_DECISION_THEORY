from string import printable

import pandas as pd
import numpy
from PIL import ImageTk, Image
import tkinter


class PlayerData:
    def __init__(self, elo: float, kd: float, elo_diff: float,
                 loss_in_30: float, name):
        self.elo = elo
        self.kd = kd
        self.elo_diff = elo_diff
        self.loss30 = loss_in_30
        self.name = name
        """
            print("По лексикографической оптимизации лучшим вариантом является:", best_player)
            root = tkinter.Tk()
            lex_img = Image.open("")
            root.geometry("503x711")
            root.maxsize(503, 711)
            img = ImageTk.PhotoImage(lex_img)
            label1 = tkinter.Label(image=img)
            label1.image = img
            label1.place(x=0, y=0)
            root.mainloop()
        """


player_list = []
electra_list = []
player_dict = {'Alias': [],
               'ELO': [],
               'ELO diff': [],
               'K/D': [],
               'Losses in the last 30': []}


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



def get_electra_list(*, player_name_index = 0):
    player = player_list[player_name_index]
    if player.elo > 2900:
        elo = 15
    elif 2400 < player.elo <= 2900:
        elo = 10
    else:
        elo = 5

    if player.elo_diff > 400:
        elo_diff = 15
    elif 100 < player.elo_diff <= 400:
        elo_diff = 10
    else:
        elo_diff = 5

    if player.kd > 1.1:
        kd = 15
    elif 1 < player.kd <= 1.1:
        kd = 10
    else:
        kd = 5

    if player.loss30 > 18:
        loss = 15
    elif 12 < player.loss30 <= 18:
        loss = 10
    else:
        loss = 5

    electra_list.append(PlayerData(elo, kd, elo_diff, loss, player.name))


def calc_p_n_d(index1: int, index2: int, *, printable=False):
    p = 0
    n = 0
    d = 0
    output_p = "P" + str(index1) + str(index2)
    output_n = "N" + str(index1) + str(index2)
    output_d = "D" + str(index1) + str(index2) + " = " + output_p + '/' + output_n + ' = '
    player1 = electra_list[index1 - 1]
    player2 = electra_list[index2 - 1]
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

    if printable is False and p == 0 and n != 0:
        return numpy.inf
    if printable is False and p != 0 and n != 0:
        return p / n
    if printable is False and n == 0:
        return 0

    if n != 0:
        d = p / n
        if d > 1:
            print(output_d, d, '> 1 - принимаем;')
        else:
            if p == 0:
                d = numpy.inf
                print(output_d, d, '> 1 - принимаем;')
            else:
                print(output_d, d, '< 1 - отбрасываем;')
    else:
        print(output_d, d, '- деление на 0, отбрасываем')
    return d


def loop_through_electra_list(*, c = 0):
    arr = numpy.zeros((9, 9), dtype=object)
    for i in range(9):
        for j in range(9):
            if i == j:
                arr[i, j] = 'X'
            if i == j or i > j:
                continue
            # print(f"Рассмотрим альтернативы {i} и {j} (i = {i}, j = {j})")
            r1 = calc_p_n_d(i + 1, j + 1)
            r2 = calc_p_n_d(j + 1, i + 1)
            if r1 > c:
                arr[i, j] = r1
            else:
                arr[i, j] = ''
            if r2 > c:
                arr[j, i] = r2
            else:
                arr[j, i] = ''

            # print('\n')
    d = pd.DataFrame(arr)
    d.index += 1
    d.columns += 1
    print(d, '\n')


def main() -> None:
    autoListFromTask()  # switchable with userAddToList(10)

    df = pd.DataFrame(player_dict)
    df.index += 1
    print(df, '\n')
    for _ in range(0, 9):
        get_electra_list(player_name_index=_)
    loop_through_electra_list(c=2)


if __name__ == "__main__":
    main()
