CREATE DATABASE almoxarifado;
USE almoxarifado;

CREATE TABLE usuario (
id int primary key auto_increment,
matricula int not null unique,
senha varchar(200) not null,
nome varchar(200) not null,
email varchar(200) not null,
telefone char(15)
);


CREATE TABLE categoria (
id int primary key auto_increment,
nome_categoria varchar(200) not null
);

CREATE TABLE material (
id int primary key auto_increment,
data_de_cadastro timestamp default current_timestamp,
nome_produto varchar(50) not null,
quantidade int,
endereçamento varchar(30) not null,

id_categoria int,
constraint fk_id_categoria foreign key (id_categoria) references categoria(id),

cadastrado_por int,
constraint fk_id_usuario_entrada foreign key (cadastrado_por) references usuario(id)

);


CREATE TABLE saida_material (
id int primary key auto_increment,
id_usuario int,
id_material int,
quantidade_retirada int,
data_retirada timestamp default current_timestamp,

constraint fk_id_usario_saida foreign key (id_usuario) references usuario(id),
constraint fk_id_material_saida foreign key (id_material) references material(id)
);


