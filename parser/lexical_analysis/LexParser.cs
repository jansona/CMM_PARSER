using System;
using System.Collections.Generic;
using System.Text;

namespace lexical_analysis
{
    class LexParser
    {

        public List<Token> ParseSentence(string sentence)
        {
            List<Token> tokens = new List<Token>();
            Char[] chars = sentence.ToCharArray();

            for (int i = 0; i < sentence.Length; i++)
            {
                Char c = chars[i];

                if(Char.IsLetter(c) || c.Equals('_'))
                {
                    string word = "";
                    while(IsLetterUnderLineNumber(c))
                    {
                        word += c;
                        ++i;
                        if( i >= sentence.Length)
                        {
                            break;
                        }
                        c = chars[i];
                    }

                    if (SigTable.pairs.ContainsKey(word))
                    {
                        Token keywordToken = new Token();
                        keywordToken.Id = SigTable.pairs[word];

                        tokens.Add(keywordToken);
                    }
                    else
                    {
                        Token identityToken = new Token();
                        identityToken.Id = SigTable.pairs["identity"];
                        identityToken.Name = word;

                        tokens.Add(identityToken);
                    }

                    --i;
                    continue;
                }
                else if (Char.IsNumber(c))
                {
                    string numberStr = "";
                    while (IsNumberDot(c))
                    {
                        numberStr += c;             
                        
                        ++i;
                        if (i >= sentence.Length)
                        {
                            break;
                        }
                        c = chars[i];
                    }

                    Token numberToken = new Token();
                    numberToken.Id = SigTable.pairs["constnum"];
                    numberToken.Val = numberStr;
                    tokens.Add(numberToken);

                    --i;
                    continue;
                }
                else
                {
                    switch (c)
                    {
                        case ' ':
                        case '\n':
                        case '\t':
                            continue;
                        case '+':
                        case '-':
                        case '>':
                        case '(':
                        case ')':
                        case '{':
                        case '}':
                        case '[':
                        case ']':
                        case ';':
                            Token sigToken = new Token();
                            sigToken.Id = SigTable.pairs[c.ToString()];
                            tokens.Add(sigToken);
                            continue;
                        case '*':
                        case '/':
                        case '=':
                        case '<':
                            string sigStr = c.ToString() + chars[i + 1].ToString();
                            if (SigTable.pairs.ContainsKey(sigStr))
                            {
                                Token doubleCharToken = new Token();
                                doubleCharToken.Id = SigTable.pairs[sigStr];
                                tokens.Add(doubleCharToken);
                                ++i;
                            }
                            else
                            {
                                Token sigleCharToken = new Token();
                                sigleCharToken.Id = SigTable.pairs[c.ToString()];
                                tokens.Add(sigleCharToken);
                            }
                            continue;

                    }
                }

            }

            return tokens;
        }

        private bool IsLetterUnderLineNumber(Char c)
        {
            return Char.IsLetter(c) || c.Equals('_') || Char.IsNumber(c);
        }

        private bool IsNumberDot(Char c)
        {
            return Char.IsNumber(c) || c.Equals('.');
        }

        private Token ParseOneWord(string word)
        {
            Token token = new Token();



            return token;
        }

        public static void CheckTokens(List<Token> tokens)
        {
            foreach(Token token in tokens)
            {
                Console.Write("id:"+SigTable.GetKey(token.Id) + "   ");
                if(token.Name!=null) Console.Write("name:"+token.Name+"   ");
                if (SigTable.GetKey(token.Id) == "constnum") Console.Write("value:" + token.Val + "\n");
                else Console.Write("\n");
            }
        }
    }
}
