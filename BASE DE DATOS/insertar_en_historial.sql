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
END