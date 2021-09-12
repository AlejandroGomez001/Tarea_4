class Lista:
    def __init__(self,listas): #getproperty
        self.__lista=listas
        
    @property
    def lista(self):
        return self.__lista  
    
    #busca un valor en la lista; retorna la posiccion si la encuentra
    #y sino lo encuentra retorna -1  
    def busquedaLineal(self,buscado):
        pos=0
        enc=False
        lon = len(self.__lista)
        # recorre la lista hasta que la posicion sea igual a la longitud
        while pos < lon and enc == False :
            if self.__lista[pos]["nombre"] == buscado:
                enc = True
            else:
                pos = pos + 1
                
        if enc: return pos 
        else: return -1
    def sort(lista):
        izquierda = []
        centro = []
        derecha = []
        if len(lista) > 1:
            pivote = lista[0]
            for i in lista:
                if i < pivote:
                    izquierda.append(i)
                elif i == pivote:
                    centro.append(i)
                elif i > pivote:
                    derecha.append(i)
            #print(izquierda+["-"]+centro+["-"]+derecha)
            return sort(izquierda)+centro+sort(derecha)
        else:
          return lista

    print(lista)
    print(sort(lista))
                
    def ordenar(self,orden):
        orden= orden.lower()
        if orden == "asc":
           for pos in range(0,len(self.__lista)):
              for sig in range(pos+1, len(self.__lista)):
                 if self.__lista[pos]["nombre"] > self.__lista[sig]["nombre"]:
                   aux = self.__lista[pos]
                   self.__lista[pos]=self.lista[sig]
                   self.__lista[sig]=aux
        else:
           for pos in range(0,len(self.__lista)):
              for sig in range(pos+1, len(self.__lista)):
                 if self.__lista[pos]["nombre"] < self.__lista[sig]["nombre"]:
                   aux = self.__lista[pos]
                   self.__lista[pos]=self.lista[sig]
                   self.__lista[sig]=aux
                   
    def busquedaBinaria(self,buscado):
        self.ordenar("asc")
        fin = len(self.lista) -1 #guardar la posicion final del segmento
        inicio= 0 # guarda la posicion inicial del segmento lista
        enc= False
        #se busca mientras que la posicion inicial sea menor que la final
        while inicio <= fin and enc == False:
            medio = (inicio+fin)//2
            if self.lista[medio]["nombre"] == buscado:enc == True
            elif  self.lista[medio]["nombre"] < buscado: inicio = medio +1
            else: fin = medio-1
        if enc: return medio 
        else: return -1
    
notas= [
    {"nombre":"Alex","n1":20,"n2":40},
    {"nombre":"Carla","n1":30,"n2":50},
    {"nombre":"Dayana","n1":40,"n2":50},
    {"nombre":"Daniel","n1":50,"n2":40},
    {"nombre":"Jose","n1":55,"n2":40},
    {"nombre":"Maria","n1":60,"n2":40},
    
]  

        
bus = Lista(notas)
posicion = bus.busquedaBinaria("Alex")
if posicion != -1:
    print(bus.lista[posicion])
else:
    print("Nombre no se encuentra en la lista")

