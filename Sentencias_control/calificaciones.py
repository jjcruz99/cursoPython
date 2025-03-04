print('****Programa calificaciones****')
calificacion = float(input('Digite su nota (0 a 10): '))
nota = None
if calificacion <= 10 and calificacion >= 9:
    nota = 'A'
elif calificacion >= 8 and calificacion <= 9:
    nota = 'B'
elif calificacion >= 7 and calificacion <= 8:
    nota = 'C'
elif calificacion >= 6 and calificacion <= 7:
    nota = 'D'
elif calificacion >= 0 and  calificacion <= 6:
    nota = 'F'
else :
    nota = 'Valor desconocido'

print(f'Su nota : {nota}')