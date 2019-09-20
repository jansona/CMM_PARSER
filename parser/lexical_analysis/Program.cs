using System;
/*

    按照文档中保留字和特殊符号的顺序来进行编码  基础部分共25个  编码范围为0--24
    常数种别码为50
    变量种别码为51  
 */
namespace lexical_analysis
{
    class Program
    {
      public  int IF = 0;
      public  int ELSE = 1;
      public  int WHILE = 2;
      public  int READ = 3;
      public  int WRITE = 4;
      public int INT = 5;
      public int REAL = 6;
      public int plus = 7;
      public int minus = 8;
      public int multyply = 9;
      public int division = 10;
      public int assign = 11;
      public int lessthan = 12;
      public int morethan = 13;
      public int equal = 14;
      public int noequal = 15;
      public int leftPar = 16;
      public int rightPar = 17;
      public int semicolon = 18;
      public int leftBrace = 19;
      public int rightBrace = 20;
      public int leftNotes = 21;
      public int rightNotes = 22;
      public int leftSqu = 23;
      public int rightSqu = 24;
      public int constNum = 50;
      public int variable = 51;



        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
        }
    }
}
