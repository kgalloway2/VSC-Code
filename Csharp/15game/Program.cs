using System;
using System.Collections.Generic;

namespace _15game
{
    class Program
    {
        static void Main(string[] args)
        {
            // GameBoard newGame = new GameBoard();
            // Console.WriteLine("Welcome to the 15-puzzle game! Here is your board: ");
            // int moves = 0;

            // while (true) {
            //     Console.WriteLine("---------------------------");
            //     newGame.viewBoard();
            //     Console.Write("Enter the number to move: ");
            //     string moveString = Console.ReadLine();
            //     int moveInt;

            //     bool isParsable = Int32.TryParse(moveString, out moveInt);

            //     if (isParsable) {
            //         if (newGame.moveAllowed(moveInt)) {
            //             newGame.makeMove(moveInt);
            //             moves++;
            //             if (newGame.isWin()) {
            //                 break;
            //             }
            //         }
            //         else {
            //             Console.WriteLine("You cannot make that move.");
            //         }
            //     }
            //     else {
            //         Console.WriteLine("Invalid input! Please try again.");
            //     }
            // }

            // newGame.viewBoard();
            // Console.WriteLine($"Congratulations! You won in {moves} moves!");
        
            // GameBoard tempGame = new GameBoard();
            int[,] newBoard = new int[,] {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}, {13, 14, 0, 15}};
            int[,] solution = new int[,] {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}, {13, 14, 15, 0}};
            solver unsolvedBoard = new solver(newBoard, solution);
            List<int[,]> solutionPath = unsolvedBoard.AStar(newBoard, solution);

            foreach (var t in solutionPath) {
                Console.WriteLine(t);
            }
        }
    }
}
