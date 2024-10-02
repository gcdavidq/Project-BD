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
  `decision` ENUM('1', '2', '3', '4', '5') NOT NULL,
  `nivel` TINYINT UNSIGNED NOT NULL,
  `posicion_x` INT NOT NULL,
  `posicion_y` INT NOT NULL,
  PRIMARY KEY (`id_historial`),
  UNIQUE INDEX `id_historial_UNIQUE` (`id_historial` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 93
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
  `posicion_x` INT NOT NULL,
  `posicion_y` INT NOT NULL,
  PRIMARY KEY (`id_votos`),
  UNIQUE INDEX `id_votos_UNIQUE` (`id_votos` ASC) VISIBLE,
  INDEX `fk_votos_historial_idx` (`votos_id_historial` ASC) VISIBLE,
  CONSTRAINT `fk_votos_historial`
    FOREIGN KEY (`votos_id_historial`)
    REFERENCES `bd_project`.`historial` (`id_historial`))
ENGINE = InnoDB
AUTO_INCREMENT = 166
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
AUTO_INCREMENT = 141
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
	DECLARE _voto ENUM('1','2','3','4','5');
	DECLARE _nivel	TINYINT; 
	DECLARE _posicion_x INT;
	DECLARE _posicion_y INT;
	DECLARE _tem INT;
   
   SELECT voto, nivel, posicion_x, posicion_y, COUNT(voto) AS frecuencia
   INTO _voto, _nivel, _posicion_x, _posicion_y, _tem
	FROM votos JOIN verificaciones ON votos.id_votos = verificaciones.verificaciones_id_votos
	GROUP BY voto, nivel, posicion_x, posicion_y
	HAVING frecuencia = 0
	ORDER BY frecuencia DESC
	LIMIT 1;
	
	UPDATE verificaciones
   SET verificacion = 1 
   WHERE verificacion = 0;

   INSERT INTO historial (decision, nivel, posicion_x, posicion_y)
   VALUES (_voto, _nivel, _posicion_x, _posicion_y);
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
	IN `_x` INT,
	IN `_y` INT
)
BEGIN
	DECLARE last_voto_id INT;
	
	INSERT INTO votos (tiempo_registro, voto, votos_id_historial, nivel, posicion_x, posicion_y)
	VALUES (NOW(), _voto, _votos_id_historial, _nivel , _x, _y);
	
   SET last_voto_id = LAST_INSERT_ID();

   INSERT INTO verificaciones (verificaciones_id_votos, verificacion)
   VALUES (last_voto_id, 0);
END$$

DELIMITER ;
USE `bd_project`;

DELIMITER $$

USE `bd_project`$$
DROP TRIGGER IF EXISTS `bd_project`.`control_tiempo` $$
USE `bd_project`$$
CREATE
DEFINER=`user1_magno`@`%`
TRIGGER `bd_project`.`control_tiempo`
AFTER INSERT ON `bd_project`.`votos`
FOR EACH ROW
BEGIN
	DECLARE primer_tiempo DATETIME;
	
	SELECT MIN(tiempo_registro) INTO primer_tiempo
	FROM votos JOIN verificaciones ON votos.id_votos = verificaciones.verificaciones_id_votos 
	WHERE verificaciones.verificacion = 0;

   IF primer_tiempo IS NOT NULL THEN
	
      IF TIMESTAMPDIFF(SECOND, primer_tiempo, NEW.tiempo_registro) >= 5 THEN

         CALL insertar_en_historial();
      END IF;
   END IF;
END$$


DELIMITER ;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
