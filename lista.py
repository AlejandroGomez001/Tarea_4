class Lista_1:
    def __init__(self,tamanio):
        self.lista=[]
        self.longitud=0
        self.size=tamanio

    def append(self,dato):
        if self.longitud < self.size:
            self.lista += [dato]
            self.longitud +=1
            return True
        else:
            return False
        
    def obtener(self,pos):
        if pos < 0 or pos >= self.longitud:
            return None
        else:
            return self.lista[pos]

    def obtenerEliminando(self,pos):
        
        if pos < 0 or pos >= self.longitud:
            return None
        else:
            eliminado=self.lista[pos]
            aux=[]
            # self.lista=self.lista[:pos] + self.lista[pos+1:]
            for ind in range(pos):
                aux=aux+[self.lista[ind]]
            for ind2 in range(pos+1,self.longitud):
                aux=aux+[self.lista[ind2]]
            self.longitud-=1
            self.lista=aux
            return eliminado,self.lista
            
    #busca un dato en la lista y retorna la posicion de ese valor en la lista
    def buscar(self,dato):
        enc=False
        for pos,ele in enumerate(self.lista):
            if ele==dato:
                enc=True
                break
        if enc==True:
           return pos
        else:
            return -1
                    
    #busca un dato con el metodo buscar y si no lo encuentra lo inserta en la lista
    def insertar(self,dato):
        res=self.buscar(dato)
        if res != -1:
            return None
        else:
            res2=self.append(dato)
            return res2
            
    # busca el dato eliminar con el metodo buscar y lo elimina de la lista
    def eliminar (self,dato):
        res=self.buscar(dato)
        if res != -1:
            for pos,ele in enumerate(self.lista):
                if ele== dato:
                    elim=self.lista[pos]
                    self.lista=self.lista[:pos] + self.lista[pos+1:]
                    self.longitud-=1       
                    return elim,self.lista
        else:
            return None

    def mostrar(self):
        print("{:3}{:9} {}".format("","Lista","Posicion"))
        for pos,ele in enumerate(self.lista):
            print("[{:8}]  {:5}".format(ele,pos))
# pos=1
# lista1=Lista_1(5)
# lista1.append("Daniel")1
# lista1.append(52)
# lista1.append(True)
# lista1.append("Milagro")
# lista1.mostrar()
# # print(lista1.obtener(pos))
# # posicion = int(input("ingrese posicion para obtener el elemento: "))
# # resp= lista1.obtenerEliminando(posicion)
# # if resp ==None:
# #     print("Posicion no valida, Verifique la Lista.....")
# # else:
# #     print("El elemento de la posicion: {} es: {}".format(posicion,resp))
# res=lista1.buscar("Daniel")
# if res != -1:
#     print(res)
# else:
#     print("no esta")

# lista1.insertar(0)
# print(lista1.eliminar(52))