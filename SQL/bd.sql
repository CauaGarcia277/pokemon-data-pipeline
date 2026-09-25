CREATE DATABASE pokemon_bd;
USE pokemon_bd;

CREATE TABLE pokemon (
    id_pokemon INT UNSIGNED NOT NULL,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT,
    altura DECIMAL(6,2),
    peso DECIMAL(7,2),
    experiencia_base INT UNSIGNED,
    geracao VARCHAR(50) NOT NULL,
    image_url VARCHAR(500),

    CONSTRAINT pk_pokemon PRIMARY KEY (id_pokemon)
);


CREATE TABLE pokemon_stat (
    id_pokemon INT UNSIGNED NOT NULL,
    hp TINYINT UNSIGNED NOT NULL,
    ataque TINYINT UNSIGNED NOT NULL,
    defesa TINYINT UNSIGNED NOT NULL,
    ataque_especial TINYINT UNSIGNED NOT NULL,
    defesa_especial TINYINT UNSIGNED NOT NULL,
    velocidade TINYINT UNSIGNED NOT NULL,

    CONSTRAINT pk_pokemon_stat PRIMARY KEY (id_pokemon),

    CONSTRAINT fk_pokemon_stat_pokemon FOREIGN KEY (id_pokemon) REFERENCES pokemon(id_pokemon)
);

CREATE TABLE tipo (
    id_tipo INT UNSIGNED NOT NULL AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,

	CONSTRAINT pk_tipo PRIMARY KEY (id_tipo),

    CONSTRAINT uq_tipo_nome UNIQUE (nome)
);

CREATE TABLE pokemon_tipo (
    id_pokemon INT UNSIGNED NOT NULL,
    id_tipo INT UNSIGNED NOT NULL,

    CONSTRAINT pk_pokemon_tipo PRIMARY KEY (id_pokemon, id_tipo),

    CONSTRAINT fk_pokemon_tipo_pokemon FOREIGN KEY (id_pokemon) REFERENCES pokemon(id_pokemon),

    CONSTRAINT fk_pokemon_tipo_tipo FOREIGN KEY (id_tipo) REFERENCES tipo(id_tipo)
);