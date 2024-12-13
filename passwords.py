import sqlite3

MASTER_PASSWORD = "SHIKAMARU"

conn = sqlite3.connect('password.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
    service TEXT NOT NULL,
    username TEXT NOT NULL,222
    password TEXT NOT NULL, 
);       
''')

def menu ():
    print("*****************************")
    print("* i : inserir nova senha    *")
    print("* l : listar serviços salvos*") 
    print("* r : recuperar uma senha   *") 
    print("* s : sair                  *") 
    print("*****************************")

while True:
    menu
    op = input("Oque deseja fazer ?")
    if op not in ['l','i','r','s']:
        print('Opção invalidada!')
        continue

    if op =='s':
        break

    conn.close()