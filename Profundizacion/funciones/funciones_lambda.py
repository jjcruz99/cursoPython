

#son funciones anonimas y son pequeñas
#no lleva parentesis ni return

mi_funcion = lambda a,b: a+b
resultado = mi_funcion(4,6)
print(resultado)

mi_funcion = lambda : 'Saludo desde la funcion lambda sin argumentos'
print(mi_funcion())

mi_funcion = lambda a=3,b=89: a*b
print(mi_funcion())
print(mi_funcion(2,5))

mi_funcion = lambda *args,**kwargs: len(args)+len(kwargs)
print(mi_funcion(1,2,3,5,a=5,b=2))

mi_funcion = lambda a,b,x=2,*args,**kwargs,: a+b+x+len(args)+len(kwargs)
print(mi_funcion(20,30,1,2,3,5, e=5,k=2))