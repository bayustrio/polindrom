def Polindrom(kata):
    belakang = kata[::-1]

    if kata == belakang:
        print('true')
    else:
        print('false')

kata = input('Masukan kata :').lower()
Polindrom(kata)

