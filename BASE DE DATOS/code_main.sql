-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema bd_project
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `bd_project` ;

-- -----------------------------------------------------
-- Schema bd_project
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `bd_project` DEFAULT CHARACTER SET utf8mb3 ;
USE `bd_project` ;

-- -----------------------------------------------------
-- Table `bd_project`.`historial`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `bd_project`.`historial` ;

CREATE TABLE IF NOT EXISTS `bd_project`.`historial` (
  `id_historial` INT NOT NULL AUTO_INCREMENT,
  `time_insert` DATETIME NULL DEFAULT NULL,
  `decision` ENUM('1', '2', '3', '4', '5') NOT NULL,
  `nivel` TINYINT UNSIGNED NOT NULL,
  `orientation` VARCHAR(10) CHARACTER SET 'utf8mb3' NULL DEFAULT NULL,
  `posicion_x` INT NOT NULL,
  `posicion_y` INT NOT NULL,
  `board` JSON NULL DEFAULT NULL,
  PRIMARY KEY (`id_historial`),
  UNIQUE INDEX `id_historial_UNIQUE` (`id_historial` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 129
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `bd_project`.`votos`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `bd_project`.`votos` ;

CREATE TABLE IF NOT EXISTS `bd_project`.`votos` (
  `id_votos` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `tiempo_registro` DATETIME NOT NULL,
  `voto` ENUM('1', '2', '3', '4', '5') NOT NULL,
  `votos_id_historial` INT NOT NULL,
  `nivel` TINYINT UNSIGNED NOT NULL,
  `orientation` VARCHAR(10) CHARACTER SET 'utf8mb3' NULL DEFAULT NULL,
  `posicion_x` INT NOT NULL,
  `posicion_y` INT NOT NULL,
  `board` JSON NULL DEFAULT NULL,
  PRIMARY KEY (`id_votos`),
  UNIQUE INDEX `id_votos_UNIQUE` (`id_votos` ASC) VISIBLE,
  INDEX `fk_votos_historial_idx` (`votos_id_historial` ASC) VISIBLE,
  CONSTRAINT `fk_votos_historial`
    FOREIGN KEY (`votos_id_historial`)
    REFERENCES `bd_project`.`historial` (`id_historial`))
ENGINE = InnoDB
AUTO_INCREMENT = 116
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `bd_project`.`verificaciones`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `bd_project`.`verificaciones` ;

CREATE TABLE IF NOT EXISTS `bd_project`.`verificaciones` (
  `id_verificaciones` INT NOT NULL AUTO_INCREMENT,
  `verificacion` TINYINT(1) NOT NULL DEFAULT '0',
  `verificaciones_id_votos` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`id_verificaciones`),
  INDEX `fk_verificaciones_votos1_idx` (`verificaciones_id_votos` ASC) VISIBLE,
  CONSTRAINT `fk_verificaciones_votos1`
    FOREIGN KEY (`verificaciones_id_votos`)
    REFERENCES `bd_project`.`votos` (`id_votos`))
ENGINE = InnoDB
AUTO_INCREMENT = 116
DEFAULT CHARACTER SET = utf8mb3;

USE `bd_project` ;

-- -----------------------------------------------------
-- procedure insertar_en_historial
-- -----------------------------------------------------

USE `bd_project`;
DROP procedure IF EXISTS `bd_project`.`insertar_en_historial`;

DELIMITER $$
USE `bd_project`$$
CREATE DEFINER=`user1_magno`@`%` PROCEDURE `insertar_en_historial`()
BEGIN
   -- Declaramos las variables que se usarán dentro de esta rutina
   DECLARE _voto ENUM('1','2','3','4','5');
   DECLARE _nivel TINYINT; 
   DECLARE _orientation VARCHAR(10);
   DECLARE _posicion_x INT;
   DECLARE _posicion_y INT;
   DECLARE _board JSON;

   -- Obtenemos el voto que más se repite con verificacion = 0
   SELECT v.voto, v.nivel, v.orientation, v.posicion_x, v.posicion_y, v.board
   INTO _voto, _nivel, _orientation, _posicion_x, _posicion_y, _board
   FROM votos v
   JOIN verificaciones ve ON v.id_votos = ve.verificaciones_id_votos
   WHERE ve.verificacion = 0
   GROUP BY v.voto, v.nivel, v.orientation, v.posicion_x, v.posicion_y, v.board
   ORDER BY COUNT(v.voto) DESC
   LIMIT 1;

   -- Insertamos en la tabla historial la decisión basada en el voto de mayor frecuencia
   INSERT INTO historial (time_insert, decision, nivel, orientation, posicion_x, posicion_y, board)
   VALUES (NOW(), _voto, _nivel, _orientation, _posicion_x, _posicion_y, _board);

END$$

DELIMITER ;

-- -----------------------------------------------------
-- procedure registrar_voto
-- -----------------------------------------------------

USE `bd_project`;
DROP procedure IF EXISTS `bd_project`.`registrar_voto`;

DELIMITER $$
USE `bd_project`$$
CREATE DEFINER=`user1_magno`@`%` PROCEDURE `registrar_voto`(
	IN `_voto` ENUM('1','2','3','4','5'),
	IN `_votos_id_historial` INT,
	IN `_nivel` TINYINT,
	IN `_orientation` VARCHAR(10),
	IN `_x` INT,
	IN `_y` INT,
	IN `_board` JSON
)
BEGIN
	-- declaramos la variable entera
	DECLARE last_voto_id INT;
	
	-- validamos que el voto no sea nulo
	-- para asigarle el valor de '5':'ninguno'
    IF _voto IS NULL THEN
        SET _voto = '5'; 
    END IF;
	
	-- insertamos los valores dentro del parámetro en la tabla votos
	INSERT INTO votos (tiempo_registro, voto, votos_id_historial, nivel, orientation, posicion_x, posicion_y, board)
	VALUES (NOW(), _voto, _votos_id_historial, _nivel , _orientation, _x, _y, _board);
END$$

DELIMITER ;
USE `bd_project`;

DELIMITER $$

USE `bd_project`$$
DROP TRIGGER IF EXISTS `bd_project`.`insertar_en_verificaciones` $$
USE `bd_project`$$
CREATE
DEFINER=`user1_magno`@`%`
TRIGGER `bd_project`.`insertar_en_verificaciones`
AFTER INSERT ON `bd_project`.`votos`
FOR EACH ROW
BEGIN
	-- insertamos los valores en la tabla verificaciones
   INSERT INTO verificaciones (verificaciones_id_votos, verificacion)
   VALUES (NEW.id_votos, 0);
END$$


DELIMITER ;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
