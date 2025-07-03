document.addEventListener("DOMContentLoaded", () => {
    const tabla = document.getElementById("tabla-clientes")
    const form = document.getElementById("form-cliente")
    const idInput = document.getElementById("cliente-id")
    const btnGuardar = document.getElementById("btn-guardar")
    const btnCancelar = document.getElementById("btn-cancelar")
    const estadoEdicion = document.getElementById("estado-edicion")
    const edicionIdSpan = document.getElementById("cliente-edicion-id")

    tabla.addEventListener("click", e => {
        if (e.target.classList.contains("editar-btn")) {
            const fila = e.target.closest("tr")
            const id = e.target.dataset.id
            idInput.value = id

            form.nombre.value = fila.children[1].textContent
            form.email.value = fila.children[2].textContent
            form.telefono.value = fila.children[3].textContent
            form.documento.value = fila.children[4].textContent

            form.action = "/actualizar_cliente"
            btnGuardar.textContent = "Actualizar"
            btnCancelar.style.display = "inline-block"
            estadoEdicion.style.display = "block"
            edicionIdSpan.textContent = `#${id}`
        }

        if (e.target.classList.contains("eliminar-btn")) {
            const idEliminar = e.target.closest("a")?.dataset.id || e.target.dataset.id
            if (idEliminar) {
                window.location.href = `/eliminar_cliente/${idEliminar}`
            }
        }
    })

    btnCancelar.addEventListener("click", () => {
        form.reset()
        idInput.value = ""
        form.action = "/guardar_cliente"
        btnGuardar.textContent = "Guardar"
        btnCancelar.style.display = "none"
        estadoEdicion.style.display = "none"
        edicionIdSpan.textContent = ""
    })

    form.addEventListener("submit", e => {
        e.preventDefault()
        const datos = {
            id: idInput.value,
            nombre: form.nombre.value,
            email: form.email.value,
            telefono: form.telefono.value,
            documento: form.documento.value,
            action: form.action
        }
        console.log("[DEBUG Cliente] Datos enviados:", datos)
        form.submit()
    })
})
