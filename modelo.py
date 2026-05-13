class Vehiculo:
    def __init__(self, patente, modelo, tarifa_diaria):
        if not patente or not patente.strip():
            raise ValueError("La patente no puede estar vacia.")
        if not modelo or not modelo.strip():
            raise ValueError("El modelo no puede estar vacio.")
        if tarifa_diaria <= 0:
            raise ValueError("La tarifa diaria debe ser un valor positivo.")
        self.patente       = patente.strip().upper()
        self.modelo        = modelo.strip()
        self.tarifa_diaria = float(tarifa_diaria)
        self.estado        = "disponible"

    def esta_disponible(self): return self.estado == "disponible"

    def marcar_alquilado(self):
        if not self.esta_disponible():
            raise ValueError(f"El vehiculo '{self.patente}' ya esta alquilado.")
        self.estado = "alquilado"

    def marcar_disponible(self):
        if self.esta_disponible():
            raise ValueError(f"El vehiculo '{self.patente}' ya esta disponible.")
        self.estado = "disponible"


class Cliente:
    def __init__(self, dni, nombre):
        if not dni or not dni.strip():
            raise ValueError("El DNI no puede estar vacio.")
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacio.")
        self.dni    = dni.strip()
        self.nombre = nombre.strip()


class Alquiler:
    def __init__(self, vehiculo, cliente, dias):
        if not isinstance(dias, int) or dias <= 0:
            raise ValueError("Los dias deben ser un entero positivo.")
        self.vehiculo = vehiculo
        self.cliente  = cliente
        self.dias     = dias

    def calcular_costo(self): return self.dias * self.vehiculo.tarifa_diaria


class Agencia:
    def __init__(self):
        self._vehiculos  = []
        self._clientes   = []
        self._alquileres = []

    def registrar_vehiculo(self, patente, modelo, tarifa):
        if self.buscar_vehiculo(patente):
            raise ValueError(f"Ya existe un vehiculo con patente '{patente.strip().upper()}'.")
        v = Vehiculo(patente, modelo, tarifa)
        self._vehiculos.append(v)
        return v

    def buscar_vehiculo(self, patente):
        p = patente.strip().upper()
        return next((v for v in self._vehiculos if v.patente == p), None)

    def listar_vehiculos(self): return list(self._vehiculos)

    def registrar_cliente(self, dni, nombre):
        if self.buscar_cliente(dni):
            raise ValueError(f"Ya existe un cliente con DNI '{dni.strip()}'.")
        c = Cliente(dni, nombre)
        self._clientes.append(c)
        return c

    def buscar_cliente(self, dni):
        d = dni.strip()
        return next((c for c in self._clientes if c.dni == d), None)

    def listar_clientes(self): return list(self._clientes)

    def alquilar_vehiculo(self, patente, dni, dias):
        v = self.buscar_vehiculo(patente)
        if not v: raise ValueError(f"Vehiculo '{patente}' no encontrado.")
        c = self.buscar_cliente(dni)
        if not c: raise ValueError(f"Cliente con DNI '{dni}' no encontrado.")
        if not v.esta_disponible():
            raise ValueError(f"El vehiculo '{v.patente}' no esta disponible.")
        if not isinstance(dias, int) or dias <= 0:
            raise ValueError("Los dias deben ser un entero positivo.")
        v.marcar_alquilado()
        a = Alquiler(v, c, dias)
        self._alquileres.append(a)
        return a

    def devolver_vehiculo(self, patente):
        v = self.buscar_vehiculo(patente)
        if not v: raise ValueError(f"Vehiculo '{patente}' no encontrado.")
        a = next((x for x in self._alquileres if x.vehiculo is v), None)
        if not a: raise ValueError(f"'{v.patente}' no tiene alquiler activo.")
        costo = a.calcular_costo()
        v.marcar_disponible()
        self._alquileres.remove(a)
        return a, costo

    def listar_alquileres(self): return list(self._alquileres)
