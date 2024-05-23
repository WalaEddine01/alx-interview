#!/usr/bin/node
const axios = require('axios');

// Making a GET request
axios.get('https://jsonplaceholder.typicode.com/posts/1')
  .then(response => {
    console.log(response.data); // The response data is automatically parsed as JSON
  })
  .catch(error => {
    console.error('Error:', error.message); // Handle errors here
  });
