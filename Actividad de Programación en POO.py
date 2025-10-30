class Maquina:
    def __init__(self, nombre):
        self.nombre = nombre

    def ensamblar_carro(self, tipo_carro):
        print(f"{self.nombre} esta ensamblando un {tipo_carro}...")
        return Carro(tipo_carro, "Sin dueño")

class Trabajador:
    def __init__(self, nombre):
        self.nombre = nombre

    def comprar_carro(self, carro):
        print(f"{self.nombre} ha comprado un {carro.tipo}.")
        carro.dueno = self.nombre

class Carro:
    def __init__(self, tipo, dueno):
        self.tipo = tipo
        self.dueno = dueno

    def mostrar_info(self):
        print("\nInformacion del carro")
        print(f"Tipo de carro: {self.tipo}")
        print(f"Dueño actual: {self.dueno}")

if __name__ == "__main__":
    nombre_maquina = input("Ingrese el nombre de la maquina: ")
    maquina = Maquina(nombre_maquina)

    nombre_trabajador = input("Ingrese el nombre del trabajador: ")
    Trabajador = Trabajador(nombre_trabajador)

    tipo_carro = input("Ingrese el tipo de carro que desea ensamblar: ")

    carro_nuevo = maquina.ensamblar_carro(tipo_carro)

    Trabajador.comprar_carro(carro_nuevo)
    carro_nuevo.mostrar_info()
