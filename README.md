<h1> Projeto Leque </h1>

Com o cenário da pandemia o Magalu decidiu disponibilizar uma plataforma para os que comerciantes possam oferecer seus produtos.

O Projeto Leque é uma API Restfull desenvolvida com o framework Django que permite consultar, criar, atualizar e inativar o cadastro de um produto.

Foram implementadas duas classes : <strong>Product</strong> e <strong>Seller</strong>

<h3>Atributos do Seller</h3>
Name e Email

<h3>Atributos do Produto</h3>
Name, Price, Seller, Quantity e Status

<h2>URLs</h2>

Para realizar POST de um produto e GET de todos os produtos cadastrados.
http://127.0.0.1:8000/produtos/

Para fazer PUT, GET por ID e inativar o produto 
http://127.0.0.1:8000/produtos/1/

Para fazer GET e POST dos sellers http://127.0.0.1:8000/produtos/sellers/

Para fazer PUT e inativar dos sellers
http://127.0.0.1:8000/produtos/sellers/1/

*<em>O número 1 na URL corresponde ao ID do Produto e do Seller</em>

<h2>Testes</h2>

Realizamos testes de unidade e de integração das rotas <strong>GET</strong> e <strong>POST</strong> das classes Produto e Seller








