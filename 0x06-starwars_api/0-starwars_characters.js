#!/usr/bin/node
const argv = require('process').argv;
const request = require('request');

const endPointFilms = 'films';
const id = argv[2];
const endPointPeople = 'people';
const url = `https://swapi-api.alx-tools.com/api/${endPointFilms}/${id}/`;
const regex = /\/(\d+)\/$/;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error with GET request:', error);
    return;
  }

  const characters = JSON.parse(body).characters;
  const numbers = characters.map(c => c.match(regex)[1]);
  numbers.sort((a, b) => a - b);

  let completedRequests = 0;
  const names = new Array(numbers.length);

  numbers.forEach((number, index) => {
    const urlPeople = `https://swapi-api.alx-tools.com/api/${endPointPeople}/${number}/`;

    request(urlPeople, (error, response, body) => {
      if (error) {
        console.error('Error with GET request:', error);
        return;
      }
      names[index] = JSON.parse(body).name;
      completedRequests++;

      if (completedRequests === numbers.length) {
        names.forEach(name => console.log(name));
      }
    });
  });
});
