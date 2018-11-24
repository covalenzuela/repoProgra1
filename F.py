#Menu

salir = "s"

while salir == "s":
    
    print "    --=** MENU **=--"
    print ""
    print "[1] Suma de Matrices"
    print "[2] Resta de Matrices"
    print "[3] Multiplicacion de Matrices"
    print "[4] Multiplicacion por un Numero"
    print "[5] Transpuesta de una Matriz"
    print ""
    
#Modelo de la Matriz
    print "Modelo de la Matriz"
    print ""
    print   "[F1C1 F1C2 F1C3]"
    print   "[F2C1 F2C2 F2C3]"
    print   "[F3C1 F3C2 F3C3]"
    print ""

#Opcion "1" SUMA
    x=input("Ingrese Opcion: ")
    print ""
    if x==1:

#Matriz "A"
        print "Ingrese la Matriz A"
        print ""
        af1c1=int(raw_input("Ingrese el valor de F1C1: "))
        af1c2=int(raw_input("Ingrese el valor de F1C2: "))
        af1c3=int(raw_input("Ingrese el valor de F1C3: "))
        af2c1=int(raw_input("Ingrese el valor de F2C1: "))
        af2c2=int(raw_input("Ingrese el valor de F2C2: "))
        af2c3=int(raw_input("Ingrese el valor de F2C3: "))
        af3c1=int(raw_input("Ingrese el valor de F3C1: "))
        af3c2=int(raw_input("Ingrese el valor de F3C2: "))
        af3c3=int(raw_input("Ingrese el valor de F3C3: "))

#Visualizacion Matriz "A"
        print ""
        print "MATRIZ A"
        print ""
        print "[", af1c1, af1c2, af1c3, "]"
        print "[", af2c1, af2c2, af2c3, "]"
        print "[", af3c1, af3c2, af3c3, "]"
        print ""

#Matriz "B"
        print "Ingrese la Matriz B"
        print ""
        bf1c1=int(raw_input("Ingrese el valor de F1C1: "))
        bf1c2=int(raw_input("Ingrese el valor de F1C2: "))
        bf1c3=int(raw_input("Ingrese el valor de F1C3: "))
        bf2c1=int(raw_input("Ingrese el valor de F2C1: "))
        bf2c2=int(raw_input("Ingrese el valor de F2C2: "))
        bf2c3=int(raw_input("Ingrese el valor de F2C3: "))
        bf3c1=int(raw_input("Ingrese el valor de F3C1: "))
        bf3c2=int(raw_input("Ingrese el valor de F3C2: "))
        bf3c3=int(raw_input("Ingrese el valor de F3C3: "))
        print ""

#Visualizacion Matriz "B"
        print "MATRIZ B"
        print""
        print "[", bf1c1, bf1c2, bf1c3, "]"
        print "[", bf2c1, bf2c2, bf2c3, "]"
        print "[", bf3c1, bf3c2, bf3c3, "]"
        print ""
    
#Operacion Suma
        rf1c1 = af1c1 + bf1c1
        rf1c2 = af1c2 + bf1c2
        rf1c3 = af1c3 + bf1c3
        rf2c1 = af2c1 + bf2c1
        rf2c2 = af2c2 + bf2c2
        rf2c3 = af2c3 + bf2c3
        rf3c1 = af3c1 + bf3c1
        rf3c2 = af3c2 + bf3c2
        rf3c3 = af3c3 + bf3c3
    
#Visualizacion Matriz "Resultado"
        print "MATRIZ Resultado"
        print ""
        print "[", rf1c1, rf1c2, rf1c3, "]"
        print "[", rf2c1, rf2c2, rf2c3, "]"
        print "[", rf3c1, rf3c2, rf3c3, "]"
        print ""
    
#Opcion "2" RESTA
    elif x==2:

#Matriz "A"
        print "Ingrese la Matriz A"
        print ""
        af1c1=int(raw_input("Ingrese el valor de F1C1: "))
        af1c2=int(raw_input("Ingrese el valor de F1C2: "))
        af1c3=int(raw_input("Ingrese el valor de F1C3: "))
        af2c1=int(raw_input("Ingrese el valor de F2C1: "))
        af2c2=int(raw_input("Ingrese el valor de F2C2: "))
        af2c3=int(raw_input("Ingrese el valor de F2C3: "))
        af3c1=int(raw_input("Ingrese el valor de F3C1: "))
        af3c2=int(raw_input("Ingrese el valor de F3C2: "))
        af3c3=int(raw_input("Ingrese el valor de F3C3: "))
        print ""
    
#Visualizacion Matriz "A"
        print "MATRIZ A"
        print ""
        print "[", af1c1, af1c2, af1c3, "]"
        print "[", af2c1, af2c2, af2c3, "]"
        print "[", af3c1, af3c2, af3c3, "]"
        print ""
    
#Matriz "B"
        print "Ingrese la Matriz B"
        print ""
        bf1c1=int(raw_input("Ingrese el valor de F1C1: "))
        bf1c2=int(raw_input("Ingrese el valor de F1C2: "))
        bf1c3=int(raw_input("Ingrese el valor de F1C3: "))
        bf2c1=int(raw_input("Ingrese el valor de F2C1: "))
        bf2c2=int(raw_input("Ingrese el valor de F2C2: "))
        bf2c3=int(raw_input("Ingrese el valor de F2C3: "))
        bf3c1=int(raw_input("Ingrese el valor de F3C1: "))
        bf3c2=int(raw_input("Ingrese el valor de F3C2: "))
        bf3c3=int(raw_input("Ingrese el valor de F3C3: "))
        print ""

#Visualizacion Matriz "B"
        print "MATRIZ B"
        print ""
        print "[", bf1c1, bf1c2, bf1c3, "]"
        print "[", bf2c1, bf2c2, bf2c3, "]"
        print "[", bf3c1, bf3c2, bf3c3, "]"
        print ""
    
#Operacion Resta    
        rf1c1 = af1c1 - bf1c1
        rf1c2 = af1c2 - bf1c2
        rf1c3 = af1c3 - bf1c3
        rf2c1 = af2c1 - bf2c1
        rf2c2 = af2c2 - bf2c2
        rf2c3 = af2c3 - bf2c3
        rf3c1 = af3c1 - bf3c1
        rf3c2 = af3c2 - bf3c2
        rf3c3 = af3c3 - bf3c3

#Visualizacion Matriz "Resultado"
        print "MATRIZ Resultado"
        print ""
        print "[", rf1c1, rf1c2, rf1c3, "]"
        print "[", rf2c1, rf2c2, rf2c3, "]"
        print "[", rf3c1, rf3c2, rf3c3, "]"
        print ""

#Opcion "3" MULTIPLICACION
    elif x==3:
    
#Matriz "A"
        print "Ingrese la Matriz A"
        print ""
        af1c1=int(raw_input("Ingrese el valor de F1C1: "))
        af1c2=int(raw_input("Ingrese el valor de F1C2: "))
        af1c3=int(raw_input("Ingrese el valor de F1C3: "))
        af2c1=int(raw_input("Ingrese el valor de F2C1: "))
        af2c2=int(raw_input("Ingrese el valor de F2C2: "))
        af2c3=int(raw_input("Ingrese el valor de F2C3: "))
        af3c1=int(raw_input("Ingrese el valor de F3C1: "))
        af3c2=int(raw_input("Ingrese el valor de F3C2: "))
        af3c3=int(raw_input("Ingrese el valor de F3C3: "))
        print ""

#Visualizacion Matriz "A"
        print "MATRIZ A"
        print ""
        print "[", af1c1, af1c2, af1c3, "]"
        print "[", af2c1, af2c2, af2c3, "]"
        print "[", af3c1, af3c2, af3c3, "]"
        print ""
    
#Matriz "B"
        print "Ingrese la Matriz B"
        print ""
        bf1c1=int(raw_input("Ingrese el valor de F1C1: "))
        bf1c2=int(raw_input("Ingrese el valor de F1C2: "))
        bf1c3=int(raw_input("Ingrese el valor de F1C3: "))
        bf2c1=int(raw_input("Ingrese el valor de F2C1: "))
        bf2c2=int(raw_input("Ingrese el valor de F2C2: "))
        bf2c3=int(raw_input("Ingrese el valor de F2C3: "))
        bf3c1=int(raw_input("Ingrese el valor de F3C1: "))
        bf3c2=int(raw_input("Ingrese el valor de F3C2: "))
        bf3c3=int(raw_input("Ingrese el valor de F3C3: "))
        print ""

#Visualizacion Matriz "B"
        print "MATRIZ B"
        print ""
        print "[", bf1c1, bf1c2, bf1c3, "]"
        print "[", bf2c1, bf2c2, bf2c3, "]"
        print "[", bf3c1, bf3c2, bf3c3, "]"
        print ""
    
#Operacion Multiplicacion    
        rf1c1= (af1c1 * bf1c1) + (af1c2 * bf2c1) + ( af1c3 * bf3c1)
        rf1c2= (af1c1 * bf1c2) + (af1c2 * bf2c2) + ( af1c3 * bf3c2)
        rf1c3= (af1c1 * bf1c3) + (af1c2 * bf2c3) + ( af1c3 * bf3c3)
        rf2c1= (af2c1 * bf1c1) + (af2c2 * bf2c1) + ( af2c3 * bf3c1)
        rf2c2= (af2c1 * bf1c2) + (af2c2 * bf2c2) + ( af2c3 * bf3c2)
        rf2c3= (af2c1 * bf1c3) + (af2c2 * bf2c3) + ( af2c3 * bf3c3)
        rf3c1= (af3c1 * bf1c1) + (af3c2 * bf2c1) + ( af3c3 * bf3c1)
        rf3c2= (af3c1 * bf1c2) + (af3c2 * bf2c2) + ( af3c3 * bf3c2)
        rf3c3= (af3c1 * bf1c3) + (af3c2 * bf2c3) + ( af3c3 * bf3c3)

#Visualizacion Matriz "Resultado"
        print "MATRIZ Resultado"
        print ""
        print "[", rf1c1, rf1c2, rf1c3, "]"
        print "[", rf2c1, rf2c2, rf2c3, "]"
        print "[", rf3c1, rf3c2, rf3c3, "]"
        print ""

#Opcion "4" MULTIPLICACION POR UN NUMERO
    elif x==4:
        z=int(raw_input("Ingrese el numero para multiplicar con la matriz: "))
        print ""
        
#Matriz "A"
        print "Ingrese la Matriz A"
        print ""
        af1c1=int(raw_input("Ingrese el valor de F1C1: "))
        af1c2=int(raw_input("Ingrese el valor de F1C2: "))
        af1c3=int(raw_input("Ingrese el valor de F1C3: "))
        af2c1=int(raw_input("Ingrese el valor de F2C1: "))
        af2c2=int(raw_input("Ingrese el valor de F2C2: "))
        af2c3=int(raw_input("Ingrese el valor de F2C3: "))
        af3c1=int(raw_input("Ingrese el valor de F3C1: "))
        af3c2=int(raw_input("Ingrese el valor de F3C2: "))
        af3c3=int(raw_input("Ingrese el valor de F3C3: "))
        print ""

#Visualizacion Matriz "A"
        print "MATRIZ A"
        print ""
        print "[", af1c1, af1c2, af1c3, "]"
        print "[", af2c1, af2c2, af2c3, "]"
        print "[", af3c1, af3c2, af3c3, "]"
        print ""

#Operacion Multiplicacion por numero

        rf1c1 = z * af1c1
        rf1c2 = z * af1c2
        rf1c3 = z * af1c3
        rf2c1 = z * af2c1
        rf2c2 = z * af2c2
        rf2c3 = z * af2c3
        rf3c1 = z * af3c1
        rf3c2 = z * af3c2
        rf3c3 = z * af3c3

#Visualizacion Matriz "Resultado"
        print "MATRIZ Resultado"
        print ""
        print "[", rf1c1, rf1c2, rf1c3, "]"
        print "[", rf2c1, rf2c2, rf2c3, "]"
        print "[", rf3c1, rf3c2, rf3c3, "]"
        print ""

#Opcion "5" Transpuesta
    elif x==5:
        
#Matriz "A"
        print "Ingrese la Matriz A"
        print ""
        af1c1=int(raw_input("Ingrese el valor de F1C1: "))
        af1c2=int(raw_input("Ingrese el valor de F1C2: "))
        af1c3=int(raw_input("Ingrese el valor de F1C3: "))
        af2c1=int(raw_input("Ingrese el valor de F2C1: "))
        af2c2=int(raw_input("Ingrese el valor de F2C2: "))
        af2c3=int(raw_input("Ingrese el valor de F2C3: "))
        af3c1=int(raw_input("Ingrese el valor de F3C1: "))
        af3c2=int(raw_input("Ingrese el valor de F3C2: "))
        af3c3=int(raw_input("Ingrese el valor de F3C3: "))
        print ""

#Visualizacion Matriz "A"
        print "MATRIZ A"
        print ""
        print "[", af1c1, af1c2, af1c3, "]"
        print "[", af2c1, af2c2, af2c3, "]"
        print "[", af3c1, af3c2, af3c3, "]"
        print ""

#Visualizacion Matriz "Resultado"
        print "MATRIZ Transpuesta"
        print ""
        print "[", af1c1, af2c1, af3c1, "]"
        print "[", af1c2, af2c2, af3c2, "]"
        print "[", af1c3, af2c3, af3c3, "]"
        print ""
    salir = raw_input("Desea realizar otra operacion?(S/N) ")
    print ""
