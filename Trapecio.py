import math

# Definimos funcion :V
def f(x):
    return (1 / (2 * math.pi)) * math.exp(-x**2 / 2)

# El valor real de la expresion
valor_real = -math.e / (6 * math.pi)

# Limites
a = -1
b = 1

# Iniciamos var..
integral_aproximada = 0.0
resultados_por_intervalo = []

# Calcular la aproximación de la integral usando el método del trapecio para cada cantidad de subintervalos
subintervalos = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024] #Definamolos
print("Aproximación con 'n' subintervalos   |   Valor   |   Error relativo %") 
print("-" * 70)
for num_subintervalos in subintervalos: #Ciclo para los calculos
    h = (b - a) / num_subintervalos
    
    integral_aproximada = 0.5 * (f(a) + f(b))
    for i in range(1, num_subintervalos):
        integral_aproximada += f(a + i * h)
    integral_aproximada *= h
    
    error_relativo = abs(integral_aproximada - valor_real) / abs(valor_real)  # Saca error%
    
    print(f"Aproximación con {num_subintervalos:4} subintervalos   |   {integral_aproximada:.6f}   |   {error_relativo:.6f}")

#extras++
print("\033[91mBy: Sebastian Camacho - M31 - Para Metodos Numericos U5") 
print("\033[0m ")
    #Itento numero 15 :)