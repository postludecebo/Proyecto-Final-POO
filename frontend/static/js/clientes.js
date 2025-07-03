document.addEventListener("DOMContentLoaded", () => {
    const tabla = document.getElementById("tabla-clientes")
    const form = document.getElementById("form-cliente")
    const idInput = document.getElementById("cliente-id")

    tabla.addEventListener("click", e => {
        if (e.target.classList.contains("editar-btn")) {
            const fila = e.target.closest("tr")
            idInput.value = e.target.dataset.id
            form.nombre.value = fila.children[1].textContent
            form.email.value = fila.children[2].textContent
            form.telefono.value = fila.children[3].textContent
            form.documento.value = fila.children[4].textContent
            form.action = "/actualizar_cliente"
        }
        if (e.target.classList.contains("eliminar-btn")) {
            window.location.href = `/eliminar_cliente/${e.target.dataset.id}`
        }
    })
})
