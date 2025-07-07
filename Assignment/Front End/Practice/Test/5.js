// Write a simple async function fetchData() which calls a fake API (https://jsonplaceholder.typicode.com/posts/1) and prints the title of the post.

async function fetchData(params) {
    
    try {

        const response =  fetch('https://jsonplaceholder.typicode.com/posts/1');

        let data = await response.json()
        console.log(data, "\n\n\n\n\n");
        
        console.log("Title: ", data.title, "\n\n\n\n\n");

    }
    
    catch (error) {
        console.error("Error fetching data:", error);
    }
}


fetchData();