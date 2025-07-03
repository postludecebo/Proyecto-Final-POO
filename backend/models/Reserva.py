import json, os
from datetime import datetime

class Reserva:
    _archivo_json = 'backend/data/reservas.json'

    def __init__(self, id=None, cliente=None, glamping=None, fecha_inicio='', fecha_fin='', total_pagado=0.0, estado='pendiente'):
        self.id = id
        self.cliente = cliente
        self.glamping = glamping
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.total_pagado = total_pagado
        self.estado = estado

    def to_dict(self):
        return {
            'id': self.id,
            'clienteId': self.cliente.id if self.cliente else None,
            'glampingId': self.glamping.id if self.glamping else None,
            'fechaInicio': self.fecha_inicio,
            'fechaFin': self.fecha_fin,
            'totalPagado': self.total_pagado,
            'estado': self.estado
        }

    @classmethod
    def from_dict(cls, data, cliente, glamping):
        return cls(
            id=data.get('id'),
            cliente=cliente,
            glamping=glamping,
            fecha_inicio=data.get('fechaInicio'),
            fecha_fin=data.get('fechaFin'),
            total_pagado=data.get('totalPagado'),
            estado=data.get('estado')
        )

    def guardar(self):
        reservas = self.cargar_todos()
        if not self.id:
            self.id = max([r['id'] for r in reservas], default=0) + 1
        reservas = [r for r in reservas if r['id'] != self.id]
        reservas.append(self.to_dict())
        with open(self._archivo_json, 'w') as f:
            json.dump(reservas, f, indent=4)
        return True

    @classmethod
    def cargar_todos(cls):
        if not os.path.exists(cls._archivo_json):
            return []
        with open(cls._archivo_json, 'r') as f:
            return json.load(f)

    @classmethod
    def obtener_reservas(cls, clientes, glampings):
        raw = cls.cargar_todos()
        reservas = []
        for r in raw:
            cliente = next((c for c in clientes if c.id == r['clienteId']), None)
            glamping = next((g for g in glampings if g.id == r['glampingId']), None)
            if cliente and glamping:
                reservas.append(cls.from_dict(r, cliente, glamping))
        return reservas

    @classmethod
    def eliminar_reserva_por_id(cls, id):
        reservas = cls.cargar_todos()
        reservas = [r for r in reservas if r['id'] != id]
        with open(cls._archivo_json, 'w') as f:
            json.dump(reservas, f, indent=4)
        return True
