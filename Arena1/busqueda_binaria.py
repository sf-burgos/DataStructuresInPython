def busquedaBinaria(unaLista, item):
	    primero = 0
	    ultimo = len(unaLista)-1
	    encontrado = False
	    c=-1
	    while primero<=ultimo and not encontrado:
	        puntoMedio = (primero + ultimo)//2
	        if unaLista[puntoMedio] == item:
                    
	            c,encontrado = puntoMedio,True
	        else:
	            if item < unaLista[puntoMedio]:
	                ultimo = puntoMedio-1
	            else:
	                primero = puntoMedio+1
	
	    return puntoMedio

print(busquedaBinaria([2,2,2,2,2],5))
