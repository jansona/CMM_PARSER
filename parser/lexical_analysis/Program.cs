using System;
using System.Collections.Generic;
/*

按照文档中保留字和特殊符号的顺序来进行编码  基础部分共25个  编码范围为0--24
常数种别码为25
变量种别码为26
*/
namespace lexical_analysis
{
    class Program
    {
        static void Main(string[] args)
        {
            string str = "int main(){ int a = 1.123;if(a > 1)write(a+1);}";
            //string str = "main()";

            LexParser parser = new LexParser();

            List<Token> tokens = parser.ParseSentence(str);
            Console.Write(str+"\n");
            LexParser.CheckTokens(tokens);
        }
    }
}
