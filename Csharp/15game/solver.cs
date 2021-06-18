using System;
using System.Collections.Generic;

namespace _15game
{
    class solver
    {
      // FIELDS 
      public int[,] board;
      Dictionary<int, int[]> solvedPositions = new Dictionary<int, int[]> {
          {1, new int[2] {0,0}}, {2, new int[2] {0,1}}, {3, new int[2] {0,2}}, {4, new int[2] {0,3}}, 
          {5, new int[2] {1,0}}, {6, new int[2] {1,1}}, {7, new int[2] {1,2}}, {8, new int[2] {1,3}}, 
          {9, new int[2] {2,0}}, {10, new int[2] {2,1}}, {11, new int[2] {2,2}}, {12, new int[2] {2,3}},
          {13, new int[2] {3,0}}, {14, new int[2] {3,1}}, {15, new int[2] {3,2}}, {0, new int[2] {3,3}}
          };

      // CONSTRUCTOR

      public solver(int[,] newBoard, int[,] goal) {
          this.board = newBoard;
      }

      // METHODS
      public double manhattanDistanceMethod(int[,] currentBoard) {
          double result = 0;
          int hdist;
          int vdist;
          for (int i = 0; i < 4; i++) {
              for (int j = 0; j < 4; j++) {
                  int[] position = solvedPositions[currentBoard[i,j]];
                  hdist = Math.Abs(j - position[1]);
                  vdist = Math.Abs(i - position[0]);
                  result += (hdist + vdist);
              }
          }
          return result;
      }

      public int[] indexOfNum(int[,] currentBoard, int number) {
          for (int i = 0; i < 4; i++) {
              for (int j = 0; j < 4; j++) {
                  if (currentBoard[i,j] == number) {
                      return new int[] {i, j};
                  }
              }
          }
          return new int[] {-1,-1};
      }

      public double mDistance(int[,] currentBoard, int[,] nextBoard) {
          double result = 0;
          int hdist;
          int vdist;
          for (int n = 1; n <= 15; n++) {
              vdist = Math.Abs(indexOfNum(currentBoard, n)[0] - indexOfNum(nextBoard, n)[0]);
              hdist = Math.Abs(indexOfNum(currentBoard, n)[1] - indexOfNum(nextBoard, n)[1]);
              result += (hdist + vdist);
            }
          return result;
        }

      public List<int[,]> reconstructPath(Dictionary<int[,], int[,]> cameFrom, int[,] current) {
          List<int[,]> totalPath = new List<int[,]>();
          totalPath.Add(current);
          while (cameFrom.ContainsKey(current))
            current = cameFrom[current];
            totalPath.Insert(0, current);
        return totalPath;
      }

      public List<int[,]> AStar(int[,] start , int[,] goal) {
          List<int[,]> openSet = new List<int[,]>();
          openSet.Add(start);

          Dictionary<int[,], int[,]> cameFrom = new Dictionary<int[,], int[,]>();

          Dictionary<int[,], double> gScore = new Dictionary<int[,], double>();
          gScore.Add(start, 0);

          Dictionary<int[,], double> fScore = new Dictionary<int[,], double>();
          fScore.Add(start, manhattanDistanceMethod(start));

          while (openSet.Count > 0) {
              int[,] current = openSet[0];
              double currentMinValue = fScore[openSet[0]];
              foreach (int[,] x in openSet) {
                  if (fScore[x] < currentMinValue) {
                      current = x;
                  }
              }

              if (current == goal) {
                  return reconstructPath(cameFrom, current);
              }

              openSet.Remove(current);
              List<int[,]> neighbors = new List<int[,]>();
              foreach (int move in validMoves(current)) {
                  int[,] moveToAdd = makeMove(current, move);
                  neighbors.Add(moveToAdd);
              }
              foreach (int[,] neighbor in neighbors) {
                //   double cGScore;
                //   if (gScore.ContainsKey(current)) {
                //       cGScore = gScore[current];
                //   }
                //   else {
                //       cGScore = 0;
                //   }
                  double cGScore = gScore[current];
                  double tentativeScore = cGScore + mDistance(current, neighbor);
                  double nGScore;
                  if (gScore.ContainsKey(neighbor)) {
                      nGScore = gScore[neighbor];
                  }
                  else {
                      nGScore = double.PositiveInfinity;
                  }
                  if (tentativeScore < nGScore) {
                      cameFrom[neighbor] = current;
                      gScore[neighbor] = tentativeScore;
                      fScore[neighbor] = nGScore + manhattanDistanceMethod(neighbor);
                      if (!openSet.Contains(neighbor)) {
                        openSet.Add(neighbor);
                      }
                  }
              }
            }
            return openSet;

        }

        public List<int> validMoves(int[,] currentBoard) {
            int[] numberIndex = new int[2];
            for (int i = 0; i < 4; i++) {
                for (int j = 0; j < 4; j++) {
                    if (currentBoard[i,j] == 0) {
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

        public int[,] makeMove(int[,] currentBoard, int numberToMove) {
            int[,] newBoard = new int[4,4];
            for (int i = 0; i < 4; i++) {
                for (int j = 0; j < 4; j++) {
                    newBoard[i,j] = currentBoard[i,j];
                }
            }

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
            newBoard[emptyIndex[0],emptyIndex[1]] = numberToMove;
            newBoard[numberIndex[0],numberIndex[1]] = 0;
            return newBoard;
        }
    }
}