fileku = open("kereta.txt", "w") 
fileku.write('Prameks\n') 
fileku.write('Joglosemarkerto\n') 
fileku.write('Sancaka\n') 
fileku.close() 

my_file = open("kereta.txt", "a+") 
print("filenamenya adalah : ",my_file.name) 
print("file modelnya adalah", my_file.mode) 
print("Encoding filenya adalah", my_file.encoding) 
print("Apakah file sudah ditutup?", my_file.closed) 
my_file.close() 
print("Apakah file sudah ditutup", my_file.closed)