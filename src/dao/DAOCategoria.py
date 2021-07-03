import pymysql

class DAOCategoria:

    def __init__(self):
        pass

    def connect(self):
        return pymysql.connect(host="localhost", port=3307,user="root",password="",database="proyecto_db")

    def read(self,id):
        con = DAOCategoria.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute("SELECT * FROM categoria order by codigo")
            else:
                cursor.execute("SELECT * FROM categoria where id = %s order by codigo",(id,))
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()