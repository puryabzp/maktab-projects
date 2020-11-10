function flat_arrays(arr){
         var flats = arr.flat(Infinity)
         flats.sort((a,b)=>{return a-b})
         return flats
     }  
     var arr = [1, [2, 3], [[]], [4, [5]], 6]; 
     console.log(flat_arrays(arr))
