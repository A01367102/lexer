from globalTypes import *
from scanner import *
import os


path = r"C:/Users/TheOnlyOne67/Desktop/lexerc-/lexer R"
assert os.path.isfile(path)
with open(path, "r") as f:
    pass

f = open("C:/Users/TheOnlyOne67/Desktop/lexerc-/lexer R")
program = f.read() 		# lee todo el archivo a compilar
f.close()                       # cerrar el archivo con programa fuente
progLong = len(program) 	# longitud original del programa
program = program + '$' 	# agregar un caracter $ que represente EOF
position = 0 			# posición del caracter actual del string

# Para probar el scanner solito
recibeScanner(program, position, progLong) # para mandar los globales

token, tokenString, _ = getToken()
while (token != TokenType.ENDFILE):
    token, tokenString, _ = getToken()
