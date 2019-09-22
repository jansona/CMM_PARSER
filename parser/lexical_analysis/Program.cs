using System;
using System.Collections.Generic;
/*

按照文档中保留字和特殊符号的顺序来进行编码  基础部分共25个  编码范围为0--24
常数种别码为50
变量种别码为51  
*/
namespace lexical_analysis
{
    class Program
    {
        static void Main(string[] args)
        {
            string str = "int main(){ int a = 1; write(a + 2);}";
            //string str = "main()";

            LexParser parser = new LexParser();

            List<Token> tokens = parser.ParseSentence(str);

            LexParser.CheckTokens(tokens);
        }
    }
}
