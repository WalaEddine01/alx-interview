#!/usr/bin/node
const argv = require('process').argv;
const request = require('request');

const endPointFilms = 'films'; const id = argv[2]; const endPointPeople = 'people'; const i = 1;
const url = `https://swapi-api.alx-tools.com/api/${endPointFilms}/${id}/`;
const urlPeople = `https://swapi-api.alx-tools.com/api/${endPointPeople}/${i}/`;
const regex = /\/(\d+)\/$/;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error with GET request:', error);
    return;
  }

  const characters = JSON.parse(body).characters;
  const numbers = [];
  for (const c of characters) {
    const match = c.match(regex);
    const lastNumber = match[1];
    numbers.push(lastNumber);
  }
  numbers.sort((a, b) => a - b);
  for (const j of numbers) {
    request(urlPeople.replace(i, j), (error, response, body) => {
      if (error) {
        console.error('Error with GET request:', error);
        return;
      }
      console.log(JSON.parse(body).name);
    });
  }
});
