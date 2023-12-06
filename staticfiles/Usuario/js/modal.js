function openSearchModal() {
    document.getElementById("searchModal").style.display = "block";
}

function closeSearchModal() {
    document.getElementById("searchModal").style.display = "none";
}

function search() {
    // Obtener los valores seleccionados
    var categoriaSeleccionada = document.getElementById("categoria").value;
    var estadoSeleccionado = document.getElementById("estado").value;
    console.log(categoriaSeleccionada,estadoSeleccionado)
    // Enviar una solicitud AJAX al servidor con los filtros
    fetch(`/buscar/?categoria=${categoriaSeleccionada}&estado=${estadoSeleccionado}`)
        .then(response => response.json())
        .then(data => {
            // Limpiar los productos actuales en la página
            document.getElementById("productos-container").innerHTML = '';

            // Manejar los resultados de la búsqueda aquí
            console.log("Resultados de la búsqueda:", data.resultados);
            if (data.resultados.length > 0){
                // Iterar sobre los resultados y agregarlos a la página
                for (var i = 0; i < data.resultados.length; i++) {
                    var producto = data.resultados[i];
                    var nuevoProductoHTML = `
                        <div class="card">
                            <img src="${producto.imagen_url}">
                            <h5>${producto.descripcion}</h5>
                            <p class="p">$${producto.precio}</p>
                            <p>Estado: ${producto.condicion}</p>
                            <a href="{% url 'detalle' %}">Ver</a>
                        </div>
                    `;
                    // Agregar el nuevo producto al contenedor en la página
                    document.getElementById("productos-container").innerHTML += nuevoProductoHTML;
                    document.getElementById("rb").style.display="block"
                    document.getElementById('nb').style.display="none"
                }
            }
            else{
                document.getElementById('nb').style.display="block"
            }
                ocultarDiv()
                presentarFiltros()

        })
        .catch(error => {
            console.error("Error al realizar la búsqueda:", error);
        });

    // Cerrar el modal después de realizar la búsqueda

    closeSearchModal()

}
function ocultarDiv () {
    var filtrarDiv = document.getElementById('search-button-container')
    filtrarDiv.style.display='none'
}
function presentarFiltros() {
    var filtros = document.getElementById('filtros')
    filtros.style.display='block'

}

function search0() {
    // Obtener los valores seleccionados
    var categoriaSeleccionada = document.getElementById("categoria0").value;
    var estadoSeleccionado = document.getElementById("estado0").value;
    console.log(categoriaSeleccionada,estadoSeleccionado)
    // Enviar una solicitud AJAX al servidor con los filtros
    fetch(`/buscar/?categoria=${categoriaSeleccionada}&estado=${estadoSeleccionado}`)
        .then(response => response.json())
        .then(data => {
            // Limpiar los productos actuales en la página
            document.getElementById("productos-container").innerHTML = '';

            // Manejar los resultados de la búsqueda aquí
            console.log("Resultados de la búsqueda:", data.resultados);
            if (data.resultados.length > 0){
                // Iterar sobre los resultados y agregarlos a la página
                for (var i = 0; i < data.resultados.length; i++) {
                    var producto = data.resultados[i];
                    var nuevoProductoHTML = `
                        <div class="card">
                            <img src="${producto.imagen_url}">
                            <h5>${producto.descripcion}</h5>
                            <p class="p">$${producto.precio}</p>
                            <p>Estado: ${producto.condicion}</p>
                            <a href="{% url 'detalle' %}">Ver</a>
                        </div>
                    `;
                    // Agregar el nuevo producto al contenedor en la página
                    document.getElementById("productos-container").innerHTML += nuevoProductoHTML;
                    document.getElementById("rb").style.display="block"
                    document.getElementById('nb').style.display="none"
                }
            }
            else{
                document.getElementById('nb').style.display="block"
            }
                ocultarDiv()
                presentarFiltros()

        })
        .catch(error => {
            console.error("Error al realizar la búsqueda:", error);
        });

    // Cerrar el modal después de realizar la búsqueda

    closeSearchModal()

}