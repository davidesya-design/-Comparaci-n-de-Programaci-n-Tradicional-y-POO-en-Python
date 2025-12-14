"""
Programa para calcular el promedio semanal del clima usando programación tradicional.
Espero que no halla yo dejado alguna falla.

/\     /\
  \ _____\
   (_)-(_)

Ya que no se mucho programar en pyton tengo que revisar la documentacion y uno que otro tutorial.
   
"""

# Ingresar las temperaturas diarias
def ingresar_temperaturas():
    """
    Aqui solicito las temperaturas de los 7 días de la semana.
    Retorna una lista con las temperaturas ingresadas.
    """
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    temperaturas = []
    
    print("=== INGRESO DE TEMPERATURAS SEMANALES ===")
    
    for i in range(7):
        while True:
            try:
                temp = float(input(f"Ingrese la temperatura para el {dias_semana[i]}: "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Error: Por favor ingrese un número que sea válido.")
    
    return temperaturas


# Función para calcular el promedio semanal
def calcular_promedio_semanal(temperaturas):
    """
    Calcula el promedio de las temperaturas de la semana.
    Recibe una lista de temperaturas y retorna el promedio.
    """
    if not temperaturas:
        return 0
    
    suma = sum(temperaturas)
    promedio = suma / len(temperaturas)
    return promedio


# Función para mostrar los resultados
def mostrar_resultados(temperaturas, promedio):
    """
    Muestra las temperaturas diarias y el promedio semanal.
    """
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    
    print("\n=== RESULTADOS SEMANALES ===")
    print("Temperaturas diarias:")
    for i in range(7):
        print(f"  {dias_semana[i]}: {temperaturas[i]}°C")
    
    print(f"\nPromedio semanal: {promedio:.2f}°C")
    
    # Análisis de la temperatura maxima y minima 
    temp_max = max(temperaturas)
    temp_min = min(temperaturas)
    print(f"Temperatura máxima: {temp_max}°C")
    print(f"Temperatura mínima: {temp_min}°C")


# Función principal que organiza el flujo del programa
def main():
    """
    Función principal que coordina el flujo del programa.
    """
    print("PROGRAMA PARA CALCULAR EL PROMEDIO SEMANAL DEL CLIMA")
    print("=" * 50)
    
    # Paso 1: Ingresar temperaturas
    temperaturas = ingresar_temperaturas()
    
    # Paso 2: Calcular promedio
    promedio = calcular_promedio_semanal(temperaturas)
    
    # Paso 3: Mostrar los  resultados :)
    mostrar_resultados(temperaturas, promedio)


# Desde aqui es el punto de entrada
if __name__ == "__main__":
    main()
