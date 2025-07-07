// Function to fetch posts from the API using .then() and .catch()
function fetchPosts() {
    // Fetch data from the demo API
    fetch('https://jsonplaceholder.typicode.com/posts')
        .then(function(response) {
            // Check if the response is OK (status code 200)
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            // Parse the response as JSON
            console.log(response, "\n\n\n\n\n\n\n\n");
            return response.json();
        })
        .then(function(posts) {
            // Log the posts to the console (or display them)
            // console.log(posts);
            console.log(posts[0]);
        })
        .catch(function(error) {
            // If there is any error, log it
            console.error('There was an error fetching the posts:', error);
        });
}

// Call the function to fetch the posts
fetchPosts();
