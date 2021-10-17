

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


def atacarejo_infos():
    """
    ----------------------------------------------------- CONCEITO -----------------------------------------------------
    Mistura das modalidades atacado com varejo

    ------------------------------------------------- CONTEXTUALIZAÇÃO -------------------------------------------------
    Ao levar uma quantidade x de itens do varejo, ganha-se desconto de atacado
    Para saber mais, ver o método [ produto_promocao ]
    """


# Verificar dados de lucro ou deficit
def calendario_financeiro():
    """
    ------------------------------------------------------ FONTE ------------------------------------------------------
    Calendário financeiro (financeiro)     [ Item 254 ]
    https://vrsystem.info/publico/post.aspx?Id=167c7aa7-3e50-4caf-ad8d-90576da2bae3
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
    - Foi recomendado que o uso dessa utilidade seja feita por um gestor
    """


# Informações sobre o item: carta de frete (incompleto) (terminar de ver o vídeo do Lenilson)
def carta_frete_infos():
    """
    ----------------------------------------------------- CONCEITO -----------------------------------------------------
    - Documento produzido para mapear as rotas que produtos deverão fazer, devendo seguir toda a rota planejada

    ----------------------------------------------------- DETALHE -----------------------------------------------------
    - Deve vir acompanhada de uma nota fiscal do produto
    """


# Como localizar um CFOP (pendente)
def cfop_localizar():
    """
    --------------------------------------------------- SIGNIFICADO ---------------------------------------------------
    - Certificado Fiscal de Operação (pesquisar)

    ----------------------------------------------------- DETALHE -----------------------------------------------------
    - O vídeo abaixo precisa ser verificado para saber se o CFOP é configurado na criação de uma classe de imposto
        Classe imposto (estoque)     [ Item 11 ]
        https://vrsystem.info/publico/post.aspx?Id=eabd5bfb-9e61-461a-a06a-2e2cdc123c12

    ----------------------------------------------------- CAMINHO -----------------------------------------------------
    dropdown=Estoque    link=Produtos    aba=Impostos    botão=Classe imposto    aba=Classe imposto    botão=Buscar
    acessar um imposto    acessar uma operação    janela=Operações classe de imposto    aba=Geral    input=CFOP
    """


# Setup para ligamento da máquina
def computador_setup():
    """
    ----------------------------------------------------- CUIDADOS -----------------------------------------------------
    - Verificar a voltagem (saber se a voltagem nas tomadas é 110V ou 220V)
    - Ajustar o botão vermelho na traseira do gabinete (115V ou 220V no painel)

    ------------------------------------------------------ SETUP ------------------------------------------------------
    - Cabo de energia/alimentação
    - Cabo de vídeo (VGA) [ Video graphic adaptor ]
    - Cabo de rede
    - Entradas USB (Mouse, Teclado)
    - Com esses componentes, a máquina está apta a ser ligada
    """


# Onde preencher formulário para o contador
def contador_registrar():
    """
    ----------------------------------------------------- DETALHE -----------------------------------------------------
    - O contador é criado juntamente a filial da empresa que usará o Etrade

    ----------------------------------------------------- CAMINHO -----------------------------------------------------
    dropdown=Configurações    link=Filial    aba=Filial    Acessar uma filial    aba=Contador

    --------------------------------------------------- PROCEDIMENTO ---------------------------------------------------
    - Preencher os campos e clicar no botão [ Salvar ]
    """


# Configuração de uma classe de imposto (incompleto)
def imposto_criar():
    """
    ----------------------------------------------------- DETALHES -----------------------------------------------------
    - A questão de impostos é uma tarefa para o contador
    - O que o contador deve saber é onde fica sua parte no software e quais ferramentas estão a sua disposição

    ----------------------------------------------------- CAMINHO -----------------------------------------------------
    dropdown=Estoque    link=Produtos    aba=Impostos    botão=Classe imposto    aba=Classe de imposto    botão=Novo
    """


# Informações relevantes sobre imposto
def imposto_infos():
    """
    - Há normalmente 2 tipos de imposto básicos     || Tributado, Substituição tributária
    - Há normalmente 2 tipos de impostos tributados || Regime simples, regime normal
    - Imposto do tipo substituição tributária       || Compra que já foi paga com os impostos embutidos
    - Imposto do tipo tributado                     || Compra cujos impostos são pagos ao fim do mês
    - Isento                                        || Quando não há impostos

    - Um imposto tributado em regime normal, leva diferentes níveis de porcentagem (12%, 25%)
    - Um produto tributado em regime normal, pode possuir porcentagens variadas, e para cada porcentagem, uma classe de
      imposto deve ser criada

    - A tributação é algo que não deve ser feita pelas técnicos, mas pelos contadores, porém é preciso que eles saibam
      onde estão os recursos pertinentes

    ------------------------------------------------ SEFAZ (aliquotas) ------------------------------------------------
    - Tributação em regime simples: Para impresas que lucram abaixo de 100.000 (alíquota única)
    - Tributação em regime normal: Para impresas que lucram acima de 100.000
    - Em regime simples, independente do produto possuir demais tributações, o SEFAZ ignora e aplica somente a
      tributação simples
    - Em regimes normais, a tributação varia de porcentagem de acordo com o produto, podendo então gerar várias classes
      de impostos
    - Quando uma empresa começa a lucrar próximo ao regime normal, os donos tendem a criar outro CNPJ para evitar a
      transição de regimes

    ----------------------------------------------------- CAMINHO -----------------------------------------------------
    OBS: Na janela de criação não aparecem os mesmos campos de filiais já configuradas
    OBS: Sendo assim, abaixo será descrito o caminho para consultar o [ regime ] de uma filial

    dropdown=Configurações    link=Filial    aba=Filial    botão=Nova   Acessar uma filial    aba=Adicionais
    dropdown=Regime

    -------------------------------------------------- FONTE PENDENTE --------------------------------------------------
    Regime especial (configurações)     [ Item 359 ]
    https://vrsystem.info/publico/post.aspx?Id=e352b7c1-d292-4e7b-b09c-446124f2374d
    """


# Setup para configurar um ip fixo em um PC
def computador_configurar_ip_fixo():
    """
    ----------------------------------------------------- PARTE 1 -----------------------------------------------------
    - Botão direito no ícone de internet na área de trabalho, selecionar [ Abrir configurações de rede e internet ]
    - Clicar em [ Alterar opções de adaptador ]
    - Será aberta uma janela de conexões de rede

    ----------------------------------------------------- DETALHE -----------------------------------------------------
    - Para que um PC tenha ip fixo, é preciso saber qual ip a máquina capturou ao conectar o cabo de rede com um
      aparelho de rede (modem, switch, hub), que são os provedores
    - No windows, a geração de um IP já vêm automático para gerar endereços (ver a parte 3)

    ----------------------------------------------------- PARTE 2 -----------------------------------------------------
    PONTO DE REFERÊNCIA: Alterar opções de adaptador

    - Botão direito no ícone de rede que possui um ícone de um cabo de rede, e selecionar [ status ]
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
    - Servidor DNS:            [ preferencial = 8.8.8.8 ] [ alternativo = 8.8.4.4 ]
    """


#
def entrada_infos():
    """
    - A parte de entradas do Etrade é movida por operações
    - A quantidade de operações pode ser customizada, de acordo com o que o contador achar melhor

    -------------------------------------------- CRIACÃO DE NOVAS OPERAÇÕES --------------------------------------------
    Dropdown=Configurações    link=Operação    botão=Nova
    """


# Recursos relacionados ao Etrade
def etrade_infos():
    """
    - O Etrade possui dois softwares para saída, sendo eles: Etrade próprio, PDV
    - O etrade é recomendável para locais onde as compras são mais caras e lentas
    - O PDV é recomendável para quaisquer compras rápidas (caixas de supermercado)
    """


#
def filial_criar():
    """
    ----------------------------------------------------- DETALHE -----------------------------------------------------
    - O campo de CEP, pela lupa, complementa outros campos

    -------------------------------------- [ aba=Endereço ] - campos em destaque --------------------------------------
    input=Nome    input=Fantasia    input=Razão Social    input=CNPJ    dropdown=Tipo IE    input=I.E
    input=Endereço + número    input=Bairro    input=Cidade    input=UF    input=CEP    input=Telefone

    ------------------------------------- [ aba=Adicionais ] - campos em destaque -------------------------------------
    dropdown=regime

    -------------------------------------- [ aba=Contador ] - campos em destaque --------------------------------------
    - Basicamente todos os campos
    """


# Diferenças entre tipos de nota fiscal
def nota_fiscal_infos():
    """
    Nota fiscal eletrônica (NF-e)                || nota fiscal grande (CNPJ) (transporte mecânico)
    Nota fiscal do consumidor eletrônica (NFC-e) || nota fiscal de bobina (CPF) (transporte humano)
    Carta de frete (CF-e)                        || ver a função [ carta_frete ]

    ----------------------------------------------------- DETALHE -----------------------------------------------------
    - A geração da nota também serve para provar que algo é seu, em caso de roubo

    ----------------------------------------------------- CAMINHO -----------------------------------------------------
    dropdown=Comercial    link=Saídas    aba=Saídas    botão=Saída    abas=NF-e/NFC-e/CF-e/NFS-e

    ------------------------------------------------- FONTES PENDENTES -------------------------------------------------
    Nota fiscal referenciada (comercial)     [ Item 171 ]
        https://vrsystem.info/publico/post.aspx?Id=72c6d24e-5939-4df7-9c43-803f6e815deb

    Campo de UF e Cidade na nota avulsa do MDFe (comercial)     [ Item 198 ]
        https://vrsystem.info/publico/post.aspx?Id=aac88f7a-a32f-4d65-aded-4a2093060d77

    Informe peso dos produtos para emissão de nota (comercial)     [ Item 205 ]
        https://vrsystem.info/publico/post.aspx?Id=b4a1e182-74a0-46bd-ae4d-09da7a33892b

    Emissão de nota com informação de pedido (comercial)     [ Item 219 ]
        https://vrsystem.info/publico/post.aspx?Id=47d2d200-3a12-43a8-b007-cb9483e7b4b1

    Teste nota (comercial)     [ Item 220 ]
        https://vrsystem.info/publico/post.aspx?Id=b99522a3-021a-4e49-bdf0-f3208aa535f0

    Como enviar nota para o exterior (comercial)     [ Item 222 ]
        https://vrsystem.info/publico/post.aspx?Id=d6b8b173-13f5-4945-86e5-108bbd896d0e

    Como gerar nota de devolução importando XML do fornecedor (comercial)     [ Item 224 ]
        https://vrsystem.info/publico/post.aspx?Id=284e7b45-dcdc-4f2e-9280-6bd0e8ee6cea

    Inutilização de nota fiscal avulsa (comercial)     [ Item 236 ]
        https://vrsystem.info/publico/post.aspx?Id=e6765c6d-3ce3-48e0-bbb6-c9b9ad096b7a

    Explicando particularidades no envio da nota (configurações)     [ Item 395 ]
        https://vrsystem.info/publico/post.aspx?Id=fbe40ab7-3152-40ab-80a0-8eb5ec4163f2

    Particularidades por Estado no Envio de Nota Fiscal (configurações)     [ Item 413 ]
        https://vrsystem.info/publico/post.aspx?Id=598518c9-b1ef-4d27-bfa5-8d147f4c2fba

    Emissão de nota em Homologação (outros)     [ Item 532 ]
        https://vrsystem.info/publico/post.aspx?Id=8f3b1cf5-4dab-4175-9cb5-633ea005cb8d
    """


#
def nota_fiscal_referenciar():
    """
    Nota fiscal referenciada (comercial)     [ Item 171 ]
        https://vrsystem.info/publico/post.aspx?Id=72c6d24e-5939-4df7-9c43-803f6e815deb
        https://youtu.be/2gqUX0unjHM

    ----------------------------------------------------- CONTEXTO -----------------------------------------------------
    - Adicionar várias notas referenciadas (podendo ser diferentes) na tela de saída

    ----------------------------------------------------- CAMINHO -----------------------------------------------------
    dropdown=Comercial    link=Saídas    aba=Saídas    botão=Saída    Preencher Operação, Vendedor, Cliente
    Preencher o campo Código na div Produtos/Serviços    botão=Outras opções + Doc. referenciado

    PARADA: 3:00
    MOTIVO: Chave de homologação (não sei como gerar uma)
    """


# Informações relevantes sobre Operações
def operacao_infos():
    """
    - Operações possuem classificação: interna e externa (respectivamente dentro e fora do estado naquele país)
    - Cada operação possui um CFOP diferente

    - Operações podem ser semelhantes tanto em valor, quanto em códigos de impostos (ICMS, PIS, COFINS),
      seus CFOPS serão diferentes, ou seja:

      ---------------------------------------------------------------------------
      Se eu moro no PI, a operação para vendas é 500, mas o CFOP é 5102
      Se eu moro em outro estado, a operação para vendas é 500, mas o CFOP é 6102
      ---------------------------------------------------------------------------

    - Quando é feita uma venda, a SEFAZ é acionada, tomando por base a operação, então captura os impostos vinculados a
      ela, além de consultar a classe de imposto em cada produto

      ------- EXEMPLO -------
      Se a operação for venda (500) então ela possui impostos como: ICMS PIS CONFIS, podendo ser tributado de regime
      simples/normal
    """


# Configuração de uma validade para alteração de orçamentos
def orcamento_data_para_modificar():
    """
    ------------------------------------------------------ FONTES ------------------------------------------------------
    Recalcular preço ao carregar movimento na tela de saídas e validade para orçamento (comercial)     [ Item 154 ]
    https://vrsystem.info/publico/post.aspx?Id=70e42581-cd45-4c15-be86-cbbd1025df8c
    https://youtu.be/mlKn0lXNvJc

    ----------------------------------------------------- OBJETIVO -----------------------------------------------------
    - Configurar um período padrão (em dias) para que um orçamento sofra alterações (caso um produto tenha alterado o
      preço e esteja incluso nesse orçamento) e caso a compra não seja imediata

    ----------------------------------------------------- CAMINHO -----------------------------------------------------
    dropdown=Comercial    link=Saídas    aba=Saídas    botão=Saídas    botão=configurar
    janela=Configurar tela de saída    aba=Produto    checkbox=Recalcular o preço dos produtos ao carregar o movimento
    input=Validade (em dias)    botão=confirmar

    ---------------------------------------------------- EXPLICAÇÃO ----------------------------------------------------
    - O [ input=Validade ] é diretamente relacionado ao [ checkbox=Recalcular o preço dos produtos ao carregar o movimento ]
    - O [ input=Validade ] pode ser explicado através do seguinte contexto:

        Supondo que a validade foi configurada para 5 dias, então estou dizendo que este é o prazo para recálculo
        O cliente fez um orçamento, mas não efetuou a compra imediata
        O preço de um produto que está no orçamento foi alterado
        Se o cliente não efetuar a compra na validade configurada, acontecerá um recálculo, mudando o orçamento

    ------------------------------------------- CONSULTAR MANUALMENTE A DATA -------------------------------------------
    dropdown=Comercial    link=Saída    aba=Saídas    botão=Buscar    Acessar um ticket    janela=Saídas
    botão=Outras opções    link=Verificar informações e totais    aba=Informações
    Procurar pelos campos: [ Data alteração ] [ Preços válidos até ]
    """


# Como fazer um orçamento e gerar um ticket (saída)
def orcamento_gerar_editar():
    """
    ----------------------------------------------------- CAMINHO -----------------------------------------------------
    dropdown=Comercial    link=Saídas    aba=Saídas    botão=Saídas

    ---------------------------------------------- ADICIONANDO UM PRODUTO ----------------------------------------------
    input=Operação    input=Cliente    input=Vendedor    div=Produtos/Serviços    input=Código (buscar ou consultar)
    input=Qtde.    botão=OK/Enter

    ------------------------------------------- EDITANDO UM PRODUTO NA SAÍDA -------------------------------------------
    Dropdown=Comercial    link=Saídas    aba=Saídas    botão=Buscar    Selecionar uma saída   botão=Editar
    Selecionar um produto    Clicar no X    Digitar o número da linha do item    botão=OK

    ------------------------------------------------------ SALVAR ------------------------------------------------------
    botão=Gravar
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


# Relacionar produtos para situações específicas
def produto_relacionamento_criar():
    """
    ----------------------------------------------------- DETALHE -----------------------------------------------------
    - Ao relacionar produtos, no Etrade é configurado para que eles tenham o mesmo preço
    - Muito provavelmente, a criação de relacionamentos visa contextos como:
        PROMOÇÃO DE PRODUTOS IGUAIS, MAS DE TIPOS DIFERENTES (SABORES, ESSENCIAS)
        KIT (ex: cesta básica)

    ----------------------------------------------- CRIAR RELACIONAMENTO -----------------------------------------------
    dropdown=Estoque    link=Produtos    buscar um produto (ex: carne)    acessar o produto por duplo clique
    aba=Relacionados    input=Produto relacionado (ex: carne)    botão=Lupa (Buscar registro)
    janela=Busca de produtos/serviços

    TUTORIAL
    input=Produto relacionado = Produto a ser buscado para criar um relacionamento

    --------------------------------------------------- PROCEDIMENTO ---------------------------------------------------
    RELACIONAMENTO 1 PARA 1
    Selecionar um produto     botão=Selecionados    botão=Salvar
    RELACIONAMENTO 1 PARA MUITOS
    Selecionar pelo (ctrl + mouse) os produtos que quiser relacionar    botão=Selecionados    botão=Salvar
    """


# Customizar campos de impressão para Tickets com produtos baseados em dimensões
def produto_dimensoes_ticket():
    """
    ------------------------------------------------------ FONTE ------------------------------------------------------
    Impressão dos campos de dimensões dos produtos (estoque)     [ Item 4 ]
    https://vrsystem.info/publico/post.aspx?Id=833b7098-9bed-4458-bfc5-d75a75e02632
    https://www.youtube.com/watch?v=kVNcieFXJSc

    ----------------------------------------------------- CONTEXTO -----------------------------------------------------
    - Inserir na impressão do ticket campos como largura/altura/profundidade para produtos baseados em dimensão que
      estejam contidos nesse documento

    ----------------------------------------------------- CAMINHO -----------------------------------------------------
    Dropdown=Configurações    link=Impressão e email    botão=Impressão    botão=Buscar    Acessar um ticket
    janela=Configurar layout ticket    aba=Produtos    campos=Movimento Produto - Dimensão altura
                                                                                  Dimensão com nome
                                                                                  Dimensão largura
                                                                                  Dimensão profundidade
    """


# Parada em 00:55 (os gráficos não aparecem, talvez precise de um relatório de movimentação)
def produto_grafico_infos():
    """
    ------------------------------------------------------ FONTE ------------------------------------------------------
    Gráficos cadastro de produtos (estoque)     [ Item 42 ]
    https://vrsystem.info/publico/post.aspx?Id=ade7d884-2419-4c16-a070-7150a01e6d70
    https://www.youtube.com/watch?v=ED0prndnQLw

    ---------------------------------------------- GRÁFICOS DE HISTÓRICO ----------------------------------------------
    dropdown=Estoque    link=Produtos    aba=Produtos    botão=Buscar    Acessar um produto    botão=Histórico

    ---------------------------------------------- GRÁFICOS (outra opção) ----------------------------------------------
    dropdown=Estoque    link=Produtos    aba=Produtos    botão=Buscar    Acessar um produto    aba=Gráficos
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
    ----------------------------------------------------- CAMINHO -----------------------------------------------------
    dropdown=Estoque    link=Produtos    botão=Buscar (ou pesquisar)    Acessar um produto    janela=Cadastro de produto
    aba=Promoção    dropdown=Tipo

    --------------------------------------- EXPLICAÇÃO RESUMIDA: A partir de... ---------------------------------------
    EXEMPLO: Coca cola [ 2,00 ] (preço sem promoção) (unidade)

        A partir de uma certa quantidade de produtos comprada... (ex: 3)
        uma promoção é ativada, aplicando um certo desconto... (ex: 10%)
        até uma certa quantidade máxima de produtos ela será válida... (ex: 5)
        ultrapassando essa quantidade, o desconto da quantidade máxima ainda se aplica... (ex: 5)

    ------- CONTEXTO NÃO SATISFATÓRIO -------
    Coca cola x2 não recebe a promoção, pois é a partir de 3

    ------- CONTEXTO SATISFATÓRIO -------
    Coca cola x3 recebe a promoção, pois já são 3, (3 x 2) * 10/100, fica [ 0.6 ] então [ 6 - 0.6 = 5.40 ]
    Coca cola x4 recebe a promoção, pois já são 3, (4 x 2) * 10/100, fica [ 0.8 ] então [ 8 - 0.8 = 7.20 ]
    Coca cola x5 recebe a promoção, pois já são 3, (5 x 2) * 10/100, fica [ 1.0 ] então [ 10 - 1 = 9.00 ]

    ------- CONTEXTO SATISFATÓRIO MAS EXCEDIDO -------
    Coca cola x6 não recebe a promoção, pois já são 3, mas a qtd. máxima é 5, mas o desconto de 5 ainda aplica
    Então (6 x 2) é subtraída pelo desconto da qtd. máxima (5), que é [ 1.0 ] então [ 12 - 1 = 11.00 ]



    ------------------------------------------ EXPLICAÇÃO RESUMIDA: A cada... ------------------------------------------
    EXEMPLO: Coca cola [ 2,00 ] (preço sem promoção) (unidade)

       A cada quantidade específica (ex: 3)
       Aplicar um desconto específico apenas quando a quantidade específica for satisfeita (ex: 10%)
       Sendo a promoção aplicável uma quantidade repetida de vezes (ex: 2)

    ------- CONTEXTO NÃO SATISFATÓRIO -------
    Coca cola x2 não recebe a promoção, pois é a partir de 3

    ------- CONTEXTO SATISFATÓRIO -------
    Coca cola x3 recebe a promoção, pois já são 3, (3 x 2) * 10/100, fica [ 0.6 ] então [ 6 - 0.6 = 5.40 ]

    ------- CONTEXTO SATISFATÓRIO (COM SOBRA) -------
    Coca cola x4 recebe a promoção, pois já são 3, (3 x 2) * 10/100, então [ 6 - 0.6 = 5.40 ], sobrou 1, [ 5.40 + 2.00 ]
    Coca cola x5 recebe a promoção, pois já são 3, (3 x 2) * 10/100, então [ 6 - 0.6 = 5.40 ], sobrou 2, [ 5.40 + 4.00 ]

    ------- CONTEXTO SATISFATÓRIO (SEM SOBRA) -------
    Coca cola x6 recebe a promoção 2 vezes, pois a promoção é a cada 3
    A fórmula do desconto é aplicada 2 vezes: (3 x 2) * 10/100, então [ 6 - 0.6 = 5.40 ], sem sobras, [ 5.40 + 5.40 ]
    """


# Gerar um relatório de saídas com ou sem filtragem (ex: saídas por cliente, caixa)
def produto_saida_relatorio_movimento():
    """
    ------------------------------------------------------ FONTE ------------------------------------------------------
    Relatório de movimentação saída de produtos (comercial)     [ Item 192 ]
        https://vrsystem.info/publico/post.aspx?Id=1cbc2023-7329-4870-9ec2-7bddcc1dc645
        https://www.youtube.com/watch?v=fdHYci6hUFk

    ---------------------------------------------------- REQUISITO ----------------------------------------------------
    - É necessário que haja uma saída criada, tendo ou não um financeiro

    ----------------------------------------------------- CAMINHO -----------------------------------------------------
    dropdown=Comercial    link=Saídas    aba=Saídas    botão=Outros    dropdown=Movimentos
    janela=Relatórios de movimento

    --------------------------------------------------- CONFIGURAÇÃO ---------------------------------------------------
    dropdown=Tipo (escolher: produto resumido)

    [ aba=Geral ]
    input=Filial    dropdown=Tipo data (filtrar o tipo de exibição)
    dropdown=Atalho (escolher um período de tempo)    Os input de data inicial e final são para datas mais específicas

    [ aba=Avançado ]
    input=Cliente (parece ser o mais prático para filtragem)

    ------- PROCEDIMENTOS -------
    Se todas as configurações pertinentes forem feitas, clicar no botão=Imprimir
    Se tudo estiver certo, um relatório será gerado com as movimentações baseadas em uma filtragem estabelecida
    botão=Imprimir
    """


#
def saida_infos():
    """
    - A parte de saídas do Etrade é movida por operações
    - A quantidade de operações pode ser customizada, de acordo com o que o contador achar melhor

    -------------------------------------------- CRIACÃO DE NOVAS OPERAÇÕES --------------------------------------------
    Dropdown=Configurações    link=Operação    botão=Nova
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
def tabela_preco_criar():
    """
    ------------------------------------------------------- DICA -------------------------------------------------------
    - Uma tabela de preço pode ter utilidade ao querer criar uma promoção, então produtos podem ser selecionados, dados
      apelidos iguais para todos eles, e então todos podem ser chamados na busca e adicionados a tabela de preço alvo

    ----------------------------------------------------- CAMINHO -----------------------------------------------------
    dropdown=Estoque    link=Produtos    aba=Preço    botão=Tabela    aba=Tabela de preço    botão=Nova

    ------------------------------------------------------ CAMPOS ------------------------------------------------------
    CAMPOS RECOMENDADOS
        input=Nome (recomendável)    input=Margem (recomendável)

    CAMPOS OPCIONAIS (criar outros tipos de tabela ou desabilitar uma dos registros de um produto)
        checkbox=Tabela de custo
        checkbox=Tabela de custo médio
        checkbox=Inativo

    EXPLICAÇÃO DURANTE O VÍDEO:
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
    ------------------------------------------------------ FONTE ------------------------------------------------------
    https://www.youtube.com/watch?v=-hMrSUrX8AA
    Configurar tabelas de preços de custo padrão no sistema (estoque)     [ Item 114 ]
    https://vrsystem.info/publico/post.aspx?Id=31c6590d-385f-47f5-a7d7-5650b2b284a9

    ------------------------------------------------- OBJETIVO DE USO -------------------------------------------------
    - Clientes com várias filiais que precisam que haja um preço para cada filial
    - Filiais diferentes podem compartilhar da mesma tabela, por exemplo, elas estando próxima uma da outra, podem
      compartilhar do mesmo preço de custo

    ----------------------------------------------------- DETALHE -----------------------------------------------------
    - Uma tabela de custo serve para controle de preço
    - Uma tabela de custo não deve ser um campo exibível no produto
    - Cada produto tem um preço de custo, que pode ser atualizado (mensalmente)

    ----------------------------------------------------- CAMINHO -----------------------------------------------------
    dropdown=Estoque    link=Produtos    aba=preço    botão=tabela    botão=tabela padrão
    janela=Configuração tabela de custo padrão

    ------------------------------------------------------ CAMPOS ------------------------------------------------------
    input=Filial

    dropdown=Custo
        seleção de uma ou + tabelas já criadas
        só haverá + de uma opção se uma tabela nova tiver sido criada pelo [ botão=Nova ] e configurada como [ tabela de custo ])
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
def treinamento_hiper():
    """
    Hiper caixa (web app)
    Certificado digital
    Impressora configurada
    Cadastro simplificado não é recomendado
    A SEFAZ exige para cupons eletrônicos e notas fiscais: CPF ou CNPJ
        Esse cadastro não oferece esses campos, e caso seja gerada uma nota fiscal, ele não terá essas informações em
        qualquer nota que venha a ser tirada em suas compras
    """


# Algo sobre classe de imposto (não sei a utilidade)
def nao_sei_a_utilidade():
    """
    ----------------------------------------------------- CONTEXTO -----------------------------------------------------
    - Está sendo feita uma operação de venda (500) e é desejado consultar a classe de imposto pelo painel de saída
    - Eu não sei a razão, mas aparentemente, esse aula serve para saber duas coisas:
        Saber os códigos de imposto referente ao estado alvo
        Saber os códigos de imposto referentes a um tipo de operação

    ----------------------------------------------------- CAMINHO -----------------------------------------------------
    dropdown=Comercial    link=Saídas    aba=Saídas    botão=Saída    aba=Opções
    Preencher os valores referentes à: operação, cliente, vendedor
    div=Produtos/Serviços    input=Código    input=Qtde. (opcional)

    --------------------------------------------------- PROCEDIMENTO ---------------------------------------------------
    aba=Outros    botão=Classe imposto    janela=Cadastro classe de imposto
    na barra de pesquisa, digitar a operação (ex: 500)    é exibido

    """


# Parada em 03:40 (não consigo validar um fornecedor, por não ter uma nota fiscal original)
def _():
    """
    Entrada de produtos (estoque)     [ Item 117 ]
        https://vrsystem.info/publico/post.aspx?Id=0f3bb565-5bcd-4a7a-9d17-1d5a60e5aa1c
        https://www.youtube.com/watch?v=YjfGjxTTyDU

    ----------------------------------------------------- CONTEXTO -----------------------------------------------------
    - A mercadoria do fornecedor foi comprada e é desejado dar uma entrada dessa compra dentro do Etrade
    - O fornecedor apresenta um arquivo XML (da nota fiscal de compra) que ao ser referenciado pelo Etrade, retira a
      necessidade de cadastro tanto do produto quanto do fornecedor

    ----------------------------------------------------- CAMINHO -----------------------------------------------------
    dropdown=Estoque    link=Entradas    aba=Entradas    botão=Nova entrada    input=Operação (buscar permitido)
    input=Funcionário    botão=Configurar

    ----------------------------------------------- PROCEDIMENTO PADRÃO -----------------------------------------------
    - A cada entrada criada, configura-se qual o código para localizar os produtos (sua filial ou do fabricante)
    - Configurar também qual código virá na nota fiscal (sua filial ou do fabricante)

    PARA FAZER ISSO, SEGUIR O CAMINHO
    aba=XML    dropdown=Código de busca para listagem (marcar opção pertinente)    botão=Confirmar    botão=Importar XML
    Selecionar um arquivo XML do fornecedor e colar na barra de pesquisa

    ----------------------------------------------------- DETALHE -----------------------------------------------------
    Se na aba=Fornecedor, input=Fornecedor estiver vazio ou inacessível, pode significar:

        O fornecedor ainda não existe no sistema
        O fornecedor existe, mas seus dados cadastrais essenciais podem estar vazios (ex: CNPJ)
    """


def tutorial_duvidas():
    """
    - Na abertura do xml da nota do fornecedor, quando haver campos em branco, você pode adicionar o nome manualmente ou
      precisa usar o botão=Localizar produto?

    - Como funciona a unidade de medida fardo?
    """


def tutorial():
    """
    ------------------------------------------------- É PRECISO SABER -------------------------------------------------
    - Antes de iniciar uma entrada, é preciso que o produto já tenha sido cadastrado
    - Esse vídeo (https://www.youtube.com/watch?v=YjfGjxTTyDU) explica uma automação da instrução 1, mas eu não entendi
    - Isso porque este produto é referenciado com os produtos da nota fiscal importada (para gerar um estoque dele)
    - É melhor que o preço dos produtos seja inserido após fazer o financeiro (parte 3)

    ----------------------------------------------- PARTE 1: HOMOLOGAÇÃO -----------------------------------------------
    REQUISITO:
        ter uma nota fiscal eletrônica de compra com o código de barras ou chave (homologação/certificado digital)

    ETAPAS
    - Abrir o site [ Fsist ], que gera arquivos xml de notas fiscais homologadas (após aprovação da SEFAZ)
    - No site do [ Fsist ], bipar o código de barras ou inserir a chave da nota
    - Solicitar uma consulta
    - O site da [ SEFAZ ] é acionado e a nota precisará ser submetida à uma verificação
    - Se as etapas forem cumpridas, haverá um retorno ao site do [ Fsist ] com a opção de download do cert. digital

    --------------------------------- PARTE 2: ENTRADA DA NOTA DOS PRODUTOS NO ETRADE ---------------------------------
    CAMINHO:
    dropdown=Estoque    link=Entradas    botão=Nova entrada    input=Operação (valor=10)
    input=Fornecedor (ver método fornecedor_criar)    botão=Importar XML    janela=Importar XML da nota de entrada
    botão=Ler xml    Abrir o caminho do arquivo xml gerado na parte 1 ou inserir sua chave    Abrir o arquivo

    OBS:
    - O [ input=Fornecedor ] no Etrade, quando estiver fazendo uma nova entrada, não necessariamente precisa que um
      fornecedor já tenha sido criado, pois pela abertura do xml que foi gerado, através do CNPJ, o Etrade abre uma tela
      de criação do fornecedor com os dados já cadastrados, bastando apenas [ salvar ]

    CONTINUAÇÃO
    aba=Produtos
    Se tudo foi feito corretamente, uma listagem dos produtos da nota deve surgir
    Preencher campos em branco tomando por base o produto do fornecedor (associação)
    Se há campos preenchidos, verificar se a associação está correta

    PROCEDIMENTO PADRÃO PARA A ENTRADA DE PRODUTO
        REFERÊNCIA ATUAL: janela=Importar XML da nota de entrada

        aba=Produtos    Selecionar um produto da lista com nome vazio    botão=Localizar produto
        janela=Busca de produtos/serviços    Pesquisar o produto usando * antes do seu nome
        Selecionar o produto já cadastrado para associá-lo ao da nota    botão=Selecionar    botão=Salvar associações

    DETALHE:
        - O procedimento de associação deve ser repetido entre todos os produtos
        - Na parte inferior esquerda da tela, há um refenciador marcando quantos itens já foram associados

    -------------------- PARTE 3: GERAR O FINANCEIRO QUANDO TODOS OS PRODUTOS ESTIVEREM ASSOCIADOS --------------------
    - A parte financeira só pode ser feita após a associação de todos os produtos
    - As associações são feitas na parte 2 deste tutorial, e em seguida, podem ser feitas as ações abaixo

    REFERÊNCIA ATUAL:
        janela=Importar XML da nota de entrada    botão=Confirmar    Verificar no canto da tela se o valor é o esperado
        botão=Gravar    botão=Financeiro    janela=Pagamento entrada

    DETALHE:
        - Nessa janela temos as abas referentes as formas de pagamento: Dinheiro, Parcelamento, Crédito, Conta bancária

        ABA MAIS COMUM: [ aba=Parcelamento ]
        INPUTS (interpretação)
            - Vencimento || Normalmente uma data 1 mês do dia que o financeiro está sendo gerado
            - Descrição  || Texto de informação para saber a qual fornecedor se direciona a compra
            - Valor      || Valor total da compra
            - Qtde.      || Número de parcelas do parcelamento
            - Intervalo  || Frequência do pagamento
        AÇÕES
            botão=Lançar    botão=Confirmar

    - Com a confirmação do financeiro, os estoques mudam, por exemplo:
        -> Em um estabelecimento, há um produto "refrigerante coca cola 250ML" com estoque 13
        -> Esse produto é associado com o de uma nota fiscal, que contêm um estoque 12
        -> O produto "refrigerante coca cola 250ML" aumenta seu estoque para 25
    """


def produto_gerar_estoque():
    """
    ----------------------------------------------------- FORMA 1 -----------------------------------------------------
    - Entrada de nota (importar xml) [ ver método: produto_entrada ]
    - É considerada a maneira mais correta, por ser criada a partir da nota, é mais automática, mas pode ser + difícil

    ----------------------------------------------------- FORMA 2 -----------------------------------------------------
    - Contagem de estoque [ ver método: produto_contagem ]
    - É considerada a maneira menos correta, por não precisar de nota, ser manual, podendo ser mais fácil
    """


# Contagem de estoque (atualizar/incrementar)
def produto_contagem():
    """
    ----------------------------------------------------- DETALHE -----------------------------------------------------
    - Produtos com medida em KG, é recomendável usar a opção de atualizar, ao invés de incrementar, pois é mais fácil
    - Esse procedimento de contagem é manual, sem a necessidade da entrada de uma nota

    ----------------------------------------------------- CAMINHO -----------------------------------------------------
    dropdown=Estoque    link=Produtos    aba=Estoque    Pesquisar um produto ou usar o botão=Buscar

    DETALHE
        Verificar a quantidade do produto no campo de estoque para saber se a atividade de contagem é efetiva

    INICIANDO UMA CONTAGEM
    aba=Estoque    botão=Contagem de estoque    botão=Novo    janela=Contagem de estoque

    AS INSTRUÇÕES ABAIXO ACONTECEM A PARTIR da [ janela=Contagem de estoque ]

    ----------------------------------------------------- PARTE 1 -----------------------------------------------------
    INCREMENTAR SOMENTE 1

    AÇÃO
    botão=Novo    aba=Dados    dropdown=Lançamento (incrementar quantidade)    dropdown=efetivação (Incrementar estoque)
    dropdown=Tabela (informar)    aba=Produtos    input=código (ENTER)    botão=Efetivar

    DETALHE
        Nesse contexto já há uma configuração p/ incrementar +1 automaticamente, não precisando informar uma quantidade

    ----------------------------------------------------- PARTE 2 -----------------------------------------------------
    INCREMENTAR + DE 1
        Quando fazer o cálculo de incremento, o valor é - 1 ao que seria (ex: De 21 p/ 25 são 4, então 4 - 1 = 3)

    AÇÃO
    botão=Novo    aba=Dados    dropdown=Lançamento (incrementar quantidade)    dropdown=efetivação (Incrementar estoque)
    dropdown=Tabela (informar)    aba=Produtos    input=código (ENTER)    Selecionar o produto na tabela
    campo=Estoque (duplo clique)    Direcionamento ao input de quantidade    Inserir o valor    botão=Efetivar

    ----------------------------------------------------- PARTE 3 -----------------------------------------------------
    ATUALIZAR
        O processo de atualizar é mais simples, bastando apenas inserir o valor desejado de forma direta

    AÇÃO
    botão=Novo    aba=Dados    dropdown=Lançamento (atualizar quantidade)    dropdown=efetivação (atualizar estoque)
    dropdown=Tabela (informar)    aba=Produtos    input=código (ENTER)
    Selecionar o produto na tabela    campo=Estoque (duplo clique)    Direcionamento ao input de quantidade
    Inserir o valor    botão=Efetivar
    """


# Registrar um novo fornecedor
def fornecedor_criar():
    """
    ----------------------------------------------------- CAMINHO -----------------------------------------------------
    dropdown=CRM    link=Cliente e Fornecedor    aba=Clientes ou Fornecedores    botão=Nova

    ABA MANDATÓRIA          || Básico
    ABA MANDATÓRIA (campos) || Fantasia, Endereço, Bairro, Cidade, UF, CEP, Física/Jurídica, CNPJ, Tipo IE, IE
    DETALHE                 || Pelo input=CNPJ é possível auto preencher outros campos
    """
