BEGIN
    -- Declaramos la variable para el tiempo actual
    DECLARE tiempo_actual DATETIME;
    
    -- Asignamos el tiempo actual
    SET tiempo_actual = NOW();
    
    -- Comprobamos si han pasado exactamente 5 segundos
    IF (TIMESTAMPDIFF(SECOND, '2024-01-01 00:00:00', tiempo_actual) % 10) = 0 THEN
    
        -- Llamamos a la función para insertar en el historial y mover el bloque
        CALL insertar_en_historial();
        
        -- Actualizamos la verificación para marcar el voto como procesado
        UPDATE verificaciones
        SET verificacion = 1
        WHERE verificacion = 0;
    END IF;
    
END