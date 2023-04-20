def main():
    H_kolumny = 16
    H_bityparzystosci = 8
    macierzH = [[1,1,1,1,1,1,1,1, 1,0,0,0,0,0,0,0],
                [1,1,1,1,1,1,1,0, 0,1,0,0,0,0,0,0],
                [1,1,1,1,1,1,0,0, 0,0,1,0,0,0,0,0],
                [1,1,1,1,1,0,0,0, 0,0,0,1,0,0,0,0],
                [1,1,1,1,0,0,0,0, 0,0,0,0,1,0,0,0],
                [1,1,1,0,0,0,0,0, 0,0,0,0,0,1,0,0],
                [1,1,0,0,0,0,0,0, 0,0,0,0,0,0,1,0],
                [1,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,1]]
    wiadomosc =   [1,1,1,1,1,1,1,1, 1,0,1,0,1,0,1,0]
    wiadomosc_z_bladem = [1,0,1,1,1,0,1,1, 0,1,0,1,0,1,0,1]
    #Нужно проверить каждый бит четности по очереди Н_bityparzystosci - количество битов четности
    #macierzE - строка с ошибками, 1 - означает что на этом месте ошибка (этот бит четности содержит ошибку)
    macierzE = []
    poprawnosc = True
    print ('Wiadomosc z bitami parzystosci: ', wiadomosc_z_bladem)
    for i in range(H_bityparzystosci):
        E = sprawdzenieBitu(macierzH, wiadomosc_z_bladem, i, H_kolumny)
        macierzE.append(E)
        if (E == 1):
            poprawnosc = False
    print('E:', macierzE)
    if (poprawnosc == False):
        wiadomoscPoprawna = korekcja(wiadomosc_z_bladem, macierzE, macierzH, H_kolumny, H_bityparzystosci)
        print('Poprawna wiadomosc z bitami parzystosci', wiadomoscPoprawna)


def sprawdzenieBitu(macierzH, wiadomosc, wiersz, H_kolumny):
    c = 0
    for i in range(H_kolumny):
        c += macierzH[wiersz][i] * wiadomosc[i]
    c = c%2
    return c

def korekcja(wiadomosc, macierzE, macierzH, H_kolumny, H_bityparzystosci):
    aktualnaKolumna = []
    zbiorKolumn = []
    for i in range(H_kolumny):
        for j in range(H_bityparzystosci):
            wiersz = macierzH[j]
            if (wiersz[i] == 1):
                bufor = 1
            else:
                bufor = 0
            aktualnaKolumna.append(bufor)
        zbiorKolumn.append(aktualnaKolumna)
        if (aktualnaKolumna == macierzE):
            wiadomosc[i] = (~wiadomosc[i])%2
            return wiadomosc
        aktualnaKolumna = []

    for i in range(H_kolumny):
        czynnik1 = zbiorKolumn[i]
        for j in range(H_kolumny):
            if i == j:
                break
            else:
                czynnik2 = zbiorKolumn[j]
            for k in range(H_bityparzystosci):
                xor = czynnik1[k] ^ czynnik2[k]
                aktualnaKolumna.append(xor)
            if aktualnaKolumna == macierzE:
                wiadomosc[i] = (~wiadomosc[i]) % 2
                wiadomosc[j] = (~wiadomosc[j]) % 2
                return wiadomosc
            aktualnaKolumna.clear()

main()
