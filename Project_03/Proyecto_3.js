
$(function(){
    obtieneInformacion("1")
    $('#btnConsulta').click(function(){
        let textoBtn = $(this).text();
        console.log(textoBtn);
        if (textoBtn == "Página 2") {
            $("#tarjetas").empty();
            obtieneInformacion("2");
            $(this).text("Página 1");
        }
        else {
            $("#tarjetas").empty();
            obtieneInformacion("1");
            $(this).text("Página 2")
        }
    });
});

function obtieneInformacion(pagina) {
    let url_creado = 'https://reqres.in/api/users?page=' + pagina
    $.ajax({
        // url: 'https://reqres.in/api/users',
        url: url_creado,
        type: 'GET',
        dataType: 'Json',
        success: function(data) {
            console.log(data);
            procesaInformacion(data);
        },
        error: function(xhr, status, error) {
            console.log(status); 
            console.log(error);    
        }
    })
    console.log(url_creado);
};

function procesaInformacion(datos) {
    arreglo = datos.data;
    $.each(arreglo, function(index, element) {
        let plantilla = 
        "<div class='card'>" +
            "<h3 class='card-title'>Nombre Apellido</h3>" + 
            "<img class='card-image' src='ImgPersona' style='width: 100%;'/>" + 
            "<div class='bodyCard'><p class='card-description'>Correo</p>" + 
            "</div>" +
        "</div>";
        let renglon = plantilla.replace("Nombre", element.first_name);
        renglon = renglon.replace("Apellido", element.last_name);
        renglon = renglon.replace("ImgPersona", element.avatar);
        renglon = renglon.replace("Correo", element.email);

        $("#tarjetas").append(renglon);
    });
};
