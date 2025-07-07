// Write a JavaScript Promise that resolves after 3 seconds and prints "Task Complete" to the console. Use async/await to call this promise.

let myPromise = new Promise(function (myResolve, myReject) {
    setTimeout(() => {
        myResolve("Task Completed");
    }, 3000);
})

async function executeTask() {
    try{
        const result = await myPromise;
        console.log(result);
    }
    catch (error) {
        console.log("Error: ", error);
    }
}

executeTask();