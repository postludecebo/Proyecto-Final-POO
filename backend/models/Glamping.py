import json, os

class Glamping:
    
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    _archivo_json = os.path.join(BASE_DIR, '../data/glampings.json')


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
        id = int(data.get("id")) if data.get("id") else None
        return cls(
            id=id,
            nombre=data.get("nombre", ""),
            capacidad=int(data.get("capacidad", 0)),
            precio_por_noche=float(data.get("precio_por_noche", 0)),
            descripcion=data.get("descripcion", "")
        )


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
            with open(cls._archivo_json, 'w') as f:
                json.dump([], f)

        with open(cls._archivo_json, 'r') as f:
            contenido = f.read().strip()
            if not contenido:
                return []
            return json.loads(contenido)


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
