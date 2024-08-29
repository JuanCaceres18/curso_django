const $formularioCurso = document.getElementById('formularioCurso');
const $txtNombre = document.getElementById('txtNombre');
const $creditos = document.getElementById('numCreditos');
const btnsEliminacion = document.querySelectorAll('.btnEliminacion');

console.log("Hola")


(function(){
    notificacionSwal(document.title, "Cursos listados con éxito", "success", "Ok!")

    $formularioCurso.addEventListener('submit',function(e){
        let nombre = String($txtNombre.value).trim()
        if (nombre.length < 3){
            notificacionSwal(document.title, "El nombre del curso no puede ir vacío", "warning", "Ok!")
            e.preventDefault();
        } else {
            let creditos = parseInt($creditos.value)
            if (creditos < 1 || creditos > 10){
                notificacionSwal(document.title, "Los creditos deben ser un numero entre 1 y 10", "warning", "Ok!")
                e.preventDefault();
            }
        }
    })

    btnsEliminacion.forEach(btn => {
        btn.addEventListener('click', function(e){
            let confirmacion = confirm("¿Confirma la eliminación del curso?")
            if (!confirmacion){
                btn.preventDefault();
            }
        })
    })
})()