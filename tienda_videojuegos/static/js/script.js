document.addEventListener("DOMContentLoaded", function () {
    const btn = document.getElementById("toggle-theme");
    const html = document.documentElement;

    //Recuperar el tema guardado en el localStorage al cargar la pagina
    const savedTheme = localStorage.getItem("theme");
    if (savedTheme) {
        html.setAttribute("data-bs-theme", savedTheme);
    }

    btn.addEventListener("click", function () {
        const current = html.getAttribute("data-bs-theme");
        const next = current === "dark" ? "light" : "dark";
        html.setAttribute("data-bs-theme", next)

        //Guardar el tema elegido en localStorage
        localStorage.setItem("theme", next)
    });
});

// Mostrar/ocultar contraseña
function togglePassword(fieldId) {
    const field = document.getElementById(fieldId);
    const icon = document.getElementById('icon-' + fieldId);
    if (field.type === "password") {
        field.type = "text";
        icon.classList.remove('bi-eye');
        icon.classList.add('bi-eye-slash');
    } else {
        field.type = "password";
        icon.classList.remove('bi-eye-slash');
        icon.classList.add('bi-eye');
    }
}

// EFECTO NAVBAR AL HACER SCROLL
window.addEventListener("scroll", function () {
    const navbar = document.getElementById("mainNavbar");

    if (window.scrollY > 50) {
        navbar.classList.add("navbar-scrolled");
    } else {
        navbar.classList.remove("navbar-scrolled");
    }
});

// Mensajes flotantes
document.addEventListener("DOMContentLoaded", function () {

    const toastElList = document.querySelectorAll('.toast');

    toastElList.forEach(function (toastEl) {

        console.log("Toast encontrado:", toastEl); // DEBUG

        const toast = new bootstrap.Toast(toastEl, {
            delay: 3000,

        });

        toast.show();
    });

});