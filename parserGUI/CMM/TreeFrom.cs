using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace CMM
{
    public partial class TreeFrom : Form
    {
        string filePath;
        string partName;
        public TreeFrom(string filePath, string partName)
        {
            this.filePath = filePath;
            this.partName = partName;
            InitializeComponent();
        }
        private string pathname = string.Empty;     		//定义路径名变量       
                      
                    
        private void TreeFrom_Load(object sender, EventArgs e)
        {
            pathname = ($"{filePath}/{partName}.png");   //获得文件的绝对路径
            this.pictureBox1.Load(pathname);
        }

        private void TreeFrom_FormClosed(object sender, FormClosedEventArgs e)
        {
            this.Dispose();
            this.Close();
        }
    }
}
