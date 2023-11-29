
function zuginot(){
let ar = [2, 3, 4, 5, 6, 7]
let min = 0, max = 0, avg = 0

for (let index = 0; index < ar.length; index++) {
    if (ar[index] % 2 == 0) {
        console.log(ar[index]);
        avg += ar[index]
    }
    // if ( ar[index]%2!=0) {
    //     console.log(ar[index]);
    // }
    //    אי זוגי

}
}

function sarch(arr, num) {
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] == num) {
            return true
        }
        else
            return false
    }
}
function sum(arr) {
    let sum = 0
    for (let i = 0; i < arr.length; i++) {

        sum += arr[i];
    }
    return sum
}
function back(arr) {
    for (let i = arr.length - 1; i >= 0; i--) {
        console.log(arr[i]);

    }
}


let arr = [1, 2, 3, 4]
console.log(sarch(arr, 2));
console.log(sum(arr));
back(arr)