using System;

namespace _15game
{
    class Program
    {
        static void Main(string[] args)
        {
            GameBoard newGame = new GameBoard();
            Console.WriteLine("Welcome to the 15-puzzle game! Here is your board: ");
            int moves = 0;

            while (true) {
                Console.WriteLine("---------------------------");
                newGame.viewBoard();
                Console.Write("Enter the number to move: ");
                string moveString = Console.ReadLine();
                int moveInt;

                bool isParsable = Int32.TryParse(moveString, out moveInt);

                if (isParsable) {
                    if (newGame.moveAllowed(moveInt)) {
                        newGame.makeMove(moveInt);
                        moves++;
                        if (newGame.isWin()) {
                            break;
                        }
                    }
                    else {
                        Console.WriteLine("You cannot make that move.");
                    }
                }
                else {
                    Console.WriteLine("Invalid input! Please try again.");
                }
            }

            newGame.viewBoard();
            Console.WriteLine($"Congratulaions! You won in {moves} moves!");
        }
    }
}
