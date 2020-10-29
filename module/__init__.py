"""

    Este paquete contiene un modulo llamado ``funciones.py`` donde se pueden encontrar las funciones necesarias
    poder replicar los resultados del informe. A continuación mostramos como
    utilizar este paquete desde la ventana de comandos.

    #. Abrimos la ventana de comandos, cmd.exe en windows.
    #. Nos situamos en la carpeta donde se encuentra el archivo ``main.py``
    #. Indicamos el número del apartado cuyo resultados queremos obtener. En la :numref:`tblfuns` podemos ver
       que funciones tenemos disponibles.

    .. _tblfuns:

    .. list-table:: Tabla de las funciones utilizadas para cada apartado
        :widths: 50 50
        :header-rows: 1
        :align: center

        * - Función
          - Número
        * - resolucionApartadoA()
          - 1
        * - resolucionApartadoB()
          - 2
        * - resolucionComparativa()
          - 3
        * - resolucionConvergencia()
          - 4

    De modo que si queremos obtener los resultados del primer apartado deberíamos escribir lo siguiente:

    .. code-block::

        python main.py 1

    Una vez ejecutado el comando deberíamos obtener la siguiente respuesta del programa, ver :numref:`figcmd1`.
    En la ventana de comandos debe aparecer los datos que se muestran en el informe y debe aparecer una ventana
    adicional donde aparecen graficados los datos de la tabla.

    .. _figcmd1:

    .. figure:: imgs/cmd1.png
        :align: center
        :alt: Captura de pantalla de la ventana de comandos

        Captura de pantalla del resultado para el primer apartado.

    .. admonition:: Nota

        Todos los apartados generan una **carpeta propia** donde se guandan las imágenes que se han mostrado por pantalla
        y además guarda un .csv con los datos

"""