# Taller de Regresión Logística: abandono de producto financiero

## 1. Qué se hizo

Se analizó la base de datos de abandono de clientes de un producto financiero, con la variable dependiente binaria llamada abandono. La base se cargó desde el archivo disponible en la carpeta del proyecto y se verificó que tenía una unidad de observación por cliente, variables explicativas del perfil financiero y una respuesta dicotómica.

Se desarrolló el análisis siguiendo los siete puntos del taller:

1. Estructura de los datos.
2. Descriptivo univariado.
3. Relación bivariada con la variable respuesta.
4. Estimación del modelo logit.
5. Comparación de varios modelos y odds ratios.
6. Predicción en muestra de prueba y matriz de confusión.
7. Perfil de riesgo y conclusión final.

La intención general fue explicar qué factores están asociados con la probabilidad de que un cliente abandone el producto y cómo se puede usar un modelo de regresión logística para identificar clientes de mayor riesgo.

## 2. Resultados principales

### Base y estructura

La base tiene 10.000 observaciones y 14 columnas. La variable respuesta abandono presenta una proporción dominante de clientes que permanecen en comparación con los que abandonan, lo cual es típico en este tipo de análisis y exige cuidado en la interpretación porque la clase positiva es menos frecuente.

### Variables relevantes

Se encontró que variables como puntaje crediticio, edad, antigüedad, saldo, número de productos, miembro activo, sexo y país muestran una relación importante con la probabilidad de abandono. En particular, la pertenencia a ciertos grupos de país y la condición de miembro activo resultaron muy relevantes para explicar el riesgo.

### Modelo logit

El modelo logit estimado mostró que algunos predictores incrementan la probabilidad de abandono, mientras que otros la reducen. Por ejemplo:

- La probabilidad de abandono aumenta cuando el cliente es mujer, en comparación con el grupo de referencia.
- La probabilidad de abandono disminuye cuando el cliente es miembro activo y cuando pertenece a ciertos países con menor riesgo relativo.
- El puntaje crediticio y la antigüedad tienen una relación negativa con el riesgo de abandono: a mejor perfil financiero, menor probabilidad de dejar el producto.

### Odds ratios

Los odds ratios permiten interpretar el efecto relativo de cada variable sobre la probabilidad de abandonar. Los valores mayores que 1 aumentan la probabilidad relativa de abandono, y los valores menores que 1 la reducen. En los resultados observados, las variables con mayor efecto se ubican alrededor de la categoría de sexo, edad, país y pertenencia activa.

### Predicción en prueba

Al separar la muestra en entrenamiento y prueba, el modelo logró una buena capacidad general para clasificar a los clientes no abandonos, pero tuvo menor sensibilidad para detectar correctamente a los clientes que abandonan. Esto refleja un problema clásico de clases desbalanceadas: el modelo presenta buena precisión global, pero identifica menos bien a la clase minoritaria.

Los resultados obtenidos en prueba fueron:

- Accuracy: 0.8080
- Precision: 0.5891
- Recall: 0.1867
- F1-score: 0.2836

### Perfil de riesgo alto

Se definió un perfil de riesgo alto con los clientes que estaban en el percentil 90 de la probabilidad estimada de abandono. Ese grupo tuvo una probabilidad promedio de abandono de 0.5778, mucho más alta que la de los clientes restantes, cuya probabilidad promedio fue 0.1621.

El perfil de riesgo alto se caracteriza por:

- menor puntaje crediticio
- mayor edad relativa
- menor permanencia activa
- menor nivel de engagement o membresía activa
- mayor concentración en ciertos segmentos por país y sexo

Esto permite usar el modelo como herramienta de segmentación y retención, priorizando atención a clientes con mayor probabilidad de abandono.

## 3. Respuestas por punto del taller

### Punto 1. Estructura de los datos

La base corresponde a clientes de un banco o entidad financiera, con una observación por cliente y una variable respuesta binaria llamada abandono. La estructura es compatible con un modelo logit porque se cuenta con información de características del cliente y un resultado observado en dos categorías.

### Punto 2. Descriptivo univariado

La variable respuesta está desbalanceada: una parte importante de la base permanece y una fracción menor abandona. Las variables numéricas tienen rangos y distribución distintos, y las variables categóricas muestran diferencias de composición dentro de la cartera. Esto sugiere que el comportamiento del cliente no es homogéneo y que ciertos segmentos tienen mayor riesgo.

### Punto 3. Bivariado con la respuesta

La comparación por grupos mostró diferencias importantes entre clientes que abandonan y los que permanecen. Algunas variables tienen diferencias claras, especialmente las relacionadas con el país, el sexo, la membresía activa y algunas variables de comportamiento financiero. La prueba chi-cuadrado confirmó que varias de estas diferencias son estadísticamente significativas.

### Punto 4. De la recta al logit

El modelo logit reemplaza la relación lineal por una relación lineal en el logit, de forma que la probabilidad de abandono queda acotada entre 0 y 1. La estimación del modelo permitió observar cómo cambian las probabilidades según cada predictor.

### Punto 5. Varios modelos y odds ratios

Se compararon varios modelos para evaluar el ajuste. El modelo completo tuvo mejor rendimiento que el modelo nulo y el reducido. Los odds ratios permitieron interpretar el efecto de cada variable sobre la probabilidad de abandono, mostrando qué factores aumentan y cuáles reducen el riesgo.

### Punto 6. Predicción en test y matriz de confusión

La predicción en muestra de prueba mostró que el modelo clasifica adecuadamente a la mayoría de clientes estables, pero es menos eficaz para identificar a los clientes que abandonan. La matriz de confusión confirmó esta situación: el modelo tiene alta exactitud global, pero baja sensibilidad para la clase positiva.

### Punto 7. Perfiles de riesgo y conclusión final

El perfil de riesgo alto permite diferenciar a los clientes con mayor probabilidad de abandono. Estos clientes tienen peor perfil crediticio, menor vinculación activa y mayor exposición a condiciones de riesgo. Por lo tanto, el modelo resulta útil para retención, segmentación y decisiones preventivas.

## 4. Conclusión final

La regresión logística fue una herramienta adecuada para este problema porque la variable dependiente es binaria y se busca estimar la probabilidad de que un cliente abandone el producto. El análisis mostró que el riesgo de abandono no depende de una sola variable, sino de una combinación de factores financieros, demográficos y de comportamiento del cliente.

En términos prácticos, el modelo permite identificar clientes con mayor riesgo, priorizar acciones de retención y diseñar estrategias orientadas a la prevención del abandono del producto financiero.

## 5. Observación final sobre la práctica

El taller se desarrolló con la base real disponible en la carpeta del proyecto, en lugar del conjunto de datos original del ejemplo alemán. Esto fue necesario para responder al caso real del abandono de producto financiero y permitió vincular la metodología con una situación de negocio más cercana a la práctica.

El resultado general es consistente con la lógica del problema: el riesgo de abandono está asociado a clientes con menor fortaleza financiera y menor nivel de participación activa en la relación con la entidad.
