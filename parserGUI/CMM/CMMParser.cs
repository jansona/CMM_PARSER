using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.IO;
using System.Diagnostics;
using System.Drawing.Drawing2D;
using System.Runtime.InteropServices;

namespace CMM
{
    public partial class CMMParser : Form
    {

        string fileName = "";
        string filePath = "";

        string initialText = "\r\n/* Put your code here. */\r\n\r\n";

        public CMMParser()
        {
            InitializeComponent();
        }

        private void CMMParser_Load(object sender, EventArgs e)
        {           
            richTextBox1.Text = initialText;
            richTextBox1.Focus();
            richTextBox1.Select();
            richTextBox1.Select(richTextBox1.Text.Length, 0);
        }

        private void toolStripButtonAnalyze_Click(object sender, EventArgs e)
        {
            string path = Environment.CurrentDirectory;
            string cmdStr = $"py {path}\\cmm_parser.py -lsfg {filePath}{fileName} & exit";
            //Process parseProcess = Process.Start(filePath);
            System.Diagnostics.Process p = new System.Diagnostics.Process();
            p.StartInfo.FileName = "cmd.exe";
            p.StartInfo.RedirectStandardInput = true;
            p.StartInfo.RedirectStandardOutput = true;
            p.StartInfo.RedirectStandardError = true;
            p.StartInfo.CreateNoWindow = true;
            p.StartInfo.UseShellExecute = false;
            p.Start();
            p.StandardInput.WriteLine(cmdStr);

            string output = p.StandardOutput.ReadLine();
            p.WaitForExit();
            p.Close();
            try
            {
                if (richTextBox1.Text != "" && richTextBox1.Text != initialText)
                {
                    string part_name = fileName.Split('.')[0];
                    OutputRtx1.Text = System.IO.File.ReadAllText($"{filePath}{part_name}.lex");
                    OutputRtx2.Text = System.IO.File.ReadAllText($"{filePath}{part_name}.syn");
                    //OutputRtx3.Text = interpreter.Output(gramParser.getIntercode());
                    Pre();
                    sl_Status.Text = "Analysis done successfully";
                }
                else
                {
                    MessageBox.Show("Please input your code!", "Empty code", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                }
            }
            catch(Exception)
            {
                OutputRtx1.Text = "";
                OutputRtx2.Text = "";
                //OutputRtx3.Text = "";
                MessageBox.Show("Please check your code and correct the errors before analyzing!", "Error", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                sl_Status.Text = "Error occurred";
            }
        }
        //添加一个Panel控件显示行号
        private void richTextBox1_TextChanged(object sender, EventArgs e)
        {
            panel1.Invalidate();
        }
        private void richTextBox1_VScroll(object sender, EventArgs e)
        {
            panel1.Invalidate();
        }

        private void panel1_Paint(object sender, PaintEventArgs e)
        {
            showLineNo();
        }

        private void showLineNo()

        {
            //获得当前坐标信息
            Point p = this.richTextBox1.Location;
            int crntFirstIndex = this.richTextBox1.GetCharIndexFromPosition(p);
            int crntFirstLine = this.richTextBox1.GetLineFromCharIndex(crntFirstIndex);
            Point crntFirstPos = this.richTextBox1.GetPositionFromCharIndex(crntFirstIndex);
            //
            p.Y += this.richTextBox1.Height;
            int crntLastIndex = this.richTextBox1.GetCharIndexFromPosition(p);
            int crntLastLine = this.richTextBox1.GetLineFromCharIndex(crntLastIndex);
            Point crntLastPos = this.richTextBox1.GetPositionFromCharIndex(crntLastIndex);
            //准备画图
            Graphics g = this.panel1.CreateGraphics();
            Font font = new Font(this.richTextBox1.Font, this.richTextBox1.Font.Style);
            SolidBrush brush = new SolidBrush(Color.Green);

            //画图开始

            //刷新画布
            Rectangle rect = this.panel1.ClientRectangle;
            brush.Color = this.panel1.BackColor;
            g.FillRectangle(brush, 0, 0, this.panel1.ClientRectangle.Width, this.panel1.ClientRectangle.Height);
            brush.Color = Color.Green;//重置画笔颜色
                                      //绘制行号
            int lineSpace = 0;
            if (crntFirstLine != crntLastLine)
            {
                lineSpace = (crntLastPos.Y - crntFirstPos.Y) / (crntLastLine - crntFirstLine);
            }
            else
            {
                lineSpace =Convert.ToInt32(this.richTextBox1.Font.Size);
            }
            int brushX = this.panel1.ClientRectangle.Width - Convert.ToInt32(font.Size * 3);
            int brushY = crntLastPos.Y + Convert.ToInt32(font.Size * 0.21f);
            for (int i = crntLastLine; i >= 0; i--)
            {
                g.DrawString((i + 1).ToString(), font, brush, brushX, brushY);
                brushY -= lineSpace;
            }
            g.Dispose();
            font.Dispose();
            brush.Dispose();
        }

        //另一种方式.不过行号问题已经解决，在此留作备用
        /*private void tableLayoutPanel2_Paint(object sender, PaintEventArgs e)
        {

            //获得当前坐标信息
            Point p = this.OutputRtx1.Location;
            int crntFirstIndex = this.OutputRtx1.GetCharIndexFromPosition(p);

            int crntFirstLine = this.OutputRtx1.GetLineFromCharIndex(crntFirstIndex);

            Point crntFirstPos = this.OutputRtx1.GetPositionFromCharIndex(crntFirstIndex);

            p.Y += this.OutputRtx1.Height;

            int crntLastIndex = this.OutputRtx1.GetCharIndexFromPosition(p);

            int crntLastLine = this.OutputRtx1.GetLineFromCharIndex(crntLastIndex);
            Point crntLastPos = this.OutputRtx1.GetPositionFromCharIndex(crntLastIndex);

            //准备画图
            Graphics g = this.panel1.CreateGraphics();

            Font font = new Font(this.OutputRtx1.Font, this.OutputRtx1.Font.Style);

            SolidBrush brush = new SolidBrush(Color.Green);

            //画图开始

            //刷新画布

            Rectangle rect = this.panel1.ClientRectangle;
            brush.Color = this.panel1.BackColor;

            g.FillRectangle(brush, 0, 0, this.panel1.ClientRectangle.Width, this.panel1.ClientRectangle.Height);

            brush.Color = Color.White;//重置画笔颜色

            //绘制行号

            int lineSpace = 0;

            if (crntFirstLine != crntLastLine)
            {
                lineSpace = (crntLastPos.Y - crntFirstPos.Y) / (crntLastLine - crntFirstLine);

            }

            else
            {
                lineSpace = Convert.ToInt32(this.OutputRtx1.Font.Size);

            }
            int brushX = this.panel1.ClientRectangle.Width - Convert.ToInt32(font.Size * 3);

            int brushY = crntLastPos.Y + Convert.ToInt32(font.Size * 0.21f);
            for (int i = crntLastLine; i >= crntFirstLine; i--)
            {

                g.DrawString((i + 1).ToString(), font, brush, brushX, brushY);

                brushY -= lineSpace;
            }

            g.Dispose();

            font.Dispose();

            brush.Dispose();
        }*/

        private void toolStripButtonRun_Click(object sender, EventArgs e)
        {
            string path = Environment.CurrentDirectory;
            string cmdStr = $"py {path}\\cmm_parser.py {filePath}{fileName} & pause & exit";

            var cmd = Process.Start("cmd.exe", "/k " + cmdStr);
        }
        void OutputDataReceived(object sender, DataReceivedEventArgs e)
        {
            this.BeginInvoke(new Action(() => { textBox3.Text += "\r\n" + e.Data; }));
        }



        private void analyzeToolStripMenuItem_Click(object sender, EventArgs e)
        {
            toolStripButtonAnalyze_Click(sender, e);
        }

        private void executeToolStripMenuItem_Click(object sender, EventArgs e)
        {
            toolStripButtonRun_Click(sender, e);
        }

        private void CMMParser_ResizeEnd(object sender, EventArgs e)
        {
            tableLayoutPanel1.Width = this.Width - 20;
            tableLayoutPanel1.Height = this.Height - 35;
        }

        private void toolStripButtonCut_Click(object sender, EventArgs e)
        {
            richTextBox1.Cut();
        }

        private void toolStripButtonCopy_Click(object sender, EventArgs e)
        {
            richTextBox1.Copy();
        }

        private void toolStripButtonPaste_Click(object sender, EventArgs e)
        {
            richTextBox1.Paste();
        }

        private void toolStripButtonUndo_Click(object sender, EventArgs e)
        {
            richTextBox1.Undo();
        }

        private void exitToolStripMenuItem_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void undoToolStripMenuItem_Click(object sender, EventArgs e)
        {
            richTextBox1.Undo();
        }

        private void cutToolStripMenuItem_Click(object sender, EventArgs e)
        {
            richTextBox1.Cut();
        }

        private void copyToolStripMenuItem_Click(object sender, EventArgs e)
        {
            richTextBox1.Copy();
        }

        private void pasteToolStripMenuItem_Click(object sender, EventArgs e)
        {
            richTextBox1.Paste();
        }

        private void selectAllToolStripMenuItem_Click(object sender, EventArgs e)
        {
            richTextBox1.Focus();
            richTextBox1.SelectAll();
        }

        private void maximizeToolStripMenuItem_Click(object sender, EventArgs e)
        {
            if (this.WindowState == FormWindowState.Normal)
            {
                this.WindowState = FormWindowState.Maximized;
                ((ToolStripMenuItem)sender).Text = "Restore";
                return;
            }
            if (this.WindowState == FormWindowState.Maximized)
            {
                this.WindowState = FormWindowState.Normal;
                ((ToolStripMenuItem)sender).Text = "Maximize";
                return;
            }
        }

        private void minimizeToolStripMenuItem_Click(object sender, EventArgs e)
        {
            this.WindowState = FormWindowState.Minimized;
        }

        private void aboutToolStripMenuItem_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Developed by Group SE17-R01");
        }

        private void toolStripButtonOpen_Click(object sender, EventArgs e)
        {
            openFileDialog1.FileName = "";
            openFileDialog1.Filter = "CMM source files (*.cmm)|*.cmm|All files (*.*)|*.*";

            Stream myStream = null;

            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                string fullPath = openFileDialog1.FileName;
                string[] segments = fullPath.Split('\\');
                fileName = segments[segments.Length - 1];
                filePath = fullPath.Remove(fullPath.Length - fileName.Length, fileName.Length);
                //string s = "";

                try
                {
                    if ((myStream = openFileDialog1.OpenFile()) != null)
                    {
                        // 读取文件内容至代码框
                        StreamReader sr = new StreamReader(myStream, System.Text.Encoding.GetEncoding("GB2312"));
                        richTextBox1.Text = sr.ReadToEnd();
                        sr.Close();
                        myStream.Close();
                        sl_Status.Text = "File opened";
                    }
                }
                catch (Exception)
                {
                    sl_Status.Text = "File opening failed";
                }
            }

            
        }

        private void toolStripButton2_Click(object sender, EventArgs e)
        {
            saveFileDialog1.FileName = "";
            saveFileDialog1.Filter = "CMM source files (*.cmm)|*.cmm|All files (*.*)|*.*";

            Stream myStream = null;

            if (saveFileDialog1.ShowDialog() == DialogResult.OK)
            {
                try
                {
                    if ((myStream = saveFileDialog1.OpenFile()) != null)
                    {
                        // 保存代码至指定文件
                        StreamWriter sr = new StreamWriter(myStream, System.Text.Encoding.GetEncoding("GB2312"));
                        sr.Write(richTextBox1.Text);
                        sr.Close();
                        myStream.Close();
                        sl_Status.Text = "File saved";
                    }
                }
                catch (Exception)
                {
                    sl_Status.Text = "File saving failed";
                }
            }
        }

        private void openToolStripMenuItem_Click(object sender, EventArgs e)
        {
            toolStripButtonOpen_Click(sender, e);
        }

        private void saveToolStripMenuItem_Click(object sender, EventArgs e)
        {
            toolStripButton2_Click(sender, e);
        }

        private void richTextBox1_SelectionChanged(object sender, EventArgs e)
        {
            int row, col = 1;
            string text = richTextBox1.Text.Substring(0, richTextBox1.SelectionStart);
            string[] tokens = text.Split(new string[] { "\n" }, StringSplitOptions.None);
            row = tokens.Length;
            if (tokens.Length - 1 >= 0)
                col = tokens[tokens.Length - 1].Length + 1;
            sl_rowcol.Text = "Row " + row + "  Col " + col;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            TreeFrom f2 = new TreeFrom(filePath, fileName.Split('.')[0]);
            f2.Show();
        }
        //中间变量
        void Pre()
        {
            string path = Environment.CurrentDirectory;
            try
            {
                //创建一个StreamReader的实例来读取文件
                //using语句也能关闭StreamReader
                using (StreamReader sr = new StreamReader("{path}\\temp_dict"))
                {
                    string line;
                    string content = "";

                    //从文件读取并显示行，直到文件的末尾
                    while ((line = sr.ReadLine()) != null)
                    {
                        Console.WriteLine(line);
                        content += line;
                    }
                    //按钮
                    textBox3.Text = content;
                }
            }
            catch (Exception e)
            {
                //向用户显示出错消息
                Console.WriteLine("The file could not be read:");
                Console.WriteLine(e.Message);
            }

            //Console.ReadKey();
            Console.Read();
        }

        private void label1_Click(object sender, EventArgs e)
        {
            Pre();
        }
        /*private void panel2_Paint(object sender, PaintEventArgs e)
{
   GraphicsPath gp = new GraphicsPath();

   gp.AddEllipse(pictureBox1.ClientRectangle);

   Region region = new Region(gp);

   pictureBox1.Region = region;
   pictureBox2.Region = region;
   pictureBox3.Region = region;
   pictureBox4.Region = region;
   pictureBox5.Region = region;
   pictureBox6.Region = region;
   pictureBox7.Region = region;
   pictureBox8.Region = region;
   pictureBox9.Region = region;
   pictureBox10.Region = region;
   pictureBox11.Region = region;
   pictureBox12.Region = region;
   pictureBox13.Region = region;
   pictureBox14.Region = region;
   pictureBox15.Region = region;
   pictureBox16.Region = region;
   pictureBox17.Region = region;
   pictureBox18.Region = region;
   pictureBox19.Region = region;
   pictureBox20.Region = region;
   pictureBox21.Region = region;
   pictureBox22.Region = region;
   pictureBox23.Region = region;
   pictureBox24.Region = region;
   pictureBox25.Region = region;
   pictureBox26.Region = region;
   pictureBox27.Region = region;
   pictureBox28.Region = region;
   pictureBox29.Region = region;
   gp.Dispose();

   region.Dispose();
}*/

        protected override void DefWndProc(ref System.Windows.Forms.Message m)
        {
            switch (m.Msg)
            {
                case 1024:
                    Console.WriteLine(m.LParam);
                    break;
                default:
                    base.DefWndProc(ref m);
                    break;
            }
        }

    }
}