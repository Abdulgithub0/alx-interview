#!/usr/bin/node
/**
 * A script that Prints all characters of a Star Wars movie.
 * The first positional argument passed is the Movie ID.
 * Display one character name per line in the same order
 * as listed in the /films/ endpoint
 */

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const no = process.argv[2] + '/';
request(url + no, async (error, resp, data) => {
  if (error) return console.error(error);
  const character_urls = JSON.parse(data).characters;
  for (const character of character_urls) {
    await new Promise((resolve, reject) => {
      request(character, (error, resp, data) => {
        if (error) return console.error(err);
        console.log(JSON.parse(data).name);
        resolve();
      });
    });
  }
});
