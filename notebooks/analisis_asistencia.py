import pandas as pd

#Extraer información 
data_frame_asistencia = pd.read_csv("./data/asistencia_estudiantes_completo.csv")

#Extraer datos básicos de la data ingresada

#print(data_frame_asistencia.head(100))
#print(data_frame_asistencia.tail())
#print(data_frame_asistencia.info())
#print(data_frame_asistencia.describe())
#print(data_frame_asistencia['estrato'].value_counts().head(2))

#ANTES DE FILTRAR COMO ANALISTA DE DATOS DEBES CONCER (EXPLORAR LA FUENTE PRIMARIA)
print(data_frame_asistencia['estado'].unique())
print(data_frame_asistencia['estrato'].unique())
print(data_frame_asistencia['medio_transporte'].unique())
data_frame_asistencia['fecha'] = pd.to_datetime(data_frame_asistencia['fecha'])




#FILTROS Y CONDICIONES PARA TRANSFORMAR DATOS
#1. Reportar todos los estudiantes que asistieron
estudiantes_que_asistieron = data_frame_asistencia.query('estado == "asistio"')
print(estudiantes_que_asistieron)
#2. Reportar todos los estudiantes que faltaron
estudiantes_que_faltaron = data_frame_asistencia.query('estado == "inasistencia"')
print(estudiantes_que_faltaron)
#3. Reportar todos los estudiantes que llegaron tarde (Justificado)
estudiante_justificacion = data_frame_asistencia.query('estado ==  "justificado"')
print(estudiante_justificacion)
#4. Reportar todos los estudiantes de estrato 1
estudiante_estrato_uno = data_frame_asistencia.query('estrato == 1')
print(estudiante_estrato_uno)
#5. Reportar todos los estudiantes de estrato altos
estudiante_estrato_alto = data_frame_asistencia.query('estrato >= 4')
print(estudiante_estrato_alto)
#6. Reportar todos los estudiantes que llegan en metro
estudiantes_usan_metro = data_frame_asistencia.query('medio_transporte == "metro"')
print(estudiantes_usan_metro)
#7. Reportar todos los estudiantes que llegan en bicicleta.
estudiantes_bicicleta = data_frame_asistencia.query('medio_transporte == "bicicleta"')
print(estudiantes_bicicleta)
#8. Reportar todos los estudiantes que no caminan para llegar a la u
estudiantes_que_no_caminan = data_frame_asistencia.query('medio_transporte != "a pie"')
print(estudiantes_que_no_caminan)
#9. Reportar todos los registros de asistencia del mes de junio
estudiantes_que_mes_junio = data_frame_asistencia.query('fecha > "2025-05-31"')
print(estudiantes_que_mes_junio)
#10. Reportar los estudiantes que faltaron y usan bus para llegar a la Uni
estudiantes_que_faltan_usan_bus = data_frame_asistencia.query('medio_transporte == "bus" and estado == "inasistencia"')
print(estudiantes_que_faltan_usan_bus.info())
#11. Reportar estudiantes que usan bus y son de estratos altos
estudiantes_bus_estratos_altos = data_frame_asistencia.query('medio_transporte == "bus" and estrato >= 4 ')
print(estudiantes_bus_estratos_altos)
#12. Reportar estudiantes que usan bus y son de estratos bajos.
estudiantes_bus_estratos_bajos = data_frame_asistencia.query('medio_transporte == "bus" and estrato < 4 ')
print(estudiantes_bus_estratos_bajos)
#13. Reportar estudiantes que llegan tarde y sond de estrato 3,4, 5 0 6
estudiantes_tarde_estrato_mayor_3 = data_frame_asistencia.query('estado == "justificado" and estrato in [3,4,5,6] ')
print(estudiantes_tarde_estrato_mayor_3)
#14. Reportar estudiantes que usan transportes ecológicos
estudiantes_transporte_ecologicos = data_frame_asistencia.query('medio_transporte == "a pie" and medio_transporte == "bicicleta"')
print(estudiantes_transporte_ecologicos)
#15. Reportar estudiantes que faltan y usan carros para transportarse 
#16. Reportar estudiantes que asisten son estratos altos y caminan
#17. Reportar estudiantes que son estratos bajos y justifican su inasistencia
#18. Reportar estudiantes que son estratos altos y justifican su inasistencia
#19. Reportar estudiantes que usan carro y jsutrifican su inasistencia
#20. Reportar estudiantes que faltan y usan metro y son estratos medios.
 

#AGRUPACIONES Y CONTEOS SOBRE LOS DATOS
#1. Contar cada registro de asistencia por cada estado
#conteo_registros_por_estados = data_frame_asistencia.groupby('estado').size()
#print(conteo_registros_por_estados)

#2. Número de registro por estrato
#conteo_regristros_por_estrato = data_frame_asistencia.groupby('estrato').size()
#print(conteo_regristros_por_estrato)
#3. Cantidad de estudiantes por medio de transporte
#4. Cantidad de registros por grupo 
#5. Cruce entre estado y medio de transporte
#cruce_estado_medio_transporte = data_frame_asistencia.groupby(['estado', 'medio_transporte']).size()
#print(cruce_estado_medio_transporte)
#6. Promedio de estrato por estado de asistencia
#prom_estrato_estado = data_frame_asistencia.groupby('estado')['estrato'].mean()
#print(prom_estrato_estado)
#7. Estrato promedio por medio de transporte
#8. Máximo estrato por estado de asistencia
#9. Mínimo estrato or estado de asistencia
#10. Conteo de asistencias por grupo y por estado
#11. Transporte usado por grupo
#12. Cuantos grupos distintos registraron asistencia por fecha
#13. Promedio de estrato por fecha 
#14. Número de tipos de estado por transporte
#15. Primer registro de cada grupo 