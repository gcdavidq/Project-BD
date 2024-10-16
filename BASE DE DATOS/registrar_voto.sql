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
END