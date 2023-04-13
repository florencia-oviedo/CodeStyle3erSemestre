from NumerosIgualesException import NumerosIgualesException
resultado = None
try:
    a = int(input('Digite el primer número: '))
    b = int(input('Digite le segundo número: '))
    if a == b:
        raise NumerosIgualesException('Son números iguales')

    resultado = a / b  # modificamos
except TypeError as e:
    print(f'TypeError - Ocurrio un error: {type(e)}')
except ZeroDivisionError as e:
    print(f'ZeroDivisionError - Ocurrio un error {type(e)}')
except Exception as e:
    print(f'Exception - Ocurrió un error: {type(e)}')
else:
    print("No se arrojo ninguna excepción")
finally:  # Siempre se va a ejecutar, lo podemos usar para liberar algun recurso para informar al usurio como termino nuestro manejo de excdpciones
    print("Ejecución de este bloque finally")


print(f'El resultado es: {resultado}')
print('seguimos...')
