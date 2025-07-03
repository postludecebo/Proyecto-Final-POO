document.addEventListener("DOMContentLoaded", () => {
    const tabla = document.getElementById("tabla-glampings")
    const form = document.getElementById("form-glamping")
    const idInput = document.getElementById("glamping-id")

    tabla.addEventListener("click", e => {
        if (e.target.classList.contains("editar-btn")) {
            const fila = e.target.closest("tr")
            idInput.value = e.target.dataset.id
            form.nombre.value = fila.children[1].textContent
            form.capacidad.value = fila.children[2].textContent
            form.precio_por_noche.value = fila.children[3].textContent
            form.descripcion.value = fila.children[4].textContent
            form.action = "/actualizar_glamping"
        }
        if (e.target.classList.contains("eliminar-btn")) {
            window.location.href = `/eliminar_glamping/${e.target.dataset.id}`
        }
    })
})
