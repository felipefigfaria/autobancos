import firebird.driver as fb

# CONEXAO COM BANCO DE DADOS
con = fb.connect(
    host="localhost", 
    database="C:\SIG2000\DATABASE\TESTE-PYTHON\TESTE-PYTHON.fdb",  # Caminho do banco de dados
    user="SYSDBA", 
    password="masterkey"
)  

cur = con.cursor()
cur.execute("select a.emp_cod, a.emp_raz, a.emp_fan, a.emp_logra, a.emp_num, a.emp_cep, a.emp_cgc, a.emp_insc, a.emp_tel from setempresas a")  # Consulta de teste
print(cur.fetchall())

con.close()