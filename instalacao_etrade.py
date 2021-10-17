

# Configurar o Windows para baixar recursos essenciais
def parte_1():
    """
    - Ativar recursos do Windows
        Painel de centrole * programas e recursos
        Clicar no link [ ativar ou desativar recursos do Windows ]
        Abertura do painel [ Recursos do Windows ]
        Habilitar os 2 primeiros itens (todos os checkboxes): [ .NET Framework 3.5 ] [ .NET Framework Advanced series ]

    DETALHE
    - Será aberta uma janela nova, onde se deve permitir que o Windows procure e baixe os recursos
    - Depois de algum tempo, serão aplicadas as alterações
    """


# Softwares necessários
def parte_2():
    """
    - Baixar o SQL Server 2014 express
    - Baixar o Etrade
    - Baixar o Etrade stable
    """


# Instalar os softwares
def parte_3():
    """
    - Instalar o SQL Server 2014 express
    - Instalar o Etrade
    - Instalar o Etrade stable

    ------------------------------------- SQL Server 2014 express (64 bits) -------------------------------------
    - O caminho da instalação é o da pasta de usuário [ C:\Users\Home\Downloads\SQLEXPRADV_x64_PTB\ ]
    - CLicar no botão [ OK ]
    - O ambiente será preparado (leva algum tempo)
    - Clicar no link [ Nova instalação autônoma do SQL Server... ]
    - Marcar o checkbox [ Aceito os termos da licença ] e clicar no botão [ avançar ]
    - Há um checkbox [ Usar o microsoft update para procurar atualizações ], ignorar e clicar em [ avançar ]
    - Na etapa [ Seleção de recursos ] na div [ recursos ], marcar o checkbox [ LocalDB ] (último item)
    - Clicar em [ avançar ]
    - Na etapa [ Configuração da instância ], marcar o checkbox [ Instância nomeada ] e redefinir o nome
    - O novo nome deve ser [ SQL2014 ]
    - Clicar em [ avançar ]
    - Na etapa [ Configuração do servidor ], manter as configurações e clicar em [ avançar ]
    - Na etapa [ Configuração do mecanismo de banco de dados ], marcar o checkbox [ modo misto ]
    - Há dois inputs logo abaixo, em ambos digitar [ senha ] para configurar uma senha
    - Clicar no botão [ Avançar ]
    - Na etapa [ Configuração do reporting services ], marcar o checkbox [ Instalar e configurar ]
    - CLciar no botão [ avançar ]
    - Na etapa [ andamento da instalação ] o software será configurado e demora bastante
    - Ao fim da instalação, temos uma tabela com diferços recursos instalados com êxito
    - Clicar no botão [ Fechar ]

    -------------------------------------------- Etrade (instalador matriz) --------------------------------------------
    - A instalação é bem direta, não precisando de instruções, apenas seguir o fluxo
    - Não criar atalhos, pois os atalhos são os da instalação seguinte

    -------------------------------------- Etrade (atualizador da versão estável) --------------------------------------
    - A instalação é bem direta, não precisando de instruções, apenas seguir o fluxo
    - Marcar todos os checkboxes referentes a atalhos
    """


# Liberação do disco C para compartilhamento
def parte_4():
    """
    - Ir ao disco C * botão -> * propriedades
    - Clicar na aba [ Compartilhamento ]
    - Clicar no botão [ comportilhamento avançado ]
    - Marcar o checkbox [ Compartilhar a pasta ]
    - Clicar no botão [ Permissões ]
    - Ir à div [ Permissões para todos ]
    - Marcar o checkbox [ controle total ]
    """


# Liberar controle de todos os usuários pelo disco C
def parte_5():
    """
    - Ir ao disco local C * botão -> * propriedades
    - Clicar na aba [ segurança ]
    - Na div [ Nomes de grupo ou de usuário ] o procedimento abaixo deve ser feito com todos os usuários

        Clicar no botão [ editar ]
        Abertura da janela [ Permissões para disco local ]
        Ir à div [ Permissões para usuários autenticados ]
        Marcar o checkbox [ controle total ]
        Clicar em [ aplicar ] e [ OK ]
    """


# Desativar o firewall
def parte_6():
    """
    - Ir ao painel de controle
    - Clicar em [ Windows Defender Firewall ]
    - Clicar no link [ Configurações avançadas ]
    - Abertura da janela do Firewall
    - No lado direito há o link [ propriedades ]
    - Configuração a ser feitas nessas 3 abas: [ Perfil do Domínio ] [ Perfil particular ] [ Perfil público ]

        Na div [ Estado ] no dropdown [ Estado do firewall ] trocar para [ desligado ]
    """


# Configurações no Etrade (Substituição de bdd, ligar base, atualizar)
def parte_7():
    """
    --------------------------------- Inserir o banco de dados do estado ao Etrade ---------------------------------
    - Pelo website do [ vrsystem ] acessar [ vrsystem.info/publico/manual_index.aspx ]
    - Descer ao título [ Outros ], clicar no link [ mais... ] e procurar pelo tutorial [ Instalar o E-trade ]
    - O link é [ https://vrsystem.info/publico/post.aspx?Id=e6e90f2e-f346-4fa9-b54c-2b02d25f9c17 ]
    - O tutorial redirecionará para o website [ https://uniaopartners.wordpress.com/2019/01/25/banco-de-dados-padrao/ ]
    - Neste local, escolher o estado alvo e baixar seu banco de dados
    - Na pasta do Etrade no disco local, pegar os arquivos baixados, copiar e colar dentro da pasta

    ---------------------------------- Atualizar um banco de dados que já foi ligado ----------------------------------
    - Abrir o [ SQL Server Configuration Manager ]
    - Duplo clique no link [ Serviços do SQL Server ]
    - Nos serviços ativos, clique com o botão direito e selecione [ parar ]

    - Fazer o download dos novos bancos SQL
    - Ir à pasta do [ Etrade ] e substituir os arquivos SQL da pasta pelos baixados

    - Na pasta do Etrade, abrir o executável [ UpdateAutomatic ]
    - Clicar no botão [ executar ]
    - Esperar os procedimentos serem feitos
    - Clicar no botão [ fechar ]

    - Retornar ao [ SQL Server Configuration Manager ]
    - Duplo clique no link [ Serviços do SQL Server ]
    - Nos serviços ativos, clique com o botão direito e selecione [ iniciar ]

    ---------------------------------------------------- Ligar base ----------------------------------------------------
    - Na pasta do Etrade, procurar pelo executável [ LigaBase ] e abrí-lo
    - Clicar no botão [ Ligar base ]
    - O procedimento deve retornar uma mensagem de sucesso
    - Na pasta do Etrade, procurar pelo executável [ UpdateAutomatic ]
    - Clicar no botão [ Executar ]
    - Clicar no botão [ Fechar ]
    """


# Configurar o SQL Server Configuration Manager (TCP/IP)
def parte_8():
    """
    - Abrir o [ SQL Server Configuration Manager ]
    - Clicar no dropdown [ Configuração de rede do SQL Server ]
    - Duplo clique em [ Protocolos para SQL2014 ]
    - Clicar em [ TCP/IP ] com o botão direito e esolher [ habilitar ]
    - Duplo clique em [ TCP/IP ]
    - Clicar na aba [ Endereços IP ]
    - Descer ao final da barra de rolagem até a guia [ IPAll ]
    - Alterar o input [ Porta TCP ] para 1434
    - Clicar no botão [ Aplicar ] e [ OK ]
    - Duplo clique no link [ Serviços do SQL Server ]
    - Observe todos os serviços ativos, selecione cada um, botão direito e clicar em [ Reiniciar ]
    """


# Primeiro acesso no Etrade
def parte_():
    """
    - Pelo [ desktop ], abrir o [ Etrade ]
    - Abertura do E-trade enterprise resource planning
    - Clicar no botão [ entrar ] para dizer ao [ Etrade ] que este é seu primeiro acesso
    """
