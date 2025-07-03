from flask import Flask, render_template, request, redirect
from models.Cliente import Cliente
from models.Glamping import Glamping
from models.Reserva import Reserva

app = Flask(__name__, static_folder="../frontend/static", template_folder="templates")


# 🔹 Home
@app.route("/")
def index():
    return render_template("index.html")


# 🔹 CLIENTES
@app.route("/clientes")
def clientes():
    lista = Cliente.obtener_clientes()
    return render_template("clientes.html", clientes=lista)

@app.route("/guardar_cliente", methods=["POST"])
def guardar_cliente():
    cliente = Cliente.from_dict(request.form.to_dict())
    cliente.guardar()
    return redirect("/clientes")

@app.route("/actualizar_cliente", methods=["POST"])
def actualizar_cliente():
    cliente = Cliente.from_dict(request.form.to_dict())
    cliente.guardar()
    return redirect("/clientes")

@app.route("/eliminar_cliente/<int:id>")
def eliminar_cliente(id):
    Cliente.eliminar_cliente_por_id(id)
    return redirect("/clientes")


# 🔹 GLAMPINGS
@app.route("/glampings")
def glampings():
    lista = Glamping.obtener_glampings()
    return render_template("glampings.html", glampings=lista)

@app.route("/guardar_glamping", methods=["POST"])
def guardar_glamping():
    glamping = Glamping.from_dict(request.form.to_dict())
    glamping.guardar()
    return redirect("/glampings")

@app.route("/actualizar_glamping", methods=["POST"])
def actualizar_glamping():
    glamping = Glamping.from_dict(request.form.to_dict())
    glamping.guardar()
    return redirect("/glampings")

@app.route("/eliminar_glamping/<int:id>")
def eliminar_glamping(id):
    Glamping.eliminar_glamping_por_id(id)
    return redirect("/glampings")


# 🔹 RESERVAS
@app.route("/reservas")
def reservas():
    clientes = Cliente.obtener_clientes()
    glampings = Glamping.obtener_glampings()
    lista = Reserva.obtener_reservas(clientes, glampings)
    return render_template("reservas.html", reservas=lista, clientes=clientes, glampings=glampings)

@app.route("/guardar_reserva", methods=["POST"])
def guardar_reserva():
    datos = request.form.to_dict()
    cliente = Cliente.obtener_cliente_por_id(int(datos.get("clienteId")))
    glamping = Glamping.obtener_glamping_por_id(int(datos.get("glampingId")))
    reserva = Reserva.from_dict(datos, cliente, glamping)
    reserva.guardar()
    return redirect("/reservas")

@app.route("/actualizar_reserva", methods=["POST"])
def actualizar_reserva():
    datos = request.form.to_dict()
    cliente = Cliente.obtener_cliente_por_id(int(datos.get("clienteId")))
    glamping = Glamping.obtener_glamping_por_id(int(datos.get("glampingId")))
    reserva = Reserva.from_dict(datos, cliente, glamping)
    reserva.guardar()
    return redirect("/reservas")

@app.route("/eliminar_reserva/<int:id>")
def eliminar_reserva(id):
    Reserva.eliminar_reserva_por_id(id)
    return redirect("/reservas")


# 🔹 Ejecutar servidor
if __name__ == "__main__":
    app.run(debug=True)
