                 // Obtener referencias a los elementos
let dialogContainer = document.getElementById("dialogContainer");
let closeButton = document.getElementsByClassName("close-button")[0];
let submitButton = document.getElementById("submitButton");
let form = document.getElementById("contactForm");

// const focusLinks = document.querySelectorAll('.loginIngresar');

// focusLinks.forEach(link => {
//     link.addEventListener('click', function(event) {
//         event.preventDefault(); 
//         document.getElementById('username').focus(); // Enfoca el input
//     });
// });

if (dialogContainer) {
    closeButton.addEventListener("click", function() {
        dialogContainer.style.display = "none";
        form.submit();
    });
}

if (form) {
    form.addEventListener("submit", function (event) {
        event.preventDefault();

        let campoOculto = document.getElementsByClassName("campoObligatorio");
        let valid = true;

        let names = document.getElementById("nombre").value;
        let tel = document.getElementById("telefono").value;
        let email = document.getElementById("email").value;
        let message = document.getElementById("mensaje").value;


        if (!names || !email || !tel || !message) {
            valid = false;
        } else {
            if (message.length < 50) {
                valid = false;
            } else {
                if (!validateEmail(email)) {
                    alert('Por favor, ingrese un correo electrónico válido.');
                    valid = false;
                } else {
                    valid = true;
                }
            }
        }
        if (!valid) {
            submitButton.classList.add("button-container-moved"); //
            for (let i = 0; i < campoOculto.length; i++) {
                //submitButton.classList.add("button-container-moved"); //
                campoOculto[i].classList.add("visible");
                campoOculto[i].style.display ="inline";
            }
            setTimeout(function() {
                for (let i = 0; i < campoOculto.length; i++) {
                    campoOculto[i].classList.remove("visible");
                    campoOculto[i].style.display ="none";
                    submitButton.classList.remove("button-container-moved"); //
                }
            }, 3000);

        } else {
            // Mostrar la ventana emergente después de enviar el formulario
            showDialogContainer(names, message, email, tel);
        }

        function validateEmail(email) {
            var re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            return re.test(email);
        }

        function showDialogContainer(name, message, email, tel) {
            let titleForm = document.getElementById("title-form");
            let datosRecibidos = document.getElementById("datos-recibidos");
            let tipoConsulta = document.getElementById("tipoConsulta");
            let radioButtonMedio = document.getElementsByName("medioRespuesta");
            let medio;
            for (let i = 0; i < radioButtonMedio.length; i++) {
                if(radioButtonMedio[i].checked) {
                    medioElegido = radioButtonMedio[i].value;
                    if(medioElegido=="Email") {
                        medio = email;
                    } else {
                        medio = tel;
                    }
                    break;
                }
            }
            if(!tipoConsulta.value) {
                consulta = "Consulta";
            } else {
                consulta = tipoConsulta.value;
            }
            let recibirPromos = document.getElementById("recibirPromos");
            titleForm.textContent = `¡Hola! ${name}`;
            datosRecibidos.innerHTML = `Gracias por escribirnos, responderemos a tu <strong>${consulta}</strong> a la brevedad. Nos contactaremos a través de tu <strong>${medioElegido}</strong> a <strong>${medio}</strong>`;
            if(recibirPromos.checked) {
                datosRecibidos.innerHTML += `<br> Te estaremos enviando nuestras <strong>promos</strong>, estate atento!`;
            }
            datosRecibidos.innerHTML += `<br><br><strong>¡Hasta pronto!</strong>`;
            let mensajeRecibido = document.getElementById("mensaje-recibido");
            mensajeRecibido.innerHTML = `<i>${message}</i>`;
            dialogContainer.style.display = "block";
        }
    });
}

// funcion para el menu para pantallas
const btnMenu = document.querySelector('.btn-menu');
const menuItems = document.querySelector('.menu-items');
const menuItemsClick = document.querySelectorAll('.menu-items a');

btnMenu.addEventListener('click', () => {
    if(btnMenu.textContent=="☰") {
        btnMenu.textContent = "✕";
        menuItems.style.display = 'block';
    } else {
        btnMenu.textContent = "☰";
        menuItems.style.display = 'none';
    }
});

menuItemsClick.forEach(item => {
    item.addEventListener('click', () => {
        btnMenu.textContent = "☰";
        menuItems.style.display = 'none';
    });
});

function cambiarImagen(id_red,imagen) {
    document.getElementById(id_red).src = '/static/img/'+imagen;
}
function restaurarImagen(id_red, imagen) {
    document.getElementById(id_red).src = '/static/img/'+imagen;
}