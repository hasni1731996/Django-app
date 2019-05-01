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

    $("#patientForm").submit(function()
    {
        $p_name = $('#p_name').val();
        $age = $('#age').val();

        if($('#p_name').val() == "" || $('#age').val() == "")
        {
            alert("Please fill up the required field");
        }else
        {
            $.ajax({
                type: "POST",
                url : "",
                data: {
                    name:$p_name,
                    age:$age,
                    csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                },
                success: function(data)
                {
                    swal({
                        title: "Success!",
                        text: "Patient Created Successfully!",
                        icon: "success",
                        button: "OK",
                      });
                    
                },
                error: function(data) 
                {
                    swal({
                        title: "Sorry!",
                        text: "Error Creating Patient!",
                        icon: "error",
                        button: "OK",
                      });
                  
                }
            });
            console.log($p_name)
            $("#patientForm").print({
                title: "Print Patient's Details..!!!",
                noPrintSelector: "#btn_submit,#rest_btn",
            });
            $("#patientForm")[0].reset();
            return false;
        }
        
    });
    
    /// ends here ///

    /// Data Table Initialization

    $('#patients_table, #patients_table_user').DataTable({
        responsive: true
});

});