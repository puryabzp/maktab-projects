function find_by_element(arr,indx){
        for(i = 0; i <= arr.length; i++){
            if(i == indx){
                return arr[i]
            }
        }
     }
     arr = [[1,2,3,4],3]
     indx = 1
     var output = new Object();
     output.indx = indx;
     output.element = find_by_element(arr,indx)
     console.log(output)
     
   -----------------------  
     
     
     
     
   function find_by_element(arr,elm){
        for(i = 0; i <= arr.length; i++){
            var output = new Object();
            output.elemen = elm
            if(arr[i] == elm){
                output.indx = i
                return output
            }
        }
     }
    arr = ["a","b","c","d","e",6]
    elm = 6
    console.log(find_by_element(arr,elm))
    
