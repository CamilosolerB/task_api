function deleteNote(ide, protocol){
    Swal.fire({
        title: "¿Estas seguro?",
        text: "Si lo eliminas ya no lo tendras",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Si"
      }).then((result) => {
        if (result.isConfirmed) {
            fetch('/delete/'+ide,{
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': protocol
                }
            })
            . then( res =>{
                if(res.ok){
                    Swal.fire({
                        title: "Eliminado",
                        text: "Ha sido eliminado correctamente",
                        icon: "success"
                      });
                    location.reload();
                } else {
                    Swal.fire({
                        title: "No ha sido eliminado correctamente",
                        text: "Hubo un problema intente nuevamente",
                        icon: "error"
                      });
                }
            })
        }
      });
}

function ingressSucess(){
    const Toast = Swal.mixin({
        toast: true,
        position: "top-end",
        showConfirmButton: false,
        timer: 3000,
        timerProgressBar: true,
        didOpen: (toast) => {
          toast.onmouseenter = Swal.stopTimer;
          toast.onmouseleave = Swal.resumeTimer;
        }
      });
      Toast.fire({
        icon: "success",
        title: "Funcion realizada con exito"
      });
}

window.addEventListener('load',ingressSucess);