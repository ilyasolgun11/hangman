# **Ultimate Hangman**

## **Overview**

This hangman game is based on the original hangman game but with extra features: leaderboards, difficulty modes and word definition tokens. This game is based inside a mock terminal deployed via Heroku.

The game's challenging nature alongside with the leaderboard system creates a competitive environment with players, each trying to get a higher score and represent their Country/City.

[Click here to go to the deployed project](https://ultimate-hangman-063344ed324f.herokuapp.com/)

![Screenshot of the games welcome screen](docs/screenshots/ultimate-hangman-deployed.png)

## **Table of Contents**

- [**Ultimate Hangman**](#ultimate-hangman)
  - [**Overview**](#overview)
  - [**Table of Contents**](#table-of-contents)

## **How to Play:**

## **_Game Rules_**

- chosen by iterating through the list and using list comprehension, only words with less than 6 letters are chosen, then randomly picked to be used for the hangman word.

### **_Selection of Game Modes:_**

The player has 3 options for game modes: Easy mode, Intermediate mode and Hard mode. All words used for these modes are stored in the RandomWord class:

Easy mode words are chosen by iterating through the list and using list comprehension, only words with less than 6 letters are chosen, then randomly picked to be used for the hangman word.

Intermediate mode words are chosen by iterating through the list and using list comprehension, only words with more than 6 but less than 8 letters are chosen, then randomly picked to be used for the hangman word.

Hard mode words are chosen by iterating through the list and using list comprehension, only words with more than 8 letters are chosen, then randomly picked to be used for the hangman word.
