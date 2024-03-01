# **Ultimate Hangman**

## **Overview**

This hangman game is based on the original hangman game but with extra features: leaderboards, difficulty modes and word definition tokens. This game is based inside a mock terminal deployed via Heroku.

The game's challenging nature alongside the leaderboard system creates a competitive environment with players, each trying to get a higher score and represent their Country/City.

[Click here to go to the deployed project](https://ultimate-hangman-063344ed324f.herokuapp.com/)

![Screenshot of the game welcome screen](screenshots/ultimate-hangman-welcome-screen.png)

## **Table of Contents**

- [**Ultimate Hangman**](#ultimate-hangman)
  - [**Overview**](#overview)
  - [**Table of Contents**](#table-of-contents)
  - [**How to Play**](#how-to-play)
    - [**Game Rules**](#game-rules)
    - [**Points System**](#points-system)
    - [**Selection of Game Modes**](#selection-of-game-modes)
    - [**How Players Win**](#how-players-win)
  - [**Planning Stage**](#planning-stage)
    - [**User Stories**](#user-stories)
    - [**Site Aims**](#site-aims)
    - [**How This Will Be Achieved**](#how-will-this-be-achieved)
    - [**Game Flow Chart**](#game-flow-chart)

## **How to Play:**

### **_Game Rules_**

1. You will have 7 attempts to guess the right word by guessing the word outright or guessing with letters.
2. If you guess wrong, hangman will start to build and if you have more than 15 points, they will be deducted by 10 each time.
3. If the attempts reach 0, the hangman will be killed and you will lose the game.
4. Each time you play and your attempts reach 3 you will get a hint token, if you use it you will get the definition of the word but also 25 points will be deducted if you have more than 25 already.

### **_Points System_**

- (+ 25 points) each time you guess a letter right.
- (+ 100 points) if you guess the word right with half of the word exposed.
- (+ 750 points) if you guess the word right without revealing the first half of the word already
- (- 10 points) if you guess a letter wrong, only applies if your points are more than 15 already.
- (- 100% points), you will lose all your points if you guess the word wrong.

### **_Selection of Game Modes:_**

The player has 3 options for game modes: Easy mode, Intermediate mode and Hard mode. All words used for these modes are stored in the RandomWord class:

- Easy mode words are chosen by iterating through the list and using list comprehension, only words with less than 6 letters are chosen, then randomly picked to be used for the hangman word.

- Intermediate mode words are chosen by iterating through the list and using list comprehension, only words with more than 6 but less than 8 letters are chosen, then randomly picked to be used for the hangman word.

- Hard mode words are chosen by iterating through the list and using list comprehension, only words with more than 8 letters are chosen, then randomly picked to be used for the hangman word.

### **_How Players Win:_**

1. Correctly guessing all the letters in the hangman word.
2. Correctly guessing the hangman word outright.

# **Planning Stage**

## **_User Stories:_**

As a user, I want to be able to:

1. Have a clear way of seeing the game rules and points system.
2. Choose the game mode I want and also switch between them when I want to.
3. Play the game without any errors along the way.
4. Have my game data display on the leaderboard when I win.

## **_Site Aims:_**

The site aims to:

1. Display appropriate responses to any type of input from the user.
2. Keep the game going regardless of user input.
3. Make the instructions very clear, preventing the player from searching external sources for relevant information.
4. Give the user the satisfaction of displaying their score on the leaderboard, giving them a sense of accomplishment.

## **_How Will This Be Achieved:_**

To achieve the above, the site will:

1. Provide a welcome screen with the game logo in ASCII art.
2. Anytime the user inputs something that is not recognized as a valid input, handle it with a clear message on what the user did and should not do to proceed.
3. Not have any bugs that will hinder the player's experience resulting in an unfair game.
4. Successfully handle and display error messages when an API request is not successfully sent or retrieved.

## **_Game Flow Chart:_**

To understand the steps required to program the game, I created the below flowchart using [lucid charts](https://www.lucidchart.com/).

![Game Logic Flowchart](screenshots/hangman-logic-flowchart.png)

# **Features**

## **Welcome Screen:**

From the welcome screen, the user sees:

- The logo of the ultimate hangman game
- The welcome message
- The following inputs:
  - First name
  - Location (Country or City)

![Welcome screen](screenshots/ultimate-hangman-welcome-screen.png)

## **How to Play Guide**

From the how-to-play guide screen, the user sees:

- ASCII art displaying the game rules and points system
- A message suggesting the player read the how-to-play guide before playing
- The following options
  - Type A to choose the game mode
  - Type B to go back to the welcome screen to re-enter their name and location

![How to play guide screen](screenshots/ultimate-hangman-how-to-play-guide.png)
