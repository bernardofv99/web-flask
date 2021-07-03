import pymysql

class DAOProducto:

    def __init__(self):
        pass

    def connect(self):
        return pymysql.connect(host="localhost", port=3307,user="root",password="",database="proyecto_db")

    def read(self,id):
        con = DAOProducto.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute("SELECT * FROM producto order by codigo")
            else:
                cursor.execute("SELECT * FROM producto where id = %s order by codigo",(id,))
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def insert(self,data):
        con = DAOProducto.connect(self)
        cursor = con.cursor()
        try:
            cursor.execute("INSERT INTO producto(codigo, descripcion, precio, stock, categoria) VALUES(%s,%s,%s,%s,%s)",(data['codigo'], data['descripcion'], data['precio'], data['stock'], data['categoria'],))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()
    
    def update(self,id,data):
        con = DAOProducto.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("UPDATE producto SET codigo=%s, descripcion=%s, precio=%s, stock=%s, categoria=%s where id = %s",(data['codigo'], data['descripcion'], data['precio'], data['stock'], data['categoria'],id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def delete(self,id):
        con = DAOProducto.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("delete from producto where id = %s",(id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()
