Com o cenário da pandemia o Magalu decidiu disponibilizar uma plataforma para os que comerciantes possam oferecer seus produtos.

O Projeto Leque é uma API Restfull desenvolvida com o framework Django que permite consultar, criar, atualizar e inativar o cadastro de um produto.

Foram implementadas duas classes : Product e Seller

Atributos do Seller:
Name e Email

Atributos do Produto:
Name, Price, Seller, Quantity e Status

URLs

Para realizar POST de um produto e GET de todos os produtos cadastrados.
http://127.0.0.1:8000/produtos/

Para fazer PUT, GET por ID e inativar o produto 
http://127.0.0.1:8000/produtos/{id}/

Para fazer GET e POST dos sellers http://127.0.0.1:8000/produtos/sellers/


Para fazer PUT e inativar dos sellers
http://127.0.0.1:8000/produtos/sellers/{id}/

Testes






