# declaramos variables
try:
  archivo = open('Tecnicatura3_Py\Archivos\leccion02\prueba.txt','w',encoding='utf8') # la w es de write(escribir), utf8=> lea ascentos
  archivo.write('programamos con diferentees tipos de archivos en txt\n')
  archivo.write('los acentos son importantes para las palabras\n')
  archivo.write('como por ejemplo: acción, ejecución, producción\n')
  archivo.write('las letras son:\n"r": read leer,\n"a": append anexa\n"w": write escribe\n"x": crea un archivo\n')
  archivo.write('"t": especifica tipo de archivo .txt\n"b": archivos binarios ej pdf\n"w+": leer y escribe\n"r+": escribe y leer\n')

  archivo.write('con esto terminamos')
except Exception as e:
  print(e)
finally: #siempre se ejecuta
  archivo.close # con esto cerramos el arcivo


