import math
from typing import List


def get_longest_all_perfect_squares(lst: list[int]) -> list[int]:
    for start in range(0,len(lst)):
        if lst[start] != math.sqrt(lst[start]) * math.sqrt(lst[start]):
            return []
    return lst

def secv_perfect_squares(lst: list[int]):
    lista_secventa=[]
    for start in range(0, len(lst) + 1):
        for end in range(start+1,len(lst)+1):
            if get_longest_all_perfect_squares(lst[start:end]):
                lista_secventa.append(lst[start:end])

    max_sec=[]
    for secventa in lista_secventa:
        if len(secventa)>len(max_sec):
            max_sec=secventa

    return max_sec

def citire_lista():
    rezult_list=[]
    dimensiune=int(input("Dati dimensiunea aici: "))
    while dimensiune:
        element=int(input("Dati cate un element aici: "))
        rezult_list.append(element)
        dimensiune -=1
    return rezult_list


def main():

    while True:
        print("1.Citire lista")
        print("2.Determinare cea mai lungă subsecvență cu proprietatea: Toate numerele sunt pătrate perfecte.")
        print("x.")
        optiune= input("Alege optiunea: ")
        if optiune == "1":
            lista=citire_lista()
        elif optiune == "2":
            print(f"Cea mai lunga subsecventa de numere patrate perfecte este: {secv_perfect_squares(lista)} ")


main()
