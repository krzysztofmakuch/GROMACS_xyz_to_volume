name = 'box_sizes_v2.txt'
wynik = 'objetosc.txt'
def obj(lista):
    #print(lista)
    iloczyn = 1
    for ele in lista:
        iloczyn *= float(ele)
    #print(iloczyn)
    return iloczyn

        
with open(name, 'r') as f1, open(wynik, 'w') as f2:
    for line in f1:
        podzial = line.split()
        srednia = obj(podzial[1:])
        #print(podzial[1:])
        print('%10s %15s' %(podzial[0], round(srednia,3)), file = f2)


        
import os
os.system('xmgrace objetosc.txt')
