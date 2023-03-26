def main():
    H_kolumny = 12
    H_bityparzystosci = 4
    macierzH =   [[1,0,1,0,1,0,1,0, 1,0,0,0],
                  [0,1,1,0,0,1,1,0, 0,1,0,0],
                  [0,0,0,1,1,1,1,0, 0,0,1,0],
                  [0,0,0,0,0,0,0,1, 0,0,0,1]]
    wiadomosc =   [1,1,1,1,1,1,1,1, 1,1,1,0]
    wiadomosc_z_bladem = [1,1,1,1,1,1,0,1, 1,1,1,0]

    #Нужно проверить каждый бит четности по очереди Н_bityparzystosci - количество битов четности
    #macierzE - строка с ошибками, 1 - означает что на этом месте ошибка (этот бит четности содержит ошибку)
    macierzE = []
    poprawnosc = True
    for i in range(H_bityparzystosci):
        E = sprawdzenieBitu(macierzH, wiadomosc_z_bladem, i, H_kolumny)
        macierzE.append(E)
        if (E == 0):
            poprawnosc = False
    print(macierzE)
    if (poprawnosc == False):
        wiadomoscPoprawna = korekcja(wiadomosc_z_bladem, macierzE, macierzH, H_kolumny, H_bityparzystosci)
    print(wiadomoscPoprawna)


def sprawdzenieBitu(macierzH, wiadomosc, wiersz, H_kolumny):
    c = 0
    for i in range(H_kolumny):
        c += macierzH[wiersz][i] * wiadomosc[i]
    c = (~c%2)%2
    return c

def korekcja(wiadomosc, macierzE, macierzH, H_kolumny, H_bityparzystosci):
    for i in range(H_kolumny - H_bityparzystosci):
        for j in range(H_bityparzystosci):
            if (macierzH[j][i] == macierzE[j]):
                tenWiersz = True
            else:
                tenWiersz = False
                break
        if (tenWiersz == True):
            wiadomosc[i] = (~wiadomosc[i])%2
    return wiadomosc



main()

