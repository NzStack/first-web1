
function confirmarEliminacion(id){
    
    Swal.fire({
        title: 'Esta Seguro?',
        text: "No podras deshacer esta accion",
        type: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, Eliminar!',
        cancelButtonText: 'Cancelar'
    }).then((result) => {
      if (result.value) {
          window.location.href ="/eliminar-cliente/"+id+"/";
      }
    })
}