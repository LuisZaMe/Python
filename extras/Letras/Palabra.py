#validadr cuantos caracteres tiene una palabra y que me de 
#la segunda letra y el string viene vacio diga que no hay cadena para validar

palabra = input("Ingrese una palabra : ")
if len(palabra) > 0:
     print("Tu palabra tiene "+str(len(palabra))+" letras y la segunda letra es : "+str(palabra[1]))   
    #print("Tu palabra tiene ",len(palabra)," letras y la segunda letra es : ",palabra[1])   
else:
     print("No hay texto")
     


 