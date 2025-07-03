import json
import os

class Cliente:
    

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    _archivo_json = os.path.join(BASE_DIR, '../data/clientes.json')


    def __init__(self, id=None, nombre='', email='', telefono='', documento=''):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.documento = documento

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, data):
        id = int(data.get("id")) if data.get("id") else None
        return cls(
            id=id,
            nombre=data.get("nombre", ""),
            email=data.get("email", ""),
            telefono=data.get("telefono", ""),
            documento=data.get("documento", "")
        )


    def guardar(self):
        clientes = self.cargar_todos()
        
        if not self.id:
            self.id = max([c['id'] for c in clientes], default=0) + 1
        else:
            self.id = int(self.id)  

        clientes = [c for c in clientes if c['id'] != self.id]
        clientes.append(self.to_dict())

        with open(self._archivo_json, 'w') as f:
            json.dump(clientes, f, indent=4)
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
    def obtener_clientes(cls):
        return [cls.from_dict(d) for d in cls.cargar_todos()]

    @classmethod
    def obtener_cliente_por_id(cls, id):
        for c in cls.obtener_clientes():
            if c.id == id:
                return c
        return None

    @classmethod
    def eliminar_cliente_por_id(cls, id):
        clientes = cls.cargar_todos()
        clientes = [c for c in clientes if c['id'] != id]
        with open(cls._archivo_json, 'w') as f:
            json.dump(clientes, f, indent=4)
        return True
