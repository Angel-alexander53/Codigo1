import mysql.connector

def conectar(consulta_sql):
    configuracion = {
        'user': 'ufcarxbvvy3bumqh',
        'password': 'Pfcw2fZr9u0ysGJ2iRlS',
        'host': 'bnlmetztwkmqgknt1neh-mysql.services.clever-cloud.com',
        'database': 'bnlmetztwkmqgknt1neh',
        'raise_on_warnings': True
    }

    try:
        conexion = mysql.connector.connect(**configuracion)
        print('Conexion Exitosa...')

        consulta = conexion.cursor()
        print("Consulta ejecutada:", consulta_sql)
        consulta.execute(consulta_sql)
        resultado = consulta.fetchall()

        consulta.close()
        conexion.close()
        return resultado
    
    except mysql.connector.Error as err:
        print(f"No fue posible conectarse a la base de datos: {err}")
        return []