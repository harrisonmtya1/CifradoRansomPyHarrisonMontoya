

from cryptography.fernet import Fernet
import os





#Cargar la llave generada
def cargar_key():
    return open('key.key','rb').read()


def decifrar(items,key):
    f=Fernet(key)
    for item in items:
        #lee el archivo
        with open(item,'rb') as file:
            file_data=file.read()

        desencriptar_data=f.decrypt(file_data)

        #escribo el archivo
        with open(item,'wb') as file:
            file.write(desencriptar_data)

        os.rename(item,item + '.' + '.txt')



if __name__=='__main__':
    path_to_encrypt='C:/Users\Harrison Montoya V\OneDrive - IUE\Semestre 3\HackeoEtico\Ejercicio 3\CifradoRansomPyHarrisonMontoya\DatosCifradoDesifrado'
    items=os.listdir(path_to_encrypt)
    full_path=[path_to_encrypt+'\\' + item for item in items]
    key=cargar_key()
    decifrar(full_path,key)