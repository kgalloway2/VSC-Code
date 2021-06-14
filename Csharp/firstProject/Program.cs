using System;
using System.Collections.Generic;

namespace firstProject
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Please enter your string: ");
            string input = Console.ReadLine();
            var firstLetterIndices = new List<int>();
            firstLetterIndices.Add(0);
            for (int i = 0; i < input.Length; i++) {
                if (input[i] == ' ') {
                    firstLetterIndices.Add(i + 1);
                }
            }
            string acronym = "";
            foreach (int letterIndex in firstLetterIndices) {
                acronym += input[letterIndex];
            }
            acronym = acronym.ToUpper();
            Console.WriteLine(acronym);
        }
    }
}
