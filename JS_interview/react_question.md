## SPA
在 React 里，SPA（单页面应用）是指**只有一个 HTML 页面，依靠动态更新页面内容来响应用户操作**，能带来流畅体验，但首次加载慢、SEO 难度大，常借助 React Router 做路由管理、用状态管理库处理状态的应用模式。
## JSX
JSX 是 JavaScript 的语法扩展，允许在 JavaScript 代码里像写 HTML 一样编写 UI 结构
```jsx
const element = <h1>Hello, { 'World' }</h1>;
```
## 入口文件
index.js
```js
// 引入 React 库
import React from 'react';
// 引入 ReactDOM 库，用于将 React 组件渲染到 DOM 中
import ReactDOM from 'react-dom/client';
// 引入全局样式文件
import './index.css';
// 引入包含应用逻辑的 App 组件
import App from './App';

// 创建一个根 DOM 节点，用于挂载 React 应用
const root = ReactDOM.createRoot(document.getElementById('root'));
// 将 App 组件渲染到根节点上
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
    
```
## class vs functional component
### class
使用 this.state 来管理组件内部的状态，并且通过 this.setState 方法来更新状态，状态的更新会触发组件的重新渲染。
```jsx
import React, { Component } from 'react';

class ClassComponent extends Component {
    constructor(props) {
        super(props);
        this.state = {
            count: 0
        };
    }

    incrementCount = () => {
        this.setState({ count: this.state.count + 1 });
    };

    render() {
        return (
            <div>
                <p>Count: {this.state.count}</p>
                <button onClick={this.incrementCount}>Increment</button>
            </div>
        );
    }
}

export default ClassComponent;
```
### Functional Component
无状态（最初）：在 React Hooks 出现之前，函数组件是无状态的，只负责接收 props 并渲染 UI，没有自己的状态和生命周期方法。

React Hooks 引入后，函数组件可以使用 useState 来管理状态，使用 useEffect 来处理副作用
```jsx
import React, { useState } from 'react';

const FunctionalComponent = () => {
    const [count, setCount] = useState(0);

    const incrementCount = () => {
        setCount(count + 1);
    };

    return (
        <div>
            <p>Count: {count}</p>
            <button onClick={incrementCount}>Increment</button>
        </div>
    );
};

export default FunctionalComponent;
```
## state, props
state: mutable, private，被它所属的component控制。

props: immutable
```jsx
import React from'react';

const ChildComponent = (props) => {
    return (
        <div>
            <p>{props.message}</p>
        </div>
    );
};

export default ChildComponent;
```

```jsx
import React from'react';
import ChildComponent from './ChildComponent';

const ParentComponent = () => {
    const message = "Hello from parent";
    return (
        <div>
            <ChildComponent message={message} />
        </div>
    );
};

export default ParentComponent;
```
## stateful vs stateless
stateless 无状态组件：适用于简单的、只负责展示内容的场景，比如展示静态文本、列表项等。它的优点是代码简洁、容易理解和测试，并且因为没有状态变化和复杂的生命周期逻辑，渲染性能相对较高。

stateful 有状态组件：内部有一个 state。 适用于需要管理内部状态和响应生命周期事件的情况，比如处理用户交互（如按钮点击、输入框输入）、动态数据展示（数据从服务器获取并更新）等场景。

## Controlled Component（受控组件）
受控组件里**表单元素**的值受 React 组件的 **state 或 props** 控制，通过onChange等事件更新。可以**实时验证用户输入的内容。**

对于表单元素，比如<input'>，当用户在输入框中输入内容时，React 会将输入框的值与state中的某个变量绑定，当用户输入内容时，触发的onChange事件会将新的值通过setState方法更新到state中，然后 React 根据新的state重新渲染组件，从而保持输入框的值与state的同步。
## 非受控组件
非受控组件：表单元素的值由 DOM 自身维护，React 只是在组件挂载时获取一次初始值，用ref获取初始值或最新值。
stateless component（无状态组件）也可以受控，通过父组件的props控制。

提交表单的时候，用 ref获取输入，只有在点击提交的时候，输入内容才能得到验证。
```jsx
import React, { useRef } from'react';

const UncontrolledForm = () => {
    // 创建一个 ref 对象，用于引用 DOM 元素
    const inputRef = useRef(null);

    const handleSubmit = (e) => {
        e.preventDefault();
        // 通过 ref 获取输入框的值
        const inputValue = inputRef.current.value;
        console.log('输入的值是:', inputValue);
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                ref={inputRef}
                placeholder="请输入内容"
            />
            <button type="submit">提交</button>
        </form>
    );
};

export default UncontrolledForm;    
```


## Key Attribute
当渲染列表（如数组映射生成的多个组件）时，给每个列表项添加一个唯一的key属性
```jsx
const items = [
  { id: 1, name: 'Item 1' },
  { id: 2, name: 'Item 2' },
  { id: 3, name: 'Item 3' }
];

<li key={item.id}>{item.name}</li>
```

## Fragment
允许我们在不添加额外 DOM 节点的情况下，将多个元素组合在一起。

React Fragment is a feature in React that will help club all the elements inside one parent node.

The bonus of using React Fragment is that it does not add any extra nodes to the DOM like <div>.

```jsx
function MyComponent() {
  return (
    <>
      <h1>Hello, World!</h1>
      <p>This is a paragraph.</p>
    </>
  );
}
```

## Virtual DOM
真实的 DOM是一种树状结构的宿主对象 ，由浏览器提供，用于表示和操作 HTML 或 XML 文档

虚拟 DOM 如此轻量的原因在于它仅仅是一组节点，不像真实 DOM 那样，已经应用了样式和 JavaScript 功能 。

每当页面发生任何变化时，这些变化会首先在虚拟 DOM 上进行。之后，会在真实 DOM 上进行变化的 “打补丁” 操作，这意味着只有特定的部分会被重新渲染。这节省了大量时间

## lifecycle methods
开发者可以利用这些函数在组件生命周期的不同阶段执行特定的代码逻辑。例如，在组件挂载（mount）时执行某些初始化操作，在组件更新（update）时进行数据的重新获取或 DOM 的操作，在组件卸载（unmount）时清理资源等。

在早期的 React 中，类组件（class - based components）有一系列的生命周期方法，如componentDidMount（组件挂载后调用）、componentDidUpdate（组件更新后调用）、componentWillUnmount（组件卸载前调用）等。不过随着 React Hooks 的出现，函数式组件也可以实现类似的功能，例如useEffect Hook 可以在函数式组件中模拟生命周期方法的行为。
### 挂载（Mounting）阶段
1. constructor（构造函数）
```jsx
constructor(props) {
    super(props);
    this.state = { count: 0 };
    this.handleClick = this.handleClick.bind(this);
}
```
2. getDerivedStateFromProps
静态方法，在组件挂载和更新时都会被调用。它的作用是根据传入的 props 来更新组件的状态。它接收两个参数：props（当前传入的属性）和 state（当前组件的状态）。
```jsx
static getDerivedStateFromProps(props, state) {
    if (props.someProp!== state.someProp) {
        return { someProp: props.someProp };
    }
    return null;
}
```
如果props中的someProp值有更新，此时返回一个包含新someProp值的对象{ someProp: props.someProp }。React 会根据这个返回的对象自动更新组件的state，将state中的someProp更新为props中最新的someProp

3. render（渲染）：
这是 React 组件中必须实现的方法，它用于返回组件的 JSX 结构，也就是描述组件在页面上的呈现方式。它是一个纯函数，不应该有副作用（例如改变组件的状态或进行网络请求等）。

render方法的主要作用是生成虚拟 DOM，并将其渲染到页面上形成真实 DOM 结构。
```jsx
render() {
    return <div>{this.state.someProp}</div>;
}
```
4. componentDidMount: 在组件挂载到 DOM 后立即被调用。这个方法常用于执行一些需要在组件加载完成后进行的操作，比如发起网络请求获取数据、添加事件监听器等。之后，重新渲染部分页面内容。
```jsx
componentDidMount() {
    fetch('https://example.com/api/data')
        .then(response => response.json())
        .then(data => this.setState({ data }));
}
```
### Updating（更新）阶段
组件已经挂载到 DOM 上之后，由于 props 或 state 发生变化，导致组件重新渲染
1. getDerivedStateFromProps
2. shouldComponentUpdate: 用于判断组件是否需要进行更新。它接收两个参数，即 nextProps（即将到来的 props）和 nextState（即将到来的 state），返回一个布尔值。如果返回 true，则组件会继续进行更新流程
3. render: 生成虚拟 DOM
4. getSnapshotBeforeUpdate： 该方法在 render 方法之后、DOM 更新之前被调用。它的主要作用是获取当前 DOM 的一些信息（例如滚动位置），并返回一个值，这个值会**作为参数传递给 componentDidUpdate 方法**。
5. componentDidUpdate：**在组件更新后执行一些副作用操作。**
- 在组件更新完成（即 DOM 已经更新）后被调用。它接收三个参数，即 prevProps（之前的 props）、prevState（之前的 state）和 snapshot。
- 比如getSnapshotBeforeUpdate 方法可以获取列表的滚动位置，在 componentDidUpdate 方法中根据滚动位置的变化来决定是否需要调整列表的显示状态。

### Unmounting（卸载）阶段
组件从 DOM 中被移除的过程。

1. componentWillUnmount: 
清理资源、移除事件监听器以及取消订阅
```jsx
componentWillUnmount() {
    this.subscription.unsubscribe();
    clearInterval(this.timerId);
    document.removeEventListener('click', this.handleClick);
}
```

## useState, useEffect
```jsx
import React, { useState, useEffect } from'react';

const DataComponentWithEffect = () => {
    const [data, setData] = useState([]);
    const [isLoading, setIsLoading] = useState(true);

    useEffect(() => {
        // 模拟数据获取
        const fetchData = async () => {
            try {
                // 这里可以是实际的API请求，比如使用fetch或axios
                const response = await fetch('https://example.com/api/data');
                const fetchedData = await response.json();
                setData(fetchedData);
                setIsLoading(false);
            } catch (error) {
                console.error('Error fetching data:', error);
                setIsLoading(false);
            }
        };

        fetchData();
    }, []);
```
### useState
Used to store the fetched data and the loading state
### useEffect
用于在函数组件中执行**副作用操作**，比如数据获取、订阅、事件监听等.
```jsx
const Timer = () => {
  const [seconds, setSeconds] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      setSeconds(prev => prev + 1);
    }, 1000);

    return () => clearInterval(interval);
  });
};
```
在 useEffect 中返回的函数是一个清理函数，它会在组件卸载（unmount）时被调用。

## Context API
Context API 可以让数据在组件树中共享，而不需要逐层传递 props。通过创建一个上下文，组件可以直接从上下文中获取数据，避免了 props drilling 的问题。
1. 创建上下文对象，创建一个Provider组件
```jsx
import React, { createContext, useState } from'react';

export const UserContext = createContext();

export function UserProvider({children}){
    const [user, setUser] = useState({name: 'John', age:30});

    return (
        <UserContext.Provider value={user}>
            {children}
        </UserContext.Provider>
    )
}
```
2. 
```jsx
const App = () => {
    return (
        <div>
            <UserProvider>
                <Child />
            </UserProvider>
        </div>
    );
};

export default App;
```
```jsx
const Child = () => {
    return (
        <div>
            <h1>Child</h1>
            <Grandchild />
        </div>
    );
};

export default Child;
```


```jsx
const GrandChild = () => {

    const user = useContext(UserContext);

    return (
        <div>
            <h1>GrandChild Component</h1>
            <p>Name: {user.name}, Age: {user.age}</p>
        </div>
    );
};

export default GrandChild;
```

## Higher-order Components
It is a function that **takes a component as an input** and **returns a new component** with additional functionality or modified behavior.

在渲染之前，检查用户是否登录.
```jsx
const UserDisplay = (props) => {
    return <div>Hello, {props.userName}</div>;
};
```
```jsx
const withAuth = (WrappedComponent) => {
    return (props) => {
        const isLoggedIn = true; // 这里假设一个登录状态，实际应用中需要从状态管理或其他地方获取
        if (isLoggedIn) {
            return <WrappedComponent {...props} />;
        } else {
            return <div>Please log in first.</div>;
        }
    };
};
```
```jsx
const AuthenticatedUserDisplay = withAuth(UserDisplay);
```
## Reconciliation
1. initial render：当 React 应用首次加载时，会进行初始渲染。在这个阶段，React 会根据组件的初始状态（state）和属性（props），生成虚拟 DOM（Virtual DOM）树。
2. State or Props Change
3. 一旦有变化，React 会**创建出一个新的虚拟 DOM Tree**，且对新的虚拟 DOM 树和旧的虚拟 DOM 树进行对比。React 使用一种高效的算法来快速找出两棵树之间的差异，例如，它会首先比较顶层节点，如果节点类型相同，则继续比较子节点；如果节点类型不同，则直接替换整个子树。通过这种方式，**React 能够确定哪些部分的 DOM 需要更新**，而不是重新渲染整个页面。
4. React 会根据对比结果，计算出需要对真实 DOM 进行的最小更改集。然后，React 会将这些更改应用到真实 DOM 上，只更新那些实际发生变化的部分
5. React 会进入提交阶段，将计算出的更改真正提交到真实 DOM 中。
## React Portals
在 React 中，portal 是一种将组件的子元素渲染到父组件层级之外的 DOM 的不同部分的方式，同时还能保持 React 的组件结构。

## React Element vs React Node
1. React 元素是一个普通的 JavaScript 对象, 例如 
```jsx
const element = <h1>Hello, React!</h1>;
```
2. React 节点是 React 中可以出现在 return 语句中的各种类型的值的统称。
```jsx
文本节点： 如图中的 const textNode = 'This is a text node.';，文本字符串就是一种 React 节点。

数字节点： 例如 const numberNode = 42; ，数字也可以作为 React 节点。

元素节点： 像 const elementNode = <p>This is a React element node.</p>; 这样的 React 元素也是 React 节点。

使用场景：在 React 组件的 return 语句中，可以返回一个或多个 React 节点。例如图中的 MyComponent 函数组件，在 return 中返回了一个 <div> 元素，其中包含了文本节点、数字节点和元素节点。
```

## Router
当用户在应用程序中导航到不同的路由时，React - Router 能够在不刷新整个页面的情况下，根据当前的路由渲染相应的组件。
```js
import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import Home from './Home';
import About from './About';
import Contact from './Contact';

const App = () => {
  return (
    <div>
      <nav>
        <ul>
          <li><Link to="/">Home</Link></li>
          <li><Link to="/about">About</Link></li>
          <li><Link to="/contact">Contact</Link></li>
        </ul>
      </nav>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/contact" element={<Contact />} />
      </Routes>
    </div>
  );
};

export default App;
    
```
## Axios
```js
axios.get('https://example.com/api/data')
  .then(response => console.log(response.data))
  .catch(error => console.error(error));
```
1. 自动数据转换：它会自动将服务器响应的数据转换为 JSON 格式
2. Axios 基于 Promise 实现，这使得它在处理异步操作时非常方便。可以使用 then 方法来处理成功的响应，使用 catch 方法来捕获错误