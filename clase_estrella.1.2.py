class Estrella():
    """
    Clase que representa una estrella. Sus atributos principales son:

    Atributos:
    - nombre: El nombre de la estrella. (público)
    - masa: La masa de la estrella. (protegido)
    - radio: El radio de la estrella. (protegido)
    - temperaturasuperficial: La temperatura superficial de la estrella. (protegido)
    - distancia: La distancia de la estrella. (protegido)
    - movimientopropio: El movimiento propio de la estrella. (protegido)
    """

    def __init__(self, nombre, masa, radio, temperaturasuperficial, distancia, movimientopropio):
        self.nombre = nombre
        self._masa = masa
        self._radioestrella = radio
        self._teff= temperaturasuperficial
        self._distancia = distancia
        self._movimientopropio= movimientopropio
    
    def luminosidad_total(self):
        """
        Calcula la luminosidad total de la estrella.

        Returns:
        - La luminosidad total de la estrella.
        """
        return float(4 * np.pi * (self._radioestrella**2) * self._teff)
    
    def luminosidad_secuencia_principal(self,l_sol, m_sol):
        """
        Calcula la luminosidad de la estrella en la secuencia principal.

        Parámetros:
        - l_sol: La luminosidad del Sol.
        - m_sol: La masa del Sol.

        Returns:
        - La luminosidad de la estrella en la secuencia principal.
        """
        return  float( l_sol * (self._masa/m_sol)**3.5)

    def clasificar_estrella(self):
        #Funcion que clasifica las estrellas de acuerdo a su temperatura superficial.
        #Parametros: Temperatura superficial del objeto estrella.
        #Retorna: El tipo de estrella (O,B,A,F,G,K,M).
        if 2500<self._teff<3500:
            print("La estrella es de tipo M")
        elif 3500<self._teff<5000:
            print("La estrella es de tipo K")
        elif 5000<self._teff<6000:
            print("La estrella es de tipo G")
        elif 6000<self._teff<7500:
            print("La estrella es de tipo F")
        elif 7500<self._teff<10000:
            print("La estrella es de tipo A")
        elif 10000<self._teff<28000:
            print("La estrella es de tipo B")
        else:
            print("La estrella es de tipo O")
    
    def calcular_densidad(self): 
        #Funcion que calcula la densidad de la estrella.
        #Parametros: masa y radio de la estrella.
        #Retorna: La densidad de la estrella.
        densidad = self._masa / ((4/3) * np.pi * self._radioestrella**3)    
        return densidad