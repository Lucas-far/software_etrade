

"""
Aceita quantidade fracionada (checkbox): produtos em KG, L, M
A partir de: [ estoque/produtos/promoção ] quantidade inicial para validar a promoção
CFOP
CFOP 5405 = substituição
CEST: possui consulta no Etrade (estoque/produtos/buscar/configurações do produto)
Classe de imposto: Isento
Classe de imposto: Tributado
Classe de imposto: Substituição tributária
CNM
EAN
Exportar para balança: para mercados e supermercados
Inativo: em [ estoque/produtos ] significa desabilitar o produto da tabela de vendas
Operações (ex: 500 = venda)
Qtde. Máx: [ estoque/produtos/promoção ] quantidade limite para manter a promoção
SEFAZ
Serviço de contingência
Tabela de custos
Tabela de custo médio
Tributação

Qual a diferença entre tabela de preço e tabela de custo?
"""


def atacarejo():
    """
    ------- CONCEITO -------
    Mistura das modalidades atacado com varejo

    ------- CONTEXTUALIZAÇÃO -------
    Ao levar uma quantidade x de itens do varejo, ganha-se desconto de atacado
    EX: Compre 3 sacos de arroz e leve um de feijão
    EX: Compre 3 sacos de arroz e e o quarto é gratuito
    """


# Verificar dados de lucro ou deficit
def calendario_financeiro():
    """
    https://youtu.be/99ku9Fml5UQ

    ----------------------------------------------------- CAMINHO -----------------------------------------------------
    dropdown=Financeiro    link=Calendário    janela=Calendário de contas

    ----------------------------------------------------- DETALHE -----------------------------------------------------
    - Ao fazer o caminho, a janela padrão aberta já é a referente ao botão [ Aberto ]

    ------------------------------------------------------ BOTÕES ------------------------------------------------------
    Compotência
        Consulta o bdd de venda e fornece dados: [ Ticket médio de venda ] [ Quantidade ] [ Lucro do dia ]
        Por duplo clique, fornece informações sobre quais meios o [ lucro ] ou [ deficit ] aconteceram (ex: dinheiro, cartão)

    Aberto
        Fluxo de caixa não quitado (em aberto, tanto para pagar quanto para receber)

    Quitado
        Fluxo de caixa quitado (o que já aconteceu, o que pagou e recebeu)

    --------------------------------------------- LEGENDAS SOBRE OS DADOS ---------------------------------------------
    [ azul ou vermelho ] Saldo positivo ou negativo
    [ verde ]            Valor recebido
    [ vermelho ]         Valor Pago

    ------------------------------------------------------- OBS -------------------------------------------------------
    - Foi recomendado no vídeo que o uso dessa utilidade seja feita por um gestor
    """


# Setup para ligamento da máquina
def computador_setup():
    """
    - Verificar a voltagem (saber se a voltagem nas tomadas é 110V ou 220V)
    - Ajustar o botão vermelho na traseira do gabinete (115V ou 220V no painel)

    ------------------------------------------------------ SETUP ------------------------------------------------------
    - Entradas USB (Mouse, Teclado)
    - Cabo de energia/alimentação
    - Cabo de vídeo (VGA) [ Video graphic adaptor ]
    - Cabo de rede
    - Com esses componentes, a máquina está apta a ser ligada
    """


def ean():
    """
    EAN = Numeração Européia de Artigos (sequência numérica de 13 dígitos)

    EAN = Sintaxe construída apartir dos dados:

          país de origem,    [ dígitos: 3       ] (3 primeiros dígitos) (ex: Brasil= 789, 790)
          fabricante         [ dígitos: 4 até 6 ]
          modelo do produto  [ dígitos: 3 até 5 ]
          dígito verificador [ dígitos: 1       ]
    """


# Setup para configurar um ip fixo em um PC
def computador_cofigurar_ip_fixo():
    """
    ----------------------------------------------------- PARTE 1 -----------------------------------------------------
    - Botão direito no ícone de internet na área de trabalho, selecionar [ Abrir configurações de rede e internet ]
    - Clicar em [ Alterar opções de adaptador ]
    - Será aberta uma janela de conexões de rede

    ----------------------------------------------------- DETALHE -----------------------------------------------------
    - Para que um PC tenha ip fixo, é preciso saber qual ip a máquina capturou ao conectar o cabo de rede
    - Se a máquina está com ip automático, quem fornecerá o IP é o: [ roteador/switch/hub ]
    - No windows, a configuração já vêm automático para gerar endereços (ver a parte 3)

    ----------------------------------------------------- PARTE 2 -----------------------------------------------------
    - Botão direito no ícone de rede com um cabo e selecionar [ status ]
    - Clicar no botão [ detalhes ]
    - Todos os endereços da máquina estão contidos nesse painel, e alguns deles servirão de referência para configuração

    ----------------------------------------------------- PARTE 3 -----------------------------------------------------
    - Fechar as janelas abertas na parte 2
    - Botão direito no ícone de rede com um cabo e selecionar [ propriedades ]
    - Na aba [ rede ], na segunda [ div ], selecionar o item [ Protocolo TCP/IP Versão 4 ] e no botão [ propriedades ]
    - Na primeira div, selecionar o checkbox [ Usar o seguinte endereço IP ]
    - Preencher os campos [ Endereço IP ] [ Máscara de sub-rede ] [ Gateway padrão ] com os dados disponíveis na [ parte 2 ]
    - Ao clicar no botão [ OK ], a conexão passará por uma verificação, e se há uma conexão, o ícone de internet mudará
    - Os ícones possíveis que eu conheço: [ monitor ] [ traços de faixa de sinal ]

    ----------------------------------------------------- DETALHES -----------------------------------------------------
    - Na mesma janela aberta na parte 3, há uma div referente aos dados citados abaixo, e sua configuração é opcional
    - Endereço de IP na Marko: [ 192.168.50.17/18/19 ]
    - Servidor DNS: [ preferencial = 8.8.8.8 ] [ alternativo = 8.8.4.4 ]
    """


# Configuração de uma validade para alteração de orçamentos
def orcamento_data_para_modificar():
    """
    Recalcular preço ao carregar movimento na tela de saídas e validade para orçamento (comercial)     [ Item 154 ]
    https://vrsystem.info/publico/post.aspx?Id=70e42581-cd45-4c15-be86-cbbd1025df8c
    https://youtu.be/mlKn0lXNvJc

    ----------------------------------------------------- OBJETIVO -----------------------------------------------------
    - Configurar um período padrão (em dias) para que um orçamento sofra alterações (caso um produto tenha alterado o
      preço e esteja incluso nesse orçamento) e caso a compra não seja imediata

    ----------------------------------------------------- CAMINHO -----------------------------------------------------
    dropdown=Comercial    link=Saídas    aba=Saídas    botão=Saídas    botão=configurar
    janela=Configurar tela de saída

    aba=Produto    checkbox=Recalcular o preço dos produtos ao carregar o movimento    input=Validade (em dias)
    botão=confirmar

    ---------------------------------------------------- EXPLICAÇÃO ----------------------------------------------------
    - O [ input=Validade ] é diretamente relacionado ao [ checkbox=Recalcular o preço dos produtos ao carregar o movimento ]
    - O [ input=Validade ] pode ser explicado através do seguinte contexto:

        Supondo que a validade foi configurada para 5 dias.
        O cliente fez um orçamento, mas não efetuou a compra imediata
        O preço de um produto que está no orçamento foi alterado
        Se o cliente não efetuar a compra na validade configurada, acontecerá um recálculo, mudando o orçamento

    ------------------------------------------- CONSULTAR MANUALMENTE A DATA -------------------------------------------
    dropdown=Comercial    link=Saída    aba=Saídas    botão=Buscar    acessar um ticket por duplo click    janela=Saídas
    botão=Outras opções    link=Verificar informações e totais    aba=Informações

    Procurar pelos campos: [ Data alteração ] [ Preços válidos até ]
    """


# Como fazer um orçamento e gerar um ticket
def orcamento_gerar():
    """
    ----------------------------------------------------- CAMINHO -----------------------------------------------------
    dropdown=Comercial    link=Saídas    aba=Saídas    botão=Saídas

    ------------------------------------------------ CAMPOS NECESSÁRIOS ------------------------------------------------
    [ input ] Operação (consultável via lupa)
    [ input ] Cliente  (consultável via lupa)
    [ input ] Vendedor (consultável via lupa)

    TUTORIAL SOBRE ESTE CAMPO: [ div ] Produtos/Serviços [ input ] Código (consultável via lupa)
    - Clicar na lupa    botão=Buscar ENTER    Selecionar um produto    botão=Selecionar    ENTER/botão=OK

    [ input ] Qtde.

    GERANDO O TICKET
    --------------------------------------------------- PROCEDIMENTO ---------------------------------------------------
    botão=Gravar    Fechar a janela    botão=Buscar    O ticket gravado deve ser exibido
    """


# Cadastrar um produto
def produto_cadastrar():
    """
    --------------------------------------- NOMEMCLATURA PARA NOMES DE PRODUTOS ---------------------------------------
    1. O que é?    2. Marca    3. Complemento    4. Informações métricas (opcional)
    EX: BICICLETA KALOI ARO 29
    EX: REFRIGERANTE COCA-COLA DIET 200ML

    ----------------------------------------------------- CAMINHO -----------------------------------------------------
    dropdown=Estoque    link=Produtos    aba=Produtos    botão=Novo

    ---------------------------------------------- CAMPOS MAIS FREQUENTES ----------------------------------------------
    Básico, Adicionais, Balança

    --------------------------------------------- OUTROS CAMPOS RELEVANTES ---------------------------------------------
    Promoção, Relacionados

    ------------------------------------ CAMPOS MAIS FREQUENTES (CAMPOS RELEVANTES) ------------------------------------
    1. [ Básico     ]    Principal    EAN    Unidade    Imposto    NCM
    2. [ Adicionais ]    Aceita quantidade fracionada    Utiliza mais de 2 casas decimais
    3. [ Balança    ]    Exportar para balança

    1. EAN e NCM são dados consultáveis
    2. para produtos em KG, L, M
    3. para mercados e supermercados

    --------------------------------------------------- PROCEDIMENTO ---------------------------------------------------
    - Ao fazer todas as configurações pertinentes, clicar no botão [ Salvar ]
    """


# Customizar campos de exibição dos produtos
def produto_campos_editar():
    """
    ----------------------------------------------------- CAMINHO -----------------------------------------------------
    dropdown=Estoque    link=Produtos    aba=Produtos    botão=Configurar    janela=Configurar busca de produtos
    aba=visualização    link=clique aqui para incluir

    ------------------------------------------------------ CAMPOS ------------------------------------------------------
    Pos || (int) posição do campo na tabela de produto
    Tam || (int) largura do retângulo do campo
    A   || alinhamento do conteúdo para <- ou ->, representado pelos valores D e E

    -------------------------------------------------- PROCEDIMENTOS --------------------------------------------------
    Preencher os campos e clicar no botão [ Confirmar ]
    É provável que no layout [ Produtos ] seja necessário usar o botão [ Buscar ] para ver as alterações
    """


#
def produto_criar_relacionamento():
    """
    ----------------------------------------------------- DETALHE -----------------------------------------------------
    - Ao relacionar produtos, fica implícito que eles tenham o mesmo preço
    - Muito provavelmente, a criação de relacionamentos visa contextos como:
        PROMOÇÃO DE PRODUTOS IGUAIS, MAS DE TIPOS DIFERENTES (SABORES, ESSENCIAS)
        KIT (ex: cesta básica)

    ----------------------------------------------- CRIAR RELACIONAMENTO -----------------------------------------------
    dropdown=Estoque    link=Produtos    buscar um produto (ex: carne)    acessar o produto por duplo clique
    aba=Relacionados    input=Produto relacionado (ex: carne)    botão=Lupa (Buscar registro)
    janela=Busca de produtos/serviços

    --------------------------------------------------- PROCEDIMENTO ---------------------------------------------------
    RELACIONAMENTO 1 PARA 1
    Selecionar um produto     botão=Selecionados    botão=Salvar

    RELACIONAMENTO 1 PARA MUITOS
    Selecionar pelo (ctrl + mouse) os produtos que quiser relacionar    botão=Selecionados    botão=Salvar
    """


# Inserir um produto para ter um preço dentro de uma tabela específica
def produto_inserido_tabela():
    """
    ----------------------------------------------------- DETALHE -----------------------------------------------------
    - Ver [ tabela_preco ]

    ----------------------------------------------------- CAMINHO -----------------------------------------------------
    dropdown=Estoque    link=produto    botão=buscar    Acessar um produto por duplo clique
    janela= Cadastro de produto

    --------------------------------------------------- PROCEDIMENTO ---------------------------------------------------
    div=Tabela    Selecionar a tabela    campo=Preço    botão=Salvar
    """


# Diferenças entre: [ promoção atacarejo a partir ] vs [ promoção atacarejo a cada ]
def produto_promocao():
    """
    ---------------------------------------------------- CONTEXTO 1 ----------------------------------------------------
    CONTEXTO       || Aracarejo, a partir de
    PRODUTO        || Coca Cola
    PREÇO DE VENDA || R$ 2,00

    ABA            || Promoção
    DROPDOWN       || Tipo (Atacarejo - a partir de...)

    INPUTS
    [ input=A partir de ] = 3   || quantidade inicial para validar a promoção
    [ input=Qtde. Máx   ] = 5   || quantidade limite para manter a promoção
    [ input=Desconto    ] = 10% ||

    NOS EXEMPLOS ABAIXO, OS DADOS ENTRE CHAVES SÃO RESPECTIVAMENTE: qtd_prod &

    _____________________________________________________ 3 COCAS _____________________________________________________
    [ 3 = 3 ] [ {3} x {2} = 6 x 10/100 = 0,60 ] [ 6 - 0,80 = 5,40 ]
    São 3 cocas, a promoção se aplica a partir de 3
    TOTAL: 5,40

    _____________________________________________________ 4 COCAS _____________________________________________________
    [ 4 > 3 ] [ {4} x {2} = 8 x 10/100 = 0,60 ] [ 8 - 0,80 = 7,20 ]
    São 4 cocas, a promoção se aplica a partir de 3
    TOTAL: 7,20

    _____________________________________________________ 5 COCAS _____________________________________________________
    [ 5 > 3 ] [ {5} x {2} = 10 x 10/100 = 1,00 ] [ 10 - 1,00 = 9,20 ]
    São 5 cocas, a promoção se aplica a partir de 3
    TOTAL: 7,20

    QUANDO A QUANTIDADE EXCEDE
    _____________________________________________________ 6 COCAS _____________________________________________________
    [ 6 > 3 ] [ {6} x {2} = 12 ] é aplicado a subtração refere ao da qtd. máxima (que é 5)
    Então [ 12 - 1,00 ] (que é desconto de 5)
    São 6 cocas, a promoção não se aplica totalmente, mas se aplica até a qtd. máxima (que é 5)
    TOTAL: 11,00

    _____________________________________________________ 7 COCAS _____________________________________________________
    [ 7 > 3 ] [ {7} x {2} = 14 ] é aplicado a subtração refere ao da qtd. máxima (que é 5)
    Então [ 14 - 1,00 ] (que é desconto de 5)
    São 7 cocas, a promoção não se aplica totalmente, mas se aplica até a qtd. máxima (que é 5)
    TOTAL: 13,00





    ---------------------------------------------------- CONTEXTO 2 ----------------------------------------------------
    CONTEXTO       || Atacarejo a cada...
    PRODUTO        || Coca Cola
    PREÇO DE VENDA || R$ 2,00
    ABA            || Promoção
    DROPDOWN       || Tipo (Atacarejo - a cada...)

    INPUTS
    [ input=A cada    ] = 3   || quantidade inicial para validar a promoção
    [ input=Qtde. Máx ] = 2   || quantidade de repetições que a promoção pode ser aplicada
    [ input=Desconto  ] = 10% ||

    CONTEXTO PARA EXPLICAR OS VALORES ACIMA
    [ input=A cada    ] = 3...Se a promoção é engatilhada a cada 3 produtos
    [ input=Qtde. Máx ] = 2...Se a sua aplicação só pode se repetir até 2 vezes
    Então é aplicada ao máximo de 6 produtos, pois se chegar a 9, seria sua 3a aplicação, quando o permitido é somente 2

    NOS EXEMPLOS ABAIXO, OS DADOS ENTRE CHAVES SÃO RESPECTIVAMENTE: qtd_prod. & qtd_máx_promo

    _____________________________________________________ 3 COCAS _____________________________________________________
    [ 3 = 3 ] [ {3} x {2} = 6 x 10/100 = 0,60 ] [ 6 - 0,80 = 5,40 ] Primeiro é aplicado em 3
    Como são 3 cocas, o cálculo é feito a cada 3, então todos entraram na promoção
    TOTAL: 5,40
    _____________________________________________________ 4 COCAS _____________________________________________________
    [ 3 < 4 ] [ {3} x {2} = 6 x 10/100 = 0,60 ] [ 6 - 0,80 = 5,40 ] Primeiro é aplicado em 3
    - São 4 cocas, o cálculo é feito a cada 3, então 1 ficau fora da promoção, é somada com seu preço normal
    TOTAL: 5,40 + 2,00 = 7,40
    _____________________________________________________ 5 COCAS _____________________________________________________
    [ 3 < 5 ] [ {3} x {2} = 6 x 10/100 = 0,60 ] [ 6 - 0,80 = 5,40 ] Primeiro é aplicado em 3
    - São 5 cocas, o cálculo é feito a cada 3, então 2 ficam fora da promoção, são somadas com seus preços normais
    TOTAL: 5,40 + 4,00 = 9,40
    _____________________________________________________ 6 COCAS _____________________________________________________
    [ 3 < 6 ] [ {3} x {2} = 6 x 10/100 = 0,60 ] [ 6 - 0,80 = 5,40 ]    Primeiro é aplicado em 3
    [ 3 < 6 ] [ {3} x {2} = 6 x 10/100 = 0,60 ] [ 6 - 0,80 = 5,40 ]    Depois em +3
    TOTAL: 10,80
    _____________________________________________________ 7 COCAS _____________________________________________________
    [ 3 < 7 ] [ {3} x {2} = 6 x 10/100 = 0,60 ] [ 6 - 0,80 = 5,40 ]    Primeiro é aplicado em 3
    [ 3 < 7 ] [ {3} x {2} = 6 x 10/100 = 0,60 ] [ 6 - 0,80 = 5,40 ]    Demais é aplicado em 3
    - São 7 cocas, o cálculo é feito a cada 3, então 1 ficou fora da promoção, é somada com seu preço normal
    TOTAL: 5,40 + 5,40 + 2,00 = 12,80
    """


# Customizar campos de exibição de tickets (impressão também)
def ticket_campos_editar():
    """
    ----------------------------------------------------- CAMINHO -----------------------------------------------------
    dropdown=Comercial    link=Saídas    aba=Saídas    botão=Configurar    janela=Configurar tela de saídas
    aba=Visualização    texto=Clique aqui para incluir

    ------------------------------------------------------ CAMPOS ------------------------------------------------------
    CAMPOS DE PREENCHIMENTO
    Pos   || ordem de surgimento do campo na tabela
    Campo || Campo a ser incluído na tabela
    Tam   || Largura do frame do campo (90 parece bom)
    A     || alinhamento do texto do campo

    OPÇÕES DE COLUNA
    Movimento - Data    Movimento - Sequência    Cliente - Nome    Movimento - Total Final
    Ticket impresso - Data hora da impressão    Ticket impresso - Funcionário código    Ticket impresso - Impressão

    -------------------------------------------------- PROCEDIMENTOS --------------------------------------------------
    Preencher os campos e clicar no botão [ Confirmar ]
    """


# Download de tickets
def ticket_download():
    """
    dropdown=Comercial, link=Saídas, botão=Buscar
    -----> Acessar algum dos tickets por duplo clique ]
    janela=Saídas, botão=Ticket
    -----> O ticket selecionado será baixado
    """


# Criar uma tabela de preço
def tabela_preco():
    """
    ----------------------------------------------------- CAMINHO -----------------------------------------------------
    dropdown=Estoque    link=Produtos    aba=Preço    botão=Tabela    aba=Tabela de preço    botão=Nova

    ------------------------------------------------------ CAMPOS ------------------------------------------------------
    [ input    ] Nome                  [ recomendável ]
    [ input    ] Margem                [ recomendável ]
    [ checkbox ] Tabela de custo       []
    [ checkbox ] Tabela de custo médio []
    [ checkbox ] Inativo               []

    EXPLICAÇÃO:
        É importante determinar uma margem quando for fazer uma entrada de nota fiscal, pois quando esse produto subir
        de preço, o sistema vai automaticamente pegar o seu preço de custo, colocar a margem que você quer, e determinar
        um novo preço de venda

    -------------------------------------------------- PROCEDIMENTOS --------------------------------------------------
    Preencher os campos e clicar no botão [ Salvar ]

    ------------------------------------------------------ BOTÕES ------------------------------------------------------
    Voltar        ||
    Editar        || reconfigurar atributos da tabela (nome, tipo...)
    Apagar        ||
    Tabela padrão || para criação de uma tabela de custo
    """


# Criar uma tabela de custo
def tabela_custo():
    """
    https://www.youtube.com/watch?v=-hMrSUrX8AA
    Configurar tabelas de preços de custo padrão no sistema (estoque)     [ Item 114 ]
    https://vrsystem.info/publico/post.aspx?Id=31c6590d-385f-47f5-a7d7-5650b2b284a9

    ------------------------------------------------- OBJETIVO DE USO -------------------------------------------------
    - Clientes com várias filiais que precisam que haja um preço para cada filial

    ----------------------------------------------------- DETALHE -----------------------------------------------------
    - Filiais diferentes podem compartilhar da mesma tabela, por exemplo, elas estando próxima uma da outra, podem
      compartilhar do mesmo preço de custo

    ----------------------------------------------------- CAMINHO -----------------------------------------------------
    dropdown=Estoque    link=Produtos    aba=preço    botão=tabela    botão=tabela padrão
    janela=Configuração tabela de custo padrão

    ------------------------------------------------------ LAYOUT ------------------------------------------------------
    [ input    ] Filial (seleção de uma ou + tabelas já criada) (só haverá + de uma opção se uma tabela nova tiver sido
                         criada pelo [ botão=Nova ] e configurada como [ tabela de custo ])

    [ dropdown ] Custo    (não sei)
    [ dropdown ] C. médio (não sei)
    [ botão    ] Salvar
    """


# Desativar/Esconder uma tabela (preço/custo)
def tabela_desabilitar():
    """
    ----------------------------------------------------- CAMINHO -----------------------------------------------------
    dropdown=Estoque    link=Produtos    aba=preço    botão=Tabela    selecionar uma tabela    botão=Editar
    dropdown=Inativo    botão=Salvar

    --------------------------------------------------- PROCEDIMENTO ---------------------------------------------------
    - Ao acessar qualquer produto, a tabela não deve estar presente
    """


# Treinamento sobre Hiper
def treinamento():
    """
    Hiper caixa (web app)

    Certificado digital
    Impressora configurada

    Cadastro simplificado não é recomendado
    A SEFAZ exige para cupons eletrônicos e notas fiscais: CPF ou CNPJ
        Esse cadastro não oferece esses campos, e caso seja gerada uma nota fiscal, ele não terá essas informações em
        qualquer nota que venha a ser tirada em suas compras
    """
