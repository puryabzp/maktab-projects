function replace_func(arr,old_elm,new_elm){
            for(i=0;i<arr.length;i++){
                if(arr[i]==old_elm){
                    arr[i]=new_elm
                }
            }
            return arr

     }
     var arr=["a", "b", "c", "d", "e", "f"]
     console.log(replace_func(arr,"e","t"))
