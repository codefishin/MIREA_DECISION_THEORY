class PlayerData:
    def __init__(self, elo: float, kd: float, elo_diff: float, loss_in_30: float, pos: int):
        self.elo = elo
        self.kd = kd
        self.elo_diff = elo_diff
        self.loss30 = loss_in_30
        self.pos = pos


player_list = []

def addToList(e: float, kd: float,
               ed: float, l: float, pos: int) -> None:
    player = PlayerData(e, kd, ed, l, pos)
    player_list.append(player)


def autoListFromTask() -> None:
    addToList(3318, 1.14, -216, 11, 1) # 1
    addToList(2473, 1.04, 629, 14, 2) # 2
    addToList(2244, 1.08, 858, 19, 3) # 3
    addToList(2448, 1.10, 654, 18, 4) # 4
    addToList(1978, 1.24, 1124, 15, 5) # 5
    addToList(2342, 0.96, 760, 17, 6) # 6
    addToList(3002, 1.26, 100, 11, 7) # 7
    addToList(1766, 1.09, 1336, 13, 8) # 8
    addToList(2608, 1.11, 494, 14, 9) # 9


def userAddToList(length: int) -> None: # for fun
    for i in range(0, length):
        addToList(float(input("Enter elo")),
                float(input("Enter k/d")),
                float(input("Enter elo diff")),
                float(input("Enter loss/30")),
                  i + 1)


def Pareto():
    index = 0
    last_index = index
    result = []
    for player in player_list:
        index += 1
        for next_player in player_list:
            if (player.elo > next_player.elo
                    and player.kd > next_player.kd
                    and player.elo_diff < next_player.elo_diff
                    and player.loss30 < next_player.loss30):
                print("A" + str(player.pos) + " доминирует над А" + str(next_player.pos))
                if index != last_index:
                    last_index = index
                    result.append(index)
                    continue
    return result


def FirstPareto():
    index = 0
    result = []
    print("Условия:\nОтличие в эло не выше 200.\nK/D игрока выше 1.\n\n")
    for player in player_list:
        index += 1
        if player.elo_diff < 200 and player.kd > 1:
            print("A" + str(index) + " удовлетворяет условиям.")
            result.append(index)
            continue
    return result


def Suboptimization():
    index = 0
    result = []
    print("Условия:\nГлавное: ELO выше 3050.\nОтличие в ELO меньше 100, но не меньше -250.\nK/D больше 1,1.\nКол-во поражений меньше 15.\n\n")
    for player in player_list:
        index += 1
        if (player.elo > 3050
                and 100 > player.elo_diff > -250
                and player.kd > 1.1
                and player.loss30 < 15):
            print("A" + str(index) + " удовлетворяет условиям.")
            result.append(index)
            continue
    return result


def main() -> None:
    autoListFromTask() # switchable with userAddToList(10)
    print("PARETO\n")
    print(Pareto())
    print("\nFIRST PARETO\n")
    print(FirstPareto())
    print("\nSUB-OPTIMIZATION\n")
    print(Suboptimization())

if __name__ == "__main__":
    main()
