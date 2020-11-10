function combine_arrays(arr){
        var combArray = Array.prototype.concat.apply([], arr);
        combArray.sort((a,b)=>{return a-b})
        return combArray
     }
     var arr = [[4,11,1],[2,47,6],[7,50,9]]
     console.log(combine_arrays(arr))
