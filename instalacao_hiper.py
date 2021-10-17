

def duvidas():
    """
    - Configurações * Fiscal * Série Fiscal * Nova série fiscal * Modelo do documento fiscal
    - Não há a opção 'Manifesto eletrônico de documento fiscal', ou há, mas foi modificado?
    """


#
def hiper_detalhes():
    """
    - Campos como: inscrição estadual, cpf, cnpj não devem conter caracteres especiais
    """


#
def tutorial():
    """
    Site para baixar recursos do Hiper: https://portal.hiper.com.br/ (acesso necessário)

    -------------------------------------- TESTAR PING PARA SABER SE HÁ INTERNET --------------------------------------
    - Ir ao terminal e executar ping endereço_website (ex: ping www.google.com)

    ------------------------------------- CRIAR REGRAS DE EXCEÇÃO PARA O FIREWALL -------------------------------------
    Acessar o painel de controle    Windows defender firewall    configurações avançadas    regras de entrada
    nova regra    porta (marcar)    avançar    tcp (marcar)
    portas locais específicas (9094,9095,9096,9097,9098,9099,1433)    avançar    permitir a conexão (marcar)
    avançar    avançar    nome (opcional)    concluir

    Acessar o painel de controle    Windows defender firewall    configurações avançadas    regras de saída
    nova regra    porta (marcar)    avançar    tcp (marcar)
    portas locais específicas (9094,9095,9096,9097,9098,9099,1433)    avançar    permitir a conexão (marcar)
    avançar    avançar    nome (opcional)    concluir

    -------------------------------------------------- DESATIVAR IPv6 --------------------------------------------------
    Ícone internet (botão ->)    abrir configurações de rede e internet    alterar opções de adaptador
    selecionar a conexão da máquina (botão ->)    propriedades    protocolo ip versão 6 (desmarcar)    OK

    ----------------------------------- INSTALAR OS SOFTWARES RELACIONADOS AO HIPER -----------------------------------
    - Logar no site [ Hiper / Hiperador ] (as credenciais usadas foram as de um funcionário, eu não tenho a minha)
    - Clicar em 'downloads e links' e no link 'hiper loja e caixa'
    - No instalador, selecionar os softwares do Hiper um de cada vez e baixar seus executáveis
    - No instalador, instalar o SQL Server 2008
    - Ao término, o instalador vai instalar o 'Hiper' na disco local

    ---------------------------------------------- CONFIGURAR PASTA HIPER ----------------------------------------------
    Selecionar a pasta do Hiper (botão ->) no disco local    propriedades    segurança    editar...    adicionar...
    digitar 'todos' no input    OK    Selecionar a opção 'todos'    OK
    Se o dropdown 'controle total' estiver desmarcado, então marcar    aplicar    OK

    ------------------------------------------- ANTIVÍRUS: CRIAR RESTRIÇÕES -------------------------------------------
    - A recomendação é criar regras de exceção ao desativamento do antivírus enquanto o sistema estiver sendo usado

    - ATIVAR RECURSOS DO WINDOWS -
    Painel de centrole    programas e recursos    link=ativar ou desativar recursos do Windows
    Abertura do painel [ Recursos do Windows ]    Habilitar os 2 primeiros itens (e todos os seus checkboxes)
    Os softwares [ .NET Framework 3.5 ] [ .NET Framework Advanced series ] são os que devem ser instalados

    DETALHE
    - Será aberta uma janela nova, onde se deve permitir que o Windows procure e baixe os recursos
    - Depois de algum tempo, serão aplicadas as alterações

    ------------------------------------- ATIVAR PROTOCOLOS DE REDE NO SQL SERVER -------------------------------------
    - Este computador * botão -> * gerenciar * Serviços e aplicativos * SQL server configuration mananger
      * Configuração de rede do SQL Server * Protocolos para SQL2014 * Habilitar todos os serviços

    ---------------------------------------------- REINICIAR O SQL SERVER ----------------------------------------------
    Serviços do SQL Server    SQL Server (botão -> * reiniciar)

    ------------------------------------------ ATIVAR PROTOCOLOS DE SEGURANÇA ------------------------------------------
    Acessar o Painel de controle    Acessar 'Opções da internet'    Aba=Avançadas    Checkbox=SSL & TLS (marcar todos)
    Aplicar    OK

    ----------------------------------------- INSTALAR ATUALIZAÇÕES DO WINDOWS -----------------------------------------
    Menu Iniciar    Pesquisar 'Verificar se há atualizações'    Instalar atualizações pendentes (se há)

    DETALHE
        Pela atualização são mantidas as manutenções tanto do SSL, TLS e .Net framework

    ------------------------------------------------------- WMI -------------------------------------------------------
    - Licenças no Windows, que nesse contexto, criariam licenças para validar os softwares alvos deste tutorial
    (Hiper windows & Novo hiper)

    PROBLEMA
        Segundo o professor deste tutorial, o WMI pode apresentar problemas em suas licenças, e isso é, na maioria das
        vezes, um problema que requer formatação
    """


# Devolução de vendas
def compra_devolucao():
    """
    ------------------------------------------------------ FONTE ------------------------------------------------------
    https://youtu.be/eU5MbZvhRyo

    ----------------------------------------------------- CAMINHO -----------------------------------------------------
    Dropdown=Vendas    Link=Operações    Link=Devoluções de venda    Pesquisar pelo cliente na barra de pesquisa
    Dropdown=Produto    Dropdown=Vendedor    Input=Quantidade    Botão=Salvar e liberar

    -------------------------------------------------- CAMINHOS EXTRA --------------------------------------------------
    Ao executar a devolução, haverá uma redirecionamento para página com uma listagem de devoluções de venda
    O link da sua listagem deve ser o primeiro, pois é o mais recente
    Os links com as devoluções podem ser acessados, e possuem no seu escopo, ações que gerenciam o produto

    DETALHE
        A venda cancelada servirá de saldo para uma próxima compra
    """


#
def certificado_digital():
    """
    - SIGNIFICADO -
    Documento homologado pela SEFAZ, que permite o gerenciamento de qualquer documentação fiscal, sendo um requisito
    Se o transportador for o emitente ou destinatário, ele não precisa informar o RNTRC
    """


# MDF-e
def manifesto():
    """
    --------------------------------------------------- SIGNIFICADO ---------------------------------------------------
    - Manifesto de documento fiscal eletrônico (MDF-e)

    ----------------------------------------------------- CONCEITO -----------------------------------------------------
    - Documento emitível que serve como um complemento de uma nota fiscal, para indicar que a nota será submetida a
      transporte de um ponto A para um B

    - Vínculo entre a nota fiscal eletrônica (NF-e) e o (CT-e) conhecimento de transporte eletrônico

    ----------------------------------------------------- DETALHE -----------------------------------------------------
    - Pode ser integrado ao cliente criado pelo portal 'Hiperador', caso contrário, disponível somente no 'Hiper gestão'
      , adquirível na loja de aplicativos

    - Para o seu envio, é necessário um certificado digital do tipo A1

    --------------------------------------------------- PROCEDIMENTO ---------------------------------------------------
    - Ver o método [ def serie_fiscal ], e ao final dos procedimentos, será possível emitir documentos MDF-e

    ---------------------------------------------- CONFIGURANDO UM MDF-e ----------------------------------------------
    dropdown=Fiscal    link=Emitir MDF-e

    ----- Dados gerais -----
    Série                 || [ def serie_fiscal ] referente à [ Código de série fiscal ]
    Número                || [ def serie_fiscal ] referente à [ Sequência ]
    Data de emissão       || data atual
    Hora de emissão       || hora atual
    Tipo do emitente      || prestador e não prestador de serviço
    Tipo do transportador || opcional [ CTC ETC TAC ]
                             CTC = Cooperativa de transporte de cargas
                             ETC = Empresa transportadora de carga
                             TAC = Transportador autônomo de cargas
    Modalidade            || rodoviário ou aquático



    ----- Locais de carregamento -----
    UF do carregamento        || Sigla do estado
    Município de carregamento || Auto explicativo (permitido adição)
    UF do percurso            || Local(is) por onde a carga passará
    UF do descarregamento     || Local de chegada e permanência da carga



    ----- Rodoviário -----
    RNTRC              || Registro Nacional dos Transportes Rodoviários de Cargas
    Placa              ||
    Uf do veículo      ||
    Renavam            || Registro Nacional de Veículos Automotores
    Tipo de rodado     ||
    Tipo de carroceria ||
    Peso bruto         ||



    ----- Dropdown= O proprietário do veículo não é o emitente -----

    Se desmarcado, então preencher os campos
    - CPF
    - Nome do condutor

    Se marcado, então preencher os campos
    - Tipo de pessoa
    - CPF ou CNPJ
    - Razão social/Nome do proprietário
    - Inscrição estadual
    - RNTRC
    - Tipo proprietário
    - UF



    ----- Documentos fiscais -----
    - A explicação não foi satisfatória
    - Podem ser feitas várias notas em sequência, que se agrupam no [ h1=Listagem dos documentos fiscais ]

    NF-e -> Município de descarregamento
    NF-e -> Chave de acesso
    NF-e -> Valor (valor da carga)
    NF-e -> Peso  (peso somente da carga)
    botão=Adicionar



    ----- Totalizadores -----
    - Não foi explicado se os cálculos nos campos foram feitos automaticamente
    - Ao preencher todos os campos, clicar em [ Salvar alterações ]

    Valor total da carga ||
    Unidade de medida    ||



    ----- SEGURO -----
    Responsável pelo seguro ||
    Tipo de pessoa          ||
    CNPJ do emitente        ||
    Número da apólice       ||
    CNPJ da seguradora      ||
    Seguradora              ||



    Ao final, clicar no [ botão=Adicional ] e em seguida [ botão=Emitir MDF-e ]



    -------------------------------------------- CONFIGURAÇÕES POSTERIORES --------------------------------------------
    dropdown=Fiscal    h1=Documentos fiscais    link=Documentos fiscais    Acessar o MDF-e gerado

    Clicar no botão de ações do MDF-e no canto direito da tela, e preencher as abas: Adicionar condutor
                                                                                     Cancelar MDF-e
                                                                                     Encerrar MDF-e

    EXPLICAÇÕES
        Adicionar condutor = É comum haver troca de condutores durante viagens muito longas
        Cancelar MDF-e     = Descrever o motivo do cancelamento e enviar
        Encerrar MDF-e     = Preencher para informar a chegada da carga ao seu destino e a finalização do transporte
                             Preencher para, caso este seja o caso, zerar e renovar um novo transporte com um mesmo
                             veículo

    ------------------------------------------------------ ERROS ------------------------------------------------------
    173 - Chave de comunicação inválida (Inscrição estadual com caracteres especiais)
    215 - Emissão de MDF-e rejeitada pelo emitente não possuir uma 'inscrição estadual'
    580 - Emissão de MDF-e, não sendo o transportador o emitente ou destinatário (contrato de um 3o sem RNTRC achado pelo CPF)
    611 - Quando não ocorre o encerramento definitivo de uma MDF-e
    """


# Explicação pendente
def serie_fiscal():
    """
    ----------------------------------------------------- CAMINHO -----------------------------------------------------
    dropdown=Configurações    h1=Fiscal    link=Série Fiscal    botão=Nova série fiscal

    ---------------------------------------------- CAMPOS (interpretação) ----------------------------------------------
    CNPJ                       = referente ao da filial que emitirá o MDF-e
    Código da série fiscal     = consultar contador
    Sequência                  = consultar contador
    Modelo do documento fiscal = MDF-e ou Nota fiscal eletrônica
    Sistema                    = Gestão

    - PROCEDIMENTO -
    Preencher os campos necessários e clicar no botão [ Salvar série fiscal ]
    """


#
def tabela_preco():
    """
    ------------------------------------------------------ FONTE ------------------------------------------------------
    https://www.youtube.com/watch?v=ZTot8IlUodk

    ----------------------------------------------------- CAMINHO -----------------------------------------------------
    Dropdown=Cadastros    Link=Importação    Link=Importar tabela de preço (formato .csv)
    """
