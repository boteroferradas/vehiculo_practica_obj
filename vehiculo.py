from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, matricula, velocidadeMaxima, autonomia):
        self.matricula = matricula
        self.velocidadeMaxima = velocidadeMaxima
        self.autonomia = autonomia


    @property
    def matricula(self):
        return self._matricula

    @matricula.setter
    def matricula(self, matricula):
        if isinstance(matricula, str):
            if len(matricula) == 7:
                if matricula[:4].isdecimal():
                    if matricula[5:].isalpha():
                        self._matricula = matricula
                    else:
                        raise ValueError("Los ultimos tres caracteres de la matricula tienen que ser letras")
                else:
                    raise ValueError("Los primeros cuatros caracteres de la matricula tienen que ser numeros")
            else:
                raise ValueError("La matricula tiene que tener 7 caracteres")
        else:
            raise ValueError("La matricula tiene que ser un string")


    @property
    def velocidadeMaxima(self):
        return self._velocidadeMaxima

    @velocidadeMaxima.setter
    def velocidadeMaxima(self, velocidadeMaxima):
        if isinstance(velocidadeMaxima, int):
            if velocidadeMaxima > 100:
                self._velocidadeMaxima = velocidadeMaxima
            else:
                raise ValueError("La velocidad maxima tiene que ser una valor mayor de 100")
        else:
            raise ValueError("La velocidad tiene que ser un int")

    @property
    def autonomia(self):
        return self._autonomia

    @autonomia.setter
    def autonomia(self, autonomia):
        self._autonomia = autonomia

    @abstractmethod
    def arrincar(self):
        pass

    @abstractmethod
    def deter(self):
        print(f"O vehiculo {self._matricula} esta detido")

    @abstractmethod
    def mostrarDatos(self):
        pass

    def __str__(self):
        return f"La matricula es {self.matricula}\nLa velocidad maxima es {self._velocidadeMaxima}\nLa matricula es {self._matricula}"


class Terrestre(Vehiculo, ABC):
    def __init__(self, matricula, velocidadeMaxima, autonomia, numeroRodas):
        super().__init__(matricula, velocidadeMaxima, autonomia)
        self.numero_rodas = numeroRodas

    @property
    def numeroRodas(self):
        return self._numeroRodas

    @numeroRodas.setter
    def numeroRodas(self, numeroRodas):
        self._numeroRodas = numeroRodas

class Aereo(Vehiculo, ABC):
    def __init__(self, matricula, velocidadeMaxima, autonomia, altitudeMaxima):
        super().__init__(matricula, velocidadeMaxima, autonomia)
        self.altitude_maxima = altitudeMaxima

    @property
    def altitudeMaxima(self):
        return self._altitudeMaxima

    @altitudeMaxima.setter
    def altitudeMaxima(self, altitudeMaxima):
        self._altitudeMaxima = altitudeMaxima

class CocheAutonomo(Terrestre):
    def __init__(self, matricula, velocidadeMaxima, autonomia, numeroRodas, numeroPrazas):
        super().__init__(matricula, velocidadeMaxima, autonomia, numeroRodas)
        self.numeroPrazas = numeroPrazas

    @property
    def numeroPrazas(self):
        return self._numeroPrazas

    @numeroPrazas.setter
    def numeroPrazas(self, numeroPrazas):
        self._numeroPrazas = numeroPrazas


coche = Vehiculo("3456ABC",120,100)
print(coche)
coche2 = Vehiculo("3456ABC",120,100)
print(coche2)