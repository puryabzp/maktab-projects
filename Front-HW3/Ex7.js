function unique(arr){
        unique_arr = [...new Set(arr)]
        return unique_arr
     }
     arr = [1,2,3,4,5,6,1,3,2,7,1,9]
     console.log(unique(arr))
