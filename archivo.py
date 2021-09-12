class Texto:
    def __init__(self,nombreArchivo):
        self.archivo=nombreArchivo
        
    def leer(self):
        with open("estudiantes.txt",'r',encoding="UTF-8")as file:
            for linea in file:
                print(linea[:-1])
                
    def escribir(self,datos,modo):
        with  open(self.archivo,modo,encoding="UTF-8") as file:
            for dato in datos:
                file.write(dato+"\n")
                
arch1 = Texto("estudiantes.txt")
arch1.escribir(["Marcos Vera", "Ana Bohorquez","Miguel Vera"],"w")
arch1.leer()