import sys
import os
import firebird.driver as fb
from dotenv import load_dotenv

argvs = sys.argv
caminho_banco = argvs[1]
nome_empresa = argvs[2]
empresa = argvs[3]
dotenv_path = os.path.join(os.path.dirname(__file__), '.env.example')

load_dotenv(dotenv_path)
# CREDENCIAIS BANCO DE DADOS
db_user = os.getenv('DB_USER')
db_pass = os.getenv('DB_PASS')

# INFORMACOES EMPRESA
razao_social = os.getenv('RAZAO_SOCIAL')
nome_fantasia = os.getenv('NOME_FANTASIA')
endereco = os.getenv('ENDERECO')
end_numero = os.getenv('END_NUMERO')
end_compl = os.getenv('END_COMPL')
end_bairro = os.getenv('END_BAIRRO')
cidade = os.getenv('CIDADE')
estado = os.getenv('ESTADO')
cep = os.getenv('CEP')
cnpj = os.getenv('CNPJ')
insc_estadual = os.getenv('INSC_ESTADUAL')
contato = os.getenv('CONTATO')
emp_sigla = os.getenv('EMP_SIGLA')
emp_email = os.getenv('EMP_EMAIL')
emp_raz_xml = os.getenv('EMP_RAZAO_XML')

# CONEXAO COM BANCO DE DADOS
con = fb.connect(
    database=argvs[1],  # Caminho do banco de dados
    user=db_user,
    password=db_pass
)  
cur = con.cursor()

def info_empresa():
           
    # SETEMPRESAS
    cur.execute(f"""
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
        WHERE (EMP_COD = {argvs[3]});
    """, (razao_social, nome_fantasia, endereco, end_numero, end_compl, end_bairro, cidade, estado, cep, cnpj, 
          insc_estadual, contato, emp_sigla, emp_email, emp_raz_xml))

    con.commit()
    con.close()

def updates():

    # SETCONFIG
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
        WHERE (EMP_COD = {argvs[3]});
    """)   

    # SETCONFIGNFE
    cur.execute(f"""
        UPDATE SETCONFIGNFE SET 
            NFE_DANFE = 'X:\\ARQUIVOS\\{argvs[2]}\\FISCAL\\00{argvs[3]}\\Nfe\\Danfe\\retrato.rtm',
            LOG_PATH = 'X:\\ARQUIVOS\\{argvs[2]}\\Fiscal\\00{argvs[3]}\\NFe\\Logs',
            XML_PATH = 'X:\\ARQUIVOS\\{argvs[2]}\\Fiscal\\00{argvs[3]}\\NFe\\XML',
            NFCE_DANFE = 'X:\\ARQUIVOS\\{argvs[2]}\\Fiscal\\00{argvs[3]}\\NFCe\\Danfe\\retrato.rtm',
            LOG_PATH_NFCE = 'X:\\ARQUIVOS\\{argvs[2]}\\Fiscal\\00{argvs[3]}\\NFCe\\Log',
            XML_PATH_NFCE = 'X:\\ARQUIVOS\\{argvs[2]}\\Fiscal\\00{argvs[3]}\\NFCe\\XML',
            LOG_PATH_MDFE = 'X:\\ARQUIVOS\\{argvs[2]}\\Fiscal\\00{argvs[3]}\\MDFe\\LOG',
            XML_PATH_MDFE = 'X:\\ARQUIVOS\\{argvs[2]}\\Fiscal\\00{argvs[3]}\\MDFe\\XML'
        WHERE (EMP_COD = {argvs[3]});        
    """)  

    # COMFORNECEDORESPAR
    cur.execute(f"""
        UPDATE COMFORNECEDORESPAR SET 
            PED_PATH = 'X:\\ARQUIVOS\\{argvs[2]}\\REPORT\\Compras\\Reports\\ComprasReport.rav'
        WHERE (EMP_COD = {argvs[3]});        
    """)            

    # VENPARAMETROS
    cur.execute(f"""
        UPDATE VENPARAMETROS SET 
            PED_PATH = 'X:\\ARQUIVOS\\{argvs[2]}\\Report\\Vendas\\Reports\\VendasReport.rav',
            PRO_PATH = 'X:\\ARQUIVOS\\{argvs[2]}\\Report\\Vendas\\Reports\\PreVendaReport.rav',
            NF_PATH = 'X:\\ARQUIVOS\\{argvs[2]}\\Report\\Produtos\\Reports\\ProdutosReport.rav',
            DP_PATH = 'X:\\ARQUIVOS\\{argvs[2]}\\Report\\Vendas\\Reports\\BoletoPadrao.rav',
            IMP_PORTA = 'UNIVERSAL PRINTER',
            IMP_PORTA_PROP = 'UNIVERSAL PRINTER',
            IMP_PORTA_PLAL = 'UNIVERSAL PRINTER',
            IMP_PORTA_FRET = 'UNIVERSAL PRINTER',
            IMP_PORTA_RETI = 'UNIVERSAL PRINTER',
            IMP_PORTA_ESPE = 'UNIVERSAL PRINTER',
            IMP_PORTA_BOLT = 'UNIVERSAL PRINTER',
            IMP_PORTA_FAX = 'UNIVERSAL PRINTER',
            IMP_PORTA_KIT = 'UNIVERSAL PRINTER',
            MAPA_PATH = 'X:\\ARQUIVOS\\{argvs[2]}\\Report\\Vendas\\Reports\\MapaCargaReport.rav',
            PLA_PATH = 'X:\\ARQUIVOS\\{argvs[2]}\\Report\\Vendas\\Reports\\Vendaspla_separacao.rav',
            ORCAMENTO_PATH = 'X:\\ARQUIVOS\\{argvs[2]}\\Report\\Vendas\\Reports\\Orcamento.fr3'
        WHERE (EMP_COD = {argvs[3]});
    """)        

    # PCPPARAMETROS
    cur.execute(f"""
        UPDATE PCPPARAMETROS SET 
            OP_PATH = 'X:\\ARQUIVOS\\{argvs[2]}\\REPORT\\PCP\\Reports\\SIGPCPReport_OP_Padrao.rav',
            LAUDO_PROD_PRODUCAO_PATH = 'X:\\ARQUIVOS\\{argvs[2]}\\REPORT\\PCP\\Reports\\SIGPCPReport_Laudo_Produto_Producao_Padrao.rav',
            LAUDO_PROD_ACABADO_PATH = 'X:\\ARQUIVOS\\{argvs[2]}\\REPORT\\PCP\\Reports\\SIGPCPReport_Laudo_Produto_Acabado_Padrao.rav',
            ETIQUETA_APTO_PATH = NULL
        WHERE (EMP_COD = {argvs[3]});        
    """)
    con.commit()
    con.close()

print(f"Caminho da base: {argvs[1]}")
print(f"Alias da base: {argvs[2]}")
print(f"Código da empresa: {argvs[3]}")
print("")

print("########## ESCOLHA UMA OPÇÃO ##########")
resposta = input("1 - Informações da empresa / 2 - Ajuste dos caminhos: ")
if resposta == "1":
    info_empresa()
    print("Informações da empresa registradas.")
elif resposta == "2":
    updates()
    print("Updates executados.")
else:
    print("Resposta inválida.")