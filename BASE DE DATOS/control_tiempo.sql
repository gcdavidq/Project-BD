-- --------------------------------------------------------
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
END