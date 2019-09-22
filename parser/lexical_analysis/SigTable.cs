using System;
using System.Collections.Generic;
using System.Text;

namespace lexical_analysis
{
    class SigTable
    {
        public static Dictionary<string, int> pairs = new Dictionary<string, int>
        {
            {"if", 0},
            {"else", 1},
            {"while", 2},
            {"read", 3},
            {"write", 4},
            {"int", 5},
            {"real", 6},
            {"+", 7},
            {"-", 8},
            {"*", 9},
            {"/", 10},
            {"=", 11},
            {"<", 12},
            {">", 13},
            {"==", 14},
            {"<>", 15},
            {"(", 16},
            {")", 17},
            {";", 18},
            {"{", 19},
            {"}", 20},
            {"/*", 21},
            {"*/", 22},
            {"[", 23},
            {"]", 24},
            {"constnum", 25},
            {"identity", 26},
        };

        public static string GetKey(int value)
        {
            foreach(KeyValuePair<string, int> keyValue in pairs)
            {
                if (keyValue.Value.Equals(value))
                {
                    return keyValue.Key;
                }
            }

            return "ERR";
        }
    }
}
