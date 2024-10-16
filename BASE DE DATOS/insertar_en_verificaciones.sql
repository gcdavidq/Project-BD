BEGIN
	-- insertamos los valores en la tabla verificaciones
   INSERT INTO verificaciones (verificaciones_id_votos, verificacion)
   VALUES (NEW.id_votos, 0);
END