/*
The idea of the program is to create a simple, solvable maze.

The current problem is the following: when entering a subproblem a list of available wall spots is passed in
with indices from the original problem. However, the subproblem 'resets' its indices to 0 up to the appropriate size.
So the subproblem occasionally picks a spot on the wall that is not actually in its range of wall spots.
*/

import java.util.ArrayList;

public class maze {
    int height;
    int length;
    String[][] generatedMaze; 

    public maze(int mazeHeight, int mazeLength) {
        height = mazeHeight;
        length = mazeLength;
        generatedMaze = new String[height][length];

    }
    
    public String[][] recursiveMaze(int h1, int h2, int l1, int l2, ArrayList<Integer> availableHeightWalls, ArrayList<Integer> availableLengthWalls) {
        //generate empty maze
        int recHeight = h2 - h1 + 1;
        int recLength = l2 - l1 + 1;
        String[][] tempMaze = new String[recHeight][recLength];
        ArrayList<Integer> newHeightWalls = new ArrayList<Integer>();
        for (int x:availableHeightWalls) {
            if (x < h2 && x > h1) {
                newHeightWalls.add(x);
            }
        }
        ArrayList<Integer> newLengthWalls = new ArrayList<Integer>();
        for (int x:availableLengthWalls) {
            if (x < l2 && x > l1) {
                newLengthWalls.add(x);
            }
        }
        if (recHeight > 1 && recLength > 1) {

            // Pick random points along the sides at which to draw walls.

            System.out.println(newHeightWalls);
            System.out.println(newLengthWalls);
            System.out.println("current Height " + recHeight);
            System.out.println("current Length " + recLength);
            int heightPoint = newHeightWalls.get((int)(Math.random() * newHeightWalls.size()));
            int lengthPoint = newLengthWalls.get((int)(Math.random() * newLengthWalls.size()));
            System.out.println(heightPoint);
            System.out.println(lengthPoint);

            for (int i = 0; i < recHeight; i++) {
                tempMaze[i][lengthPoint] = "\u2588";
            }
            for (int j = 0; j < recLength; j++) {
                tempMaze[heightPoint][j] = "\u2588";
            }
 
            //Recursive step - set up submazes and copy them to temp maze. there are 9 cases here
            if (heightPoint == 0) {
                if (lengthPoint == 0) {
                    System.out.println("checkpoint in case1");
                   int[] wallHoleBD = {heightPoint, (int)(Math.random() * (recLength - lengthPoint - 1)) + lengthPoint};
                   tempMaze[wallHoleBD[0]][wallHoleBD[1]] = " ";
                   int[] wallHoleCD = {(int)(Math.random() * (recHeight - heightPoint - 1)) + heightPoint, lengthPoint};
                   tempMaze[wallHoleCD[0]][wallHoleCD[1]] = " ";
                   
                   newHeightWalls.remove(Integer.valueOf(wallHoleBD[0]));
                   newHeightWalls.remove(Integer.valueOf(wallHoleCD[0]));
                   newLengthWalls.remove(Integer.valueOf(wallHoleBD[1]));
                   newLengthWalls.remove(Integer.valueOf(wallHoleCD[1]));
            
                   int[] submazeDDim = {recHeight - 1, recLength - 1};
                   String[][] submazeD = recursiveMaze(heightPoint + 1, h2 - 1, lengthPoint + 1, l2 - 1, newHeightWalls, newLengthWalls);
                   for (int di = 0; di < submazeD.length; di++) {
                       for (int dj = 0; dj < submazeD[0].length; dj++) {
                           tempMaze[di + heightPoint + 1][dj + lengthPoint + 1] = submazeD[di][dj];
                       }
                   }
                } else if (lengthPoint == recLength - 1) {
                    System.out.println("checkpoint in case2");
            
                   int[] wallHoleCD = {(int)(Math.random() * (recHeight - heightPoint - 1)) + heightPoint, lengthPoint};
                   tempMaze[wallHoleCD[0]][wallHoleCD[1]] = " ";
                   int[] wallHoleAC = {heightPoint, (int)(Math.random() * lengthPoint)};
                   tempMaze[wallHoleAC[0]][wallHoleAC[1]] = " ";
                   
                   newHeightWalls.remove(Integer.valueOf(wallHoleCD[0]));
                   newHeightWalls.remove(Integer.valueOf(wallHoleAC[0]));
                   newLengthWalls.remove(Integer.valueOf(wallHoleCD[1]));
                   newLengthWalls.remove(Integer.valueOf(wallHoleAC[1]));
            
                   int[] submazeCDim = {recHeight - 1, recLength - 1};
                   String[][] submazeC = recursiveMaze(heightPoint + 1, h2 - 1, l1 + 1, lengthPoint - 1, newHeightWalls, newLengthWalls);
                   for (int ci = 0; ci < submazeC.length; ci++) {
                       for (int cj = 0; cj < submazeC[0].length; cj++) {
                           tempMaze[ci + heightPoint + 1][cj] = submazeC[ci][cj];
                       }
                   }
                } else {
                    System.out.println("checkpoint in case3");
            
                   int[] wallHoleBD = {heightPoint, (int)(Math.random() * (recLength - lengthPoint - 1)) + lengthPoint};
                   tempMaze[wallHoleBD[0]][wallHoleBD[1]] = " ";
                   int[] wallHoleCD = {(int)(Math.random() * (recHeight - heightPoint - 1)) + heightPoint, lengthPoint};
                   tempMaze[wallHoleCD[0]][wallHoleCD[1]] = " ";
                   int[] wallHoleAC = {heightPoint, (int)(Math.random() * lengthPoint)};
                   tempMaze[wallHoleAC[0]][wallHoleAC[1]] = " ";
            
                   
                   newHeightWalls.remove(Integer.valueOf(wallHoleBD[0]));
                   newHeightWalls.remove(Integer.valueOf(wallHoleCD[0]));
                   newHeightWalls.remove(Integer.valueOf(wallHoleAC[0]));
                   newLengthWalls.remove(Integer.valueOf(wallHoleBD[1]));
                   newLengthWalls.remove(Integer.valueOf(wallHoleCD[1]));
                   newLengthWalls.remove(Integer.valueOf(wallHoleAC[1]));
            
            
                   int[] submazeCDim = {recHeight - 1, lengthPoint};
                   String[][] submazeC = recursiveMaze(heightPoint + 1, h2 - 1, l1 + 1, lengthPoint - 1, newHeightWalls, newLengthWalls);
                   for (int ci = 0; ci < submazeC.length; ci++) {
                       for (int cj = 0; cj < submazeC[0].length; cj++) {
                           tempMaze[ci + heightPoint + 1][cj] = submazeC[ci][cj];
                       }
                   }
                   int[] submazeDDim = {recHeight - 1, recLength - lengthPoint - 1};
                   String[][] submazeD = recursiveMaze(heightPoint + 1, h2 - 1, lengthPoint + 1, l2 - 1, newHeightWalls, newLengthWalls);
                   for (int di = 0; di < submazeD.length; di++) {
                       for (int dj = 0; dj < submazeD[0].length; dj++) {
                           tempMaze[di + heightPoint + 1][dj + lengthPoint + 1] = submazeD[di][dj];
                       }
                   }
                }
               
            } else if (heightPoint == recHeight - 1) {
               if (lengthPoint == 0) {
                   System.out.println("checkpoint in case4");
                   int[] wallHoleAB = {(int)(Math.random() * heightPoint), lengthPoint}; 
                   tempMaze[wallHoleAB[0]][wallHoleAB[1]] = " ";
                   int[] wallHoleBD = {heightPoint, (int)(Math.random() * (recLength - lengthPoint - 1)) + lengthPoint};
                   tempMaze[wallHoleBD[0]][wallHoleBD[1]] = " ";
                   
                   newHeightWalls.remove(Integer.valueOf(wallHoleAB[0]));
                   newHeightWalls.remove(Integer.valueOf(wallHoleBD[0]));
                   newLengthWalls.remove(Integer.valueOf(wallHoleAB[1]));
                   newLengthWalls.remove(Integer.valueOf(wallHoleBD[1]));
            
                   int[] submazeBDim = {recHeight - 1, recLength - 1};
                   String[][] submazeB = recursiveMaze(h1 + 1, heightPoint - 1, lengthPoint + 1, l2 - 1, newHeightWalls, newLengthWalls);
                   for (int bi = 0; bi < submazeB.length; bi++) {
                       for (int bj = 0; bj < submazeB[0].length; bj++) {
                           tempMaze[bi][bj + lengthPoint + 1] = submazeB[bi][bj];
                       }
                   }
               } else if (lengthPoint == recLength - 1) {
                   System.out.println("checkpoint in case5");
                   int[] wallHoleAB = {Math.max(1, (int)(Math.random() * heightPoint)), lengthPoint}; 
                   tempMaze[wallHoleAB[0]][wallHoleAB[1]] = " ";
                   int[] wallHoleAC = {heightPoint, Math.max(1, (int)(Math.random() * lengthPoint))};
                   tempMaze[wallHoleAC[0]][wallHoleAC[1]] = " ";
                   
                   newHeightWalls.remove(Integer.valueOf(wallHoleAB[0]));
                   newHeightWalls.remove(Integer.valueOf(wallHoleAC[0]));
                   newLengthWalls.remove(Integer.valueOf(wallHoleAB[1]));
                   newLengthWalls.remove(Integer.valueOf(wallHoleAC[1]));
            
                   int[] submazeADim = {recHeight - 1, recLength - 1};
                   String[][] submazeA = recursiveMaze(h1 + 1, heightPoint - 1, l1 + 1, lengthPoint - 1, newHeightWalls, newLengthWalls);
                   for (int ai = 0; ai < submazeA.length; ai++) {
                       for (int aj = 0; aj < submazeA[0].length; aj++) {
                           tempMaze[ai][aj] = submazeA[ai][aj];
                       }
                   }
               } else {
                   System.out.println("checkpoint in case6");
                   int[] wallHoleAB = {Math.max(1, (int)(Math.random() * heightPoint)), lengthPoint}; 
                   tempMaze[wallHoleAB[0]][wallHoleAB[1]] = " ";
                   int[] wallHoleBD = {heightPoint, Math.max(1, (int)(Math.random() * (recLength - lengthPoint - 1)) + lengthPoint)};
                   tempMaze[wallHoleBD[0]][wallHoleBD[1]] = " ";
                   int[] wallHoleAC = {heightPoint, Math.max(1, (int)(Math.random() * lengthPoint))};
                   tempMaze[wallHoleAC[0]][wallHoleAC[1]] = " ";
                   
                   newHeightWalls.remove(Integer.valueOf(wallHoleAB[0]));
                   newHeightWalls.remove(Integer.valueOf(wallHoleBD[0]));
                   newHeightWalls.remove(Integer.valueOf(wallHoleAC[0]));
                   newLengthWalls.remove(Integer.valueOf(wallHoleAB[1]));
                   newLengthWalls.remove(Integer.valueOf(wallHoleBD[1]));
                   newLengthWalls.remove(Integer.valueOf(wallHoleAC[1]));
            
                   int[] submazeADim = {recHeight - 1, lengthPoint};
                   String[][] submazeA = recursiveMaze(h1 + 1, heightPoint - 1, l1 + 1, lengthPoint - 1, newHeightWalls, newLengthWalls);
                   for (int ai = 0; ai < submazeA.length; ai++) {
                       for (int aj = 0; aj < submazeA[0].length; aj++) {
                           tempMaze[ai][aj] = submazeA[ai][aj];
                       }
                   }
                   int[] submazeBDim = {recHeight - 1, recLength - lengthPoint - 1};
                   String[][] submazeB = recursiveMaze(h1 + 1, heightPoint - 1, lengthPoint + 1, l2 - 1, newHeightWalls, newLengthWalls);
                   for (int bi = 0; bi < submazeB.length; bi++) {
                       for (int bj = 0; bj < submazeB[0].length; bj++) {
                           tempMaze[bi][bj + lengthPoint + 1] = submazeB[bi][bj];
                       }
                   }  
               }
            
            } else {
               if (lengthPoint == 0) {
                   System.out.println("checkpoint in case7");
                   int[] wallHoleAB = {(int)(Math.random() * heightPoint), lengthPoint}; 
                   tempMaze[wallHoleAB[0]][wallHoleAB[1]] = " ";
                   int[] wallHoleBD = {heightPoint, (int)(Math.random() * (recLength - lengthPoint - 1)) + lengthPoint};
                   tempMaze[wallHoleBD[0]][wallHoleBD[1]] = " ";
                   int[] wallHoleCD = {(int)(Math.random() * (recHeight - heightPoint - 1)) + heightPoint, lengthPoint};
                   tempMaze[wallHoleCD[0]][wallHoleCD[1]] = " ";
                   
                   newHeightWalls.remove(Integer.valueOf(wallHoleAB[0]));
                   newHeightWalls.remove(Integer.valueOf(wallHoleBD[0]));
                   newHeightWalls.remove(Integer.valueOf(wallHoleCD[0]));
                   newLengthWalls.remove(Integer.valueOf(wallHoleAB[1]));
                   newLengthWalls.remove(Integer.valueOf(wallHoleBD[1]));
                   newLengthWalls.remove(Integer.valueOf(wallHoleCD[1]));
            
                   int[] submazeBDim = {heightPoint, recLength - 1};
                   String[][] submazeB = recursiveMaze(h1 + 1, heightPoint - 1, lengthPoint + 1, l2 - 1, newHeightWalls, newLengthWalls);
                   for (int bi = 0; bi < submazeB.length; bi++) {
                       for (int bj = 0; bj < submazeB[0].length; bj++) {
                           tempMaze[bi][bj + lengthPoint + 1] = submazeB[bi][bj];
                       }
                   }
                   int[] submazeDDim = {recHeight - heightPoint - 1, recLength - 1};
                   String[][] submazeD = recursiveMaze(heightPoint + 1, h2 - 1, lengthPoint + 1, l2 - 1, newHeightWalls, newLengthWalls);
                   for (int di = 0; di < submazeD.length; di++) {
                       for (int dj = 0; dj < submazeD[0].length; dj++) {
                           tempMaze[di + heightPoint + 1][dj + lengthPoint + 1] = submazeD[di][dj];
                       }
                   }
               } else if (lengthPoint == recLength - 1) {
                   System.out.println("checkpoint in case8");
                   int[] wallHoleAB = {Math.max(1, (int)(Math.random() * heightPoint)), lengthPoint}; 
                   tempMaze[wallHoleAB[0]][wallHoleAB[1]] = " ";
                   int[] wallHoleCD = {Math.max(1, (int)(Math.random() * (recHeight - heightPoint - 1)) + heightPoint), lengthPoint};
                   tempMaze[wallHoleCD[0]][wallHoleCD[1]] = " ";
                   int[] wallHoleAC = {heightPoint, Math.max(1, (int)(Math.random() * lengthPoint))};
                   tempMaze[wallHoleAC[0]][wallHoleAC[1]] = " ";
                   
                   newHeightWalls.remove(Integer.valueOf(wallHoleAB[0]));
                   newHeightWalls.remove(Integer.valueOf(wallHoleCD[0]));
                   newHeightWalls.remove(Integer.valueOf(wallHoleAC[0]));
                   newLengthWalls.remove(Integer.valueOf(wallHoleAB[1]));
                   newLengthWalls.remove(Integer.valueOf(wallHoleCD[1]));
                   newLengthWalls.remove(Integer.valueOf(wallHoleAC[1]));
            
                   int[] submazeADim = {heightPoint, recLength - 1};
                   String[][] submazeA = recursiveMaze(h1 + 1, heightPoint - 1, l1 + 1, lengthPoint - 1, newHeightWalls, newLengthWalls);
                   for (int ai = 0; ai < submazeA.length; ai++) {
                       for (int aj = 0; aj < submazeA[0].length; aj++) {
                           tempMaze[ai][aj] = submazeA[ai][aj];
                       }
                   }
                   int[] submazeCDim = {recHeight - heightPoint - 1, recLength - 1};
                   String[][] submazeC = recursiveMaze(heightPoint + 1, h2 - 1, l1 + 1, lengthPoint - 1, newHeightWalls, newLengthWalls);
                   for (int ci = 0; ci < submazeC.length; ci++) {
                       for (int cj = 0; cj < submazeC[0].length; cj++) {
                           tempMaze[ci + heightPoint + 1][cj] = submazeC[ci][cj];
                       }
                   }
            
               } else {
                   System.out.println("checkpoint in case9");
                   int[] wallHoleAB = {Math.max(1, (int)(Math.random() * heightPoint)), lengthPoint}; 
                   tempMaze[wallHoleAB[0]][wallHoleAB[1]] = " ";
                   int[] wallHoleBD = {heightPoint, Math.max(1, (int)(Math.random() * (recLength - lengthPoint - 1)) + lengthPoint)};
                   tempMaze[wallHoleBD[0]][wallHoleBD[1]] = " ";
                   int[] wallHoleCD = {Math.max(1, (int)(Math.random() * (recHeight - heightPoint - 1)) + heightPoint), lengthPoint};
                   tempMaze[wallHoleCD[0]][wallHoleCD[1]] = " ";
                   int[] wallHoleAC = {heightPoint, Math.max(1, (int)(Math.random() * lengthPoint))};
                   tempMaze[wallHoleAC[0]][wallHoleAC[1]] = " ";
                   
                   newHeightWalls.remove(Integer.valueOf(wallHoleAB[0]));
                   newHeightWalls.remove(Integer.valueOf(wallHoleBD[0]));
                   newHeightWalls.remove(Integer.valueOf(wallHoleCD[0]));
                   newHeightWalls.remove(Integer.valueOf(wallHoleAC[0]));
                   newLengthWalls.remove(Integer.valueOf(wallHoleAB[1]));
                   newLengthWalls.remove(Integer.valueOf(wallHoleBD[1]));
                   newLengthWalls.remove(Integer.valueOf(wallHoleCD[1]));
                   newLengthWalls.remove(Integer.valueOf(wallHoleAC[1]));
            
                   int[] submazeADim = {heightPoint, lengthPoint};
                   String[][] submazeA = recursiveMaze(h1 + 1, heightPoint - 1, l1 + 1, lengthPoint - 1, newHeightWalls, newLengthWalls);
                   for (int ai = 0; ai < submazeA.length; ai++) {
                       for (int aj = 0; aj < submazeA[0].length; aj++) {
                           tempMaze[ai][aj] = submazeA[ai][aj];
                       }
                   }
                   int[] submazeBDim = {heightPoint, recLength - lengthPoint - 1};
                   String[][] submazeB = recursiveMaze(h1 + 1, heightPoint - 1, lengthPoint + 1, l2 - 1, newHeightWalls, newLengthWalls);
                   for (int bi = 0; bi < submazeB.length; bi++) {
                       for (int bj = 0; bj < submazeB[0].length; bj++) {
                           tempMaze[bi][bj + lengthPoint + 1] = submazeB[bi][bj];
                       }
                   }
                   int[] submazeCDim = {recHeight - heightPoint - 1, lengthPoint};
                   String[][] submazeC = recursiveMaze(heightPoint + 1, h2 - 1, l1 + 1, lengthPoint - 1, newHeightWalls, newLengthWalls);
                   for (int ci = 0; ci < submazeC.length; ci++) {
                       for (int cj = 0; cj < submazeC[0].length; cj++) {
                           tempMaze[ci + heightPoint + 1][cj] = submazeC[ci][cj];
                       }
                   }
                   int[] submazeDDim = {recHeight - heightPoint - 1, recLength - lengthPoint - 1};
                   String[][] submazeD = recursiveMaze(heightPoint + 1, h2 - 1, lengthPoint + 1, l2 - 1, newHeightWalls, newLengthWalls);
                   for (int di = 0; di < submazeD.length; di++) {
                       for (int dj = 0; dj < submazeD[0].length; dj++) {
                           tempMaze[di + heightPoint + 1][dj + lengthPoint + 1] = submazeD[di][dj];
                       }
                   }
               }
            }
            return tempMaze;
            } else {
            for (int i = 0; i < recHeight; i++) {
               for (int j = 0; j < recLength; j++) {
                   tempMaze[i][j] = " ";
               }
            }
            return tempMaze;
            }
            }
            
                public static void main(String[] args){
        int height = 10;
        int length = 10;
        maze myMaze = new maze(height, length);
        ArrayList<Integer> availableHeightWalls = new ArrayList<Integer>();
        ArrayList<Integer> availableLengthWalls = new ArrayList<Integer>();

        for (int i = 1; i < height; i++) {
            availableHeightWalls.add(i);
        }

        for (int i = 0; i < length - 1; i++) {
            availableLengthWalls.add(i);
        }
        
        String[][] tempMaze = myMaze.recursiveMaze(0, height - 1, 0, length - 1, availableHeightWalls, availableLengthWalls);
        for (int k = 0; k < length + 1; k++) {
            System.out.print("\u2588");
        }
        System.out.print("\u2588" + "\n");
        for (int i = 0; i < height; i++) {
            System.out.print("\u2588");
            for (int j = 0; j < length; j++) {
                System.out.print(tempMaze[i][j]);
            }
            System.out.print("\u2588" + "\n");
        }
        for (int k = 0; k < length + 2; k++) {
            System.out.print("\u2588");
        }
    }
    
}
