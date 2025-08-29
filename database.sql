-- database.sql
-- Script para crear la estructura de la base de datos y agregar datos de ejemplo.

-- Eliminar tablas si existen para una importación limpia
DROP TABLE IF EXISTS detalle_pedido;
DROP TABLE IF EXISTS pedido;
DROP TABLE IF EXISTS producto;
DROP TABLE IF EXISTS categoria;
DROP TABLE IF EXISTS usuario;

-- Tabla de Usuarios
CREATE TABLE usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL
);

-- Tabla de Categorías
CREATE TABLE categoria (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL UNIQUE,
    descripcion TEXT
);

<<<<<<< HEAD
=======
-- Tabla de Productos
>>>>>>> 657b5456f15faee7f40f73cfa361a8b525282106
CREATE TABLE producto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    precio REAL NOT NULL,
    stock INTEGER NOT NULL,
    categoria_id INTEGER,
    FOREIGN KEY (categoria_id) REFERENCES categoria (id)
);

<<<<<<< HEAD
-- Datos de ejemplo
INSERT INTO usuario (first_name, last_name, email, password) VALUES
('Juan', 'Perez', 'juan.perez@email.com', 'testpassword123');

INSERT INTO categoria (nombre, descripcion) VALUES
('Electrónicos', 'Artículos de tecnología y gadgets');
=======
-- Tabla de Pedidos
CREATE TABLE pedido (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha TEXT NOT NULL,
    estado TEXT NOT NULL,
    total REAL,
    usuario_id INTEGER,
    FOREIGN KEY (usuario_id) REFERENCES usuario (id)
);

-- Tabla de Detalle de Pedidos
CREATE TABLE detalle_pedido (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cantidad INTEGER NOT NULL,
    subtotal REAL NOT NULL,
    pedido_id INTEGER,
    producto_id INTEGER,
    FOREIGN KEY (pedido_id) REFERENCES pedido (id),
    FOREIGN KEY (producto_id) REFERENCES producto (id)
);


-- Insertar datos de ejemplo
INSERT INTO usuario (nombre, apellido) VALUES
('Juan', 'Perez'),
('Ana', 'Gomez');

INSERT INTO categoria (nombre, descripcion) VALUES
('Electrónicos', 'Artículos de tecnología y gadgets'),
('Libros', 'Libros de texto y novelas');

INSERT INTO producto (nombre, precio, stock, categoria_id) VALUES
('Laptop Pro', 1500.00, 10, 1),
('Mouse Inalámbrico', 25.50, 50, 1),
('Novela de Ficción', 15.99, 100, 2);
>>>>>>> 657b5456f15faee7f40f73cfa361a8b525282106
