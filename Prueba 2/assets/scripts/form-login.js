// Validacion para el formulario de inicio de sesion [WIP]

$(document).ready(function () {

    console.log('Cargando...');

    $('#formLogin').submit(function (e) { 

        e.preventDefault();

        var emailLogin = $('#emailLogin').val();
        var passwordLogin = $('#passwordLogin').val();

        $(".error").remove();

        if (passwordLogin.lenght < 12) {
            $('#passwordLogin').after('<span class="error"> Debe tener mas de 12 caracteres </span>')
        }

        if (emailLogin.lenght < 1) {
            var regEx = /^[A-Z0-9][A-Z0-9._%+-]{0,63}@(?:[A-Z0-9-]{1,63}\.){1,125}[A-Z]{2,63}$/;
            var emailValido = regEx.test(emailLogin);

            if (!emailValido) {
                $('#emailLogin').after('<span class="error"> Rellena este campo </span>')
            }
        }
    });
});