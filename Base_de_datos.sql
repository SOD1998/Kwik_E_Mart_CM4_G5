DROP DATABASE IF EXISTS kwik_e_mart;
CREATE DATABASE kwik_e_mart CHARACTER SET utf8mb4;
USE kwik_e_mart;

CREATE TABLE administradores (
id int,
usuario varchar(20),
clave varchar(50)
);

CREATE TABLE clientes (
cliente_id int,
usuario varchar(20),
clave varchar(50),
nombre_cliente varchar(300),
celular varchar(10),
domicilio varchar(300),
DNI varchar(12)
);

CREATE TABLE facturas (
num_factura int,
fecha varchar(10),
nombre_cliente varchar(300),
celular_cliente varchar(10)
);

CREATE TABLE productos (
producto_id int,
clase varchar(300),
marca varchar(300),
nombre_producto varchar(300),
stock int,
precio_unitario float
);

INSERT INTO administradores VALUES (1,'selimdahan', '123456'),
(2,'milagro', 'qwerty');

INSERT INTO clientes VALUES (1,'luni', 'asdfgh', 'Luna', '3873123456', 'Tartagal - Richieri 831', '12345678'),
(2,'nieves', 'zxcvbn', 'Nieves', '3873654321', 'Tartagal - Richieri 831', '87654321');

INSERT INTO productos VALUES (1,'Comida', 'Marolio', 'Mate', 50, 39.99),
(2,'Comida','Marolio','Cafe',100,279.99),
(3,'Comida','Marolio','Harina',80,144.99),
(4,'Comida','Marolio','Palmitos',60,339.99),
(5,'Comida','Marolio','Yerba',50,179.99),
(6,'Comida','Marolio','Mermelada',0,124.99),
(7,'Comida','Marolio','Cacao',15,124.99),
(8,'Comida','Marolio','Picadillo',0,54.99),
(9,'Comida','Marolio','Pate',100,49.99),
(10,'Comida','Marolio','Caballa',200,299.99),
(11,'Comida','Marolio','Arroz',250,104.99),
(12,'Comida','Marolio','Arvejas',30,84.99),
(13,'Comida','Marolio','Sardinas',150,249.99),
(14,'Comida','Marolio','Atun',200,199.99),
(15,'Comida','Marolio','Choclo',50,84.99),
(16,'Comida','Marolio','Lentejas',40,84.99),
(17,'Bebida','LaSerenisima','Leche',200,184.99),
(18,'Bebida','CampoQuijano','Yogurt',180,344.99),
(19,'Bebida','Manaos','Soda',90,414.99),
(20,'Postre','Grido','Helado',270,504.99);
