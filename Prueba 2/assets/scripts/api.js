// API para obtener el clima

$(document).ready(function() {
    const apiUrl = 'https://api.weatherapi.com/v1/forecast.json?key=d8a5a530c42b4cb9ba3194443242905&q=Ancud&days=10&aqi=no&alerts=yes';

    $.ajax({
        url: apiUrl,
        method: 'GET',
        success: function(data) {
            const tabla = $('#tabla_clima');

            console.log(data);

            data.forecast.forecastday.forEach(day => {
                const fecha = new Date(day.date);
                const formattedDate = fecha.toLocaleDateString('es-ES', {year: 'numeric', month: 'long', day: 'numeric' }); // Dar formato de fecha local
                const mintemp = day.day.mintemp_c;
                const maxtemp = day.day.maxtemp_c;
                const lluvia = day.day.daily_chance_of_rain;
                const clima = day.day.condition.icon;
                
                // No considerar [Solo para testeo de respuestas]

                console.log('Date:', fecha);
                console.log('Min Temp:', mintemp); 
                console.log('Max Temp:', maxtemp);
                console.log('Probabilidad de lluvia: ', lluvia);
                console.log('Clima: ', clima);
                console.log('------------------------------');

                // Crear campos dinamicos para la tabla que muestra el clima 

                const fila = 
                `
                <tr>
                    <td>${formattedDate}</td>
                    <td>${'🌡 ' + mintemp + '°C'}</td>
                    <td>${'🌡 ' + maxtemp + '°C'}</td>
                    <td>${'🌧 %' + (lluvia)}</td>
                    <td><img src="${clima}" alt=""></td>
                </tr>
                `
                tabla.append(fila);
            });
        },
        error: function(jqXHR, textStatus, errorThrown) {
            console.error('Error: ', textStatus, errorThrown);
        }
    });
});
