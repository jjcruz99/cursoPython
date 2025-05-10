
conjuntoA = {1,2,3,4,5}
conjuntoB = {5,6,7,8,9}
conjuntoC = {3,5,7,0}
conjuntoD = {3,4}

#unir dos sets
print(conjuntoA.union(conjuntoB))
print(conjuntoB.union(conjuntoA))#conmutativa

#intersepcion
print('\nIntersepcion', conjuntoC.intersection(conjuntoA))

print(f'\nDiferencia setB : {conjuntoB.difference(conjuntoA)}')

print(f'\nDiferencia simetrica, elimina los valores de la intersepcion : {conjuntoB.symmetric_difference(conjuntoA)}')

print('Preguntas con set'.center(50,'*'))
print(f'Si un conjunto esta contenido en otro {conjuntoD.issubset(conjuntoA)}')
print(f'Si un conjunto contiene a otro {conjuntoA.issuperset(conjuntoD)}')
print(f'Si un conjunto no contiene a otro {conjuntoA.isdisjoint(conjuntoD)}')
print(f'Si un conjunto no contiene a otro {conjuntoA.isdisjoint(conjuntoB)}')


