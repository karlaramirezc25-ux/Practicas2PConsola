class Mensaje:
    """Representa un mensaje simple (por ejemplo, "Hola Mundo programacion en clase")."""

    def __init__(self, texto: str):
        self.texto = texto

    def __str__(self) -> str:
        return self.texto

