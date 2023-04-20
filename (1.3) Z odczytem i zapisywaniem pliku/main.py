def main():
    H_kolumny = 16
    H_bityparzystosci = 8
    macierzH = [[0,1,1,1,1,1,1,1, 1,0,0,0,0,0,0,0],
                [1,0,1,1,1,1,1,1, 0,1,0,0,0,0,0,0],
                [1,1,0,1,1,1,1,1, 0,0,1,0,0,0,0,0],
                [1,1,1,0,1,1,1,1, 0,0,0,1,0,0,0,0],
                [1,1,1,1,0,1,1,1, 0,0,0,0,1,0,0,0],
                [1,1,1,1,1,0,1,1, 0,0,0,0,0,1,0,0],
                [1,1,1,1,1,1,0,1, 0,0,0,0,0,0,1,0],
                [1,1,1,1,1,1,1,0, 0,0,0,0,0,0,0,1]]
    choice = None
    while choice != '0':
        choice = input('Wybierz co chcesz zrobić: \n1. Zakodować\n2. Odkodować\n\n0. Wyjście')
        if choice == '1':
            filename = input("Wpisz nazwę pliku(w formacie txt): ")
            wiadomosci = encoding(filename, macierzH, H_kolumny, H_bityparzystosci)
            filename = input("Wpisz nazwę pliku do którego chcesz zapisać(w formacie txt): ")
            writeWithoutDecoding(filename, H_kolumny, wiadomosci)
        elif choice == '2':
            filename = input("Wpisz nazwę pliku(w formacie txt): ")
            wiadomosci = readWithoutDecoding (filename)
            filename = input("Wpisz nazwę pliku do którego chcesz zapisać(w formacie txt): ")
            decoding(filename, H_bityparzystosci, wiadomosci, H_kolumny, macierzH)
        elif choice != '0':
            print ("Spróbuj jeszcze raz")


    return 0

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
            aktualnaKolumna.append(macierzH[j][i])
        zbiorKolumn.append(aktualnaKolumna)
        if (aktualnaKolumna == macierzE):
            wiadomosc[i] = (~wiadomosc[i])%2
            return wiadomosc
        aktualnaKolumna = []

    for i in range(H_kolumny):
        czynnik1 = zbiorKolumn[i]
        for j in range(H_kolumny):
            if i != j:
                czynnik2 = zbiorKolumn[j]
            else:
                continue
            for k in range(H_bityparzystosci):
                xor = czynnik1[k] ^ czynnik2[k]
                aktualnaKolumna.append(xor)
            if aktualnaKolumna == macierzE:
                wiadomosc[i] = (~wiadomosc[i]) % 2
                wiadomosc[j] = (~wiadomosc[j]) % 2
                return wiadomosc
        aktualnaKolumna.clear()
    return wiadomosc

def encoding (filename, macierzH, H_kolumny, H_bityparzystosci):
    file = open(filename, "r")
    data = file.read()
    file.close()
    lst = []
    for letter in data:
        lst.append(letter)
    for i in range(len(lst)):
        lst[i] = ord(lst[i])
        lst[i] = bin(lst[i])
    wiadomosci = [[] for i in range(len(lst))]
    for i in range(len(lst)):
        for j in lst[i]:
            if j != "b":
                wiadomosci[i].append(int(j))
        while len(wiadomosci[i]) < 8:
            wiadomosci[i].insert(0, 0)
    for i in range(len(wiadomosci)):
        wiadomosci[i] = dodawanieBitowParzystosci(wiadomosci[i], macierzH, H_kolumny, H_bityparzystosci)
    return wiadomosci

def decoding(filename, H_bityparzystosci, wiadomosci, H_kolumny, macierzH):
    for i in range(len(wiadomosci)):
        macierzE = []
        poprawnosc = True
        for j in range(H_bityparzystosci):
            E = sprawdzenieBitu(macierzH, wiadomosci[i], j, H_kolumny)
            macierzE.append(E)
            if (E == 1):
                poprawnosc = False
        if (poprawnosc == False):
            wiadomosci[i] = korekcja(wiadomosci[i], macierzE, macierzH, H_kolumny, H_bityparzystosci)
    #####################################
    for i in range(len(wiadomosci)):
        kod = ''
        for j in range(H_bityparzystosci):
            del wiadomosci[i][-1]
        for j in range(H_bityparzystosci):
            if j == 0:
                kod += '0b'
            kod += str(wiadomosci[i][j])
        wiadomosci[i] = kod
        wiadomosci[i] = int(wiadomosci[i], 2)
        wiadomosci[i] = chr(wiadomosci[i])
    data = ''
    for i in range(len(wiadomosci)):
        data += wiadomosci[i]
    file = open(filename, "w+")
    file.write(data)
    file.close()

def writeWithoutDecoding (filename,H_kolumny, wiadomosci):
    for i in range(len(wiadomosci)):
        kod = ''
        for j in range(H_kolumny):
            kod += str(wiadomosci[i][j])
            if j == H_kolumny-1:
                kod += ' '
        wiadomosci[i] = kod
    data = ''
    for i in range(len(wiadomosci)):
        data += wiadomosci[i]
    file = open(filename, "w+")
    file.write(data)
    file.close()

def readWithoutDecoding (filename):
    file = open(filename, "r")
    data = file.read()
    file.close()
    lst = []
    for letter in data:
        if letter != ' ':
            lst.append(letter)
    wiadomosci = [[] for i in range(int(len(lst)/16))]
    for k in range(int(len(lst)/16)):
        i = k * 16
        for j in range(16):
            wiadomosci[k].append(int(lst[j + i]))
    return wiadomosci

def dodawanieBitowParzystosci(wiadomosc, macierzH, H_kolumny, H_bityparzystosci):
    for i in range(H_bityparzystosci):
        sum = 0
        for j in range(H_kolumny - H_bityparzystosci):
            sum += wiadomosc[j] * macierzH[i][j]
        if (sum%2 == 1):
            wiadomosc.append(1)
        else:
            wiadomosc.append(0)
    return wiadomosc


main()
