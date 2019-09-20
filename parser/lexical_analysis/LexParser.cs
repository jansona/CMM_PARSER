using System;
using System.Collections.Generic;
using System.Text;

namespace lexical_analysis
{
    class LexParser
    {

        private List<Token> ParseSentence(string sentence)
        {
            List<Token> tokens = new List<Token>();

            foreach(Char c in sentence)
            {
                switch (c)
                {
                    case ' ':
                    case '\n':
                    case '\t':
                        continue;
                }

                if(Char.IsLetter(c) || c.Equals('_'))
                {

                }
            }

            return tokens;
        }

        private Token ParseOneWord(string word)
        {
            Token token = new Token();




            return token;
        }
    }
}
