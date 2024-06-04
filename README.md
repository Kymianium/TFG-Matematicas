# Introducción

El texto que se encuentra a continuación sirve como presentación y guía de uso del programa de simulación para el algoritmo adaptativo presentado en el trabajo de fin de grado de la Universidad de Murcia, titulado "Análisis de algoritmos de aprendizaje adaptativo y su aplicación a entornos de Cyber Range".

El código del programa no está particularmente pulido, ya que no se creó con la idea de ser utilizado por otra persona más que su creador, para generar las gráficas pertinentes y obtener los resultados que se buscaban a la hora de realizar el trabajo de fin de grado. Aun así, se ha decidido publicar el código para que pueda ser utilizado por cualquier persona que desee hacerlo.

# Guía de uso

## Instalar dependencias

En primer lugar, es necesario instalar las dependencias necesarias.

### Python

En caso de no tener Python instalado, se puede descargar desde la [página oficial](https://www.python.org/downloads/). La versión utilizada para ejecutar el software ha sido, concretamente, python 3.10. Cualquier versión cuyo prefijo sea 3.10 es compatible (3.10.12, 3.10.13...).

### Librerías

Es muy aconsejable utilizar un entorno virtual para instalar las librerías necesarias. Para ello se puede ejecutar el siguiente comando en una terminal:
```bash
python -m venv .venv
```

Posteriormente, usando ```pip``` se instalarán las librerías necesarias:
```bash
pip install -r requirements.txt
```

Para utilizar el entorno virtual, se usa el comando

```bash
source .venv/bin/activate
```

## Ejecutar el software

Ahora, una vez dentro del entorno virtual, basta con ejecutar
```bash
python main.py
```

Nada más comenzar, se deben introducir tres valores:

- Un número de estudiantes
- Un número de retos
- El número de retos a realizar por estudiante.

  Nótese que, si el tercer número es mayor que el segundo, [se repetirán algunos de los retos.](https://es.wikipedia.org/wiki/Principio_del_palomar})

Estos tres valores, en la mayoría de casos de uso, serán ignorados. Al usuario, una vez introducidos, se le presentan tres opciones.

**Continuar con la simulación \[c\]**

En esta opción, se indica cuántos retos más debe realizar cada estudiante. Al finalizar, se muestran algunas estadísticas tanto de un estudiante como de un reto, y se abre en el navegadoor una comparación gráfica entre el nivel en las competencias de los estudiantes y su inferencia.

**Calcular estadísticas \[s\]**

Aunque este modo no se utilice en el trabajo de fin de grado, se incluyó para tener una métrica del error antes de introducir el cálculo del R². Se especifica un número de estudiantes, un número de retos y un número de ciclos. Durante tantos ciclos como se haya especificado, los estudiantes indicados se enfrentan a los retos indicados (que se generan, aleatoriamente, en cada ciclo). El sistema, después, muestra una media de los errores cometidos en todos los ciclos. La métrica del error es similar al error cuadrático medio, pero ligeramente modificada. No resultó de suficiente relevancia para incluirlo en el trabajo de fin de grado.

**Calcular R² \[r\]** 

Se especifica un número de estudiantes y un número de retos. Después, el sistema pregunta si se pretenden generar estadísticas o gráficas.

- Si se selecciona la opción de gráficas, el sistema enfrenta los estudiantes a los retos y, después, muestra una gráfica relacionando el nivel de compentencia real y la inferencia del algoritmo, y una regresión lineal sobre el plano.
- Si se selecciona la opción de estadísicas, se especifica un número de ciclos en los que, de nuevo, estudiantes se enfrentan a ejercicios. Una vez completados, se calcula el R² medio entre las inferencias y los valores reales, y se muestra por terminal. Esta métrica es la que ha sido utilizada en el documento.

**Simular un duelo \[d\]**

Se escogen tres estudiantes aleatorios de los generados al abrir el programa y tres retos aleatorios. El usuario escoge un estudiante y un reto, y los enfrenta entre sí. Por terminal, se muestra la adaptación llevada a cabo, comparando los recursos originales del reto y su adaptación. **Esta versión puede fallar si no hay suficientes estudiantes o retos.**

**Salir \[q\]**

Sale del programa.
