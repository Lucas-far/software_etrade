

#
def ean():
    """
    ----------------------------------------------------- CONCEITO -----------------------------------------------------
    - Código referente ao código de barras de um fabricante

    ------------------------------------------------------ INFOS ------------------------------------------------------
    EAN = Numeração Européia de Artigos (sequência numérica de 13 dígitos)
    EAN = Sintaxe construída apartir dos dados:
          país de origem,    [ dígitos: 3       ] (3 primeiros dígitos) (ex: Brasil= 789, 790)
          fabricante         [ dígitos: 4 até 6 ]
          modelo do produto  [ dígitos: 3 até 5 ]
          dígito verificador [ dígitos: 1       ]

    ----------------------------------------------------- DETALHE -----------------------------------------------------
    - É essencial que este campo seja preenchido no cadastro do produto, caso contrário, sua dinâmica de compra será
      prejudicada em compras rápidas

    --------------------------------------------------- RELACIONADOS ---------------------------------------------------
    Código EAN opcional na grade de produtos (estoque)     [ Item 16 ]
        https://vrsystem.info/publico/post.aspx?Id=cecd0f3b-e8ea-4767-9eb5-2659bde96ee0

    Exibir histórico de produtos com grade (estoque)     [ Item 36 ]
        https://vrsystem.info/publico/post.aspx?Id=475ac9c4-d19d-4fe2-a32b-6b2165b6e005

    Compra - Importar XML produtos com grade e cadastro padrão de classificação (estoque)     [ Item 83 ]
        https://vrsystem.info/publico/post.aspx?Id=4fabc71d-21f6-4f34-90c7-a5bb640c3d33
    """


# Detalhes sobre o imposto ICMS (Pendente)
def icms():
    """
    --------------------------------------------------- SIGNIFICADO ---------------------------------------------------
    - Imposto sobre circulação de mercadoria e serviços
    - O foco desse imposto é variável, e no meu caso, é redirecionado para mercadorias
    - É um imposto estadual
    - É um imposto que age baseando em operações, mais frequentemente com operações internas e externas
    """


#
def inscricao_estadual():
    """"""


# Informações sobre a SEFAZ
def sefaz():
    """
    --------------------------------------------------- SIGNIFICADO ---------------------------------------------------
    - Secretaria de fazenda

    ---------------------------------------------------- OBJETIVOS ----------------------------------------------------
    - Gerenciamento de notas fiscais
    - Regulamenta questões tributárias (impostos)
    """


#
def mdf_e():
    """"""


# Campo referente ao cadastro do produto
def ncm():
    """
    --------------------------------------------------- SIGNIFIFICADO ---------------------------------------------------
    Nomemclatura comum do Mercosul

    ----------------------------------------------------- DETALHE -----------------------------------------------------
    - Exemplo de pesquisa: NCM nome do produto    OBS: É provável que o site da SEFAZ tenha esses dados
    - O nome do produto pode ser considerado parte da nomemclatura [ família ]
    - Se no cadastro do produto, for inserido o NCM e o campo CEST não preencher automaticamente, isso pode significar
      que o NCM é inválido
    """


# Detalhes sobre o imposto PIS
def pasep():
    """
    --------------------------------------------------- SIGNIFICADO ---------------------------------------------------
    -

    ----------------------------------------------------- DETALHES -----------------------------------------------------
    - Vinculado a direitos trabalhistas (servidor público)
    - Operado pelo Banco do Brasil
    """


# Detalhes sobre o imposto PIS
def pis():
    """
    --------------------------------------------------- SIGNIFICADO ---------------------------------------------------
    - Programa de integração social / abono salarial

    ----------------------------------------------------- DETALHES -----------------------------------------------------
    - Vinculado a direitos trabalhistas (iniciativa privada)
    - Operado pela Caixa Econômica
    - É recebido 1 vez ao ano
    - É concedido sob as condições:
        ter carteira assinada na iniciativa privada a pelo menos 5 anos
        ser assalariado em média de 2 salários
        deve ter trabalhado para pessoa jurídica
        ter trabalhado pelo menos 30 dias no ano anterior
        ter sido informado na empresa pela RAIS (Relação Anual de Informações Sociais) (será substituída pelo E social)

    - Não é concebido sob a condição:
        ter trabalhado para pessoa física
    """


#
def rntrc():
    """"""
