import psycopg2 
from CriptografhData import ExtractTableData
from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os 

load_dotenv(r'/home/pedro/Área de Trabalho/ITL/Credentials/Credentials_Hot.env')

class ExtractDatabaseHOT(ExtractTableData):
    def __init__(self):
        super().__init__()

        try:    
            self.PortHOT = os.getenv('PORT')
            self.HostHOT = os.getenv('HOST')
            self.DatabaseHOT = os.getenv('DATABASE_NAME')

            print('Successfully capturing data from the database and .env')

        except Exception as e:
            print('fatal error with description:', {e})
            
        try:
            self.key = self.QuerySqlKEY
            self.cipher = Fernet(self.key)

            self.PasswordHOTDescritp = self.cipher.decrypt(self.QuerySqlPassword).decode()
            print(self.PasswordHOTDescritp)

            self.UsernameHOTDescritp = self.cipher.decrypt(self.QuerySqlUsername).decode()
            print(self.UsernameHOTDescritp)

            print('Successfully decrypted')

        except Exception as e:
            print('Erro to decrypted', {e})


#Fourth_Connection = ExtractDatabaseHOT()


class ConnectToDatabaseHOT(ExtractDatabaseHOT):
    def __init__(self):
        super().__init__()

        try:
            self.ConnectDatabaseHOT = psycopg2.connect(
                user=self.UsernameHOTDescritp,
                password=self.PasswordHOTDescritp,
                port=self.PortHOT,
                host=self.HostHOT,
                database=self.DatabaseHOT
            )

            print('Successful connection to database intended for production')

        except Exception as e:    
             print('fatal error with description:', {e})

#Fifth_Connection = ConnectToDatabaseHOT() # Vamos levar para outro codigo para servir de execução para as querys ! 



