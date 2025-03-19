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

    function cook(ing1, ing2, ing3){
        console.log(`${this.name} is having a meal with ${ing1}, ${ing2} and ${ing3}`);
    }
    
    const adam = { name: "Adam" };
    
    cook.call(adam, "rice", "beans", "water");
    cook.apply(adam, ["rice", "beans", "water"]);
    
    const cookForAdam = cook.bind(adam, "rice", "beans", "water");
    
    cookForAdam();