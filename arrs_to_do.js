// 1
// Given an array and an additional value, insert this value at the beginning of the array. Do this without using any built-in array methods.

function pushFront(arr, x){
    var newArr = []
    for(var i = 0; i < arr.length; i++){
        newArr[i+1] = arr[i]
    }
    newArr[0] = x
    return newArr
}
// console.log(pushFront([1,2,3,4,5,6,6,7,7,5], 60))

// 2
// Given an array, remove and return the value at the beginning of the array. Do this without using any built-in array methods except pop().

function popFront(arr){
    var newArr = []
    for(var i = 1; i < arr.length; i++){
        newArr[i-1] = arr[i]
    }
    return newArr
}

// console.log(popFront([2,3,4,5]))

// 3
// Given an array, index, and additional value, insert the value into array at given index. Do this without using built-in array methods. You can think of pushFront(arr,val) as equivalent to insertAt(arr,0,val).

function insertAt(arr,val,ind){
    for (var i = arr.length - 1; i >= ind; i--) {
        arr[i+1] = arr[i];
    }
    arr[ind] = val;
}
console.log(insertAt([1,2,3,4],3,4))