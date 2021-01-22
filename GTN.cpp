#include <iostream>

int Upperlimit;
int Maxguesses;
int level_choice;
int Number;
int Tries;
int Guess;

void Levelchoice() {

  std::cout << "Input level choice: ";
  std::cin >> level_choice;
  if (level_choice > 3) {
    std::cout << "Imput to high, enter new number\n";
    Levelchoice();
  }
  else if (level_choice < 1) {
    std::cout << "Imput to low, enter new number\n";
    Levelchoice();
  }
  else {
    std::cout << "Selected level: " << level_choice << "\n\n";
  }
}

void Level() {

  if (level_choice == 1) {
    Upperlimit = 10;
    Maxguesses = 3;
    std::cout << "Number is 0 - " << Upperlimit << "\n";
    std::cout << "You have " << Maxguesses << " guesses to find the correct number\n\n";
  }
  else if (level_choice == 2) {
    Upperlimit = 20;
    Maxguesses = 6;
    std::cout << "Number is 0 - " << Upperlimit << "\n";
    std::cout << "You have " << Maxguesses << " guesses to find the correct number\n";
  }
  else if (level_choice ==3) {
    Upperlimit = 30;
    Maxguesses = 9;
    std::cout << "Number is 0 - " << Upperlimit << "\n";
    std::cout << "You have " << Maxguesses << " guesses to find the correct number\n";
  }

}

void Numbergeneration() {

  srand(time(NULL));

  Number = rand() % Upperlimit;
  //std::cout << "DEBUG - Random number is: " << Number << "\n";


}

void Guesses() {

  while (Tries < Maxguesses) {

    //std::cout << "DEBUG - Tries: " << Tries << "\n";
    //std::cout << "DEBUG - Maxguesses are: " << Maxguesses << "\n";
    std::cout << "Enter Guess: ";
    std::cin >> Guess;

    if (Guess < Number) {
      std::cout << "Guess is low\n";
      Tries = Tries + 1;
    }
    else if (Guess > Number) {
      std::cout << "Guess is high\n";
      Tries = Tries + 1;
    }
    else {
      std::cout << "Correct\n";
      Tries = 0;
      break;
    }
  }
  while (Tries == Maxguesses) {
    std::cout << "Game Over...\n";
    std::cout << "Correct number was " << Number << "\n\n";
    Tries = 0;
    break;
  }

}

int main() {

  Levelchoice();
  Level();
  Numbergeneration();
  Guesses();

  std::string answer;
  std::cout << "Would you like to play again?\nEnter: y/n\n";
  std::cin >> answer;
  if (answer == "y") {
    main();
  }
  else if (answer == "n") {
    std::cout << "Thank you for playing!\n\n";
  }
}
