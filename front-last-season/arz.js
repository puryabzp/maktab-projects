// $(document).ready(function () {
//     $('#subbtn').click(function (e) { 
//         e.preventDefault();
//         myfunc()

//     });
// })
setInterval(() => {
    myfunc().then((data) => {
        $('#time').text(Date());
        var out = JSON.parse(data)
        var result = out['Currency']
        console.log(data)
        for(let index = 0;index < result.length;index++){
            $("#users-table").append(`<tr><td>${result[index]['Code']}</td><td>${result[index]['Currency']}</td><td>${result[index]['Sell']}</td><td>${result[index]['Buy']}</td></tr>`);
        }
    }).catch((err) => {
        alert(err)
    })
},500);
// function myfunc(){
   
// }




// $.ajax({
//     type: "get",
//     url: "https://currency.jafari.li/json",
//     success: function (response) {
        

//     }
// });

function myfunc(){
    let promise = new Promise((resolve, reject)=> {
        $.ajax({
                            type: "get",
                            url: "https://currency.jafari.li/json",
                            success: function (response) {
                                resolve(response)
                             },
                             fail: function(error){
                                 reject('has error')
                             }
                        
                    });
        });
        return promise;  
        }
