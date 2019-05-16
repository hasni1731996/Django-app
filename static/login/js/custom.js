$(document).ready(function(){
    /// User registration ///
    $("#registrationForm").submit(function()
    {
        $first_name = $('#first_name').val();
        $last_name = $('#last_name').val();
        $cnic = $('#cnic').val();
        $user_role = $('#user_role').val();
        $mobile = $('#mobile').val();
        $email = $('#email').val();
        $address = $('#address').val();
        $img = $('#img').val();
        $username = $('#username').val();
        $pass = $('#password2').val();

        if($('#username').val() == "" || $('#pass').val() == "")
        {
            alert("Please fill up the required field");
        }else
        {
            $.ajax({
                type: "POST",
                url : "",
                data: {
                    first_name:$first_name,
                    last_name:$last_name,
                    cnic:$cnic,
                    user_role:$user_role,
                    mobile:$mobile,
                    email:$email,
                    address:$address,
                    img:$img,
                    username: $username,
                    pass: $pass,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                },
                success: function(data)
                {
                    swal({
                        title: "Congrats!",
                        text: "You Have Successfully Created User!",
                        icon: "success",
                        button: "OK",
                      });
                    console.log(data)
                },
                error: function(data) 
                {
                    swal({
                        title: "Sorry!",
                        text: "Error Creating User!",
                        icon: "error",
                        button: "OK",
                      });
                  
                }
            });
            $("#registrationForm")[0].reset();
            return false;
        }
        
    });
    ///// ends here ///

    /// patient registration ///

    $("#btn_submit").click(function()
    {
        data =
        {
            name:$('#p_name').val(),
            age:$('#age').val()
        }
        $.ajax({
            type: "post",
            url : "",
            data:JSON.stringify(data),
            contentType: 'application/json; charset=utf-8',
            //dataType: 'json', #####it specifies the result format which return from view
            success: function(data)
            {
                //alert('SUccess')
                console.log(data)
                swal({
                    title: "Success!",
                    text: "Patient Created Successfully!",
                    icon: "success",
                    button: "OK",
                    });
                
            },
            error: function(data) 
            {
                //alert('Error..')
                console.log(data)
                swal({
                    title: "Sorry!",
                    text: "Error Creating Patient!",
                    icon: "error",
                    button: "OK",
                    });
                
            }
        });
            $("#patientForm").print({
                title: "Print Patient's Details..!!!",
                noPrintSelector: "#btn_submit,#rest_btn",
            });
            $("#patientForm")[0].reset();
        return false;
        
    });
    
    /// ends here ///

    //// Update (patient's data) by admin
    
    $("#update_btn").click(function()
    {  
        data = 
        {
           id : $('#patientid').val(),
           name: $('#name').val(),
           age : $('#age').val(),
           created_date : $('#created_date').val()
            }
            $.ajax({
                type: "PUT",
                url : "",
                data:JSON.stringify(data),
                contentType: 'application/json; charset=utf-8',
                //dataType: 'json',
                success: function(data)
                {
                    //console.log(data);
                    swal({
                    title: "Success!",
                    text: "Patient Details Updated!",
                    icon: "success",
                    button: "OK",
                    });
                    location.reload(true);
                },
                error: function(data) 
                {
                    //console.log(data);
                    swal({
                    title: "Sorry!",
                    text: "Error Updating Details!",
                    icon: "error",
                    button: "OK",
                    });
                }
            });
        return false;
    });
    // Ends Here ////////

    $("#delete_btn").click(function()
    {  
        //alert('delet value'+$('#delid').val());
        data = 
        {
           id : $('#delid').val(),
            }
            $.ajax({
                type: "DELETE",
                url : "",
                data:JSON.stringify(data),
                contentType: 'application/json; charset=utf-8',
                //dataType: 'json',
                success: function(data)
                {
                    //console.log(data);
                    swal({
                        title: "Success!",
                        text: "Patient Deleted Successfully!",
                        icon: "success",
                        button: "OK",
                        });
                    location.reload(true);
                },
                error: function(data) 
                {
                    //console.log(data);
                    swal({
                    title: "Sorry!",
                    text: "Error Deleting Patient!",
                    icon: "error",
                    button: "OK",
                    });
                }
            });
        return false;  
    });

    /// Ends///////

    /// Data Table Initialization

    $('#patients_table, #patients_table_user').DataTable({
        responsive: true
    });

    //// Ends Here ///////

});