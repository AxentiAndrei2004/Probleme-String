nume_prenume=str(input('Introduceti numele si prenumele dumneavoastra:'))
if (ord(nume_prenume[0]) in range (65,91)) and (ord(nume_prenume[nume_prenume.find(' ')+1]) in range (65,91)):
    print('DA')
else:
    print('NU')