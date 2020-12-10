$(document).ready(function () {
    $('#subbtn').click(function (e) { 

        e.preventDefault();
        var value1=$("#urlinput").val();
        console.log(value1)
        myfunc(value1).then((data)=>{
            $('#output').text(data["result_url"]);

        }).catch((err) => {
            alert(err)
        })

    })
});

function myfunc(arg){
    let promise = new Promise((resolve, reject)=> {
        $('#loader').show()
        $.ajax({
                        type: "post",
                        url: "https://cleanuri.com/api/v1/shorten",
                        data: {'url':arg},
                        success: function (response) {
                            // $('#output').text(response.result_url);
                            // var valforcopy = response.result_url
                            resolve(response);
                        },
                        error: function (error) {
                            reject('has error');
                        },
                        
                    });
        });
        return promise;  
        }













// $(document).ready(function () {
//     $('#subbtn').click(function (e) { 

//         e.preventDefault();
//         var value1=$("#urlinput").val();
//         $.ajax({
//             type: "post",
//             url: "https://cleanuri.com/api/v1/shorten",
//             data: {'url':value1},
//             success: function (response) {
//                 $('#output').text(response.result_url);
//                 var valforcopy = response.result_url
//             }
//         });
        
//     });
// });
