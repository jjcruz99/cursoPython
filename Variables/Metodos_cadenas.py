#metodos

cadena1= " Hola MUNdO   "
print(f"Cadena original: {cadena1}")
mayusculas = cadena1.upper()
print(f'Cadena metodo upper: {mayusculas}')
print(f'Cadena metodo lower: {cadena1.lower()}')
print(f'Quitar espacios inicio y final: {cadena1.strip()}')

#aplicar varios metodos a la vez
print(cadena1.strip().lower().replace(' ','.'))

print(len(cadena1))
