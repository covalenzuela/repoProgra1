#INVERSA
print "Ingrese los valores:"
#vision de la matriz
print "|a00 a01 a02|"
print "|a10 a11 a12|"
print "|a20 a21 a22|"
#valores
af1c1 = float(raw_input('Ingrese el valor a00 '))
af1c2 = float(raw_input('Ingrese el valor a01 '))
af1c3 = float(raw_input('Ingrese el valor a02 '))
af2c1 = float(raw_input('Ingrese el valor a10 '))
af2c2 = float(raw_input('Ingrese el valor a11 '))
af2c3 = float(raw_input('Ingrese el valor a12 '))
af3c1 = float(raw_input('Ingrese el valor a20 '))
af3c2 = float(raw_input('Ingrese el valor a21 '))
af3c3 = float(raw_input('Ingrese el valor a22 '))

#operadores
total = af1c1*af2c2*af3c3 + af2c1*af3c2*af1c3 + af3c1*af1c2*af2c3;
total = total + (af1c3*af2c2*af3c1)*-1 + (af2c3*af3c2*af1c1)*-1 + (af3c3*af1c2*af2c1)*-1;

#si el determinante no es cero
#existe inversa
if total!=0:
    print " ",(af2c2*af3c3-af3c2*af2c3)/total,' ',((af1c2*af3c3-af3c2*af1c3)*-1)/total,' ',(af1c2*af2c3-af2c2*af1c3)/total;
    print " ",((af2c1*af3c3-af3c1*af2c3)*-1)/total,' ',((af1c1*af3c3-af3c1*af1c3))/total,' ',((af1c1*af2c3-af2c1*af1c3)*-1)/total;
    print " ",((af2c1*af3c2-af3c1*af2c2))/total,' ',((af1c1*af3c2-af3c1*af1c2)*-1)/total,' ',(af1c1*af2c2-af2c1*af1c2)/total;

#DETERMINANTE 0
else:
    print "Error el det. da 0";
