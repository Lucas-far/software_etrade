

# Configurar produtos que tenham dimensões para serem impressas no ticket
def item_4():
    """
    Impressão dos campos de dimensões dos produtos (estoque)     [ Item 4 ]
    https://vrsystem.info/publico/post.aspx?Id=833b7098-9bed-4458-bfc5-d75a75e02632

    Link secundário: https://youtu.be/kVNcieFXJSc

    ---------- DETALHE ----------
    Inclusão na parte de impressão do ticket os atributos de [ altura x largura x profundidade ] de produtos que
    necessitam desse tipo de métrica (ex: Marmorarias, Portas, Madeira, Vidracaria). As informações antes poderiam ser
    colocadas nas informações do produto, mas agora podem ser também salvas no banco de dados

    [ dropdown=Configurações ]
        [ link=Impressão e email ]
            [ botão=Impressão ]
                [ botão=Buscar ]
                    [ Se há tickets disponíveis, eles surgirão na tabela ]
                        [ Duplo clique em algum ticket ]
                            [ janela=configurar layout ticket ]

    [ aba=produtos ]
        [ link=Clique aqui para adicionar uma nova linha ]
            [ dropdown=Campo ]

    CAMPOS REFERENTES AO OBJETIVO DA AULA
        - Movimento Produto - Dimensão altura
        - Movimento Produto - Dimensão com nome (ex: A: 1 L: 2 P: 3)
        - Movimento Produto - Dimensão largura
        - Movimento Produto - Dimensão profundidade

    ----------- DETALHES -----------
    - Exemplos claros não foram fornecidos
    - Preenchimento dos campos não foram explicados
    """


# Sem descrição
def item_5():
    """
    Configuração de busca de produtos (estoque)     [ Item 5 ]
    https://vrsystem.info/publico/post.aspx?Id=03768e1c-8197-4dff-873e-e546bfcdbf0f
    """


# Sem descrição
def item_6():
    """
    Super busca de produtos (estoque)     [ Item 6 ]
    https://vrsystem.info/publico/post.aspx?Id=307565de-5f09-4863-a72c-0ed2553e0489
    """


# Aplicar um promoção para uma quantidade grande de produtos (incompleto)
def item_7():
    """
    Copiar promoção entre produtos (estoque)     [ Item 7 ]
    https://vrsystem.info/publico/post.aspx?Id=c8f0849d-9bae-47b3-abf3-647e38c0e1b3
    Youtube: https://youtu.be/WZIYRnj7DXs

    CONTEXTO
    Você é dono de um supermercado, e você já fez promoções em determinado dia (ex: terça das frutas)
    Imagine ter que aplicar um preço de promoção para todos os produtos

    dropdown=Estoque
      link=Produtos
        botão=Buscar
          Pesquisar um produto que represente uma categoria
            Duplo clique em um produto da tabela
              janela=Cadastro de produto

    dropdown=Tipo (escolher) (ex: Atacarejo - a partir de...)

    DETALHE
    - A aula trava aqui [ 02:35 ] pois a tabela não mostra o produto
    """


# (complemento ao item 39)
def item_38():
    """
    Promoção Atacarejo agora considera produtos relacionados (estoque)     [ Item 38 ]
    https://vrsystem.info/publico/post.aspx?Id=2bf90fda-86f6-4df2-b9d9-1b0b3e2a73df
    Youtube: https://www.youtube.com/watch?v=1gLs9GgvJHo

    dropdown=Estoque
      link=Produtos
        [ buscar um produto ]
          [ acessar o produto ]
            aba=Relacionados (Pela lógica, devem surgir produtos)
    """


# Informações pertinentes sobre promoção (complemento ao item 7)
def item_39():
    """
    Tudo sobre promoção (estoque)     [ Item 39 ]
    https://vrsystem.info/publico/post.aspx?Id=de2440c7-41e7-4a39-9935-c8a0f2bdc0f3
    Youtube:
    """


# Criar relacionamento entre produtos (complemento ao item 38)
def item_95():
    """
    Produto relacionado (estoque)     [ Item 95 ]
    https://vrsystem.info/publico/post.aspx?Id=9893c532-7be3-4f18-b28b-5cfab4ac317a
    Youtube: não

    ------- DETALHE -------
    - Ao relacionar produtos, você está determinando que eles tenham o mesmo preço

    CRIAR RELACIONAMENTO
    dropdown=Estoque
      link=Produtos
        [ buscar um produto ] ex: carne (A lógica p/ relacionamento é que exista + de 1 do mesmo tipo)
          [ selecionar o produto a iniciar o relacionamento ]
            aba=Relacionados
              input=Produto relacionado (ex: carne)
                botão=Lupa (Buscar registro)
                  janela=Busca de produtos/serviços

    [ Selecionar pelo (ctrl + mouse) os produtos que quiser relacionar ]
      botão=Selecionados
        botão=Salvar

    ------- DETALHE -------
    Se um produto, por exemplo, foi relacionado a outros 3, para esse relacionamento ser desvinculado, todos devem ser
    editados

    RETIRAR RELACIONAMENTO
    dropdown=Estoque
      link=Produtos
        [ buscar um produto ] ex: carne
          [ acessar um produto ]
              aba=Relacionados
                [ selecionar um produto relacionado ]
                  botão=Remover relacionamentos
                    botão=Salvar
    """
