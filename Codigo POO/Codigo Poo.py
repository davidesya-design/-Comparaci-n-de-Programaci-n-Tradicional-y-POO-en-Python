"""
Programa para calcular el promedio semanal del clima usando Programación Orientada a Objetos.
utiliza clases, objetos y encapsulamiento.

Espero que no halla yo dejado alguna falla.

───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───
───█▒▒░░░░░░░░░▒▒█───
────█░░█░░░░░█░░█────
─▄▄──█░░░▀█▀░░░█──▄▄─
█░░█─▀▄░░░░░░░▄▀─█░░█
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
Ya que no se mucho programar en pyton tengo que revisar la documentacion y uno que otro tutorial.
"""

# Clase base que representa un día del clima
class DiaClima:
    """
    Clase que representa la información del clima de un día específico.
    Encapsula los datos del día y su temperatura.
    """
    
    def __init__(self, nombre_dia, temperatura):
        """
        Constructor de la clase DiaClima.
        Inicializa el nombre del día y la temperatura.
        """
        self._nombre_dia = nombre_dia  # Atributo privado (encapsulamiento)
        self._temperatura = temperatura  # Atributo privado
    
    # Métodos getter para acceder a los atributos privados
    def get_nombre_dia(self):
        """Retorna el nombre del día."""
        return self._nombre_dia
    
    def get_temperatura(self):
        """Retorna la temperatura del día."""
        return self._temperatura
    
    # Método setter para modificar la temperatura
    def set_temperatura(self, nueva_temperatura):
        """nueva temperatura para el día."""
        self._temperatura = nueva_temperatura
    
    def __str__(self):
        """DiaClima."""
        return f"{self._nombre_dia}: {self._temperatura}°C"


# Clase que representa una semana completa de clima (hereda conceptos)
class SemanaClima:
    """
    representar una semana completa de registros sobre el clima.
     lista de objetos DiaClima y métodos para poder usarlos.
    """
    
    def __init__(self):
        """
        Constructor de la clase SemanaClima.
        Inicializa una lista vacía para los días de clima.
        """
        self._dias_clima = []  # Lista privada de días
    
    def agregar_dia(self, dia_clima):
        """
        Agrega un objeto DiaClima a la semana.
        
        Parámetros:
        dia_clima: Objeto de tipo DiaClima a agregar
        """
        self._dias_clima.append(dia_clima)
    
    def ingresar_temperaturas_semana(self):
        """
        Método para ingresar las temperaturas de toda la semana.
        Solicita al usuario las temperaturas para cada día.
        """
        dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        
        print("=== INGRESO DE TEMPERATURAS SEMANALES (POO) ===")
        
        for nombre_dia in dias_semana:
            while True:
                try:
                    temp = float(input(f"Ingrese la temperatura para el {nombre_dia}: "))
                    dia = DiaClima(nombre_dia, temp)
                    self.agregar_dia(dia)
                    break
                except ValueError:
                    print("Error: Por favor ingrese un número válido.")
    
    def calcular_promedio_semanal(self):
        """
        Calcula el promedio de temperaturas de la semana.
        
        Retorna:
        float: El promedio semanal de temperaturas
        """
        if not self._dias_clima:
            return 0
        
        suma = sum(dia.get_temperatura() for dia in self._dias_clima)
        promedio = suma / len(self._dias_clima)
        return promedio
    
    def obtener_temperatura_maxima(self):
        """
        Encuentra la temperatura máxima de la semana.
        
        Retorna:
        tuple: (nombre_dia, temperatura) del día más caluroso
        """
        if not self._dias_clima:
            return None
        
        dia_max = max(self._dias_clima, key=lambda dia: dia.get_temperatura())
        return (dia_max.get_nombre_dia(), dia_max.get_temperatura())
    
    def obtener_temperatura_minima(self):
        """
        Encuentra la temperatura mínima de la semana.
        
        Retorna:
        tuple: (nombre_dia, temperatura) del día más frío
        """
        if not self._dias_clima:
            return None
        
        dia_min = min(self._dias_clima, key=lambda dia: dia.get_temperatura())
        return (dia_min.get_nombre_dia(), dia_min.get_temperatura())
    
    def mostrar_resumen_semanal(self):
        """
        Muestra un resumen completo de la semana  el clima.
        """
        print("\n=== RESUMEN SEMANAL DEL CLIMA (POO) ===")
        print("Temperaturas diarias:")
        
        for dia in self._dias_clima:
            print(f"  {dia}")
        
        promedio = self.calcular_promedio_semanal()
        print(f"\nPromedio semanal: {promedio:.2f}°C")
        
        # Mostrar temperatura máxima y mínima
        max_dia, max_temp = self.obtener_temperatura_maxima()
        min_dia, min_temp = self.obtener_temperatura_minima()
        
        print(f"Temperatura máxima: {max_dia} con {max_temp}°C")
        print(f"Temperatura mínima: {min_dia} con {min_temp}°C")
        
        # Análisis adicional usando polimorfismo conceptual
        self._analizar_tendencia_climatica()
    
    def _analizar_tendencia_climatica(self):
        """
        Ejemplo de encapsulamiento.
        """
        if len(self._dias_clima) < 2:
            return
        
        # Calcular diferencia entre primer y último día
        primer_dia_temp = self._dias_clima[0].get_temperatura()
        ultimo_dia_temp = self._dias_clima[-1].get_temperatura()
        
        diferencia = ultimo_dia_temp - primer_dia_temp
        
        if diferencia > 2:
            print("Tendencia: Temperaturas en aumento durante la semana ↗")
        elif diferencia < -2:
            print("Tendencia: Temperaturas en descenso durante la semana ↘")
        else:
            print("Tendencia: Temperaturas estables durante la semana →")


# Clase principal para ejecutar el programa
class ProgramaClima: 
    def ejecutar(self):
        """
        Ejecuta el flujo del programa.
        """
        print("PROGRAMA PARA CALCULAR EL PROMEDIO SEMANAL DEL CLIMA (POO)")
        print("=" * 60)
        
        # Crear objeto SemanaClima
        semana = SemanaClima()
        
        # Ingresar temperaturas
        semana.ingresar_temperaturas_semana()
        
        # Mostrar resultados
        semana.mostrar_resumen_semanal()


# Entrada del programa
if __name__ == "__main__":
    programa = ProgramaClima()
    programa.ejecutar()
