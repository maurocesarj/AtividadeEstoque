create database comerce_sports;
use comerce_sports;

create table Fabricante (
cod_fabricante int auto_increment,
nome_fabricante varchar(60) not null,
primary key (cod_fabricante)
);

create table Produto (
cod_produto int auto_increment,
nome_produto varchar(60) not null,
fabricante_produto varchar(60) not null,
quantidade_produto int not null,
primary key (cod_produto)
);

create table historico_compra (
cod_historicoc int auto_increment,
cod_produto_hc varchar(60) not null,
data_hc date not null,
quantidade_produto_hc int not null,
primary key (cod_historicoc)
);

create table historico_venda (
cod_historicov int auto_increment,
cod_produto_hv varchar(60) not null,
data_hv date not null,
quantidade_produto_hv int not null,
primary key (cod_historicov)
);



