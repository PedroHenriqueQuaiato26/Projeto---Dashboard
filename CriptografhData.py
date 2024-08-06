import psycopg2
from dotenv import load_dotenv
import os 

load_dotenv(r'../Projeto Dashboard (LAB)/Credentials/Credentials_Defual.env')

# Extração do arquivo como .env 

class ExtractDatatoENV():
    def __init__(self):
        self.username = os.getenv('USER')
        self.password = os.getenv('PASSWORD')
        self.port = os.getenv('PORT')
        self.host = os.getenv('HOST')
        self.database = os.getenv('DATABASE_NAME')


#First_Connection = ExtractDatatoENV() # Comentado pois foi usado somente em teste para confirmar a presença dos dados do .env


class ConnectPostgresDatabasePass(ExtractDatatoENV):
    def __init__(self):
        super().__init__()
        try:
            
            self.ConnectDatabaseCredentials = psycopg2.connect(
                user=self.username,
                password=self.password,
                port=self.port,
                host=self.host,
                database=self.database
            )

            print('Connect Success !!')
            
        except Exception as e:
            print('Erro to connect postgres ', {e})
            
#Second_Connection = ConnectPostgresDatabasePass()


class ExtractTableData(ConnectPostgresDatabasePass):
    def __init__(self):
        super().__init__()

        self.cursor = self.ConnectDatabaseCredentials.cursor()  # Comentário de identificação do cursor
        
        self.SQLusername = "SELECT username FROM credentials WHERE id = '1';"
        self.SQLpassword = "SELECT password FROM credentials WHERE id = '1';"
        self.SQLKEY = "SELECT key_decrypt FROM credentials WHERE id = '1';"

        try:
            self.cursor.execute(self.SQLpassword)
            result = self.cursor.fetchall()
            self.QuerySqlPassword = result[0][0] if result else None
            
            print('password: ', self.QuerySqlPassword) 

            self.cursor.execute(self.SQLusername)
            result = self.cursor.fetchall()
            self.QuerySqlUsername = result[0][0] if result else None
            
            print('username: ', self.QuerySqlUsername)  

            self.cursor.execute(self.SQLKEY)
            result = self.cursor.fetchall()
            self.QuerySqlKEY = result[0][0] if result else None
            
            print('key_secret: ', self.QuerySqlKEY)  
            
            self.cursor.close()

        except Exception as e:
            print('Error when querying the password database and capturing them for use in the code:', e)

            


            
