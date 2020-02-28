'''
Created on Feb 28, 2020

@author: Jevist
Program Test PT Okademo
'''
def romawitoangka(a):
    print ("Simbol Romawi : V=5, X=10, L=50, C=100, D=500, M=1000")
    a = str(a)
    array_simbol = list(a)
    array_value = list(a)
    I=1
    V=5
    X=10
    L=50
    C=100
    D=500
    M=1000
    Hasil = 0
    for i in range (len(a)):
            if array_simbol[i] == "M":
                array_value[i] = M
            elif array_simbol[i] == "D":
                array_value[i] = D
            elif array_simbol[i] == "C":
                array_value[i] = C
            elif array_simbol[i] == "L":
                array_value[i] = L
            elif array_simbol[i] == "X":
                array_value[i] = X
            elif array_simbol[i] == "V":
                array_value[i] = V
            elif array_simbol[i] == "I":
                array_value[i] = I
            else:
                print("Ada Simbol masukan ada yang salah")
    k = len(a)
    for j in range (k):
        if j+1 == k:
            z = j
            if array_value[j] >= array_value[z]:
                Hasil = Hasil + array_value[j]
            else:
                Hasil = Hasil + (array_value[z] - array_value[j])
                Hasil = Hasil - array_value[z]
        else:
            z=j+1
            if array_value[j] >= array_value[z]:
                Hasil = Hasil + array_value[j]
            else:
                Hasil = Hasil + (array_value[z] - array_value[j])     
                Hasil = Hasil - array_value[z]
    print("Hasil bentuk angka= ", end="")            
    print(Hasil)
    return(Hasil)     

'''
Program Konversi angka ke romawi
'''

def angkatoromawi(z):
    print ("Simbol Romawi : V=5, X=10, L=50, C=100, D=500, M=1000") 
    I=1
    V=5
    X=10
    L=50
    C=100
    D=500
    M=1000
    angka_M = int(z/M)
    for i in range(angka_M):
        print("M", end="")
    sisa_angka_M = int(z%M)
    b = int(sisa_angka_M/C)
    while(b >= 5):
        if b > 5:
            if b == 9:
                print("CM", end="")
                b = b-9
            elif b >= 5:
                print("D", end="")
                b = b-5
    while(b >= 1):
        if b == 4:
            print("CD", end="")
            b = b-4
        elif b >= 1:
            print("C", end="")
            b = b-1
    c = sisa_angka_M%C
    d = int(c/X)
    while(d >= 5):
        if d > 5:
            if d == 9:
                print("XC", end="")
                d = d-9
            elif d >= 5:
                print("L", end="")
                d = d-5         
    while(d >= 1):
        if d == 4:
            print("XL", end="")
            d = d-4
        elif d >= 1:
            print("X", end="")
            d = d-1
    e = sisa_angka_M%X
    f = int(e/I)
    while(f >= 5):
        if f > 5:
            if f == 9:
                print("IX", end="")
                f = f-9
        elif f >= 5:
            print("V", end="")
            f = f-5
    while(f >= 1):
        if f == 4:
            print("IV", end="")
            f = f-4
        elif f >= 1:
            print("I", end="")
            f = f-1
    return()

def main():
    I=1
    V=5
    X=10
    L=50
    C=100
    D=500
    M=1000
    glob = input("glob is = ")
    prok = input("prok is = ")
    pish = input("pish is = ")
    tegj = input("tegj is = ")
    array_nama_value = [glob,prok,pish,tegj]
    array_value =[glob,prok,pish,tegj]
    for i in range (len(array_nama_value)):
            if array_nama_value[i] == "M":
                array_value[i] = M
            elif array_nama_value[i] == "D":
                array_value[i] = D
            elif array_nama_value[i] == "C":
                array_value[i] = C
            elif array_nama_value[i] == "L":
                array_value[i] = L
            elif array_nama_value[i] == "X":
                array_value[i] = X
            elif array_nama_value[i] == "V":
                array_value[i] = V
            elif array_nama_value[i] == "I":
                array_value[i] = I
            else:
                print("Ada Simbol masukan ada yang salah")
        
    
    

    return()


# main()


# a = input("Masukan Simbol Romawi= ")
# romawitoangka(a)
# z = int(input("Masukan Angka= "))
# angkatoromawi(z)