from clase_privados import  Privado

class Sociedad_anonima(Privado):
    nombre_sociedad_anonima=""
    representante=""
    correo_representante=""

    def mostrar_datos(self):
        super().mostrar_datos()
        print("Nombre de Socidedad Anonima.:",self.nombre_sociedad_anonima)
        print("Representante: ",self.representante)
        print("Correo:",self.correo_representante)
        

