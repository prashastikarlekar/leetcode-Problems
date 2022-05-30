// // 0. Defining variables

// // we can define variables with var as well as let
// // the scope of let is at block level i.e it defines a local variable and let is new standard for js so should be used instead of var
// // we also use const which defines a constant value and cannot be updated

// // 1.Datatypes in javascript

// console.log("JS is loaded")
// var num1 = 34;
// var num2 = 78.6;
// var str1= "This is a string";
// var dict = {
//     "Ravi":"my love"
// }
// var arr =[1,2,3,'string']
// // console.log(num1+num2)
// console.log(typeof(dict)) //object

// // 2. Functions in javascript
// function avg(a,b){
//     return (a+b)/2
// } 
// c = avg(4,6)
// console.log("value of c is "+c)

// // 3. Loops
// for(var i=0;i<arr.length;i++){
//     console.log(arr[i]);
// }
// // there also a foreach loop
// arr.forEach(function(Element){
//     console.log("This is from foreach loop "+Element)
// })


function a ()
{
    console.log("This from main function "+b);
    c();
    function c(){
        console.log("This is from the inner function"+b);
    }
}
var b =10;
a();