"""Módulo de prueba para la documentación con Doxygen."""

class Salurador:
    """Clase principal para gestionar saludos."""

    def saludar(self, nombre: str) -> str:
        """Devuelve un saludo personalizado.

        @param nombre Nombre de la persona a saludar.
        @return El mensaje de saludo formateado.
        """
        return f"¡Hola, {nombre}!"