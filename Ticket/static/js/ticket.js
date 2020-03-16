
$(document).ready(function(){

    $('form').on('submit', function(e){

        e.preventDefault();
        var Input = {
            'name' : $('#name').val(),
            'age' : $('#age').val(),
            'gender' : $('#gender').val(),
            'berth' : $('#berth').val(),
        }

        $.ajax({
            type : "POST",
            url : '/ticket_book',
            data : JSON.stringify(Input),
            success : function(data)
            { 
                console.log("Ajax Ss");

                if (data.is_success == "success"){
                    if (data.alert){
                       
                        swal({
                            title: "Alert!",
                            text: data.alert,
                            icon: "info",
                        });
                    }
                    if (data.msg){
                        swal({
                            title: "Booking Status!",
                            text: data.msg,
                            icon: "success",
                          });
                       
                    }

                    $('#create_form').trigger('reset');
                }
                
                if (data.is_success == "unsuccess"){
                    if (data.error_message){
                        swal({
                            title: "Alert!",
                            text: data.error_message,
                            icon: "info",

                        });
 
                      
                    }
                }    
            }

        });

    });


});