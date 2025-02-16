class ChocolateData:
    def __init__(self, p: float, r: float, w: float, c: float):
        self.price = p
        self.rating = r
        self.weight = w
        self.calories = c


chocolate_list = []

def addToList(p: float, r: float,
               w: float, c: float) -> None:
    chocolate = ChocolateData(p, r, w, c)
    chocolate_list.append(chocolate)


def autoListFromTask() -> None:
    addToList(199.99, 4.97, 80, 534) # 1
    addToList(499.99, 4.61, 90, 545) # 2
    addToList(179.99, 4.97, 84, 566) # 3
    addToList(164.99, 4.91, 90, 550) # 4
    addToList(299.99, 4.95, 100, 560) # 5
    addToList(149.99, 4.94, 85, 538) # 6
    addToList(699.99, 4.94, 270, 543) # 7
    addToList(124.99, 4.94, 90, 560) # 8
    addToList(149.99, 4.83, 90, 529) # 9


def userAddToList(length: int) -> None: # for fun
    for i in range(0, length):
        addToList(float(input("Enter price")),
                float(input("Enter rating")),
                float(input("Enter weight")),
                float(input("Enter calories")),)


def Pareto():
    index = 0
    result = []
    for chocolate in chocolate_list:
        index += 1
        for next_choco in chocolate_list:
            if (0 < next_choco.price - chocolate.price <= 30
                    and -.1 < next_choco.rating - chocolate.rating <= .1
                    and 5 >= next_choco.weight - chocolate.weight >= 0
                    and next_choco.calories - chocolate.calories <= 40):
                result.append(index)
                continue
    return result


def FirstPareto():
    index = 0
    result = []
    for chocolate in chocolate_list:
        index += 1
        if chocolate.price < 200 and chocolate.calories < 545:
            result.append(index)
            continue
    return result


def Suboptimization():
    index = 0
    result = []
    for chocolate in chocolate_list:
        index += 1
        if (chocolate.price < 200 and chocolate.rating > 4.9
                and chocolate.weight > 80 and chocolate.calories < 550):
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
