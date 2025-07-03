import json, os

class Glamping:
    _archivo_json = 'backend/data/glampings.json'

    def __init__(self, id=None, nombre='', capacidad=0, precio_por_noche=0.0, descripcion=''):
        self.id = id
        self.nombre = nombre
        self.capacidad = capacidad
        self.precio_por_noche = precio_por_noche
        self.descripcion = descripcion

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

    def guardar(self):
        glampings = self.cargar_todos()
        if not self.id:
            self.id = max([g['id'] for g in glampings], default=0) + 1
        glampings = [g for g in glampings if g['id'] != self.id]
        glampings.append(self.to_dict())
        with open(self._archivo_json, 'w') as f:
            json.dump(glampings, f, indent=4)
        return True

    @classmethod
    def cargar_todos(cls):
        if not os.path.exists(cls._archivo_json):
            return []
        with open(cls._archivo_json, 'r') as f:
            return json.load(f)

    @classmethod
    def obtener_glampings(cls):
        return [cls.from_dict(d) for d in cls.cargar_todos()]

    @classmethod
    def obtener_glamping_por_id(cls, id):
        for g in cls.obtener_glampings():
            if g.id == id:
                return g
        return None

    @classmethod
    def eliminar_glamping_por_id(cls, id):
        glampings = cls.cargar_todos()
        glampings = [g for g in glampings if g['id'] != id]
        with open(cls._archivo_json, 'w') as f:
            json.dump(glampings, f, indent=4)
        return True
