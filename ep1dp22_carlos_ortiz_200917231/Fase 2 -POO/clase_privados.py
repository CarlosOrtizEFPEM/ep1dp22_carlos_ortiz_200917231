from clase_centro_educativo import centro_educativo

class Privado(centro_educativo):
    cantidad_hombres=0
    cantidad_mujeres=0

    def mostrar_datos(self):
        super().mostrarDatos()
        print("Cantidad de Hombres:",self.cantidad_hombres)
        print("Cantidad de Mujeres:",self.cantidad_mujeres)
        
        

    
    
