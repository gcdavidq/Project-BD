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

END