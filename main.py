import math
from typing import List


def get_longest_all_perfect_squares(lst: list[int]) -> list[int]:
    for start in range(0, len(lst)):
        if lst[start] != math.sqrt(lst[start]) * math.sqrt(lst[start]):
            return []
    return lst


def test_get_longest_all_perfect_squares():
    assert(get_longest_all_perfect_squares([49, 64, 100, 4]))==[49, 64, 100, 4]
    assert(get_longest_all_perfect_squares([49, 6, 100, 4]))==[]
    assert(get_longest_all_perfect_squares([49, 64, 100, 4, 121, 296]))==[49, 64, 100, 4, 121, 296]


def secv_perfect_squares(lst: list[int]):
    lista_secventa = []
    for start in range(0, len(lst) + 1):
        for end in range(start + 1, len(lst) + 1):
            if get_longest_all_perfect_squares(lst[start:end]):
                lista_secventa.append(lst[start:end])

    max_sec = []
    for secventa in lista_secventa:
        if len(secventa) > len(max_sec):
            max_sec = secventa

    return max_sec


def get_longest_same_bit_counts(lst: list[int]) -> list[int]:
    first_nr_bit_count = lst[0].bit_count()
    for start in range(1, len(lst)):
        if lst[start].bit_count()!= first_nr_bit_count:
            return []
    return lst


def test_get_longest_same_bit_counts():
    assert(get_longest_same_bit_counts([2, 4, 8, 32, 64])) == [2, 4, 8, 32, 64]
    assert(get_longest_same_bit_counts([2, 4, 8, 3, 64])) == []
    assert(get_longest_same_bit_counts([2, 4, 8, 32, 64, 256, 1048576])) == [2, 4, 8, 32, 64, 256, 1048576]

def secv_same_bit_counts(lst: list[int]):
    lista_secventa = []
    for start in range(0, len(lst) + 1):
        for end in range(start + 1, len(lst) + 1):
            if get_longest_same_bit_counts(lst[start:end]):
                lista_secventa.append(lst[start:end])

    max_sec = []
    for secventa in lista_secventa:
        if len(secventa) > len(max_sec):
            max_sec = secventa

    return max_sec


def citire_lista():
    rezult_list = []
    dimensiune = int(input("Dati dimensiunea aici: "))
    while dimensiune:
        element = int(input("Dati cate un element aici: "))
        rezult_list.append(element)
        dimensiune -= 1
    return rezult_list


def main():
    while True:
        print("1.Citire lista")
        print("2.Determinare cea mai lungă subsecvență cu proprietatea: Toate numerele sunt pătrate perfecte.")
        print(
            "3.Determinare cea mai lungă subsecvență cu proprietatea: Toate numerele au același număr de biți de 1 în reprezentarea binară.")
        print("x.")

        optiune = input("Alege optiunea: ")
        if optiune == "1":
            lista = citire_lista()
        elif optiune == "2":
            print(f"Cea mai lunga subsecventa de numere patrate perfecte este: {secv_perfect_squares(lista)} ")
        elif optiune == "3":
            print(
                f"Cea mai lunga subsecventa de numere care au acelasi numar de biti de 1 este: {secv_same_bit_counts(lista)}")


test_get_longest_same_bit_counts()
test_get_longest_all_perfect_squares()
main()
