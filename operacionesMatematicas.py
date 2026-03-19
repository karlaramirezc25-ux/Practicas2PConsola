class OperacionesMatematicas:
    """Clase para realizar operaciones matemáticas básicas."""

    def sumar(self, a: float, b: float) -> float:
        """Devuelve la suma de a y b."""
        return a + b

    def restar(self, a: float, b: float) -> float:
        """Devuelve la resta de a y b."""
        return a - b

    def multiplicar(self, a: float, b: float) -> float:
        """Devuelve el producto de a y b."""
        return a * b

    def dividir(self, a: float, b: float) -> float:
        """Devuelve la división de a entre b. Lanza una excepción si b es cero."""
        if b == 0:
            raise ValueError("No se puede dividir por cero.")
        return a / b
