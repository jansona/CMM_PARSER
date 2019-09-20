using System;
using System.Collections.Generic;
using System.Text;

namespace lexical_analysis
{
    class Token
    {
        private int id;
        private string name;
        // 作用域
        // 数值

        public int Id
        {
            get
            {
                return id;
            }
            set
            {
                id = value;
            }
        }

        public string Name
        {
            get
            {
                return name;
            }
            set
            {
                name = value;
            }
        }
    }
}
