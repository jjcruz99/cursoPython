from pool_conexion import Conexion
from cliente import Cliente
class ClienteDAO:
    SELECCIONAR = 'SELECT * FROM clientes'
    INSERTAR = 'INSERT INTO clientes(nombre,apellido,membresia) VALUES(%s,%s,%s)'
    ACTUALIZAR = 'UPDATE clientes SET nombre=%s,apellido=%s,membresia=%s WHERE id_cliente=%s'
    ELIMINAR = 'DELETE FROM clientes WHERE id_cliente=%s'

    @classmethod
    def seleccionar(cls):
        conexion= None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()

            lista_clientes = []
            for registro in registros:
                cliente = Cliente(registro[0],registro[1],registro[2],registro[3])
                lista_clientes.append(cliente)
            return lista_clientes

        except Exception as e:
            print(f'Ocurrio un error al obtener todos los clientes: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def insertar(cls,cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre,cliente.apellido,cliente.membresia)
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            return  cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al insertar el cliente')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def actualizar(cls,cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre,cliente.apellido,cliente.membresia,cliente.id_cliente)
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return  cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al actualizar el cliente')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls,id):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (id,)
            cursor.execute(cls.ELIMINAR, valores)
            conexion.commit()
            return  cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al eliminar el cliente')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

if __name__ == '__main__':

    # cliente1 = Cliente(nombre='Nelson', apellido='Cruz', membresia=3)
    # validacion = ClienteDAO.insertar(cliente1)
    # print(validacion)

    # cliente1 = Cliente(id_cliente=3,nombre='Nelson', apellido='Ariza', membresia=3)
    # validacion = ClienteDAO.actualizar(cliente1)
    # print(validacion)

    # validacion = ClienteDAO.eliminar(3)
    # print(validacion)

    clientes = ClienteDAO.seleccionar()
    for cliente in clientes:
        print(cliente.__str__())

