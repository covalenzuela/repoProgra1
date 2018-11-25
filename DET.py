#Detrminante
print "Ingrese los valores:"
print "|a00 a01 a02|"
print "|a10 a11 a12|"
print "|a20 a21 a22|"

a00 = float(raw_input('Ingrese el valor a00 '))
a01 = float(raw_input('Ingrese el valor a01 '))
a02 = float(raw_input('Ingrese el valor a02 '))
a10 = float(raw_input('Ingrese el valor a10 '))
a11 = float(raw_input('Ingrese el valor a11 '))
a12 = float(raw_input('Ingrese el valor a12 '))
a20 = float(raw_input('Ingrese el valor a20 '))
a21 = float(raw_input('Ingrese el valor a21 '))
a22 = float(raw_input('Ingrese el valor a22 '))

#               !a00 a10 a20! l2a00 l2a10
 #              !a01 a11 a21! l2a01 l2a11
  #             !a02 a12 a22! l2a02 l2a12
         
total=a00*a11*a22 + a10*a21*a02 +a20*a01*a12;
total=total+(a02*a11*a20)*-1 + (a12*a21*a00)*-1 + (a22*a01*a10)*-1;

if total!=0:
    print a00," ",a01," ",a02
    print a10," ",a11," ",a12
    print a20," ",a21," ",a22
    print "Determinante 3x3: ",total;

else:
    print "Error el det. da 0";
