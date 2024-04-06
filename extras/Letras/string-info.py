#Indexing and slicing python strings
message = input ("Enter a message: ")
lenMessage=len(message)

if lenMessage > 0:
   
   print("First letter :", message[0])
   print("last letter :", message[lenMessage-1])
   print("middle (opcion 1) letter :", message[(lenMessage//2)])
   print("middle (opcion 2) letter :", message[(int(lenMessage/2))])
   print("Even index characters:", message[0::3])
   print("Even index characters:", message[0::5])
   
   print("Odd index characters:", message[1::2])   
   print("reverse index characters:", message[::-1])   


else:
   print("no tiene texto")