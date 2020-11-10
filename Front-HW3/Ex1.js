function delete_byindex(arr,ind){
        arr.splice(ind,1)
        return arr
     }
     arr = [1,2,3,4,5,6]
     console.log(delete_byindex(arr,2))
