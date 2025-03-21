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

## arrow function
普通函数：需要使用function关键字定义，即使是简单函数，也需要完整的函数声明结构，如function add(a, b) { return a + b; } 。
1. 当只有一个参数时参数括号可以省略
```jsx
const square = x => x * x; 
```
2. 当函数体只有一条语句时，花括号和return关键字可以省略。例如，const add = (a, b) => a + b; 。

## this
全局作用域：在全局作用域中，this 指向全局对象。在浏览器环境下，全局对象是 window。

函数调用：当函数作为普通函数调用时，this 在非严格模式下指向全局对象，严格模式下是 undefined。

方法调用：若函数作为对象的方法调用，this 指向调用该方法的对象。
```js
const person = {
    name: 'John',
    sayHello: function() {
        console.log(`Hello, my name is ${this.name}`);
    }
};

person.sayHello();
```
构造函数调用：使用 new 调用函数时，this 指向新创建的对象。

箭头函数：箭头函数没有自己的 this，它继承自外层作用域的 this 值。

call、apply、bind：使用这三个方法可以显式地指定 this 的指向。

## 导出表单数据到Excel
具体而言，在实现将用户联系数据自动填充到 Google Sheets 表格的过程中，当用户在网站填写联系方式表单时，我编写的 JavaScript 代码会通过 DOM 操作，精准定位到表单中的各个输入字段。代码会实时监听表单的提交事件，一旦用户点击提交按钮，便立即触发数据收集流程。
收集到的数据会被整理成一个 JavaScript 对象，方便后续处理。接着，为了能在 HTTP 请求中正确传输这些数据，我采用了application/x-www-form-urlencoded编码格式。这种格式会将数据对象中的每个键值对，通过encodeURIComponent函数对键和值分别进行编码，以确保特殊字符能被正确识别，之后将编码后的键值对用&符号连接成字符串。
完成编码后，通过XMLHttpRequest对象发起 POST 请求，请求的目标地址就是部署在 Google Apps Script 上的 API 端点。在请求头中，我明确设置了Content-Type为application/x-www-form-urlencoded，以此告知服务器数据的格式。Google Apps Script 端接收到请求后，我编写的doPost函数会解析请求中的数据，并将其追加到预先创建好的 Google Sheets 表格的新行中。
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>客户联系方式表单</title>
</head>

<body>
    <form id="contactForm">
        <label for="name">姓名:</label>
        <input type="text" id="name" name="name" required><br>
        <label for="email">邮箱:</label>
        <input type="email" id="email" name="email" required><br>
        <label for="phone">电话:</label>
        <input type="tel" id="phone" name="phone" required><br>
        <input type="submit" value="提交">
    </form>
    <script src="script.js"></script>
</body>

</html>    
```
```js
document.getElementById('contactForm').addEventListener('submit', function (e) {
    e.preventDefault();
    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    var phone = document.getElementById('phone').value;

    var apiUrl = 'YOUR_API_URL'; // 替换为你部署的 Apps Script URL

    var formData = {
        name: name,
        email: email,
        phone: phone
    };

    var xhr = new XMLHttpRequest();
    xhr.open('POST', apiUrl, true);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            alert('数据提交成功');
            document.getElementById('contactForm').reset();
        }
    };
    var params = Object.keys(formData).map(function (key) {
        return encodeURIComponent(key) + '=' + encodeURIComponent(formData[key]);
    }).join('&');
    xhr.send(params);
});    
```
## 提高网页响应速度
1. 压缩图片/懒加载
```html
<img src="image.jpg" alt="example" loading="lazy">
```
2. 事件委托：将事件监听器绑定到父元素上，利用事件冒泡的原理，处理子元素的事件。这样可以减少事件监听器的数量，提高性能。
```js
<ul id="list">
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
</ul>
<script>
    const list = document.getElementById('list');
    list.addEventListener('click', function (event) {
        if (event.target.tagName === 'LI') {
            console.log('Clicked on item:', event.target.textContent);
        }
    });
</script>
```
3. 避免使用复杂CSS选择器：如后代选择器嵌套过深，会增加浏览器解析选择器的时间。尽量使用 ID、类名等简单选择器。
4. 合并文件：将多个 CSS 或 JavaScript 文件合并成一个，减少 HTTP 请求数量。

## GraphQL
GraphQL 是一种用于 API 的查询语言，客户端可以通过发送包含所需数据结构的查询到单一端点，精确获取所需数据，避免了过度获取或获取不足的问题，提高了数据传输效率。

例如客户端可一次性请求获取用户及其相关文章等关联数据。与 RESTful 相比，GraphQL 在数据获取的灵活性上更具优势，RESTful 通常通过不同的端点来获取不同资源，可能导致多次请求和数据冗余或不足；GraphQL 的单一端点设计使得请求更加简洁高效，且客户端能完全控制返回的数据结构；而 RESTful 则在缓存机制等方面较为成熟，且更易于理解和实现，在一些简单场景中使用广泛。

```graphql
query {
    user(id: "1") {
        name
        email
        articles {
            title
            content
        }
    }
}
```
这是服务器定义的 schema
```graphql
type Article {
    id: ID
    title: String
    content: String
}

type User {
    id: ID
    name: String
    email: String
    articles: [Article]
}

type Query {
    user(id: ID!): User
}
```