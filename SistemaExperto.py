import tkinter as tk
from tkinter import ttk, messagebox

class SistemaExperto:    
    def __init__(self, root):

        """
        Constructor que inicializa la ventana principal del sistema experto.
        
        Precondición: Se recibe una instancia de tkinter.Tk como argumento.
        Postcondición: Se inicializa la ventana y la interfaz gráfica del sistema experto.
        """
        
        self.root = root
        self.root.title("Sistema Experto")
        self.root.geometry("920x600")

        # Variables
        self.preguntas = self.generar_preguntas()
        self.respuestas = []

        # Inicializar la interfaz
        self.crear_interfaz()

    def generar_preguntas(self):

        """
        Genera una lista de preguntas relacionadas con síntomas de ansiedad.
        
        Precondición: Ninguna.
        Postcondición: Se retorna una lista con las preguntas predefinidas.
        """

        return [
            "1. Torpe o entumecido", "2. Acalorado", "3. Con temblor en las piernas",
            "4. Incapaz de relajarse", "5. Con temor a que ocurra lo peor", "6. Mareado, o que se le va la cabeza",
            "7. Con latidos del corazón fuertes y acelerados", "8. Inestable", "9. Atemorizado o asustado",
            "10. Nervioso", "11. Con sensación de bloqueo", "12. Con temblores en las manos",
            "13. Inquieto, inseguro", "14. Con miedo a perder el control", "15. Con sensación de ahogo",
            "16. Con temor a morir", "17. Con miedo", "18. Con problemas digestivos",
            "19. Con desvanecimientos", "20. Con rubor facial", "21. Con sudores, fríos o calientes"
        ]

    def crear_interfaz(self):

        """
        Crea la interfaz gráfica principal que incluye título, leyenda, encuesta, y un botón para calcular el puntaje.
        
        Precondición: Se debe haber llamado a `generar_preguntas` previamente.
        Postcondición: Se muestra la interfaz gráfica en la ventana principal.
        """

        # Título principal
        titulo_label = ttk.Label(self.root, text="Sistema Experto - Cuestionario", font=("Helvetica", 16))
        titulo_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Datos del usuario
        self.crear_datos_usuario()

        # Leyenda explicativa
        leyenda_label = ttk.Label(self.root, text="1 es No\n2 es Leve\n3 es Moderado\n4 es Bastante", font=("Helvetica", 10))
        leyenda_label.grid(row=2, column=0, columnspan=2, pady=10)

        # Crear la encuesta
        self.crear_encuesta()

        # Botón para calcular el puntaje
        calcular_button = ttk.Button(self.root, text="Calcular Resultado", command=self.calcular_puntaje)
        calcular_button.grid(row=7, column=0, columnspan=2, pady=20)

    def crear_datos_usuario(self):

        """
        Añade campos de texto a la interfaz para que el usuario ingrese su nombre y edad.
        
        Precondición: La ventana principal ha sido inicializada.
        Postcondición: Se crean los campos de texto en la ventana para el nombre y la edad del usuario.
        """

        datos_frame = ttk.Frame(self.root)
        datos_frame.grid(row=1, column=0, columnspan=2, pady=10)

        nombre_label = ttk.Label(datos_frame, text="Nombre:")
        nombre_label.pack(side="left")
        self.nombre_entry = ttk.Entry(datos_frame)
        self.nombre_entry.pack(side="left", padx=5)

        edad_label = ttk.Label(datos_frame, text="Edad:")
        edad_label.pack(side="left")
        self.edad_entry = ttk.Entry(datos_frame)
        self.edad_entry.pack(side="left", padx=5)

    def crear_encuesta(self):

        """
        Crea y organiza las preguntas del cuestionario en dos columnas dentro de la ventana principal.
        
        Precondición: Se debe haber llamado a `generar_preguntas`.
        Postcondición: Las preguntas se muestran en la ventana con opciones de respuesta.
        """

        # Primera columna
        frame_col1 = ttk.Frame(self.root)
        frame_col1.grid(row=6, column=0, padx=10, pady=10, sticky="n")

        # Segunda columna
        frame_col2 = ttk.Frame(self.root)
        frame_col2.grid(row=6, column=1, padx=10, pady=10, sticky="n")

        for i, pregunta in enumerate(self.preguntas[:11]):
            self.crear_pregunta(frame_col1, pregunta)
        for i, pregunta in enumerate(self.preguntas[11:]):
            self.crear_pregunta(frame_col2, pregunta)

    def crear_pregunta(self, frame, pregunta):

        """
        Crea una fila con una pregunta y sus opciones de respuesta (radio buttons).
        
        Precondición: `frame` es un contenedor válido y `pregunta` es una cadena no vacía.
        Postcondición: Se muestra una pregunta con opciones en el frame correspondiente.
        """

        frame_pregunta = ttk.Frame(frame)
        frame_pregunta.pack(anchor="w", pady=5)

        pregunta_label = ttk.Label(frame_pregunta, text=pregunta, width=50, anchor="w")
        pregunta_label.pack(side="left")

        respuesta_var = tk.IntVar(value=0)
        self.respuestas.append(respuesta_var)

        for valor in range(4):
            radio_button = ttk.Radiobutton(frame_pregunta, variable=respuesta_var, value=valor)
            radio_button.pack(side="left")
            label = ttk.Label(frame_pregunta, text=str(valor + 1))
            label.pack(side="left")

    def validar_nombre(nombre):
        """
        Valida que el nombre no esté vacío.

        Parámetros:
        - `nombre` (str): El nombre del usuario ingresado en la entrada de texto.

        Retorna:
        - bool: Retorna True si el nombre no está vacío, False en caso contrario.
        """
        return bool(nombre.strip())

    def calcular_puntaje(self):

        """
        Calcula el puntaje total basado en las respuestas del cuestionario, valida que el nombre no esté vacío,
        y muestra una ventana emergente con el resultado y la recomendación.

        Precondición: La entrada de nombre y las respuestas deben estar disponibles.
        Postcondición: Se muestra una ventana emergente con el nivel de ansiedad y una recomendación basada en el puntaje total.
        """

        nombre = self.nombre_entry.get()

        if not validar_nombre(nombre): 
            # Mostrar un mensaje de error si el nombre está vacío
            tk.messagebox.showerror("Error", "El nombre no puede estar vacío.")
            return

        total_puntaje = sum(var.get() for var in self.respuestas)

        if total_puntaje <= 21:
            nivel_ansiedad = "Ansiedad muy baja"
            recomendacion = f"{nombre}, tu nivel de ansiedad es muy bajo. ¡Sigue cuidándote!"
        elif 22 <= total_puntaje <= 35:
            nivel_ansiedad = "Ansiedad moderada"
            recomendacion = f"{nombre}, tu nivel de ansiedad es moderado. Es recomendable que hables con un profesional de la salud mental."
        else:
            nivel_ansiedad = "Ansiedad severa"
            recomendacion = f"{nombre}, tu nivel de ansiedad es severo. Es muy importante que busques ayuda profesional de inmediato."

        ResultadoVentana(self.root, nivel_ansiedad, recomendacion)


class ResultadoVentana:
    def __init__(self, root, nivel_ansiedad, recomendacion):

        """
        Constructor que crea una ventana emergente para mostrar el resultado del cuestionario.
        
        Precondición: `root` debe ser una instancia de `tk.Tk`, `nivel_ansiedad` y `recomendacion` deben ser cadenas no vacías.
        Postcondición: Se crea una nueva ventana que muestra el nivel de ansiedad y la recomendación.
        """

        resultado_ventana = tk.Toplevel(root)
        resultado_ventana.title("Resultado del Sistema Experto")
        resultado_ventana.geometry("400x300")

        resultado_label = ttk.Label(resultado_ventana, text="Resultado", font=("Helvetica", 16))
        resultado_label.pack(pady=10)

        nivel_label = ttk.Label(resultado_ventana, text=nivel_ansiedad, font=("Helvetica", 14))
        nivel_label.pack(pady=10)

        recomendacion_label = ttk.Label(resultado_ventana, text=recomendacion, wraplength=350, justify="center")
        recomendacion_label.pack(pady=20)

        aceptar_button = ttk.Button(resultado_ventana, text="Aceptar", command=resultado_ventana.destroy)
        aceptar_button.pack(pady=10)

# Crear la ventana principal
if __name__ == "__main__":

    """
    Crea la ventana principal de la aplicación y la instancia del Sistema Experto.
    
    Precondición: Ninguna.
    Postcondición: Se inicia el bucle principal de la aplicación y se muestra la ventana del Sistema Experto.
    """

    root = tk.Tk()
    app = SistemaExperto(root)
    root.mainloop()
