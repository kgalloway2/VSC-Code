import java.util.Scanner;

public class numberGuess {
    int max;
    int min;
    int number;
    int numOfGuesses;
    
    public numberGuess(int inputMin, int inputMax, int inputNumber) {
        max = inputMax;
        min = inputMin;
        number = inputNumber;
        numOfGuesses = 0;
        System.out.println("Welcome to the number guessing game! Please guess a number between " + min + " and " + max + ".");
    }

    public boolean checkGuess(int guess) {
        boolean gameover = false;
        if (guess > max || guess < min) {
            System.out.println("Invalid guess");
        }
        else if (guess == number) {
            numOfGuesses += 1;
            System.out.println("Correct! You won in only " + numOfGuesses + " guesses!");
            gameover = true;
        }
        else if (guess < number) {
            System.out.println("Too low!");
            numOfGuesses += 1;
        }
        else if (guess > number) {
            System.out.println("Too high!");
            numOfGuesses += 1;
        }
        return gameover;
    }

    public int takeGuess() {
        System.out.println("What is your next guess?");
        Scanner myObj = new Scanner(System.in);
        int guess = Integer.parseInt(myObj.next());
        return guess;
    }

    public static void main(String[] args) {
        numberGuess newGame = new numberGuess(1, 100, 38);
        while (true) {
            int currentGuess = newGame.takeGuess();
            boolean gameover = newGame.checkGuess(currentGuess);
            if (gameover){
                break;
            }
        }
    }
}