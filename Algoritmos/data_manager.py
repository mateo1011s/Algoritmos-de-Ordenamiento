import random

class DataManager:

    def __init__(self):
        self._base_data = []

    @property
    def base_data(self):
        return self._base_data

    def set_data_manual(self, input_string: str):

        try:
            data_list = [int(item.strip()) for item in input_string.split(',') if item.strip()]
            
            if not data_list:
                raise ValueError("No se detectaron números válidos en el texto ingresado.")
                
            self._base_data = data_list
            
        except ValueError:
            raise ValueError("El ingreso contiene caracteres no válidos. Use solo números enteros separados por comas.")
            
    def set_data_random(self, count: int):

        if count <= 0:
            raise ValueError("La cantidad de datos debe ser mayor a cero.")
            
        self._base_data = [random.randint(1, 1000) for _ in range(count)]


# --- Ejemplo de Uso del DataManager (Opcional, para pruebas unitarias) ---
if __name__ == "__main__":
    dm = DataManager()
    
    try:
        dm.set_data_manual("15, 8, 2, 99")
        print(f"Datos base (Manual): {dm.base_data}")
        copy1 = dm.get_data_copy()
        print(f"Copia para ordenar: {copy1}")
    except ValueError as e:
        print(f"Error Manual: {e}")

    try:
        dm.set_data_random(10)
        print(f"Datos base (Random): {dm.base_data}")
        copy2 = dm.get_data_copy()
        print(f"Copia para ordenar: {copy2}")
    except ValueError as e:
        print(f"Error Aleatorio: {e}")