# Proyecto-Programaci-n-1
Semstre Agosto - Diciembre 2026

## Tracker de Hábitos
**Mi aplicación trackeadora de habitos busca ser una alternativa para las personas para tener un seguimiento de cerca sobre los diferentes habitos saludables que siguen en su vida. En la actualidad, el estilo de vida "healthy" y "fit" viven en una fuerte tendencia la cuál impulsa a miles de personas a mejorar sus costumbres por lo que tenemos que ofrecerle a las personas alternativas accesibles y cómodas para tener un seguimiento de su rutina.
Esto es importante debido a que la salud es el pilar fundamental para que el cuerpo humano sea capaz de responder a las necesidades del día a día correctamente y con un buen desempeño. Al enfrentar deficiencias en esta, se le interpone una exigencia mayor al cuerpo las cuales a largo plaso son perjudiciales y van presentando consecuencias silenciosas que no muestran signos aparentes hasta que se convierten en un problema real.**

## Contexto
**En este proyecto, se busca atacar a un público joven que busca ser conciente del estilo de vida que sobrelleva mediante una aplicación la cuál te permite obtener "rachas" al acumular dias realizando ciertas practicas saludables. Este sistema de rachas es muy popular encontrarlo en aplicaciones de tipo red social las cuales indican cuantos dias continuos una persona a logrado sostener una practica, en este caso, el software te dara a escoger diferentes hábitos como dormir 8 horas, hacer ejercicio, en los cuáles podrás llevar tu progreso de cerca.
Al iniciar sesión en la aplicación, esta te dara la bienvenida con la lista de hábitos que puedes escoger para empezar a llevar tu registro, al seleccionar tus opciones preferidas te pedira indicarle las especificaciones de tiempo y diás a la semana con las que quieres cumplir dentro de un varemo segun que hábito ( dormir 7-8 horas 5 veces a la semana, hacer ejercicio 2 horas 4 veces a la semana,etc), una vez registrado, se creara tu propio perfil el cual, de manera gráfica con barras de progresión, te mostrara tu avance logrado a lo largo del tiempo. Por medio de un sistema de rangos podras ir subiendo de categoría, mientras más días acumules, las barras se iran llenando hasta lograr cierta cantidad de días indicados y pasaras a ser parte la categoría siguiente y así repetidamente. Esto para que el usuario pueda sentir y observar su progreso y encontrar una motivación en continuar con un mejor estilo de vida y no perder ese progreso logrado.**
**Para verificar que el usuario realmente esta cumpliendo con lo asignado, se buscará utilizar diferentes metodos de comprobacion entre los cuales se considera un sistema en el que el usuario tendra que empezar una cuenta atrás dentro de la aplicación la cuál te marque como cumplido el objetivo hasta llegar a 0, este frenando cada que se detecte una acción no relacionada con el objetivo, un sistema de detección de movimiento del dispositivo, limitación de espacio para realizar un hábito, entre mas.**
Ej- 
 - Si empiezas tu sesión de ejercicio de 2 horas, la cuenta atrás frenara al momento de cambiar de app o salir de un espacio delimitado por el usuario indicado como "zona de ejercicio".
 - Si comienzas tu tiempo de dormir 8 horas, la cuenta atras frenara al detectar movimiento del dispositivo

## Algoritmo
**Entradas**

 - horas_habito1 - numero decimal (minutos)
 - dias_semana1 - numero entero (dias)

**Proceso**

 1. INICIO
 2. ASIGNAR tiempo por usuario a "horas_habito1"
 3. GUARDAR "horas_habito1"
 4. ASIGNAR dias por usuario a "dias_semana1!
 5. GUARDAR "dias_semana1"
 6. INICIAR hábito
 7. SI "contador" es igual a 0
 8. ENTONCES acabar hábito 
 9. SUMAR 1 a "racha1"
 10. MOSTRAR "racha1"
 11. FIN

**Salidas**

 - racha1 - numero entero
 - AVANCE 2
 - proyecto_habitos.py

