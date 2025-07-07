function simpleTask() {
    return new Promise(function(resolve) {
        setTimeout(function() {
            resolve("Task completed!");
        }, 2000);  // Waits for 2 seconds before resolving
    });
}

async function doTask() {
    console.log("Task started!");
    
    // Wait for simpleTask() to resolve
    let result = await simpleTask();
    
    console.log(result);  // This will print after 2 seconds: "Task completed!"
}

doTask();




// Function to fetch posts from the API
async function fetchPosts() {
    try {
        // Fetch data from the demo API
        let response = await fetch('https://jsonplaceholder.typicode.com/posts');
        
        // Check if the response is OK (status code 200)
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        // Parse the response as JSON
        let posts = await response.json();
        
        // Log the posts to the console (or display them)
        // console.log(posts);
        console.log(posts[0]);
    } catch (error) {
        // If there is any error, log it
        console.error('There was an error fetching the posts:', error);
    }
}

// Call the function to fetch the posts
fetchPosts();









// jese api fetch hone me der lgti he aur ek waiting krne wala task hai usi trh promise ko waiting task ke taur pr promise bnaya hai

function task1() {
    return new Promise(resolve => setTimeout(() => resolve("Task 1 completed"), 1000));
}

function task2() {
    return new Promise(resolve => setTimeout(() => resolve("Task 2 completed"), 2000));
}

function task3() {
    return new Promise(resolve => setTimeout(() => resolve("Task 3 completed"), 3000));
}

async function doMultipleTasks() {
    console.log("Starting tasks...");

    // Run all tasks concurrently and wait for all of them to complete
    let results = await Promise.all([task1(), task2(), task3()]);

    // Output the results after all tasks are done
    console.log(results);  // ["Task 1 completed", "Task 2 completed", "Task 3 completed"]
}

doMultipleTasks();








async function processItems(items) {
    for (let item of items) {
        // Simulating asynchronous operation (e.g., API call)
        let result = await new Promise(resolve => setTimeout(() => resolve(`Processed ${item}`), 1000));
        console.log(result);
    }
}

processItems(["Item 1", "Item 2", "Item 3"]);








function fetchData(url) {
    return fetch(url).then(response => response.json());
}

async function fetchMultipleData() {
    try {
        let data1 = fetchData('https://jsonplaceholder.typicode.com/posts');
        let data2 = fetchData('https://jsonplaceholder.typicode.com/users');
        
        // Wait for both fetches to complete
        let [posts, users] = await Promise.all([data1, data2]);

        console.log("Posts:", posts);
        console.log("Users:", users);
    } catch (error) {
        console.error("Error fetching data:", error);
    }
}

fetchMultipleData();












async function riskyOperation() {
    try {
        let result = await new Promise((resolve, reject) => {
            setTimeout(() => reject("Something went wrong!"), 1000);
        });
        console.log(result);
    } catch (error) {
        console.error("Error:", error);
    }
}

riskyOperation();
