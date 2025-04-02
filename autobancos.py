import sys
import firebird.driver as fb

argvs = sys.argv
caminho_banco = argvs[1]
nome_empresa = argvs[2]

print(argvs[1])
print(argvs[2])



print("")
print("########## DADOS DA EMPRESA ##########")
print("")
emp_cod = input("Digite o código da empresa: ")
razao_social = input("Razão Social da empresa: ")
nome_fan = input("Nome fantasia: ")
endereco = input("Endereço da empresa: ")
numero_end = input("Numero: ")
complemento = input("Complemento: ")
bairro = input("Bairro: ")
cidade = input("Cidade: ")
estado = input("Estado: ")
cep = input("CEP: ")
cnpj = input("CNPJ: ")
insc_estadual = input("Inscrição Estadual: ")
contato = input("Contato: ")
emp_sigla = input("Sigla da empresa: ")
emp_email = input("Email da empresa: ")
emp_raz_xml = input ("Razão Social no XML: ")

# CONEXAO COM BANCO DE DADOS
con = fb.connect(
    database=argvs[1],  # Caminho do banco de dados
    user="SYSDBA", 
    password="masterkey"
)  

cur = con.cursor()

cur.execute("""
    UPDATE SETEMPRESAS SET
        EMP_RAZ = ?,
        EMP_FAN = ?,
        EMP_LOGRA = ?,
        EMP_NUM = ?,
        EMP_COMPL = ?,
        EMP_BAIR = ?,
        EMP_CID = ?,
        EMP_EST = ?,
        EMP_CEP = ?,
        EMP_CGC = ?,
        EMP_INSC = ?,
        EMP_TEL = ?,
        EMP_SIGLA = ?,
        EMP_EMAIL = ?,
        EMP_RAZ_XML = ?
    WHERE (EMP_COD = ?);
""", (razao_social, nome_fan, endereco, numero_end, complemento, bairro, cidade, estado, cep, cnpj, insc_estadual, contato, emp_sigla, emp_email, emp_raz_xml, emp_cod))


cur.execute(f"""
    UPDATE SETCONFIG SET 
        PATH_REPORT = 'X:\\ARQUIVOS\\{argvs[2]}\\Report',
        PATH_REPORT_PERSONALIZADA = 'X:\\ARQUIVOS\\{argvs[2]}\\Report',
        PATH_ANEXOS = 'X:\\ARQUIVOS\\{argvs[2]}\\Report',
        CAMINHO_CERTIFICADO = '',
        SENHA_CERTIFICADO = '',
        DIAS_VENCIMENTO_CERTIFICADO = 30,
        USU_CONNECTION = 100,
        USA_CLOUD = 1,
        NFE_TPAMB = '2'
    WHERE (EMP_COD >= 1);
""")   

print(cur.fetchall())
con.commit()
con.close()

print("Updates executados.")