-- Crear la tabla tarea en MySQL
CREATE TABLE tarea (
    id INT AUTO_INCREMENT PRIMARY KEY,
    descripcion_tarea VARCHAR(150) NOT NULL,
    fecha_maxima_realizacion DATE NOT NULL
);

-- Insertar 5 valores iniciales para efectuar pruebas
INSERT INTO tarea(descripcion_tarea, fecha_maxima_realizacion) VALUES
('Elaborar pequeña calculadora funcional en Python', '2024-03-04'),
('Terminar presentación de Mercadotecnia General', '2024-05-22'),
('Pagar Solvencia de Evaluaciones Finales', '2024-05-26'),
('Elaborar Circuito electrónico de transferencia', '2024-03-07'),
('Realizar Base de Datos en MongoDB y hacer consultas', '2024-02-28');