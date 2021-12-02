import sqlite3
from sqlite3.dbapi2 import Error

def conexion(db):
    conn = None
    try:
        conn=sqlite3.connect(db)
    except Error as e:
        print (e)
    return conn

def agregarpalabra(conn):
    
    print("introduzca una palabra")
    palabra = input();
    print ("introduzca su significado")
    significado = input();
    data = (palabra,significado)
    
    sql = ''' INSERT INTO panameno(palabra,significado) VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()
    return cur.lastrowid

def editarpalabra(conn):
    print ("introduzca la palabra a editar")
    palabra = input();
    print ("introduzca su significado")
    significado = input();
    
    sql = ''' UPDATE panameno SET significado = ? where palabra = ? '''
    cur = conn.cursor()
    cur.execute(sql,(significado,palabra))
    conn.commit()
    return cur.lastrowid
   
def eliminarpalabra(conn):
    print ("introduzca la palabra a eliminar")
    palabra = input();
    sql = ''' DELETE FROM panameno WHERE palabra = ? '''
    cur = conn.cursor()
    cur.execute(sql,(palabra,))
    conn.commit()
    return cur.lastrowid

def listarpalabras(conn):
    sql = ''' SELECT * FROM panameno '''
    cur = conn.cursor()
    cur.execute(sql)
    records = cur.fetchall()
    for row in records:
        print ("id:", row [0]," | palabra:", row [1], " | significado:", row [2])
    return cur.lastrowid

def buscarpalabra(conn):
    print ("introduzca la palabra a buscar")
    palabra = input();
    sql = ''' SELECT * FROM panameno where palabra = ? '''
    cur = conn.cursor()
    cur.execute(sql,(palabra,))
    records = cur.fetchall()
    for row in records:
        print ("significado:", row [2])
    return cur.lastrowid

def main():
    database = r"C:/Users/Cristhian/Downloads/SQLiteStudio/prueba.db"
    conn = conexion(database)
    
    print ("Modulo 1");
    print ("Menu");
    print ("1 - Agregar Palabra");
    print ("2  - Editar Palabra");
    print ("3  - Eliminar Palabra");
    print ("4  - Ver listado de palabra");
    print ("5  - Buscar significado");
    print ("-----------------------------");
    print ("seleccione unas de las opciones anteriores");
    opciones = int(input());

    with conn:

        if opciones == 1:
            print ("Vamos agregar una Palabra");            
            agregarpalabra(conn)
            
        if opciones == 2: 
            print ("Vamos a editar una Palabra");
            editarpalabra(conn)

        if opciones == 3:
            print ("Vamos a eliminar una Palabra");
            eliminarpalabra(conn)

        if opciones == 4:
            print ("Ver listado de palabra");
            listarpalabras(conn)  
        
        if opciones == 5:
            print ("Buscar significado");
            buscarpalabra(conn)
    
        
        

if  __name__ == '__main__':
    main()