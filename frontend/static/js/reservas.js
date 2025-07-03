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
})
