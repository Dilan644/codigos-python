cant_productos = []
productos = []
total = 0
while True:
    print("1).Agregar productos\n2).Ver canasta\n3).Ver total\n4).Salir")
    op1 = int(input("ingrese una opcion: "))
    if op1 == 1:
        while True:
            print("Productos.")
            print("1).Fideos            $1000")
            print("2).Tomates           $300")
            print("3).Vienesas          $1200")
            print("4).Coca-cola 3ltr    $2400")
            print("5).Arroz             $1000")
            produ = int(input("ingrese un producto: "))
            if produ == 1:
                cantidad = int(input("ingrese la cantidad de fideos que quiere llevar: "))
                cant_productos.insert(0,cantidad)
                productos.append("Fideos")
                total += 1000 * cantidad
            if produ == 2:
                cantidad = int(input("ingrese la cantidad de tomates que quiere llevar: "))
                cant_productos.insert(1,cantidad)
                productos.append("Tomate")
                total += 300* cantidad 
            if produ == 3:
                cantidad = int(input("ingrese la cantidad de vienesas que quiere llevar: "))
                cant_productos.insert(2,cantidad)
                productos.append("Vienesa")
                total +=1200 * cantidad
            if produ == 4:
                cantidad = int(input("ingrese la cantidad de coca-cola 3ltr que quiere llevar: "))
                cant_productos.insert(3,cantidad)
                productos.append("Coca-cola 3ltr")
                total += 2400 * cantidad
            if produ == 5:
                cantidad = int(input("ingrese la cantidad de arroz que quiere llevar: "))
                cant_productos.insert(4,cantidad)
                productos.append("Arroz")
                total += 1000 * cantidad
            print("¿Desea agregar otro producto? (S/N)")
            seguir_compra = input(":").upper()
            if seguir_compra == "N":
                break
            else:
                continue
    elif op1 == 2:
        cant_prod = len(cant_productos)
        print("Canasta.")
        for i in range(cant_prod):
            print(f"{productos[i]}   {cant_productos[i]}")
        print()
    elif op1 == 3:
        print()
        print(f"Tu total es: ${total}")
        print()
    elif op1 == 4:
        break
        
        