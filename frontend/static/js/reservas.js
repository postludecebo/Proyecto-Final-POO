document.addEventListener("DOMContentLoaded", () => {
    const tabla = document.getElementById("tabla-reservas")
    const form = document.getElementById("form-reserva")
    const idInput = document.getElementById("reserva-id")

    tabla.addEventListener("click", e => {
        if (e.target.classList.contains("editar-btn")) {
            const fila = e.target.closest("tr")
            idInput.value = e.target.dataset.id
            form.clienteId.value = fila.children[1].dataset.clienteid
            form.glampingId.value = fila.children[2].dataset.glampingid
            form.fechaInicio.value = fila.children[3].textContent
            form.fechaFin.value = fila.children[4].textContent
            form.totalPagado.value = fila.children[5].textContent
            form.estado.value = fila.children[6].textContent
            form.action = "/actualizar_reserva"
        }
        if (e.target.classList.contains("eliminar-btn")) {
            window.location.href = `/eliminar_reserva/${e.target.dataset.id}`
        }
   
    })
const btnGuardar = document.getElementById("btn-guardar")
const btnCancelar = document.getElementById("btn-cancelar")

btnCancelar.addEventListener("click", () => {
    form.reset()
    idInput.value = ""
    form.action = "/guardar_reserva"
    btnGuardar.textContent = "Guardar"
    btnCancelar.style.display = "none"
})

form.addEventListener("submit", e => {
    e.preventDefault()

    const datos = {
        id: idInput.value,
        clienteId: form.clienteId.value,
        glampingId: form.glampingId.value,
        fechaInicio: form.fechaInicio.value,
        fechaFin: form.fechaFin.value,
        totalPagado: form.totalPagado.value,
        estado: form.estado.value,
        action: form.action
    }

    console.log("[DEBUG RESERVA]", datos)

    if (!datos.id) {
        console.log("🆕 Se está creando nueva reserva")
    } else {
        console.log(`🛠️ Editando reserva #${datos.id}`)
        btnGuardar.textContent = "Actualizar"
        btnCancelar.style.display = "inline-block"
    }

    form.submit()
})
const estadoEdicion = document.getElementById("estado-edicion")
const edicionIdSpan = document.getElementById("reserva-edicion-id")

edicionIdSpan.textContent = `#${id}`
estadoEdicion.style.display = "block"

})
