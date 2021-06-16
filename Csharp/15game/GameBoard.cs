// fix formatting of gameboard and make it so someone can actually play the game

using System;
using System.Collections.Generic;

namespace _15game
{
    class GameBoard
    {
        // FIELDS
        int[,] board = new int[,] {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}, {13, 14, 15, 0}};

        // PROPERTIES

        // CONSTRUCTORS
        public GameBoard() {
            List<int> currentValidMoves;
            Random choice = new Random();
            int currentMove;
            int randMax;
            int randChoice;
            for (int i = 0; i < 150; i++) {
                currentValidMoves = validMoves();
                // foreach (int move in currentValidMoves) {
                //     Console.WriteLine(move);
                // }
                randMax = currentValidMoves.Count;
                // Console.WriteLine(randMax);
                randChoice = choice.Next(0, randMax);
                // Console.WriteLine(randChoice);
                currentMove = currentValidMoves[randChoice];
                // Console.WriteLine(currentMove);
                makeMove(currentMove);
                // this.viewBoard();
                // Console.WriteLine("------------------");
            }
        }

        // METHODS
        public void viewBoard() {
            Console.WriteLine($"| {board[0,0]} | {board[0,1]} | {board[0,2]} | {board[0,3]} |");
            Console.WriteLine($"| {board[1,0]} | {board[1,1]} | {board[1,2]} | {board[1,3]} |");
            Console.WriteLine($"| {board[2,0]} | {board[2,1]} | {board[2,2]} | {board[2,3]} |");
            Console.WriteLine($"| {board[3,0]} | {board[3,1]} | {board[3,2]} | {board[3,3]} |");
            
        }

        public void makeMove(int numberToMove) {
            int[] emptyIndex = new int[2];
            for (int i = 0; i < 4; i++) {
                for (int j = 0; j < 4; j++) {
                    if (board[i,j] == 0) {
                        emptyIndex[0] = i;
                        emptyIndex[1] = j;
                    }
                }
            }
            int[] numberIndex = new int[2];
            for (int i = 0; i < 4; i++) {
                for (int j = 0; j < 4; j++) {
                    if (board[i,j] == numberToMove) {
                        numberIndex[0] = i;
                        numberIndex[1] = j;
                    }
                }
            }
            board[emptyIndex[0],emptyIndex[1]] = numberToMove;
         board[numberIndex[0],numberIndex[1]] = 0;
        }

        public bool moveAllowed(int numberToMove) {
            int[] numberIndex = new int[2];
            for (int i = 0; i < 4; i++) {
                for (int j = 0; j < 4; j++) {
                    if (board[i,j] == numberToMove) {
                        numberIndex[0] = i;
                        numberIndex[1] = j;
                    }
                }
            }
            var adjacentCells = new List<int[]>();
            int[] move1 = new int[2] {numberIndex[0] + 1,numberIndex[1]};
            adjacentCells.Add(move1);
            int[] move2 = new int[2] {numberIndex[0] - 1,numberIndex[1]};
            adjacentCells.Add(move2);
            int[] move3 = new int[2] {numberIndex[0],numberIndex[1] + 1};
            adjacentCells.Add(move3);
            int[] move4 = new int[2] {numberIndex[0],numberIndex[1] - 1};
            adjacentCells.Add(move4);
            
            foreach (int[] cell in adjacentCells) {
                if (cell[0] <= 3 && cell[1] <= 3 && cell[0] >= 0 && cell[1] >= 0) {
                    if (board[cell[0],cell[1]] == 0) {
                        return true;
                    }
                }
            }

            return false;

        }

        public List<int> validMoves() {
            int[] numberIndex = new int[2];
            for (int i = 0; i < 4; i++) {
                for (int j = 0; j < 4; j++) {
                    if (board[i,j] == 0) {
                        numberIndex[0] = i;
                        numberIndex[1] = j;
                    }
                }
            }
            var adjacentCells = new List<int[]>();
            int[] move1 = new int[2] {numberIndex[0] + 1,numberIndex[1]};
            adjacentCells.Add(move1);
            int[] move2 = new int[2] {numberIndex[0] - 1,numberIndex[1]};
            adjacentCells.Add(move2);
            int[] move3 = new int[2] {numberIndex[0],numberIndex[1] + 1};
            adjacentCells.Add(move3);
            int[] move4 = new int[2] {numberIndex[0],numberIndex[1] - 1};
            adjacentCells.Add(move4);


            var validMovesList = new List<int>();
            for (int i = 0; i < 4; i++) {
                int[] cell = new int[2] {adjacentCells[i][0], adjacentCells[i][1]};
                if (cell[0] <= 3 && cell[1] <= 3 && cell[0] >= 0 && cell[1] >= 0) {
                    validMovesList.Add(board[cell[0],cell[1]]);
                }
            }

            return validMovesList;
        }
    }
}