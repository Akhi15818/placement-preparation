console.log('js is started')


// Syntax

// (condition) ? if block : else block

// let age = 18;

// (age > 18) ? console.log("eligible to vote") : console.log("not eligible")


// loop 

// 1. for loop

// syntax

// for(start ; end (stoping condition); increment) {
//     // code
// }


// print 1 - 10


// let a = 1

// a = a + 1

// console.log(a,'a')

// i = i + 1 ==>  i++

// post increment === > i++

// pre increment ===> ++i


let a = 5;

let b = 5


// pre ---- a = a + 1 // 6

// x = 6

let x = ++a // 6 // pre increament ---- before assigning update the a varible


// post ---- y = 5

// b = b + 1


let y = b++ // 5 // post increment ---- after assignming it will update the a variable


// console.log(x,'x')

// console.log(y,'y')

// for (let i = 1; i < 11 ; i++) {

//     console.log(i,'i')

// }


// foreach, map, filter, find,

let array = ['bmw', 'benz', 'tesla', 'tata', 'rolls', 'scorpio', 'new car'];

console.log(array[1], 'second ele');

// array.push


// for(let i = 0; i < array.length; i++) {


//     if(array[i] == 'tesla') {
//         array.splice(i,0,"car added via if ");
//         break;
//     }

//     console.log(array[i],'ele')

//     // console.log(i,'i')
// }


for (let i = 0; i < array.length; i++) {


    if (array[i] == 'tesla') {
        console.log('found the tesla')

        continue; // when u give the continue it will skip the below code of the current loop (iteration)

    }

    console.log(array[i], 'ele')

}



console.log(array, 'array')

let arr1 = ['sadhik','hemanth']

let arr2 = ['new1','new2']

// spread (three dots) --- operator ---- copying inner elements 

let arr4 = [...arr1,...arr2]

console.log(arr4,'arr4')



// 2d array, pa
// for(let i = 0;i< 5; i++) {
//     for(let j=0; j<5; j++) {

//     }
// }


// let arr3 = arr1.concat(arr2)

// for(let i = 0; i < arr2.length; i++) {
//     arr3.push(arr2[i])

// }


// console.log(arr3,'arr3')


// obj destructuring

const obj = {
    name :'sadhik',
    age : 70 ,

}


// let name = obj.name;

let { name } = obj;

const arr5  = [10,20]

let s = arr5[0] // 10
let t = arr5[1] // 20

const [e,f] = [10,20]

console.log(e,f,'e and f')


console.log(name,'obj name')



console.log('js is ended')
