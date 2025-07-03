document.addEventListener("DOMContentLoaded", () => {
    const tabla = document.getElementById("tabla-glampings")
    const form = document.getElementById("form-glamping")
    const idInput = document.getElementById("glamping-id")
    const btnGuardar = document.getElementById("btn-guardar")
    const btnCancelar = document.getElementById("btn-cancelar")
    const estadoEdicion = document.getElementById("estado-edicion")
    const edicionIdSpan = document.getElementById("glamping-edicion-id")

    tabla.addEventListener("click", e => {
        console.log("Action del formulario:", form.action)

        if (e.target.classList.contains("editar-btn")) {
            
            const fila = e.target.closest("tr")
            const id = e.target.dataset.id
            idInput.value = id
            console.log(idInput.value)
            form.nombre.value = fila.children[1].textContent
            form.capacidad.value = fila.children[2].textContent
            form.precio_por_noche.value = fila.children[3].textContent
            form.descripcion.value = fila.children[4].textContent

            form.action = "/actualizar_glamping"
            console.log(form.action)
            btnGuardar.textContent = "Actualizar"
            btnCancelar.style.display = "inline-block"
            estadoEdicion.style.display = "block"
            edicionIdSpan.textContent = `#${id}`
        }

        if (e.target.classList.contains("eliminar-btn")) {
            window.location.href = `/eliminar_glamping/${e.target.dataset.id}`
        }
    })


    btnCancelar.addEventListener("click", () => {
        form.reset()
        idInput.value = ""
        form.action = "/guardar_glamping"
        btnGuardar.textContent = "Guardar"
        btnCancelar.style.display = "none"
        estadoEdicion.style.display = "none"
        edicionIdSpan.textContent = ""
    })
form.addEventListener("submit", e => {
    e.preventDefault(); 

    const datos = {
        id: idInput.value,
        nombre: form.nombre.value,
        capacidad: form.capacidad.value,
        precio_por_noche: form.precio_por_noche.value,
        descripcion: form.descripcion.value,
        action: form.action
    }

    console.log("[DEBUG] Datos enviados desde el formulario:", datos)

    if (!idInput.value) {
        console.warn("⚠️ No hay ID, se está creando un nuevo glamping.")
    } else {
        console.info(`🛠️ Editando glamping con ID #${idInput.value}`)
    }

    form.submit(); 
})

})
