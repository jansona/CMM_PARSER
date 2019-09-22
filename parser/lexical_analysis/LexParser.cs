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
                    // TO DO assign the value
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
                            if (chars[i + 1].Equals('/'))
                            {
                                Token rightNoteToken = new Token();
                                rightNoteToken.Id = SigTable.pairs["*/"];
                                tokens.Add(rightNoteToken);
                                ++i;
                            }
                            else
                            {
                                Token mulToken = new Token();
                                mulToken.Id = SigTable.pairs["*"];
                                tokens.Add(mulToken);
                            }
                            continue;
                        case '/':
                            if (chars[i + 1].Equals('*'))
                            {
                                Token leftNoteToken = new Token();
                                leftNoteToken.Id = SigTable.pairs["/*"];
                                tokens.Add(leftNoteToken);
                                ++i;
                            }
                            else
                            {
                                Token divToken = new Token();
                                divToken.Id = SigTable.pairs["/"];
                                tokens.Add(divToken);
                            }
                            continue;
                        case '=':
                            if (chars[i + 1].Equals('='))
                            {
                                Token equalToken = new Token();
                                equalToken.Id = SigTable.pairs["=="];
                                tokens.Add(equalToken);
                                ++i;
                            }
                            else
                            {
                                Token assignToken = new Token();
                                assignToken.Id = SigTable.pairs["="];
                                tokens.Add(assignToken);
                            }
                            continue;
                        case '<':
                            if (chars[i + 1].Equals('>'))
                            {
                                Token unequalToken = new Token();
                                unequalToken.Id = SigTable.pairs["<>"];
                                tokens.Add(unequalToken);
                                ++i;
                            }
                            else
                            {
                                Token lessThanToken = new Token();
                                lessThanToken.Id = SigTable.pairs["<"];
                                tokens.Add(lessThanToken);
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
                Console.Write(SigTable.GetKey(token.Id) + " ");
            }
        }
    }
}
