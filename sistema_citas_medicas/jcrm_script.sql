DROP DATABASE jcrm_scm;
CREATE DATABASE IF NOT EXISTS jcrm_scm;
USE jcrm_scm;

CREATE TABLE doctor(
    id INT(20) NOT NULL auto_increment,
    nombre VARCHAR(30) NOT NULL,
    apellidos VARCHAR(50) NOT NULL,
    telefono VARCHAR(12) NOT NULL,
    N_consultorio VARCHAR (10) NOT NULL,
    especialidad VARCHAR(100) NOT NULL,
    email VARCHAR (255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    CONSTRAINT pk_doctores PRIMARY KEY(id),
    CONSTRAINT uq_telefono UNIQUE(telefono),
    CONSTRAINT uq_email UNIQUE(email)
)ENGINE=InnoDb;

CREATE TABLE consultas(
    id INT (20) NOT NULL auto_increment,
    id_doctor INT (20) NOT NULL,
    nom_paciente VARCHAR (100) NOT NULL,
    telefono VARCHAR(12) NOT NULL,
    edad SMALLINT NOT NULL,
    fecha DATE NOT NULL,
    CONSTRAINT pk_consultas PRIMARY KEY(id),
    CONSTRAINT fk_consulta_doctor FOREIGN KEY(id_doctor) REFERENCES doctor(id)
)ENGINE=InnoDb;