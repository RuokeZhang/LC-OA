[参考油管](https://www.youtube.com/watch?v=MX48mv73jf8 )
[对应的文档](https://intellipaat.com/blog/interview-question/javascript-interview-questions/)
## var, let, const的区别
### var
1. 使用 var 声明的变量具备**函数作用域**。在函数内部声明的变量，在函数外部无法访问。若在函数外部声明，它会成为全局变量。
2. var可以变量提升
```js
console.log(a); // 输出 undefined
var a = 5;
```
### let 
1. 块级作用域。块级作用域指的是由 {} 包裹的代码块，像 if 语句、for 循环等。在块级作用域内声明的变量，在块外部无法访问。
2. 用得比较多
### const
1. 不能重新赋值
2. 块级作用域。


## template literals是什么
使用反引号（`）来定义字符串
```js
const name2 = 'John';
const message2 = `Hello, ${name2}!`;
console.log(message2); 
```
## Hoisting变量提升
1. 使用 var 声明的变量会被提升到当前作用域的顶部，在声明之前访问该变量，其值为 undefined。
javascript
2. let 和 const 声明的变量同样会被提升，但存在暂时性死区（Temporal Dead Zone，TDZ）。在变量声明之前访问 let 或 const 声明的变量，会抛出 ReferenceError 错误。
3. 函数声明会被完整提升

## data types
### primitive
 1. Number: integer, float, infinity, NaN
 2. String: '', "", ``
 3. Boolean
 4. Undefined: 那些被declared 了的，但是没有被赋值的元素 
 5. null: 它是一个原始值，用于表明变量原本应该有值，但目前为空或者没有对象与之关联。在语义上，null 是开发者手动赋予变量的一个空值。
 6. Symbol
 7. BigInt
### non-primitive
1. Object: 可以存放key-value pair
2. Array
3. Function 

## ==, ===
==会先做类型转换，再判断值是否相等
```js
console.log(5=="5");//true
```
## isNaN
判断能否被转换为有效的数字
```js
console.log(isNaN('123')); //false
console.log(isNaN('123abc')); //true
console.log(isNaN(null)); //false，因为null会转换为 0
console.log(isNaN(undefined)); //true
```
## typeof
会返回一个string

## Map Method
```js
const myNumbers=[1,2,3];
const myDouble=myNumbers.map(num=>num*2);
console.log(myDouble);
```

## High-order function
高阶函数满足任意一个条件：  
能接收一个或多个函数作为参数；能够返回一个函数

## 事件冒泡/事件捕获
捕获阶段（Capturing Phase）：事件从文档根节点开始，依次向下查找目标元素，直到找到事件的目标元素。

冒泡阶段（Bubbling Phase）：事件从目标元素开始，依次向上冒泡，直到文档根节点。

## DOM树
```html
<!DOCTYPE html>
<html>

<body>
    <p id="myParagraph">原始文本</p>
    <script>
        // 获取节点
        const paragraph = document.getElementById('myParagraph');
        // 修改文本内容
        paragraph.textContent = '修改后的文本';
    </script>
</body>

</html>
```
## IIFE
IIFE 是一种在定义后立即执行的函数表达式.
```js
(function() {
    // 函数内部代码
    console.log('这是一个 IIFE');
})();
```
## Closures
形成闭包通常需要满足以下两个条件：


1. 存在嵌套函数：即一个函数内部定义了另一个函数。
2. 内部函数引用了外部函数的变量或参数：这样内部函数就可以访问和操作外部函数作用域中的变量。

```js
function outerFunction() {
    let outerVariable = '外部函数的变量';
    function innerFunction() {
        console.log(outerVariable);
    }
    return innerFunction;
}

const closure = outerFunction();
closure(); 
```
closure就是被返回的 innerFunction，然而 closure 可以访问 outerFunction 中的值。

应用场景：对于 Js 没有私有变量的弥补
```js
function createCounter() {
    let count = 0;
    return {
        increment: function() {
            count++;
            return count;
        },
        decrement: function() {
            count--;
            return count;
        },
        getCount: function() {
            return count;
        }
    };
}

const counter = createCounter();
console.log(counter.getCount()); 
console.log(counter.increment()); 
console.log(counter.decrement()); 
```
## setTimeout/setInterval
setTimeout: 定时执行某个 function

setInterval: 按照某个时间间隔，重复地执行某个 function。
```js
setTimeout(function() {
    console.log("This is anonymous function!");
    }, 1000);
```

## Promises
```js
const myPromise = new Promise((resolve, reject) => {
    // 模拟异步操作
    setTimeout(() => {
        const success = true;
        if (success) {
            resolve('操作成功');
        } else {
            reject('操作失败');
        }
    }, 1000);
});
myPromise
  .then((result) => {
        console.log(result);
    })
  .catch((error) => {
        console.error(error);
    });
```
当 success 为 true 时，调用 resolve('操作成功')，这会**把 myPromise 的状态从 pending 转变为 fulfilled**，同时**将 '操作成功' 这个字符串作为成功的结果**传递出去

## async/await
async: declaring a function async makes it return a promise。  
await: 必须在 async函数中使用。用于暂停函数执行，直到 Promise 状态变为 fulfilled 或 rejected

```js
async function fetchData() {
    try {
        const response = await fetch("https://jsonplaceholder.typicode.com");
        const data = await response.json();
        console.log("Data fetched!", data);
    } catch (err) {
        console.log("Errror: ", err);
    }
}
```
fetch 方法用于发起一个 HTTP 请求，它返回一个 Promise 对象。这里使用 await 关键字，意味着 fetchData 函数的执行会暂停，直到 fetch 操作返回的 Promise 被解决（即请求成功响应）。



## call, apply, bind
call和apply都是一调用就立即执行函数。

写法是func.call(object, arguments)

```js
function cook(ing1, ing2, ing3){
    console.log(`${this.name} is having a meal with ${ing1}, ${ing2} and ${ing3}`);
}

const adam = { name: "Adam" };

cook.call(adam, "rice", "beans", "water");
cook.apply(adam, ["rice", "beans", "water"]);

const cookForAdam = cook.bind(adam, "rice", "beans", "water");

// cookForAdam();
```
使用call调用：fn.call(obj, '值1', '值2')，会立即执行fn，this指向obj。

使用apply调用：fn.apply(obj, ['值1', '值2'])，同样立即执行fn，this指向obj 。

使用bind调用：let newFn = fn.bind(obj, '值1'); 

newFn('值2') ，先返回新函数newFn，之后调用newFn时才执行，且this始终指向obj。

## Event Delegation
事件委托就是把原本需要绑定在子元素的响应事件委托给父元素，让父元素担当事件监听的职务。

当子元素触发事件并冒泡到父元素时，父元素上的事件监听器捕获该事件，通过检查事件目标（event.target）来确定是否需要执行相应操作 。
```js
<script>
    const items = document.getEle('#itemList li');

    items.forEach(item => {
        item.addEventListener("click", function () {
            console.log("Clicked: ", this.textContent);
        })
    })

    items.addEventListener("click", function (e) {
        if (e.target.tagName === "LI") {
            console.log("Clicked: ", e.target.textContent);
        }
    })
</script>
```

## Event Loop
JavaScript 是单线程语言，意味着同一时间只能执行一个任务。在遇到大量任务或耗时任务时，会导致后续任务无法及时执行。

Event Loop 机制不断检查调用栈和任务队列，来决定下一步该执行什么。

调用栈（Call Stack）记录函数调用的顺序。  

任务队列（Task Queue）：当异步操作有了结果，其对应的**回调函数**就会被放入任务队列中等待执行。  

宏任务（Macrotask）和微任务（Microtask）：任务队列分为**宏任务队列和微任务队列**。  
宏任务包括整体代码块（script）、setTimeout、setInterval、I/O 操作、UI 渲染等；微任务有Promise的回调、Object.observe、MutationObserver 等。

1. 首先执行调用栈中的同步任务。
2. 当同步任务执行完，调用栈为空时，Event Loop 开始工作，检查微任务队列。
3. 如果微任务队列中有任务，会依次执行微任务队列中的所有任务，直到微任务队列为空。
4. 微任务队列清空后，进行 UI 渲染（如果有需要）。
5. 接着从宏任务队列中取出一个宏任务放入调用栈中执行。
6. 执行完当前宏任务后，再次检查微任务队列，重复上述过程。

```js
console.log('同步任务1');

setTimeout(() => {
    console.log('宏任务 - setTimeout');
}, 0);

Promise.resolve().then(() => {
    console.log('微任务 - Promise');
});

console.log('同步任务2');
```
顺序：“同步任务 1”、“同步任务 2”，接着执行微任务 “微任务 - Promise”；最后执行宏任务 “宏任务 - setTimeout”。

## promise和 async/await的区别
