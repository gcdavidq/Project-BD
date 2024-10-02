BEGIN
	DECLARE last_voto_id INT;
	
	INSERT INTO votos (tiempo_registro, voto, votos_id_historial, nivel, posicion_x, posicion_y)
	VALUES (NOW(), _voto, _votos_id_historial, _nivel , _x, _y);
	
   SET last_voto_id = LAST_INSERT_ID();

   INSERT INTO verificaciones (verificaciones_id_votos, verificacion)
   VALUES (last_voto_id, 0);
END