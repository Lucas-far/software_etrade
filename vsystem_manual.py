

def links():
    """"""
    x = '    '

    categorias = (
        '(estoque)', '(comercial)', '(financeiro)', '(crm)', '(configurações)',
        '(gourmet)', '(pdv)', '(gourmetdroid)', '(sintegra)', '(sped)', '(outros)'
    )

    fixed = 'https://vrsystem.info/publico/post.aspx?'

    contador = 1

    # ---------- ESTOQUE ----------
    estoque = """
    Manifesto Destinatário;
    Diferimento de ICMS relativo ao FCP;
    Como funciona o cálculo do ICMS Desonerado ST;
    Impressão dos campos de dimensões dos produtos;
    Configuração de busca de produtos;
    Super busca de produtos;
    Copiar promoção entre produtos;
    Novas funcionalidades na tela de pesquisa de produtos;
    Relatório de catalogo de produto;
    Gerar etiquetas na tela de remarcação de preços da compra;
    Classe imposto;
    DIFAL e antecipação de ICMS para telas de entrada;
    Ajustar a classe de imposto na importa de xml de entrada;
    Produto - infinitas fotos;
    Relatório produtos por tributação;
    Código EAN opcional na grade de produtos;
    Utilizar transferência com preço;
    Erro de Download da NFe no MDE ou Por Download da Chave;
    Melhoramos a exibição visual dos itens localizados no import do xml de entrada;
    Relatório de NCM inválidos;
    Configurar para Observação do item aparecer na venda;
    Edição em lote;
    Como Inserir Promoção nos Produtos via Banco;
    Alteração de nome do produto em lote;
    Pré-cadastro no cadastro de produtos;
    Etiqueta de balança agora com informação nutricional;
    Edição de impostos;
    Modelos de etiqueta para balança Filizola e Toledo;
    Promoção leve e pague;
    Importar XML de compra tela entrada - alterar dados;
    Custo médio no E-Trade;
    Produtos - Múltiplos códigos adicionais;
    Nome tabela de preço;
    Configuração de Quantidade Máxima para Promoções;
    Configuração para composição de custo na entrada de produtos;
    Exibir histórico de produtos com grade;
    Configuração: atualizar percentagens na composição de custo;
    Promoção Atacarejo agora considera produtos relacionados;
    Tudo sobre promoção;
    Controle de validade nos produtos;
    Relatório de inventario modelo P7;
    Gráficos cadastro de produtos;
    Configurar campos a serem exibidos no histórico de produtos;
    Gráficos na tela de produtos;
    Calculo FCP ST com diferença de base;
    Caixas com na tela de entrada;
    Relatório resumido de entrada;
    Manual de desagregação;
    Pesquisa por nome no E-Trade;
    Industria - Desagregação - Desossa bovina;
    Configurar dados padrão no cadastro de produto;
    Atualizar NCM ao importar XML de compra;
    Como funciona a tela de remarcação de preços na entrada;
    Informando despesas acessórias;
    Nova tela de cadastro de produtos;
    Ordem de desagregação - Gravar custo padrão;
    Ordem de desagregação - Quantidade;
    Como funciona o calculo do ICMS diferido;
    Como funciona o calculo do ICMS Desonerado;
    Manifesto Destinatário Eletrônico - MDe;
    Relatório desempenho de compra;
    Contagem de estoque utilizando coletor;
    Relatório detalhado de transferência;
    Margem padrão no cadastro da tabela de preço;
    Configuração para bloqueio do código principal do produto;
    Edição em lote sem selecionar itens;
    Tudo sobre ICMS desonerado;
    Múltiplas descrições para um mesmo produto;
    Configurar campos a serem exibidos na consulta de produtos;
    Reajuste de preços;
    Reajuste de preços dos produtos fabricados;
    Relatório extrato produtos transferidos;
    Recebimento de frete na compra de mercadoria;
    Compra por preço;
    Complemento na tela de Entradas;
    Manual de Contagem E-Trade;
    Novos campos medicamento e compatibilidade ABC Farma;
    Relatório de preços;
    Configurar classe de imposto para somar IPI e Frete nas base de ICMS;
    Cadastro automático de produtos na importação de XML;
    Atalhos para produtos e clientes na saida e entrada;
    Arquivos de configuração coletor de dados;
    Compra - Importar XML produtos com grade e cadastro padrão de classificação;
    Lista de atalhos PDV;
    Configurar peso dos produtos para emissão de NFe;
    Adicionamos a opção de visualizar detalhes de estoque;
    Manifesto destinatário;
    Relatório de produtos em promoção;
    Criamos relatórios de pedido e distribuição e habilitamos alteração de preços pela tela;
    Contagem de estoque por seleções como classe, sub, marca, etc...;
    Editar e gerar transferências a partir de um pedido de compra;
    Contagem de estoque;
    Limite de adicionais no Gourmet;
    Relatório de entradas;
    Produto relacionado;
    Pedido de compra;
    Pedido de compra - Configurar;
    Transferência de estoque entre filiais;
    Gerenciamento de etiquetas;
    Relacionar fornecedor aos produtos;
    Relatório de alteração preços;
    Gerenciamento de códigos para os produtos;
    Múltiplas configurações de casas decimais por produtos;
    Reajuste de Preço;
    Composição e analise de custo;
    Comissão progressiva por produto;
    Layout de Etiquetas (Modelos); 
    Classificação Mercadológica;
    Cadastr de Unidade de Venda;
    Módulo de Estoque;
    Impressão de etiquetas produtos em Laser ou Jato de Tinta;
    Módulo Produção / Indústria;
    Controle de estoque mínimo e ideal;
    Configurar tabelas de preços de custo padrão no sistema;
    Utilizando várias tabela de preço;
    Cadastro de CEST;
    Entrada de produtos;
    Relatórios de Estoque;
    Contagem Rápida de Estoque;
    Balanças - Exportação de dados;
    Cadastro de Produtos;
    Cadastro de Tabela de Preços;
    Cadastro de CFOP;
    Cadastro de Classes de Impostos;
    Cadastro de Cor;
    Cadastro de Tamanho;
    Cadastro de Família;
    Cadastro de Grupos;
    Cadastro de Subclasses;
    Cadastro de Classes""".split(';')
    estoque_f = [data + ' ' + categorias[0] for data in estoque]
    estoque_urls = f"""
    Id=7d371315-9e6e-4707-aeeb-0cae649d00bd;
    Id=1574be3d-abef-4383-afe0-f934e081005d;
    Id=29c584dd-fc7b-46a8-b5b8-2d78519be833;
    Id=833b7098-9bed-4458-bfc5-d75a75e02632;
    Id=03768e1c-8197-4dff-873e-e546bfcdbf0f;
    Id=307565de-5f09-4863-a72c-0ed2553e0489;
    Id=c8f0849d-9bae-47b3-abf3-647e38c0e1b3;
    Id=211a48e9-0b06-42fd-8783-84aef6758361;
    Id=c9222deb-2dc7-4f7e-b48e-99245d7b6998;
    Id=51b546f3-34fb-469e-acf0-4926c5685327;
    Id=eabd5bfb-9e61-461a-a06a-2e2cdc123c12;
    Id=7e6c0423-cce7-48a1-8f1d-0d6b5f2c0e87;
    Id=d10b1856-a215-4722-87bf-0cb24d54229e;
    Id=9a7f6660-2079-4884-895a-1e4476a0a9e3;
    Id=47d7b279-4739-4694-bef1-cb568e6dc2d5;
    Id=cecd0f3b-e8ea-4767-9eb5-2659bde96ee0;
    Id=81da302b-a33e-4f44-ada7-a1e2d2ef647a;
    Id=67be66ad-5f38-4d39-80e7-d00fcb006d29;
    Id=1bd06a59-ef05-4358-a44b-9259296470d7;
    Id=cf6fd90b-5a08-42bb-8711-354519a37b09;
    Id=6a383846-20ce-47d3-a5e1-813792d00111;
    Id=66d32ecf-07a7-45d6-8d94-2a9f9ffdcd65;
    Id=d2091bde-116c-46ef-9f04-036d5db4b70f;
    Id=5cc330d0-4b06-45fe-a015-fab7a5ca6850;
    Id=cd92a1cb-3bbe-4c84-a0c7-3d7f1a61798d;
    Id=69aae92b-77f3-4a10-b043-6901d4763373;
    Id=0dba4a7d-13ec-4eea-9d47-160b624de401;
    Id=722b29b0-8ac4-426b-ae77-f13ee11cdc51;
    Id=48e88afa-bb42-4b6d-82ca-de0ee8ada7af;
    Id=63ba08ca-7b14-4984-a377-af80d66acc07;
    Id=6f6847a6-a838-4116-a76f-a5b2d2d61f6b;
    Id=4c58db5f-5e48-4b35-9bfd-090461a1e345;
    Id=94f81d1b-8885-4417-bdc5-9862b702ca37;
    Id=0249981e-25d7-49f8-803d-ad11fef36e6b;
    Id=6b251650-9f9f-4e2c-a102-cfe13eba541c;
    Id=475ac9c4-d19d-4fe2-a32b-6b2165b6e005;
    Id=ddabe181-9caf-44b2-91a2-920943e4ddd2;
    Id=2bf90fda-86f6-4df2-b9d9-1b0b3e2a73df;
    Id=de2440c7-41e7-4a39-9935-c8a0f2bdc0f3;
    Id=773fe0cc-3b88-47bb-aa80-c8c033a20132;
    Id=6900c0bf-ac0e-403f-8301-00b25ab9f00e;
    Id=ade7d884-2419-4c16-a070-7150a01e6d70;
    Id=737ccfca-2b34-4a7a-8637-c5437ed410bc;
    Id=d72c9ae0-14bf-4d61-9432-82c43aefaeb4;
    Id=a37b5801-45fe-486e-bb1c-f8aba50e3066;
    Id=7561e7da-0789-4df9-b916-95b1b56a98cb;
    Id=2af139ba-8e10-4246-8c71-1f544607b39c;
    Id=829e8762-7865-4fb8-a56c-51fb97bfcdae;
    Id=184fcce4-af5b-454b-8947-e0204de14c61;
    Id=99cfe11a-06d0-4861-8af4-8fb34eea14e4;
    Id=8035b428-dcb8-4fb6-8f99-5e9ae5aa0980;
    Id=5734a663-2eb4-4355-9a23-a3eefe84d6e6;
    Id=33301039-23a6-4185-98db-4ef9e38f4d46;
    Id=bae67d98-8a03-4a9c-aca0-5b22d45e02f5;
    Id=9ce1466d-23b6-4f8d-b6f9-16274ff60f00;
    Id=a88fd01b-cefe-4cd4-9947-da3eabca6456;
    Id=5123dfa8-a42e-4246-942d-a1d035351014;
    Id=6e04bc10-83a1-4fab-8ab5-b14503fbe6aa;
    Id=6c8bac4f-aa7a-4c06-89b2-e649765f0998;
    Id=e3428538-e384-4362-ab67-6222ae1bdefa;
    Id=4ae18c2f-92c5-4bf1-80a2-2e42369b52dd;
    Id=315d0375-aeeb-46c9-80b7-c1aa109464a8;
    Id=85866e1a-c2fb-4f09-804b-8dc10fc8bc8f;
    Id=97b71c2d-3a6c-4295-bb2e-9ee475f1aa89;
    Id=a67bf146-7058-4778-8867-c017f13c1502;
    Id=56bc7476-5bb1-48a3-a5a8-f0895c30a1b8;
    Id=c6bd9189-20bf-46d7-abcf-c0bf17583f46;
    Id=5eb8624b-8d89-48a4-af7b-ab563c8cc4b1;
    Id=9ba94010-e1ae-41e1-a967-127b473a3b0a;
    Id=9318f899-8b2f-4e55-987a-030911ddd554;
    Id=efbf2d6c-d538-4722-9186-4c03800a714e;
    Id=63ab0483-07bd-4c6b-958d-5011c25192c7;
    Id=3c6cdac9-08e5-43d7-8e3f-bbd20d17f60a;
    Id=676965e2-25b3-4b87-be44-cd2c58ec62c7;
    Id=b3d01c8b-7a56-4b32-8ff7-0e865bb70dde;
    Id=d2ad9d79-d674-4461-a557-ada513555f8e;
    Id=dea12efd-fc55-46be-b237-0a9f75067b6e;
    Id=3e89fd09-deaa-4aae-a3b4-92160a075087;
    Id=4359df02-b4d2-4df8-b8ae-bb47c062dc8c;
    Id=1d344072-c378-40c4-a01d-8b3d195b8aed;
    Id=efb79f03-e7ec-4287-897a-198bcac8e381;
    Id=50cb1f97-954e-4bae-b5c3-42d9f33546b5;
    Id=4fabc71d-21f6-4f34-90c7-a5bb640c3d33;
    Id=894c2d14-587f-4353-82c1-72b00c511695;
    Id=63f1d3e0-f14a-4a64-acc2-06a2648c1c54;
    Id=9528d856-eaf5-4448-9627-f57e62a1b64f;
    Id=e957af00-9d79-4c9a-b9cc-5af9dc4ca474;
    Id=9dfb8fb3-4c42-43f0-93e4-255335c7bb4c;
    Id=1dc69f42-a7fc-48b3-b4fd-5e5a5c9cdc98;
    Id=e5037ed1-1459-41fd-aad1-1a946dfb2f65;
    Id=d82acb98-534c-44d1-96c5-e9f85d71ce29;
    Id=b1421e05-1281-4fcf-8b39-76e92d337aa9;
    Id=3a93b8ec-d73b-4470-a0bb-c5be0eaaa608;
    Id=8feaf1dc-71ee-4876-85bc-8b095348beed;
    Id=9893c532-7be3-4f18-b28b-5cfab4ac317a;
    Id=9706e120-927c-40eb-866a-2178920b2c17;
    Id=f8fd3666-8c3f-4ce7-b5af-d9390c57fc84;
    Id=632d40f2-960a-44d0-8b1a-79ef6b6cbe53;
    Id=004093c5-fc87-435a-99c6-8bda90f7bfd2;
    Id=717c0a50-f8c6-4f7b-b845-0498c2abe803;
    Id=fdf61f78-1807-48e3-903b-ab030b9e4968;
    Id=5997032b-87b9-431f-9ed8-cdf0848689ca;
    Id=42636a71-ce4f-4f6c-8778-fc57e1ff9991;
    Id=024ec353-17e8-43a9-a762-668e424ec141;
    Id=f0463081-cfa5-4076-b779-9ea800b3c6c5;
    Id=db34fc75-5100-4d8c-bdd3-1e15d26f386c;
    Id=8befdc57-ea95-4ce1-92db-bfb54a212206;
    Id=c393f394-22a0-484f-adcf-804a00433ee9;
    Id=8ba4fdb3-4b7f-4507-9ce3-352c83d42e05;
    Id=f75d800a-b3cd-44c1-83a3-320fa5d7e160;
    Id=ff52c856-2fc0-42f9-93d0-848246574f2c;
    Id=4c19ce94-a56c-43cf-9bf9-17c03635d094;
    Id=62b26ffb-eea7-4f4d-a321-dfc8261021d2;
    Id=31c6590d-385f-47f5-a7d7-5650b2b284a9;
    Id=87677600-233c-4d4c-96ec-5d8541327526;
    Id=855de16c-d128-420b-b44d-3cf520743a19;
    Id=0f3bb565-5bcd-4a7a-9d17-1d5a60e5aa1c;
    Id=a55ac76b-913d-4d05-9310-6f8cc65a27cf;
    Id=89028edd-0ded-4255-a274-8c7688ee57f6;
    Id=e8dec840-2fe9-4b58-9cd1-1e59e17cede2;
    Id=0d0d9842-7e9c-4db2-96da-9926403afd6e;
    Id=91b508d4-1a43-4e99-8861-4cef6c46ed84;
    Id=2d13961e-fbc8-4050-9913-e1c7ec8ee68f;
    Id=e75fd132-f40a-401c-b2f3-21ccad5db694;
    Id=7e345cd1-7ae9-4480-89c5-346aac4d5ff3;
    Id=8b14e49f-5921-48e6-a214-3b891af84d36;
    Id=5c49e730-fdf9-407d-8fb6-3fdecfc6b5b0;
    Id=ca24d667-a574-4343-bd66-739f8d4fb540;
    Id=4a8f7236-0b40-4d55-95a0-f337dc64f48a;
    Id=44ca24e3-0d3f-4233-8253-30c9bc130125""".split(';')
    estoque_urls_f = [fixed + data.replace('\n', '').replace('    ', '') for data in estoque_urls]

    # ---------- COMERCIAL ----------
    comercial = f"""
    Visualizar campos de impressão do ticket;
    Recalcular impostos;
    NFe em contingência via SVC e FS-DA;
    Melhorias na classe de imposto para quem trabalha no dia a dia;
    Relatório de vendas por situação tributaria;
    Relatório Gráficos;
    Efetivar operações sem financeiro;
    Medição;
    Relatório vendas Comissões;
    Relatório de vendas por vários períodos;
    Relatório de vendas por top itens por hora;
    Relatório de vendas diária por vendedor;
    Exportar xml e bot por data de gravação ou autorização;
    Importar produtos de outro movimento agrupando itens;
    Relatório de vendas por plataforma;
    Novos campos receituário ótica;
    Como colocar CPF e CNPJ autorizados para download de suas Notas;
    Relatório de comissão com vendas liquido;
    Identificador de Ordem de serviço nos clientes;
    Envio de orçamento por e-mail;
    Relatório comissão de vendas por serviço;
    Comportamento incluir novo item;
    Relatório de movimentos apagados não funciona; 
    Recalcular preço ao carregar movimento na tela de saídas e validade para orçamento;
    Erro ao selecionar uma Classe de Imposto para o item 0;
    Validade de preços em vendas;
    Unidade tributaria na NF;
    Utilizar situação do movimento (status da venda);
    Venda de produtos em M2 e M3;
    Etiqueta de entrega e-commerce;
    Venda com entrega futura;
    Cliente comissionado;
    Editar imposto manualmente;
    Relatório de vendedores por curva ABC;
    Relatório de lucratividade por venda detalhado e resumido;
    NFSe integrada no E-Trade;
    Configurar busca de saídas no E-Trade;
    Carta de correção impressão;
    Qtde saída e entrada em modo manual;
    Transformar reserva em venda;
    Nota fiscal referenciada;
    Relatório de produtos com acréscimo;
    Gráfico de vendas por dia de semana resumido;
    Relatório de vendas por dia da semana;
    Valor mínimo de desconto em vendas;
    Relatório de ranking de lucratividade;
    Relatório de comissão resumido;
    Relatório de vendas por forma de pagamento;
    Campo personalizado na Ordem de Serviço;
    Como editar valores no XML de devolução para o fornecedor;
    Relatório de comissões por data de efetivação;
    Relatório de vendas por dia de semana resumido;
    Personalizar campos da OS;
    Edição do fator de conversão no momento da venda;
    Relatório de vendas por adicionais;
    Relatório de vendas por classificação;
    Relatório produtos ABC;
    Relatório notas por CST;
    Enviar PDF da NFCe;
    Relatório de notas emitidas por cliente;
    Empréstimo de mercadoria;
    Relatório de movimentação saída de produtos;
    Clientes atendidos por vendedor;
    Relatório de vendas por tipo de recebimento sem agrupamento caixa;
    Configurar exibição de contas vencidas e limite de credito na saídas;
    Consulta automática de Limite de Crédito na tela de saídas;
    Consulta automática de contas vencidas;
    Campo de UF e Cidade na nota avulsa do MDFe;
    Relatório de vendas mensais com descontos;
    Relatório de vendas diárias com desconto;
    Romaneio;
    Relatório vendas por forma de pagamento com Ticket médio;
    Relatório comissões por valores recebidos;
    Relatório de Ordem de Serviço;
    Informe peso dos produtos para emissão de nota;
    Relatório notas emitidas com filtro por data da venda;
    Relatório totalizador de vendas;
    Filtro relatório de entradas por emissão ou cadastro;
    Puxar qtde e especie do frete na tela de saídas;
    Relatório de movimentos;
    Tudo sobre o relatório de vendas por recebimento;
    Impressão Carta de Correção eletrônica;
    Enviar movimento por e-mail com ticket customizável;
    MDF-e;
    Importação de produtos de múltiplas notas para devolução fornecedor;
    Relatório de lucratividade agrupado por produto;
    Ordem de serviço - Tudo sobre OS!;
    Relatório comissão por venda;
    Emissão de nota com informação de pedido;
    Teste nota;
    Erro no envio do bot e de notas fiscais por email;
    Como enviar nota para o exterior;
    Envio de orçamento por e-mail;
    Como gerar nota de devolução importando XML do fornecedor;
    Utilizando data e hora nos movimentos;
    Trocar tabela e recalcular valores;
    Otimizando o preenchimento da transportadora nas vendas;
    Utilizando referencia interna;
    Configuração e impressão de boleto no E-Trade;
    Como trabalhar com crédito de cliente no E-Trade;
    Relatório de venda de produtos diário;
    Inutilizar NF-e/NFC-e em Lote;
    Configuração adição de novos itens na tela de vendas;
    Análise de lucratividade do movimento;
    Inutilizar NF-e/NFC-e;
    Inutilização de nota fiscal avulsa;
    Relatório vendas de produtos por cliente;
    Relatório descontos por produto;
    Exportar XML;
    Relatório de Notas Fiscais Emitidas;
    Venda rápida;
    Módulo Comercial;
    Relatórios de lucratividade;
    Relatório de lucratividade por produto;
    Exportar arquivos XML e Notas Fiscais Eletrônicas para a contabilidade;
    Relatório de Comissões;
    Relatório de vendas por cliente;
    Exportação XML;
    Relatório de NF-e;
    Relatório de vendas;
    Notas de Contingência;
    Venda Rápida;
    Saída de produtos""".split(';')
    comercial_f = [data + ' ' + categorias[1] for data in comercial]
    comercial_urls = f"""
    Id=0e1a9da6-1895-4f6f-9c5f-03d448c4ba2e;
    Id=0aa745e6-922b-4d4d-b092-ef94efd220f7;
    Id=5f13a4d4-2c03-4ce9-9965-d1545ce2fa91;
    Id=23d3cbcc-69d0-40b4-b1cd-8288d86f8d46;
    Id=fea1e690-8190-4531-969f-6bed78ae1561;
    Id=6b414d09-dcf5-4415-8598-2d0e1e233fe7;
    Id=d348cb10-9e97-4c2d-b778-9bf99d4a0491;
    Id=e817ec49-91b8-4c6d-a878-a72dea26ae73;
    Id=322ccc6a-14cb-40ce-b1bd-eb379d507619;
    Id=bf2c37d2-6cf1-4038-8bfa-4de80cac3f93;
    Id=5ffcb62e-5e48-41cf-bbb1-80fde186d2ae;
    Id=afd757db-aa05-493e-a6ed-43b4f853c881;
    Id=71f4f69b-19a5-478a-a893-29a8028059fc;
    Id=e3662b69-b52c-415c-9460-afd2a44cb498;
    Id=ed7a95df-3d41-484b-abd1-365cb00669b1;
    Id=27e0f9c9-a578-4858-b019-53cd01ce7cee;
    Id=8ac99843-27d3-4a34-a05f-8148f950c32e;
    Id=aca55103-6b26-418c-b849-2daa9c5a2c03;
    Id=9738963b-42b4-4bde-abe3-738197e48c0b;
    Id=41b47258-ca73-4e30-b93b-094b1bd0793f;
    Id=a34e0052-2f44-4165-98e1-539009328722;
    Id=fc601c9d-b2ff-420c-a053-3fb7ea681857;
    Id=7b031483-ac99-49af-ba6c-ade55cdd34fe;
    Id=70e42581-cd45-4c15-be86-cbbd1025df8c;
    Id=789ec1df-9cde-42c6-b31c-559fa7844e03;
    Id=636bd8cf-e27f-42c2-8ffb-3e592e131d58;
    Id=1d873e2c-d3c3-4c70-b458-73ba96241a9f;
    Id=3da50cf4-6773-472c-81d0-55ca7ab1d05e;
    Id=c447e8e4-f71e-4b1d-af40-5481056206a3;
    Id=0447ab9f-caff-4321-b1cb-06a445bdea70;
    Id=b0d0cf3a-5615-4b99-9591-c0f99e2498d2;
    Id=05f137f7-5213-48b6-94e6-170ad27cc571;
    Id=8d1fd027-e604-4801-874c-a1b3d855d202;
    Id=3eaa5098-90bb-4775-97ed-1643141aa6a5;
    Id=6766be03-055d-4865-8e38-eaa08b9a5688;
    Id=58aaa7cb-53c6-4532-885b-2c1b2d5f0ea8;
    Id=8f761b35-7598-4ae0-93aa-11f7de96a0ae;
    Id=4cef6889-278e-444b-9cef-ccbc109ca077;
    Id=ee6b28ac-c520-4604-b6a7-6893bf7915d5;
    Id=0b8531ad-e4cb-4c1a-9fee-048b825a1f3d;
    Id=72c6d24e-5939-4df7-9c43-803f6e815deb;
    Id=a43b43aa-a39a-481b-9f8e-d7e247709cbb;
    Id=9b2bf5ce-97a8-4d1d-ba8e-24dce873ae0b;
    Id=888417f6-0063-4c33-af60-2b4714c00395;
    Id=a7cece69-52d8-4797-ab13-bf03471ad033;
    Id=67adf685-6b41-49b5-bc4a-a82421d78f5c;
    Id=cbbc9d07-e41e-42b2-ba76-e9dbd5f37255;
    Id=c6cc1357-1902-47f6-813c-bebd4b9a883c;
    Id=d5620c03-f231-424a-bc3e-04b41245e127;
    Id=c15a1804-71a8-4abc-98aa-4c5d08b7db51;
    Id=1e200ff2-12d2-4670-b36b-fb03871c6d8d;
    Id=293484a6-a723-46a5-a7e3-75d3774a622b;
    Id=1b97cef0-035f-49bf-86f5-c3b21a413894;
    Id=5bf3ef4d-4f03-4072-a407-f769451dde71;
    Id=b60d6905-a09c-4452-b903-9efb9482df1d;
    Id=7177786e-1ebc-49d0-8989-5289713113ec;
    Id=5d8f86dc-8cd7-4f6f-a69b-b574b78204b4;
    Id=d0bd8181-9f39-4d74-bcb8-03a28ff5eae0;
    Id=9dcaa020-ca5c-4608-ac54-890328af9025;
    Id=24e86d4f-c4c3-456a-ae41-a1cf521ca795;
    Id=8042f364-5dfb-4c83-be99-74512be2888b;
    Id=1cbc2023-7329-4870-9ec2-7bddcc1dc645;
    Id=df7e1910-b205-4d5f-b0fd-b55b82d116ea;
    Id=1582310c-3b9a-4eff-aabe-4651cf444a4b;
    Id=a0a92e5e-6136-4c1f-b378-ed42d66f5171;
    Id=7eb5cad9-8384-4e5b-b713-bb113dfe9382;
    Id=20dd006b-389b-4978-8390-cf9ae0283b40;
    Id=aac88f7a-a32f-4d65-aded-4a2093060d77;
    Id=cf31cc08-a2fa-4094-9123-969535167ad3;
    Id=1ef4882e-d465-4b5b-bd28-cc0e855d416f;
    Id=883aefda-1904-4d7c-a536-efec62505349;
    Id=9b793bbd-8918-43eb-88c0-3cfde5df28fc;
    Id=bed637b7-929d-4d94-af33-5923149e5936;
    Id=049a7cdb-2954-4bc7-95b7-e0538e55e1ef;
    Id=b4a1e182-74a0-46bd-ae4d-09da7a33892b;
    Id=cd8e992f-156c-4296-9cff-3317b5a6e4dd;
    Id=b9f0fb0d-6f00-41cc-afad-6ca6243cd732;
    Id=1bf971ff-d7ab-450b-9889-189a8919e1f3;
    Id=3d93a931-b47e-4a20-be87-4e47d85091e9;
    Id=5610469d-4155-4390-83db-7fe96e7f23d9;
    Id=178dfb57-8f7a-4321-ab75-3c7b006ef05b;
    Id=1f822cbb-5934-48de-a0b1-e6d56b04e906;
    Id=6e787a17-3dd7-496f-b74a-37a5530490b1;
    Id=cb239fec-c64b-47ce-bab6-114170848471;
    Id=77d2a157-2e2b-413f-831e-c39791ba8f64;
    Id=a991cc8d-7113-4200-b0ec-30bfdca7a9bf;
    Id=2dc2cf81-5942-441c-8918-9b14685e9898;
    Id=7e1e7021-5fc8-4bb3-a5cb-043f6801cc57;
    Id=47d2d200-3a12-43a8-b007-cb9483e7b4b1;
    Id=b99522a3-021a-4e49-bdf0-f3208aa535f0;
    Id=658ca80f-595e-4265-9864-ecd1f0ac6a96;
    Id=d6b8b173-13f5-4945-86e5-108bbd896d0e;
    Id=82315c57-451f-4f8b-9e15-17423f74b461;
    Id=284e7b45-dcdc-4f2e-9280-6bd0e8ee6cea;
    Id=2a119dfc-8a16-4101-bb4c-4327393fba0d;
    Id=937fc4d8-b04e-4d3f-9b93-7c6db912014a;
    Id=7507935d-24ae-48fb-9088-18f9a26cf8d2;
    Id=1d340672-99fd-4566-ba9a-1ac214248318;
    Id=392b416c-d183-4299-8c4a-da237c39e3a6;
    Id=48329e0b-abe7-40ab-b194-f66d8bc62eaf;
    Id=48ba6c45-b413-4976-b334-0cc5e9e21efe;
    Id=5f314c98-c5a1-4a1d-8260-bcf1c6c2e2a7;
    Id=1698c0b8-2a39-4a7d-8a8a-87a6a2bc5cc6;
    Id=fc33fc1d-b311-4228-955a-d21a2e6739d8;
    Id=37938d51-8f00-41b2-aee7-3d23299ce266;
    Id=e6765c6d-3ce3-48e0-bbb6-c9b9ad096b7a;
    Id=27684109-b5a2-4db9-954c-eeedee7c11d9;
    Id=4325151a-b757-4bb2-829b-9232e98a1141;
    Id=df5076a3-06fc-4c80-bf2a-94f0d3dedc22;
    Id=1ef11a51-e50b-4c3b-933d-85848e1d7377;
    Id=6cd0de79-602b-44ac-8d47-e9041dc8589a;
    Id=205b29e4-678e-4be2-b101-079c5d7a354a;
    Id=d72a81c5-cb5a-4710-ad9a-7db23a4cc02a;
    Id=66f2cbdd-3993-4989-8fb7-c0656ae9617d;
    Id=41c44e08-1a31-4d85-bc28-f2f9d2108667;
    Id=57ef01f9-aa85-4f9e-a4f9-46ac421abf89;
    Id=28e061b0-6c7f-4713-b531-4307f76e33f2;
    Id=0b781bb7-0ab2-4b8b-93ca-aec5f6a3d0df;
    Id=effdb2b7-1627-44ec-b2b7-b80a53cab577;
    Id=6e8b1730-81d6-438f-be81-46ab70d978d3;
    Id=1e9ca12e-2aec-497b-a426-408d9a20a4a4;
    Id=05e3fa98-19ac-45b4-ad3f-36066f8cb12c;
    Id=5c58aca9-ac14-4901-9d5d-312e38c57878""".split(';')
    comercial_urls_f = [fixed + data.replace('\n', '').replace('    ', '') for data in comercial_urls]

    # ---------- FINANCEIRO ----------
    financeiro = f"""
    Calendário financeiro;
    Configurar impressão de Carnê;
    Fechamento de caixa paginado;
    Configurar grid para exibir contas a pagar e recebíveis;
    Pagamento de contas a pagar com cheque de cliente;
    Explicando Demonstrativos; 
    Recebíveis não aparecem ao buscar na grid;
    Administradora de cartão - PIX;
    Filtro de contas entregues no relatório de contas a pagar;
    Filtro de contas a pagar por centro de custo;
    Clonar caixa;
    Exibimos o nome do computador na tela de caixas abertos;
    Permissão para fechar caixa na tela de caixas abertos do E-Trade;
    Carnê rápido - Não permite reparcelar recebimento rápido;
    Relacionamento de contas a receber e pagar em lançamentos bancários;
    Relatório de recebíveis agrupado por administradora de cartão;
    Configuração de caixa para bloquear mesa, pedido e delivery em aberto;
    Forma de pagamento;
    TEF - Habilitamos no carne rapido;
    Bloqueamos a edição de juros e descontos no contas a pagar e receber;
    Caixa integração;
    Delivery - Definir caixa padrão;
    DRE com seleção de tabela de custo;
    Relatório de recebíveis por plano de contas;
    Budget - Software para projetar seus gastos;
    Cor no plano de contas;
    PDV - Zerar caixa continuo do E-Trade;
    PDV recebimento - Cadastro formas de pagamento 1/3;
    Relatório recebíveis pagos resumido por cliente;
    Re-impressão dos movimentos de caixa;
    Configuração ticket de recebíveis;
    Fechamento caixa resumo de pagamento;
    Forma pagamento: Valor mínimo;
    Tipo de financiamento nas operações de TEF;
    Relatório de contas pagas por emissão;
    Modelos de Documentos Fiscais;
    Atualizar cotações ao iniciar o E-Trade;
    Informações fiscais no contas a pagar;
    Contas a pagar por data de competência;
    Confirmação de recebimento do boleto em contas a pagar;
    Confirmação de recebimento de boleto de contas a pagar;
    Gerador de contas a pagar;
    Relatório de contas quitadas em atraso;
    Relatório de movimentação de conta bancária;
    Voucher nas administradoras de cartão;
    Como funciona o Layout de Ticket na forma de pagamento;
    Inativo nas administradoras de cartão;
    Debito pré datado nas administradoras de cartão;
    Taxa administrativa do cartão;
    Prazo em dias no cadastro da administradora de cartões;
    Prioridade configuração envio de ticket e DF nas formas de pagamento;
    Relatório de contas pagas agrupado por fornecedor;
    Relatório fechamentos de caixa;
    Relatório contas a pagar por plano de contas;
    Importação movimentação bancária por OFX;
    Administradora cartão - configurar taxas;
    Edição de conferência do fechamento de caixa;
    Melhoramos o carne rápido - Cancelamento e alteração de juros;
    Como utilizar recebimentos no bridge;
    Relatório de notas fiscais agrupadas por CFOP;
    Demonstrativo de resultado;
    Contas bancárias - Configuração da carteira de boletos e CNAB;
    Relatório de recebíveis por dia base;
    Centro de custo;
    Visualizar cheques e cartões no caixa;
    Relatório de caixa com data inicial e final;
    Módulo Financeiro;
    Carnê Rápido;
    Cadastro de Planos de Conta;
    Cadastro de Administradora de Cartões;
    Cadastro de Bancos;
    Cadastro de Caixas;
    Relatório de Contas Pagas;
    Relatório de Contas a Pagar;
    Contas a pagar;
    Recebíveis;
    Movimentação de Caixa""".split(';')
    financeiro_f = [data + ' ' + categorias[2] for data in financeiro]
    financeiro_urls = f"""
    Id=167c7aa7-3e50-4caf-ad8d-90576da2bae3;
    Id=7951628c-e9a2-425b-879a-e0b6d661e0cc;
    Id=efd26627-ffe9-4d15-bc9d-dd81d0b3cecd;
    Id=e62d6737-36e7-4728-a111-0f57a6aa66e2;
    Id=106cd0e6-2711-4946-bd23-3abef9d625fd;
    Id=71ede200-fe42-44b9-8f5a-6ebe7bdde70b;
    Id=641d1d31-4261-413f-b84c-89da3dc2a0ce;
    Id=9161c98a-6054-4189-b20e-b61acc40a722;
    Id=f24b6484-0dc1-417e-86ac-c49627039a70;
    Id=7312384f-3dee-4a45-b625-d27ce2c3750a;
    Id=7c847f96-9760-4d47-aff2-208549177e2c;
    Id=99f77e65-ea0b-4090-bb67-91bf5bc1c95c;
    Id=f9ce8e7f-5386-4bd3-aace-86800994830a;
    Id=a3b38aae-80d6-4649-9e4c-252183033672;
    Id=784da0a4-4a66-431b-b18d-ae32eb68fd5b;
    Id=2f8b4e00-f17e-4180-ae2b-c311aee40f4e;
    Id=80f407e4-7309-4c1a-813c-df59e88ec2ff;
    Id=78f5d069-345c-43b9-8ba6-a7cfb0ed0b19;
    Id=226e2f41-334f-40de-855f-b92a8da7a150;
    Id=ff3e7ed3-131a-4ab7-aff7-4c57cca36c61;
    Id=76a9a8ee-849d-4ac6-aee4-28f254f64723;
    Id=838be37b-8468-4d04-a1e0-91a41171dbe1;
    Id=7960e1b8-388e-4ff3-9a68-cd191a575b71;
    Id=6e53fdd6-ed0b-4d6b-8433-c97475ad66f8;
    Id=6aed64e4-55d5-47ec-97a2-131522d82681;
    Id=5ca39f6d-cb73-414b-8842-aed14de62fcf;
    Id=20392728-58e0-4c23-960f-406521abeb37;
    Id=9e263079-6e73-4992-8557-fb2eb32ea7f3;
    Id=58803c0e-f1c4-44cc-8343-6092f46f6b05;
    Id=cab01588-8289-4eba-b0f6-5e73d4721201;
    Id=677dbe00-5bd8-4260-8841-e89002021827;
    Id=bce7bd47-d626-4b6a-a0f9-10c0a765b7d3;
    Id=955ff87e-1141-4c34-8910-aede0452d4a4;
    Id=188874c9-e27a-4a98-a689-61719a2c478a;
    Id=eb0f6e93-b5dd-4239-82a0-2b5664974b6b;
    Id=afc9da1a-b86b-474d-8ba9-a3ae8e06ce08;
    Id=62052824-afc3-45a9-8065-c60250726250;
    Id=b5a87913-57c3-4e67-856a-45302c13cbe8;
    Id=5243cd04-6814-4d78-bed6-58b3c9f7f5bb;
    Id=adf2df95-cbee-4eb6-9591-b9e6b98e3807;
    Id=d54cdd86-954c-4ec5-b752-7b79b07ced2d;
    Id=8973ed4b-6c45-4b70-84c4-7768280386e9;
    Id=191b67ad-879f-4630-aa40-fe3c13c02089;
    Id=b68ec7d0-be2b-4e74-99a3-0e03f09e41ce;
    Id=05b1dcec-fd03-4e3d-a039-070960b958a2;
    Id=fb7029d4-f87e-43b8-9224-eefa0b03c97f;
    Id=4159c0fa-752e-4df0-b439-6d7b9d5dfc82;
    Id=d5883d15-6a57-43d9-a8a8-7fe155e18322;
    Id=de5d0479-fda7-4b0d-8892-e79e09f96a8b;
    Id=d305bcc4-ef32-4834-850e-9d7639f223d6;
    Id=58fad4d1-2819-4c95-9676-90e70ce8b6bc;
    Id=238ba451-aaa3-46f6-8ab6-7069bcd02030;
    Id=8540ac86-7c9c-44c8-bed6-4255e54ee30c;
    Id=f24a3e5c-5dbe-4a3c-a3f0-4e1687ccb919;
    Id=51ea2f4f-0bf9-403f-bbad-c10dc58f68e7;
    Id=a44c3f6a-1744-4f7f-9353-cd2750968079;
    Id=4024d074-6360-412e-9d18-b01181fd6fb1;
    Id=1b2e24a6-7d07-4c6a-abce-ddc9e47ef2b7;
    Id=e040d135-7705-47c9-8582-294f6fe2570d;
    Id=03f5bc3a-1046-4de8-9968-3a03999722e3;
    Id=57bb9ecd-d676-4366-8def-d709790e126f;
    Id=ab9a48cd-82b0-4460-a0e2-af5cc278411a;
    Id=5fcb243e-7fe8-4377-82f9-9670f3d25e9d;
    Id=efa6b6ad-4d92-450d-8a0c-4b2429133b70;
    Id=0975dbe2-4099-4b05-9b8c-d01992fd79d3;
    Id=575ba278-76d2-4c48-9b8f-a5516e5739c5;
    Id=e6638eb8-7110-4232-84eb-5fbc855dbc72;
    Id=48239ad4-010f-4175-b274-d28414d582f0;
    Id=cf84921a-15b9-4f3e-b33d-81979b07da18;
    Id=ddab0b24-0e6c-4ce5-a119-3724391e649b;
    Id=da786202-3cfd-4e1e-9c7e-ceaa907b5404;
    Id=e8596c02-18b0-4781-b726-1fc66d60e019;
    Id=806a70eb-9873-47f4-b796-d540d73e7e3d;
    Id=08da8817-f49d-4f79-8817-2f386f25db7d;
    Id=3b19d87f-81c9-4c11-b23d-4590676effa3;
    Id=f06c7320-bb95-490c-ba3a-f9b176f74343;
    Id=0b8875b4-a596-4f97-89d9-b4a97bc58f48""".split(';')
    financeiro_urls_f = [fixed + data.replace('\n', '').replace('    ', '') for data in financeiro_urls]

    # ---------- CRM ----------
    crm = f"""
    Bloquear código principal do cliente;
    Ficha de cliente;
    Múltiplos endereços de entrega e cobranca no cliente;
    Campos novos no cliente;
    Foto no cadastro de cliente;
    Personalizar campos do Cadastro de clientes e fornecedores;
    Busca de endereço por CEP;
    Busca de cidade no cadastro de clientes;
    Busca de clientes - Configuração e uso;
    Receituário de ótica no cadastro de clientes;
    Visualizar observação do cliente no PDV e saídas;
    Configuração de busca de Clientes e Fornecedores;
    Ilimitados e-mails no cadastro de cliente;
    Capturar dados cadastrais do cliente na Receita Federal;
    Incluir produtos etiquetas avulsas para produtos;
    Configurar campos a serem exibidos na tela de busca de cliente;
    Informações de SPC no cadastro do cliente;
    Relatório de clientes por bairro;
    Configurar campos obrigatórios no cadastro de cliente;
    Vendedor obrigatório para o cliente;
    Relatório completo de clientes;
    Dia base e limite de crédito para clientes;
    Tabela obrigatório para clientes;
    Módulo CRM""".split(';')
    crm_f = [data + ' ' + categorias[3] for data in crm]
    crm_urls = f"""
    Id=884c8e1a-fc65-43ba-9d6f-07d70f7c2124;
    Id=fba9b6a2-545e-493a-b3c6-72de70274fc8;
    Id=d08448f7-7a2c-4c8e-bea6-b4f97ad168b4;
    Id=9f7ed5c0-6ecc-42e7-a875-15958d138141;
    Id=26bc2d8f-b7bb-4fa4-bb52-58bee35e0aa6;
    Id=bc1db249-e5c2-44cc-9a49-9cee2051a2b0;
    Id=844803c8-0a61-4f9d-a722-36ee8809356e;
    Id=b275533d-d660-4abe-8be4-adb76f53e1f8;
    Id=38ff0ebe-fa66-4d02-9ec3-e0ffbab08dea;
    Id=5fc6a344-e17c-448f-a62c-e556a3746a49;
    Id=bd9cd578-c15c-426a-b1ee-d00a3c8ba745;
    Id=444a2a9d-7c84-46f2-83a4-bda65e790932;
    Id=d1e004ca-f2d6-4c8d-8ee4-56682b1bd582;
    Id=29b6f70c-35db-4c5f-8cfc-a107ef314e36;
    Id=d23c1f7e-e08f-4cf1-a496-eec471999563;
    Id=c8404b65-b9a8-45d7-8d7b-5f8b656540a0;
    Id=c6f08c99-2294-4658-a94b-1d5b83d0449f;
    Id=a5ddd563-5efe-424c-9e33-23101c943ff6;
    Id=32e4dbc6-5a5b-46ca-a500-9cb9dc73df6e;
    Id=6af47ed4-f724-4d80-b0c7-140697e96937;
    Id=ed7f6cba-6a46-40d0-927d-bc58223fd6e0;
    Id=b71f3da8-fdbf-4a36-b039-899ec18b630c;
    Id=1e57cd10-63b2-4e9d-8c9f-01b5b411b96c;
    Id=c04ff60d-ec9c-499c-9559-e39e6d699fa5""".split(';')
    crm_urls_f = [fixed + data.replace('\n', '').replace('    ', '') for data in crm_urls]

    # ---------- CONFIGURAÇÕES ----------
    configuracoes = f"""
    Novos componentes de filial, caixa e classificações para o gerador de relatório;
    Contingência em Formulário de Segurança para impressão de Documento Auxiliar - (FS-DA);
    Remodelamos os grupos de permissões dos funcionários;
    Faixa de enquadramento;
    Regime especial;
    Configurar layout NFe;
    Configurar aviso vencimento certificado digital;
    Layout Carnê (modelo);
    Componente relatório: Pessoa;
    NF-e personalizada (Modelos);
    Sócio filial;
    Pré visualização de ticket;
    Não é o Braia é o E-Trade mais rápido, veloz e furioso!;
    Como configurar permissão para alteração de preço para cima;
    Configure no ticket a impressão de produtos e serviços separados;
    Setor funcionário;
    Componente tabela de preço;
    PDV - Configurar impressora para fechamento de caixa;
    Configuração para cadastrar mais de um cliente com mesmo CNPJ ou CPF;
    Permissões;
    Novos campos documentos e pagamento no cadastro de funcionários;
    Erro de Desconto na Sincronia com o Mercos;
    Testador para balança Toledo;
    Configurar Ticket com fonte, negrito e tamanho de fonte;
    Certificado Instalado não aparece no E-Trade;
    Produtos Cancelados Saindo na Etiqueta de Movimento;
    Solicitar ticket;
    Configuração Zoiper Novembro 2020;
    Download XML notas de entrada;
    Primeiros passos;
    TEF Acqio (configuração);
    Impressão de ficha de pedido;
    Gerador de relatórios - Parte 2 Totalizando;
    Gerador de relatórios - Parte 3 Agrupando;
    Gerador de relatórios - Parte 1 Básico;
    Gerador de relatórios - Parte 1 Básico;
    Favoritos relatórios;
    Relatórios personalizados (Modelos);
    Permissões de acesso e visualização;
    Ticket cozinha;
    Explicando particularidades no envio da nota;
    Senha de retirada de pedido no Ticket;
    Utilização do módulo IFood;
    Bot verificar pendências;
    Processo de transformar reserva em venda;
    Configuração de verificar pendências - Bot;
    Liberação por digital com Control ID;
    PDV recebimento - Imprimir condições pagamento no orçamento 2/3;
    PDV - Impressão opcional de comprovantes;
    Nova tela de login;
    Priorizar logo partner no PDV;
    Cadastro de motivo de cancelamento de produto;
    Cadastro de Digitais;
    Nova configuração de ticket para impressão de NFCe e CFe;
    Agenda inicial;
    Configurar ticket na forma de pagamento;
    Token captura dados clientes;
    Troca rápida de filial e usuário;
    Particularidades por Estado no Envio de Nota Fiscal;
    Implantação TEF Cappta - Stone;
    Configurando Bot para envio de arquivos grandes;
    Recuperar senha do usuário;
    Ativar modo Dark no E-Trade;
    Ticket - Como configurar imagem e ordem de impressão;
    Como configurar etiquetas;
    Configurar dados pessoais e de suporte para revendedores;
    Impressão da sequencia nas etiquetas de produtos;
    Criar grupo de permissões de acesso;
    Configurador de Etiquetas;
    Endereços WebServices;
    Layout de ticket (Modelos);
    Layout de Ticket;
    Configurar substituição nas operações do E-Trade;
    Permissão de operação por funcionário;
    Permissões de acesso por filial;
    Configurar url do QRCode da NFC-e;
    Módulo Configurações;
    Informar Seriais;
    Relatório de Log;
    Cadastro de Servidores de E-mail.;
    Cadastro de Operações;
    Configuração de Impressoras;
    Cadastro de Funcionários;
    Cadastro de Filiais;
    Cadastro de Clientes e Fornecedores""".split(';')
    configuracoes_f = [data + ' ' + categorias[4] for data in configuracoes]
    configuracoes_urls = f"""
    Id=f903f0b9-e91a-4f28-9e94-7fc76aac3fdf;
    Id=de46dd37-db8c-47ee-b098-3411da5381a4;
    Id=da2f6220-177c-459d-a485-759962c31087;
    Id=be60f8e9-c98b-49ea-ad90-11e76b803117;
    Id=e352b7c1-d292-4e7b-b09c-446124f2374d;
    Id=be770094-118b-47f2-9db4-4d83901acbb3;
    Id=90d0ceda-417d-402c-b589-ec0c87a6432a;
    Id=51c40e10-a6b4-48fc-aeb8-16133c6fb431;
    Id=d6ad9c13-e576-478b-bcfe-2a7264e501a2;
    Id=9f34595a-34e5-429c-82c8-413e926c8fa1;
    Id=edf8c245-fe68-4c8e-adc9-335e8aa721cd;
    Id=da4f9f40-d9b1-4158-aaf8-27279cee0352;
    Id=21723d4a-d1ca-4770-b78d-85fdae1d6541;
    Id=19e49cd3-037e-428e-8246-6e07e9d7faa5;
    Id=30f793c8-68d6-492a-ab12-2578d3c41217;
    Id=284ba011-8491-410e-b846-2236f93be26d;
    Id=24d113d1-2786-4935-a6ed-abdadbe44a29;
    Id=50579af7-fc7c-4ab7-a306-6d80f9b9b38c;
    Id=6d181ac8-7b38-4797-87ea-986d008e5d81;
    Id=12637b9c-04b9-4d7c-ba9b-8ca62d424e3e;
    Id=386deecf-cccb-4819-8cd9-36657a2fe5d0;
    Id=20491bf7-21b7-4909-b576-2b7e73987bf5;
    Id=06b1a5e3-8ac0-4420-9d14-6d2a3699d8d4;
    Id=69219d61-c3da-45eb-92e6-59270f4e0039;
    Id=a1edcfc6-6fef-46f9-8f1d-fa0911c519cb;
    Id=419a6de0-d9a2-4fec-a33c-0b8a06fb280f;
    Id=6378a8a3-ff62-4c2b-877a-24270afe1cb0;
    Id=030bb81e-666e-49b0-a0f4-40c51b8bd4e4;
    Id=ed0723af-ffbd-49ca-b2a3-eaaf522d7d6e;
    Id=232bacab-d3d4-4a22-8ca5-e117fdaafd0d;
    Id=44f623e6-712b-4e3c-b4d5-641c59d557bb;
    Id=a28b62b7-0b77-4a86-b5b0-cc7ccc69c2c9;
    Id=5cb8b781-e927-4853-a508-fd540e66d9b2;
    Id=8ce1dc5f-8931-465a-ae3d-7ab73fcf92ce;
    Id=540f2d7f-489d-49db-bf6e-2de8df349b5b;
    Id=41c82332-4dfd-4a1d-8bbe-3a4388fea708;
    Id=228ed1f1-1abc-4eee-8b63-13f3b7269bf4;
    Id=2efd20b6-d654-4eed-97c9-f7e9d295de6c;
    Id=204acb0a-e71e-4fab-ba2d-d704be99d53a;
    Id=54117ebd-430a-4c6a-a152-b120c6f4660b;
    Id=fbe40ab7-3152-40ab-80a0-8eb5ec4163f2;
    Id=aa783f7d-bdb5-4618-9741-fba51c2a699b;
    Id=86ee5137-2632-4d12-aeaf-be0d01763e11;
    Id=e80a3dba-717e-415e-9121-2851aecd3f94;
    Id=5f9b7317-9e53-4acc-ad10-4b9fbdf9a2f1;
    Id=4c9c7efa-11bd-4d55-91f1-8fb50c3ed299;
    Id=1fa2935b-1e18-4f11-9d21-1bb69132f122;
    Id=c089842c-92c4-4b7f-a17e-ea90f6326cce;
    Id=c1e7546b-54e5-469c-a6b1-8ed8725f675f;
    Id=41008fb9-6a15-4312-a3fe-959225701054;
    Id=269fffac-79e9-43bf-ad2f-59f41e64114e;
    Id=fd3b961b-2014-4305-aec0-d1959addcf76;
    Id=4c0f836c-eee4-4c6b-bf88-730a24c65309;
    Id=1d6d9243-50b7-444b-9134-cef67f6e1a6f;
    Id=0e46d8e4-d590-4390-b269-6055974404dc;
    Id=d72e6097-21b5-4b91-a63f-34ce0884d860;
    Id=88ee85c1-abd7-4a15-83e6-b34569e76f9b;
    Id=3d2e2ec4-8f6a-4aeb-9348-b17540ec4290;
    Id=598518c9-b1ef-4d27-bfa5-8d147f4c2fba;
    Id=325f728f-85c9-4d2f-8933-0c8aeabbca0b;
    Id=9aee59d9-e465-4983-bbd2-7001ad6ffd30;
    Id=34677c87-1aab-4dc6-baec-36e3b92e4ced;
    Id=68f28051-2be8-499c-93da-9d85930b90cf;
    Id=12edc8e5-3652-447c-8224-1dde0726cffe;
    Id=34b23b56-aaba-4e19-92de-6b040cd4ed59;
    Id=45edd37e-f31e-4b08-aa94-8963fae7d70c;
    Id=5ec9265d-e970-483f-a2c5-cf45feff6efe;
    Id=f8cf83b2-3530-4287-b89a-d0b5cd56e21d;
    Id=69957e15-e7aa-4a39-a76f-8304f1ce316e;
    Id=480686b1-e7dc-4472-ba44-8953279de677;
    Id=3f415123-491c-4975-a396-29c95768c41c;
    Id=024dc804-5d8f-43fd-a5f1-0af747a1cc57;
    Id=8ffa74fe-77fe-4232-ad55-1b99471609b4;
    Id=94f6ba7b-27d5-4160-837e-6cc62ccca690;
    Id=89b8ae4a-11a1-4107-969d-ba72df33d10c;
    Id=e7e84c45-7bed-49dd-992a-ae4a7616711e;
    Id=d77f2e9c-8ac9-4953-8cf1-cdd3915dd6f4;
    Id=aa71b2d3-cdc2-4a55-b7a0-2116851c19cc;
    Id=ea6f1869-eab6-4839-ab94-1530e1b7de5a;
    Id=9f284dd7-190a-4365-97af-4fc6e4a83aa3;
    Id=0da48f02-c79d-4331-bb2b-a73ec22897d9;
    Id=2f1c1574-5d28-4cb7-af04-deb39e4f82a6;
    Id=a86090ca-b5ae-46f4-a749-c85c6b00e071;
    Id=94e81ea7-cb01-4c9b-800f-bf46b8e11ad5;
    Id=46622eac-d419-45ce-9293-96502c2a8dc5""".split(';')
    configuracoes_urls_f = [fixed + data.replace('\n', '').replace('    ', '') for data in configuracoes_urls]

    # ---------- GOURMET ----------
    gourmet = f"""
    Filtro de data e hora no relatório de entregadores resumido;
    Agrupamento impressão ticket cozinha;
    Menu TEF Gourmet;
    Monitor Delivery - filtro operação e botão efetivar;
    Gourmet fecha ao tentar informar os padrões. Não permite salvar as alterações nas configurações;
    Gourmet - Ficha de impressão para boates e clubes;
    Gourmet - Edição de comissão;
    Gourmet - Configuração para não cobrar comissão pedido;
    Delivery - Criamos no monitor a opção de desativar aviso sonoros e confirmar pedidos automaticamente;
    Delivery - Cancelar delivery via monitor;
    Gourmet - Agora aplica couvert em mesas já abertas;
    Gourmet - Permite complemento na descrição do item;
    Delivery - Monitor via PDV 4/4;
    Delivery - Monitor via Gourmet 3/4;
    Delivery - adicionar bairro na área de entrega 2/4;
    Delivery - Gerenciar via gourmet 1/4;
    Delivery - Solicitar valor ao realizar delivery;
    Delivery - Troca motoboy;
    Gourmet - Botão de pânico para a queda de energia imprimir todas as mesas;
    Gourmet - Colocar um pedido em espera;
    Gourmet - Como mover o pedido do balcão para a mesa;
    Gourmet - Agora é possível redimensionar os botões do sistema;
    Gourmet - Como mostrar o tempo de ociosidade na mesa;
    Cadastro de mesas em lote""".split(';')
    gourmet_f = [data + ' ' + categorias[5] for data in gourmet]
    gourmet_urls = f"""
    Id=d684e80a-0e6a-4fb2-a11f-e2a1e74e96ba;
    Id=b2210e70-43d9-4baa-8d95-e23065fc781b;
    Id=0994ded1-b60e-4325-95cd-aa6274ba8688;
    Id=63672268-c874-4fd1-9227-2d4b40c6ddd8;
    Id=1e8dd19c-821e-4340-a264-e4fa00ee5fda;
    Id=1b1cd29c-299e-4b54-9bd9-e4479cdd9ef7;
    Id=b3d647a7-dcd0-4c8c-857e-12e5061a7e27;
    Id=86c49244-9ffd-4cc5-bda1-3a430a2a71e1;
    Id=1c153dfa-14b5-4138-aa1f-e0d2ea62fe4a;
    Id=03b35a0e-42f0-4f43-a339-e8cc937ab28b;
    Id=ad576bf3-8214-41df-acb4-3166b36d09af;
    Id=039766bb-d47d-402c-ac6f-2986ef82d9a6;
    Id=02ed47cd-0d69-4ab3-9355-6537614df297;
    Id=3dea9195-2ff8-4373-b7cd-ca964d45e65d;
    Id=837740a4-ea31-47c5-972c-60154b236d29;
    Id=392ce0b5-1230-40b3-a078-ddfcf3953b03;
    Id=f2e4da36-4815-431d-9510-22e72e0a91a0;
    Id=ea180ca7-b2d8-49f5-960a-3b7e9924e416;
    Id=33e0fce1-134b-48e9-a84b-4e451a663ea0;
    Id=93bd93c6-67db-4671-9234-c453abf67076;
    Id=96279bbb-d0a9-437f-9c50-8352e353b736;
    Id=818583fa-2a18-4e36-8b99-231379ac43a8;
    Id=5c62b894-7b2a-44fb-aa7b-efb63431c2c3;
    Id=52bb5fca-a009-45e1-988a-0eaf84bbe736""".split(';')
    gourmet_urls_f = [fixed + data.replace('\n', '').replace('    ', '') for data in gourmet_urls]

    # ---------- PDV ----------
    pdv = f"""
    Mudanças na pesagem da balança no PDV;
    Visualização de comandas em aberto;
    PDV - Remover item por código;
    Tornar o PDV um Consulta Preços para sua loja - Totem;
    Configurar vias de impressão de nfce e comprovantes de caixa no PDV;
    Dúvidas sobre o Totem;
    Grupo de Permissões (Padrão) para operadores de Caixa;
    PDV - Contagem de dinheiro na abertura de caixa;
    PDV - Configuração de alterar preço unitário;
    No PDV, ao lançar o primeiro item ele não é carregado na listagem, porém ao lançar os demais ele aparece;
    Leitura de etiquetas de balança no PDV;
    Abertura de Caixa;
    Delivery - PDV não pede mais cliente pré informado;
    PDV - Cancelar comissão item e venda;
    PDV - Reimprimir item cozinha;
    PDV - Permite complemento no item;
    PDV - Confirmação de peso para etiquetas de balança;
    Solicita CPF em vendas a partir de R$;
    Emitir automaticamente ao informar CPF em vendas a partir do valor acima;
    PDV - Fechamento de caixa com conferencia de saldo e calculadora de notas;
    Novo atalho para configurar o PDV;
    PDV - Associar comanda na mesa;
    Troca e devolução de mercadoria no PDV;
    Trabalhar com adicionais no PDV;
    Como configurar botões do PDV;
    Configuração botões PDV;
    Como trabalhar com pré venda no PDV;
    PDV - Como configurar geração de credito apenas para movimentos de troca;
    Como cancelar uma venda pela tela de busca do PDV;
    PDV - Impressão de itens na cozinha;
    PDV - navegar entre vendas""".split(';')
    pdv_f = [data + ' ' + categorias[6] for data in pdv]
    pdv_urls = f"""
    Id=78e5d9d9-5e3d-4aba-8dd7-c13d73696556;
    Id=7b3df538-9c68-406f-890a-ba481316e43b;
    Id=17b282a3-e4c1-4e68-9326-081df59cfea8;
    Id=7e7e4821-edc5-4b13-a310-b82ec3ebd4cf;
    Id=85797b59-3c3b-45e6-8523-0fd8e86f7c0d;
    Id=f7ff5ce1-832e-45a1-ad57-28ee489a938c;
    Id=86be2e2f-096b-41cc-b611-0da19ce7d3ee;
    Id=ddc72bdc-ee0c-4617-8e00-821752270585;
    Id=68d66e3d-a09e-4513-a931-ee5650f21b42;
    Id=36d3c2d8-ddfa-43df-a69b-5121cf2fa1e4;
    Id=69ac0e5a-12c8-4b56-81ba-93adb4b38a38;
    Id=78e9265c-d18d-4157-a783-9f7718f3c28f;
    Id=c11c0a1b-b63b-4d66-9415-a3da161c14ad;
    Id=c4f7e164-aee1-4c3e-8deb-78276b66872d;
    Id=7148896f-53f5-475d-988a-a6b3eb3942c8;
    Id=cbafde14-0041-4ed0-b6b6-e6a57eff68ef;
    Id=57e0bcce-7ffe-4608-9561-ceb0fb99c790;
    Id=0014321b-a220-413a-94da-6051ca5d0e54;
    Id=24f29ff0-968b-4aec-8b53-d91852525936;
    Id=e197a426-7a2f-44cb-8c91-1e691f402026;
    Id=3e52da2c-6bdb-431a-9e40-8d116425b040;
    Id=838de0a3-c293-45a9-b6ee-0c8c62eed767;
    Id=14ad046c-2127-443a-bbf6-c78b026178a0;
    Id=2b828291-3000-460b-9383-78badd530ef5;
    Id=2f45dcc8-e126-4570-a1ac-ea36b7c76e59;
    Id=4c38b329-7f93-4a61-9898-10dd553224e4;
    Id=e8622111-5dd4-46c4-aee4-0082fc9a4dd6;
    Id=50dfc1f0-8bba-40ab-a18f-650ec19fb8fc;
    Id=b8c8430c-d5fa-4c70-a291-934d719ee0a6;
    Id=8e9cc6e0-df73-4937-95e7-c476ca3d0aef;
    Id=ff66898b-6cf7-4d4b-85a0-7be1cf02c7e8""".split(';')
    pdv_urls_f = [fixed + data.replace('\n', '').replace('    ', '') for data in pdv_urls]

    # ---------- GourmetDroid ----------
    gourmetdroid = f"""
    Gourmet Droid .APK (Minimo Android 6 );
    Habilitando os Recursos do Windows necessários para o GourmetDroid (Powershell Script);
    Gourmet Droid - Lançar itens;
    Gourmet Droid - Primeiros passos;
    Gourmet Droid - Configurações iniciais""".split(';')
    gourmetdroid_f = [data + ' ' + categorias[7] for data in gourmetdroid]
    gourmetdroid_urls = f"""
    Id=8a9e6073-0e9c-421e-af9a-926db6b00c53;
    Id=9aae059d-1b53-494c-b6db-e6240787eaba;
    Id=4d881330-89c3-4cb0-9da7-4c5dce6ce4b2;
    Id=67298c9f-f973-488b-8073-b321320bd3ce;
    Id=f3e29d01-eea6-4fde-8462-a45f9bca3e9e""".split(';')
    gourmetdroid_urls_f = [fixed + data.replace('\n', '').replace('    ', '') for data in gourmetdroid_urls]

    # ---------- SINTEGRA ----------

    # ----------- SPED -----------
    sped = f"""
    Alterar CST e CFOP na importação de XML;
    SPED entradas""".split(';')
    sped_f = [data + ' ' + categorias[9] for data in sped]
    sped_urls = f"""
    Id=f6a89f45-94d8-45f5-b34b-56ef530a4211;
    Id=8f3603f8-e46a-4e5b-8aa7-9654bdbdc4be""".split(';')
    sped_urls_f = [fixed + data.replace('\n', '').replace('    ', '') for data in sped_urls]

    # ---------- OUTROS ----------
    outros = f"""
    Configurar atraso na inicialização do programa de backup;
    Integração com Imendes - Configurar;
    Agora temos configuração no Gourmet para automaticamente adicionar um adicional ou bloquear sua remoção;
    Envio de fechamento de caixa por email;
    SPED - Ajuste CST e CFOP;
    Delivery - Configurar baixa de estoque;
    Configurar horário de fechamento e abertura loja Ifood e CCM;
    Personalizar campos de busca de produtos;
    Como trocar a senha do SQL pelo SSMS;
    Import TXT de produtos como você nunca viu;
    Pix - Tef;
    Configurando o E-trade para trabalhar em rede;
    Como instalar o SQL Server Management Studio (SSMS);
    Importação manual de arquivo CSV - CEST, NCM e Carga Tributária;
    Erros comuns no Gestor;
    Fotos produtos;
    Mercos - Erro na carga "Falha em um produto preco - Mensagem: Registro não encontrado...";
    Remover pedidos do delivery via comando;
    Limitações utilização Mercos;
    Porque NÃO voltar a data do bridge em clientes que usam parcelado;
    Como atualizar o E-trade;
    Limite de valor na mesa e comanda;
    Comercializar Scanntech - Integração Scanntech - parte 3/3;
    Utilizar painel promoção - Integração Scanntech - parte 2/3;
    Integração Scanntech E-Trade - Parte 1/2;
    Integração E-Trade com o iFood - parte 3/3;
    iFood - Configurar cardápio - parte 2/3;
    IFood - Configurar E-Trade - parte 1/3;
    Mercos - Ajuste IdMercos dos produtos;
    CCM - Receber pagamento online;
    Emissão de nota em Homologação;
    Faturamento produto e serviço;
    Integração CCM;
    Configurar CCM;
    5 - Mercos - Catálogo eletrônico;
    4 - Mercos - B2B;
    3 - Mercos - Força de vendas;
    2 - Mercos - Como sincronizar cadastros;
    1 - Mercos - Configurar E-Trade;
    PDV recebimento - Como utilizar 3/3;
    Como configurar o Multi-NF no Bridge.;
    Bridge - Configuração Token;
    Como o bridge trabalha;
    Tela de início e pendências do sistema;
    PDV - Listagem de mesas e comandas;
    UpdateService - Manual de funcionamento;
    PDV - Super busca agora filtra operação, cliente e vendedor;
    SAT - Configurar e utilizar;
    PDV - Configurar aviso de retirada;
    PDV - Abertura de mesa;
    Utilitário de banco de dados;
    Kit;
    Atualizador automático E-Trade;
    Conversor de dados para o E-Trade;
    Correção de erro bordas do PDV cortando;
    Apresentação Gestor E-Trade;
    Configuração Integrador - Gestor;
    Regras de sincronização do bridge para Nf-e e Nfc-e;
    Regras de sincronização do bridge para Nf-e e Nfc-e;
    Como configurar o bridge;
    Configurar o sistema na estação e servidor;
    PDV - Leitura de qrCode balança;
    Relatório venda de produtos no PDV;
    Cancelar mesa de Gourmet;
    Chamar o cadastro de cliente do E-Trade no PDV;
    Habilitar o busca preço de produto no PDV;
    Aprimoramos a retirada de caixa no PDV;
    Habilitar leitura de comanda no PDV;
    Habilitar leitura de comanda no Gourmet;
    Como cancelar uma mesa ou pedido no gourmet;
    Como retirar dinheiro e gerar conta paga no PDV;
    Delivery no Gourmet;
    Relatórios de itens cancelados no PDV;
    Bridge - Vendedores externos;
    Leitura de comandas no PDV;
    Fuel;
    Configuração de área de entrega;
    Cadastro de entregador e veículos;
    Busca Preço;
    Gourmet - Operacional em detalhes;
    Gourmet - Couvert;
    Gourmet - cadastros e configurações;
    Gourmet - Apresentação;
    Configurar Bridge para sincronizar filiais;
    Bridge;
    Apresentação do Bridge;
    Como trabalhar com crédito de cliente no PDV;
    Tudo o que precisa saber sobre login no PDV;
    Módulo Gourmet;
    Módulo Bridge;
    Configurar PDV para trabalhar com pré-venda;
    Troca simplificada dentro do PDV;
    Configuração para envio de ticket automático;
    Configurar acesso ao banco via Bridge;
    Módulo de PDV;
    Relatório de Fechamento de Caixa no PDV;
    Retirada de Caixa no PDV;
    Importação de Arquivo Texto - Clientes;
    Módulo Outros;
    Programa de backup;
    Primeiro acesso ao sistema;
    Problemas mais comuns ao acessar o sistema;
    Instalar o Etrade;
    Como instalar o Framework dot.Net;
    Como instalar o Microsoft SQL Server""".split(';')
    outros_f = [data + ' ' + categorias[10] for data in outros]
    outros_urls = f"""
    Id=b03cad54-ebd5-4850-bc2c-173ef8f97282;
    Id=133f2031-9811-4136-be51-9d6950eb693a;
    Id=d64f520c-0d52-40b1-8df0-ecc160799fc4;
    Id=39ab9fc5-0771-4ac3-be59-5af4677c8fee;
    Id=4174181c-8016-4a1a-9910-0d25e3a12049;
    Id=faa36c87-f1f1-4cfd-a050-df07a01947e1;
    Id=2166bd99-f2b6-4777-8b94-ebe36fe0a30a;
    Id=580ee6c4-6975-4043-bea1-72f5ed1c8899;
    Id=13c909bd-9d42-403e-9788-8db2fd5cc5e9;
    Id=a62b5364-068d-4273-8c99-d29e69af57c3;
    Id=f170f043-72d2-4949-bfb7-7b9587af7061;
    Id=c87786ad-6aea-4caf-84d5-16834057c7ed;
    Id=b98ecff3-ceed-4d6f-b121-d0264412e7e9;
    Id=69346194-5aef-4ee8-bc0b-10770e5b5ce4;
    Id=4ad4e4db-25a2-42ec-88c5-fb3b2d403bfa;
    Id=f6f02581-3655-4294-8d91-6ea7a51eb937;
    Id=da7a3447-3d5f-42d1-a771-4bf2a709d7d9;
    Id=18704a18-e4be-4536-867a-89fd66ad5690;
    Id=a6f9a630-a096-44eb-b1ef-cfa9d91fbf55;
    Id=830e7d4f-b349-4332-a3dc-888fb3a85a86;
    Id=415f8c7f-ab43-4687-a47d-a35f7b8c3a15;
    Id=6b871ff6-abac-4a6d-9284-0c7043d274f8;
    Id=8201e465-46e2-4f38-be62-c16a26d906db;
    Id=1b239ebb-7008-481f-bd48-d53544434b1b;
    Id=a59ad651-af47-4515-b747-26c15c9df9ad;
    Id=d2aa5f8b-a0a0-459c-b7c4-974f4770a46c;
    Id=1d8756c9-5460-4c80-a4a3-105d8cfa0c87;
    Id=850a498e-d508-44c3-a265-fd81a53ad124;
    Id=dfd23341-1e73-48fd-85ee-d6820e38c34e;
    Id=105bfb0e-ce62-4ec0-8a6b-2fdd69203b72;
    Id=8f3b1cf5-4dab-4175-9cb5-633ea005cb8d;
    Id=eda4c817-f494-4a05-a14f-bc090b1628a7;
    Id=855d27a3-4cac-4aae-98c1-98150158ed27;
    Id=15a08790-889a-49b0-8bcb-19f5e377388d;
    Id=ebc9f140-06db-4cfd-93ea-f565d6bbc285;
    Id=75f69c2d-bea8-4bee-85ed-86a71066c992;
    Id=ff3b7e46-6861-4c66-bfb8-df7f613893e4;
    Id=163edcbb-4dbc-40aa-9d4d-8b9ed6d82ca4;
    Id=aea40be7-875d-4955-b009-aa25912aad32;
    Id=44648cb6-c6f8-41e4-a820-b697dc91fec7;
    Id=dd710347-c5b9-46d1-8e31-49a9952a6d2d;
    Id=a19a596b-254b-4d8c-a7b6-e06a8f18262a;
    Id=3203193c-ee73-4d5d-81a5-9671c9802bef;
    Id=1a693949-0363-47e2-9bfa-a4789930c387;
    Id=ba656b34-7909-4ba0-89cd-c91f794c36ae;
    Id=706a5dce-adb7-46a8-bab7-7ed27f950334;
    Id=140f909f-1dbe-47fb-9f12-94bdfb1dfa54;
    Id=fa98e982-4b28-432b-96f6-04a4afe1f03f;
    Id=56e5ff1b-cb20-4ca7-8f58-faf6bddb2442;
    Id=d1e5a33b-c2b5-4877-a2a9-c713183417a7;
    Id=020c8e96-27fe-41c5-9b6d-ef2de0eb57bb;
    Id=4813d852-0e39-4cfd-8068-e0b988f7b301;
    Id=005661cd-fc18-4102-b818-c20b56f74b51;
    Id=e9e23fbd-ae43-4b94-82b0-854bbf853e21;
    Id=6260b020-1ffd-44af-b881-5080c08a9ed7;
    Id=13d16106-b598-42a9-85b7-29b530dd1df3;
    Id=62dc9c0c-d2a0-403f-82c7-d2d39bae6c85;
    Id=19156292-d048-46cd-a6d5-225f9a45565c;
    Id=df6f6889-27dd-45c6-bb9c-b87e187d02d6;
    Id=ae7b0371-b1c6-45d4-92da-e43ae05aeb65;
    Id=1d44f391-2780-4f1f-880c-0f98761aad37;
    Id=63ea7645-6e80-4400-83be-ddb58dcc2510;
    Id=e0fad0a7-a754-4f07-80aa-2099c0ac7b3f;
    Id=820b2a98-ee75-430c-9317-bc1be4b0a985;
    Id=f68bd141-2a84-43ba-9394-3e67c9a98cf5;
    Id=08056a07-7b92-4623-83eb-4e634cd343c8;
    Id=d6177cb3-1ed4-47d6-814f-007685f85b50;
    Id=80283b7e-4ff8-4ab6-a9fe-e7722c909198;
    Id=8db1bbf1-4e70-417e-b044-90738b6fbcc7;
    Id=a5c9ab50-bba5-43e1-9e8b-2fad003eafcb;
    Id=c092ab31-b643-4c6f-abc2-cf5a1c191f4a;
    Id=47db8617-c2f9-4dff-bee0-a6478f0f8aaf;
    Id=60626e3e-83b7-4191-ab6c-1284d7337900;
    Id=0022b5fe-edd8-48e7-a71d-2ffabba8e8cb;
    Id=c7242d3c-0028-4615-b466-84c980366909;
    Id=73f04962-fe18-414a-bec2-8a5c8aab0710;
    Id=f868feed-08df-466a-b286-ea93726d0ee1;
    Id=42d595cd-9f70-4301-8524-349a862fe294;
    Id=21d3c761-5515-4b28-b8e6-9ebd9a52e07b;
    Id=f711599f-136a-45ba-8039-5f594d568380;
    Id=11bf6634-d564-44ec-9181-9209e9e22f08;
    Id=d5adc389-7537-47e1-b53b-c22d64316e95;
    Id=3b609ea8-dfa2-4ea6-835e-afdba9f6640a;
    Id=2d3e195c-6a07-4eb8-b719-a51bf8f9c990;
    Id=201f2608-2d74-4116-8448-e6ce8813ed38;
    Id=8dc190aa-a3ae-40a2-909e-97444a180abd;
    Id=60597cb7-25de-4c3b-98dc-015039d1fc64;
    Id=73cb399e-d445-40c4-bf1f-d4ab61881e89;
    Id=90026774-8a7b-4323-b62b-31e6f2d199c3;
    Id=63732a03-380e-4c92-be38-1cd3f21259eb;
    Id=0f627070-5388-41c5-8185-37029a407d4a;
    Id=605264fc-57a9-4636-9bc1-def9ca5cb90b;
    Id=c6735fad-1e54-47f4-8d87-bea162075c2d;
    Id=50790177-382b-4b3e-a006-2f4c44c5d156;
    Id=2eabbc28-0ae9-4314-b0b6-8320f470994d;
    Id=99643ebe-510a-4461-8fd4-33119f42cbe5;
    Id=66f4d2c3-e199-448c-b319-3f160200fd45;
    Id=3959776e-e6f5-4107-b6c9-ef1a2fa84893;
    Id=dafe6ba9-e261-4f17-a340-1b145df243f7;
    Id=6c2c095c-099a-4bce-a840-ef6385ccd769;
    Id=af52feb7-bd2b-4489-9cce-264673f68331;
    Id=fb86f72a-a63b-4f35-a403-d44021f912b3;
    Id=e6e90f2e-f346-4fa9-b54c-2b02d25f9c17;
    Id=d1336a7c-7439-4e38-9031-4c60d2dc16fe;
    Id=67efbe1e-4837-4b94-9874-7ac74a9870d1""".split(';')
    outros_urls_f = [fixed + data.replace('\n', '').replace('    ', '') for data in outros_urls]
    # Id=b66cf7e2-0213-4612-94e5-fd0f0acf156b

    for index, data in enumerate(estoque_urls_f):
        print(estoque_f[index] + f'{x} [ Item {str(contador)} ]')
        print(x + data)
        contador += 1

    for index, data in enumerate(comercial_urls_f):
        print(comercial_f[index] + f'{x} [ Item {str(contador)} ]')
        print(x + data)
        contador += 1

    for index, data in enumerate(financeiro_urls_f):
        print(financeiro_f[index] + f'{x} [ Item {str(contador)} ]')
        print(x + data)
        contador += 1

    for index, data in enumerate(crm_urls_f):
        print(crm_f[index] + f'{x} [ Item {str(contador)} ]')
        print(x + data)
        contador += 1

    for index, data in enumerate(configuracoes_urls_f):
        print(configuracoes_f[index] + f'{x} [ Item {str(contador)} ]')
        print(x + data)
        contador += 1

    for index, data in enumerate(gourmet_urls_f):
        print(gourmet_f[index] + f'{x} [ Item {str(contador)} ]')
        print(x + data)
        contador += 1

    for index, data in enumerate(pdv_urls_f):
        print(pdv_f[index] + f'{x} [ Item {str(contador)} ]')
        print(x + data)
        contador += 1

    for index, data in enumerate(gourmetdroid_urls_f):
        print(gourmetdroid_f[index] + f'{x} [ Item {str(contador)} ]')
        print(x + data)
        contador += 1

    for index, data in enumerate(sped_urls_f):
        print(sped_f[index] + f'{x} [ Item {str(contador)} ]')
        print(x + data)
        contador += 1

    for index, data in enumerate(outros_urls_f):
        print(outros_f[index] + f'{x} [ Item {str(contador)} ]')
        print(x + data)
        contador += 1

    ""
    # print('\n')
    # print(f'Estoque       || {len(estoque)} títulos')
    # print(f'Estoque       || {len(estoque_urls)} urls')
    # print(f'Comercial     || {len(comercial)} títulos')
    # print(f'Comercial     || {len(comercial_urls)} urls')
    # print(f'Financeiro    || {len(financeiro)} títulos')
    # print(f'Financeiro    || {len(financeiro_urls)} urls')
    # print(f'CRM           || {len(crm)} títulos')
    # print(f'CRM           || {len(crm_urls)} urls')
    # print(f'Configurações || {len(configuracoes)} títulos')
    # print(f'Configurações || {len(configuracoes_urls)} urls')
    # print(f'Gourmet       || {len(gourmet)} títulos')
    # print(f'Gourmet       || {len(gourmet_urls)} urls')
    # print(f'PDV           || {len(pdv)} títulos')
    # print(f'PDV           || {len(pdv_urls)} urls')
    # print(f'GourmetDroid  || {len(gourmetdroid)} títulos')
    # print(f'GourmetDroid  || {len(gourmetdroid_urls)} urls')
    # print(f'Sintegra      || SEM DADOS')
    # print(f'Sintegra      || SEM DADOS')
    # print(f'Sped          || {len(sped)} títulos')
    # print(f'Sped          || {len(sped_urls)} urls')
    # print(f'Outros        || {len(outros)} títulos')
    # print(f'Outros        || {len(outros_urls)} urls')

    ""
    # counter = 0
    # while counter < len(outros):
    #     print(outros[counter])
    #     print(outros_urls[counter])
    #     counter += 1

    # print(outros[0])
    # print(outros_urls[0])


if __name__ == '__main__':
    links()
