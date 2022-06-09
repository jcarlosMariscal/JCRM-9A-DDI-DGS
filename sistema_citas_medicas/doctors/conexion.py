import mysql.connector

def conectar():
    database = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "",
        database = "jcrm_scm",
        port = 3306
    )

    cursor = database.cursor(buffered=True)
    return [database, cursor]