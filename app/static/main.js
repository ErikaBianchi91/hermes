
$(".special").click(function (e){
    var x= e.target.id
    $.ajax({
        type: 'POST',
        data: {
            'dishes' : x,
        },
        success: function(response){
            console.log(response);
            },
        error: function(error){
            console.log(error);
            },
    });   
    e.preventDefault();    
}
)
