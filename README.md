Este script tem como objetivo facilitar o processo de configuração de novas empresas em uma base de dados, realizando tanto o preenchimento de informações cadastrais quanto o ajuste de caminhos de arquivos (layouts, XMLs, etc.).

Parâmetros de entrada:
    - Caminho do banco: Local onde está armazenada a base de dados.
    - Alias da empresa: Nome curto ou identificador utilizado para a empresa.
    - Código da empresa: Identificador numérico da empresa na base.

Funcionalidade:
Ao executar o script, será exibido um menu com duas opções:

    1. Preenchimento de informações da empresa
        Nesta opção, os dados da empresa serão inseridos ou atualizados com base nas informações contidas no arquivo info_empresa.txt.

    2.Ajuste de caminhos de arquivos
        Esta opção realiza a atualização dos caminhos de arquivos da empresa (layouts, XMLs, etc.), utilizando o alias informado como base para os novos caminhos.