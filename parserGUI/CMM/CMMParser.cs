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
            string cmdStr = $"py {path}\\cmm_parser.py -c[1] {filePath}{fileName}";
            Process data = new Process();
            data.StartInfo.FileName = "cmd.exe";
            data.StartInfo.UseShellExecute = false;
            data.StartInfo.RedirectStandardInput = true;
            data.StartInfo.RedirectStandardOutput = true;
            data.StartInfo.RedirectStandardError = true;
            data.StartInfo.CreateNoWindow = true;
            data.OutputDataReceived += OutputDataReceived;
            data.Start();
            data.BeginOutputReadLine();
            //data.StandardInput.WriteLine("ping www.baidu.com");
            data.StandardInput.WriteLine(cmdStr);
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

        private void panel2_Paint(object sender, PaintEventArgs e)
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
        }

        private Boolean fals = true;
        private void pictureBox1_Click(object sender, EventArgs e)
        {
            if (fals == true)
            {
                this.pictureBox1.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOn.png");
                fals = false;
            }
            else
            {
                this.pictureBox1.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOff.png");
                fals = true;
            }
            //此处添加接口

        }

        private void pictureBox2_Click(object sender, EventArgs e)
        {
            if (fals == true)
            {
                this.pictureBox2.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOn.png");
                fals = false;
            }
            else
            {
                this.pictureBox2.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOff.png");
                fals = true;
            }
        }

        private void pictureBox3_Click(object sender, EventArgs e)
        {
            if (fals == true)
            {
                this.pictureBox3.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOn.png");
                fals = false;
            }
            else
            {
                this.pictureBox3.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOff.png");
                fals = true;
            }
        }

        private void pictureBox4_Click(object sender, EventArgs e)
        {
            if (fals == true)
            {
                this.pictureBox4.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOn.png");
                fals = false;
            }
            else
            {
                this.pictureBox4.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOff.png");
                fals = true;
            }
        }

        private void pictureBox5_Click(object sender, EventArgs e)
        {
            if (fals == true)
            {
                this.pictureBox5.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOn.png");
                fals = false;
            }
            else
            {
                this.pictureBox5.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOff.png");
                fals = true;
            }
        }

        private void pictureBox6_Click(object sender, EventArgs e)
        {
            if (fals == true)
            {
                this.pictureBox6.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOn.png");
                fals = false;
            }
            else
            {
                this.pictureBox6.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOff.png");
                fals = true;
            }
        }

        private void pictureBox7_Click(object sender, EventArgs e)
        {
            if (fals == true)
            {
                this.pictureBox7.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOn.png");
                fals = false;
            }
            else
            {
                this.pictureBox7.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOff.png");
                fals = true;
            }
        }

        private void pictureBox8_Click(object sender, EventArgs e)
        {
            if (fals == true)
            {
                this.pictureBox8.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOn.png");
                fals = false;
            }
            else
            {
                this.pictureBox8.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOff.png");
                fals = true;
            }
        }

        private void pictureBox9_Click(object sender, EventArgs e)
        {
            if (fals == true)
            {
                this.pictureBox9.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOn.png");
                fals = false;
            }
            else
            {
                this.pictureBox9.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOff.png");
                fals = true;
            }
        }

        private void pictureBox10_Click(object sender, EventArgs e)
        {
            if (fals == true)
            {
                this.pictureBox10.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOn.png");
                fals = false;
            }
            else
            {
                this.pictureBox10.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOff.png");
                fals = true;
            }
        }

        private void pictureBox11_Click(object sender, EventArgs e)
        {
            if (fals == true)
            {
                this.pictureBox11.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOn.png");
                fals = false;
            }
            else
            {
                this.pictureBox11.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOff.png");
                fals = true;
            }
        }

        private void pictureBox12_Click(object sender, EventArgs e)
        {
            if (fals == true)
            {
                this.pictureBox12.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOn.png");
                fals = false;
            }
            else
            {
                this.pictureBox12.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOff.png");
                fals = true;
            }
        }

        private void pictureBox13_Click(object sender, EventArgs e)
        {
            if (fals == true)
            {
                this.pictureBox13.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOn.png");
                fals = false;
            }
            else
            {
                this.pictureBox13.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOff.png");
                fals = true;
            }
        }

        private void pictureBox14_Click(object sender, EventArgs e)
        {
            if (fals == true)
            {
                this.pictureBox14.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOn.png");
                fals = false;
            }
            else
            {
                this.pictureBox14.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOff.png");
                fals = true;
            }
        }

        private void pictureBox15_Click(object sender, EventArgs e)
        {
            if (fals == true)
            {
                this.pictureBox15.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOn.png");
                fals = false;
            }
            else
            {
                this.pictureBox15.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOff.png");
                fals = true;
            }
        }

        private void pictureBox16_Click(object sender, EventArgs e)
        {
            if (fals == true)
            {
                this.pictureBox16.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOn.png");
                fals = false;
            }
            else
            {
                this.pictureBox16.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOff.png");
                fals = true;
            }
        }

        private void pictureBox17_Click(object sender, EventArgs e)
        {
            if (fals == true)
            {
                this.pictureBox17.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOn.png");
                fals = false;
            }
            else
            {
                this.pictureBox17.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOff.png");
                fals = true;
            }
        }

        private void pictureBox18_Click(object sender, EventArgs e)
        {
            if (fals == true)
            {
                this.pictureBox18.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOn.png");
                fals = false;
            }
            else
            {
                this.pictureBox18.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOff.png");
                fals = true;
            }
        }

        private void pictureBox19_Click(object sender, EventArgs e)
        {
            if (fals == true)
            {
                this.pictureBox19.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOn.png");
                fals = false;
            }
            else
            {
                this.pictureBox19.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOff.png");
                fals = true;
            }
        }

        private void pictureBox20_Click(object sender, EventArgs e)
        {
            if (fals == true)
            {
                this.pictureBox20.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOn.png");
                fals = false;
            }
            else
            {
                this.pictureBox20.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOff.png");
                fals = true;
            }
        }

        private void pictureBox21_Click(object sender, EventArgs e)
        {
            if (fals == true)
            {
                this.pictureBox21.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOn.png");
                fals = false;
            }
            else
            {
                this.pictureBox21.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOff.png");
                fals = true;
            }
        }

        private void pictureBox22_Click(object sender, EventArgs e)
        {
            if (fals == true)
            {
                this.pictureBox22.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOn.png");
                fals = false;
            }
            else
            {
                this.pictureBox22.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOff.png");
                fals = true;
            }
        }

        private void pictureBox23_Click(object sender, EventArgs e)
        {
            if (fals == true)
            {
                this.pictureBox23.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOn.png");
                fals = false;
            }
            else
            {
                this.pictureBox23.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOff.png");
                fals = true;
            }
        }

        private void pictureBox24_Click(object sender, EventArgs e)
        {
            if (fals == true)
            {
                this.pictureBox24.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOn.png");
                fals = false;
            }
            else
            {
                this.pictureBox24.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOff.png");
                fals = true;
            }
        }

        private void pictureBox25_Click(object sender, EventArgs e)
        {
            if (fals == true)
            {
                this.pictureBox25.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOn.png");
                fals = false;
            }
            else
            {
                this.pictureBox25.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOff.png");
                fals = true;
            }
        }

        private void pictureBox26_Click(object sender, EventArgs e)
        {
            if (fals == true)
            {
                this.pictureBox26.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOn.png");
                fals = false;
            }
            else
            {
                this.pictureBox26.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOff.png");
                fals = true;
            }
        }

        private void pictureBox27_Click(object sender, EventArgs e)
        {
            if (fals == true)
            {
                this.pictureBox27.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOn.png");
                fals = false;
            }
            else
            {
                this.pictureBox27.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOff.png");
                fals = true;
            }
        }

        private void pictureBox28_Click(object sender, EventArgs e)
        {
            if (fals == true)
            {
                this.pictureBox28.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOn.png");
                fals = false;
            }
            else
            {
                this.pictureBox28.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOff.png");
                fals = true;
            }
        }

        private void pictureBox29_Click(object sender, EventArgs e)
        {
            if (fals == true)
            {
                this.pictureBox29.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOn.png");
                fals = false;
            }
            else
            {
                this.pictureBox29.BackgroundImage = Image.FromFile(Application.StartupPath + "\\Resources\\" + "bitOff.png");
                fals = true;
            }
        }
    }
}