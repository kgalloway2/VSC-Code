public class numberGuess {
    int max;
    int min;
    int number;
    int numOfGuesses;
    
    public numberGuess(int inputMax, int inputMin, int inputNumber) {
        max = inputMax;
        min = inputMin;
        number = inputNumber;
        numOfGuesses = 0;
    }

    public void checkGuess(int guess) {
        if (guess > max || guess < min) {
            System.out.println("Invalid guess");
        }
        else if (guess == number) {
            System.out.println("Correct! You win!");
        }
        else if (guess < number) {
            System.out.println("Too low!");
            numOfGuesses += 1;
        }
        else if (guess > number) {
            System.out.println("Too high!");
            numOfGuesses += 1;
        }
    }

    public static void main(String[] args) {

    }
}