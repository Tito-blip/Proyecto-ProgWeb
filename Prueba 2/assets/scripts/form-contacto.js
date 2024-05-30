// Validacion para el formulario de contactov

document.getElementById("postulacionForm").addEventListener("submit", function(event) {
  event.preventDefault(); // Evita el envío del formulario por defecto
  
  // Obtener los valores de los campos del formulario
  var form = event.target;
  var rut = form.elements["rut"].value;
  var nombre = form.elements["nombre"].value;
  var apellidoPaterno = form.elements["apellidoPaterno"].value;
  var apellidoMaterno = form.elements["apellidoMaterno"].value;
  var edad = form.elements["edad"].value;
  var genero = form.elements["select"].value;
  var email = form.elements["email"].value;
  var fono = form.elements["fono"].value;
  var comentarios = form.elements["comentarios"].value;

  const emailValido = email => {
    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
  }

  // Validar que todos los campos obligatorios estén completos
  if (!rut || !nombre || !apellidoPaterno || !apellidoMaterno || !edad || !genero || !email || !fono) {
      alert("Por favor, complete todos los campos obligatorios.");
      return;
  }
  
  if (rut.length < 9 || rut.length > 10) {
    alert("El rut no cumple con el numero de caracteres.");
    return;
  };

  if (nombre.length < 3 || nombre.length > 20) {
    alert("El nombre no cumple con el numero de caracteres.");
    return;
  };

  if (apellidoPaterno.length < 3 || apellidoPaterno.length > 30 || apellidoMaterno.length < 3 || apellidoMaterno.length > 30) {
    alert("El apellido no cumple con el numero de caracteres.");
    return;
  };

  if (emailValido(email.value)) {
    return;
  }

  if (edad.value < 18 || edad.value > 35) {
    alert("No cumple con la edad requerida.");
    return;
  };
  alert('¡Formulario enviado con éxito!');
  // Obtener la fecha actual para incluirla en la carta de postulación
  var fecha = new Date();
  var diaSemana = ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'];
  var mesAnyo = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'];
  var fecha_formateada = `${diaSemana[fecha.getDay()]}, ${fecha.getDate()} de ${mesAnyo[fecha.getMonth()]} de ${fecha.getFullYear()}`;
 
  // Crear una carta de postulación en formato de texto
  var carta = "Carta de Postulación\n\n";
  carta += `Nombre: ${nombre} ${apellidoPaterno} ${apellidoMaterno}\n`;
  carta += `RUT: ${rut}\n`;
  carta += `Edad: ${edad}\n`;
  carta += `Genero: ${genero}\n`;
  carta += `Correo Electrónico: ${email}\n`;
  carta += `Teléfono de Contacto: ${fono}\n`;
  carta += `Fecha de Postulación: ${fecha_formateada}\n`;
  carta += `Comentarios: ${comentarios}\n`;
  

  // Mostrar la carta de postulación en el documento HTML
  var cartaPostulacion = document.getElementById("cartaPostulacion");
  cartaPostulacion.innerText = carta;
  cartaPostulacion.style.display = "block";


  // Desplazarse hacia la carta de postulación después de mostrarla
  cartaPostulacion.scrollIntoView({ behavior: 'smooth' });

  // Crear y descargar el PDF usando jsPDF
  const { jsPDF } = window.jspdf;
  const doc = new jsPDF();

  doc.text(carta, 10, 10);
  doc.save('Carta_de_Postulacion.pdf');
 
  // Restablecer el formulario si es necesario
  postulacionForm.reset();
});
