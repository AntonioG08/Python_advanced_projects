
$(function(){
    $('#btn1').click(obtieneInformacion);
});

function obtieneInformacion() {
    let pagina = $('#txtPag').val();
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
    console.log(pagina);
    console.log(url_final);
};

function procesaInformacion() {

};
