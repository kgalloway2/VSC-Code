using System;

namespace example
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] doors = new int[100];
            Array.Clear(doors, 0, 100);

            int passes = 1;
            while (passes <= 100) {
                Console.WriteLine($"-------pass {passes} -------");
                for (int i = 0; i < 100; i += passes) {
                    Console.WriteLine($"visiting door {i}");
                    if (doors[i] == 0) {
                        doors[i] = 1;
                    }
                    else {
                        doors[i] = 0;
                    }
                }
                passes++;
            }

            int number = 1;
            foreach (int state in doors) {
                Console.WriteLine($"Door {number} is {state}.");
                number++;
            }
        }
    }
}
