

# Alterar imposto sem trocar operação (item 132) (assunto: imposto)
def comercial_tut_2():
    """
    Link original:   https://vrsystem.info/publico/post.aspx?Id=0aa745e6-922b-4d4d-b092-ef94efd220f7
    Link secundário: https://www.youtube.com/watch?v=FRCDaGvtess

    VERIFICAR DADOS MAIS COMPLETOS DE UM PRODUTO
    [ dropdown=Comercial ]
        [ link=Saídas ]
            [ aba=saídas ]
                [ botão=saída ]
                    [ janela=Saídas ]

    [ aba=opções ]
        [ input=Operação ] ex: 500 (venda)
            [ input=Vendedor ] ex: 1 (ADMIN)
                [ input=Cliente ] ex: 5
                    [ div=Produtos/Serviços ]
                        [ input=Código ] (Inserir o código do produto) (ENTER)
                            [ aba=Outros ]
                                [ botão=classe de imposto ]
                                    [ janela=Cadastro classe de imposto ]

    - Será exibido uma tabela com códigos de operação
    - Digitar a operação desejada na barra de pesquisa (ex: 500)

    Duplo clique no campo que possui UF do seu estado
    [ janela=Operações classe de imposto ]
        [ input=CFOP ] ex: 5102 para 5405 (permite consulta)
            [ aba=IPI ]
                [ dropdown=Tipo IPI ] ex: 50
                    [ div= IPI ]
                        [ input=Percentual IPI ] ex: 10
                            [ botão=Salvar ] -----> [ janela=Operações classe de imposto ]
                                [ botão=Salvar ] -----> [ janela=Cadastro classe de imposto ]
                                    [ botão=Gravar ] -----> [ janela=Saídas ]

    Como alterar os impostos de um produto lançado sem precisar trocar operação?
    [ aba=outros ]
        [ botão=recalcular impostos ]
            [ aba=Opções ]
                [ botão=gravar ]
    """


# Ativar [ SVC ] e [ FS-DA ]
def configuracoes_tut_2():
    """
    Link:   https://youtu.be/NA89PvhF7GI
    Título: NFe em contingência via SVC e FS-DA

    ----------------------------------------------------- DETALHES -----------------------------------------------------
    - Implementação de dois tipos de contingência: [ SVC ] [ FS-DA ]

    - O [ SVC ] é um servidor virtual de contingência que atende:
        . Quando SEFAZ autorizado ou SEFAZ Nacional estiverem fora do ar, esse serviço é ativado para receber as notas,
          devolvendo estas notas assim que o problema for resolvido nos servidores SEFAZ (contingência do SEFAZ)

    - O [ FS-DA ] é um formulário de segurança de documento auxiliar
        . O cliente não consegue emitir uma nota por quaisquer motivos, então o cliente pode ativar esse tipo de
          contingência (formulário de impressão), possibilitando imprimir a sua nota nesse formulário

        . O formulário é adquirido numa gráfica que é credenciada pela SEFAZ

    ATIVANDO O SVC
    [ dropdown=Configurações ]
        [ link=Filial ]
            [ No mínimo uma filial deve aparecer na tabela ]
                [ Selecionar uma filial da tabela ]
                    [ botão=Webservices ]
                        [ janela=WebServices ]
                            [ dropdown=Tipo de nota ] ex: NF-e Contingência
                                OBS: A pessoa do vídeo não salvou o que foi feito, apenas fechou

    ----------------------------------------------------- DETALHE -----------------------------------------------------
    - Foi mencionado que os dados na [ janela=webservices ] os que estão aptos a funciona são os de: [ autorização ]

    LISTA DE WEBSERVICES (via vrsystem)
    https://vrsystem.info/publico/post.aspx?Id=480686b1-e7dc-4472-ba44-8953279de677

    EMISSÃO
    [ dropdown=Comercial ]
        [ link=Saídas ]
            [ aba=Saídas ]
                [ botão=Saída ]
                    [ aba=opções ]
                        ---------- DETALHES SOBRE ESSES CAMPOS ----------
                        Ao inserir o valor, se não há preenchimento, clicar no input de algum dos outros
                        [ input=Operação ] ex: 500
                            [ input=vendedor ] ex: 1
                                [ input=Cliente ] ex: 5
                                    [ div=Produtos/Serviços ]
                                        [ input=Código ] ex: código de um produto
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

# Entrada de nota ()
# Ajuste manual (balanço de estoque)
