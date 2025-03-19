function example() {
    if (true) {
        var x = 10;
    }
    console.log(x); // 输出 10
}
example();

/*function example() {
    if (true) {
        let y = 20;
        const z = 30;
    }
    console.log(y); // 报错，y 未定义
    console.log(z); // 报错，z 未定义
}
example();*/

console.log(a); // 输出 undefined
var a = 5;

console.log(isNaN('123')); 
console.log(isNaN('123abc')); 
console.log(isNaN(123)); 
console.log(isNaN(null)); 
console.log(isNaN(undefined)); 

console.log(5=="5");

const myNumbers=[1,2,3];
const myDouble=myNumbers.map(num=>num*2);
console.log(myDouble);

function outerFunction() {
    let outerVariable = '外部函数的变量';
    console.log('这里是外部函数');
    function innerFunction() {
        console.log(outerVariable);
    }
    return innerFunction;
}
outerFunction();
const closure = outerFunction();
closure(); 

setTimeout(function() {
    console.log("This is anonymous function!");
    }, 1000);

setInterval(function() {
    console.log("This is repeated function!");
    }, 1000);

