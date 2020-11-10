function extract_func(str){
                var numbers = str.match(/(\d+)/g)
                return numbers
        }
        var str = "1 I have 2 apples and 3 pineapples 9 "
        console.log(extract_func(str)) 
