using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.IO;

namespace CMM
{
    public partial class CMMParser : Form
    {
        
        string initialText = "\r\n/* Put your code here. */\r\n\r\n";

        public CMMParser()
        {
            InitializeComponent();
        }

        private void CMMParser_Load(object sender, EventArgs e)
        {            
            InputTbx.Separators.Add(' ');
            InputTbx.Separators.Add('\t');
            InputTbx.Separators.Add('\n');
            InputTbx.Separators.Add('\r');
            InputTbx.Separators.Add('+');
            InputTbx.Separators.Add('-');
            InputTbx.Separators.Add('*');
            InputTbx.Separators.Add('/');
            InputTbx.Separators.Add('=');
            InputTbx.Separators.Add('<');
            InputTbx.Separators.Add('>');
            InputTbx.Separators.Add('(');
            InputTbx.Separators.Add(')');
            InputTbx.Separators.Add(';');
            InputTbx.Separators.Add('{');
            InputTbx.Separators.Add('}');
            InputTbx.Separators.Add('[');
            InputTbx.Separators.Add(']');

            
            InputTbx.Text = initialText;
            InputTbx.Focus();
            InputTbx.Select();
            InputTbx.Select(InputTbx.Text.Length, 0);
        }

        private void toolStripButtonAnalyze_Click(object sender, EventArgs e)
        {
            if (InputTbx.Text != "" && InputTbx.Text != initialText)
            {
                OutputRtx1.Text = System.IO.File.ReadAllText(@"D:\Coding\GitStore\CMM1\parser_py\test_code.lex");
                OutputRtx2.Text = System.IO.File.ReadAllText(@"D:\Coding\GitStore\CMM1\parser_py\test_code.syn");
                //OutputRtx3.Text = interpreter.Output(gramParser.getIntercode());
                sl_Status.Text = "Analysis done successfully";
            }
            else
            {
                MessageBox.Show("Please input your code!", "Empty code", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
        }

        private void toolStripButtonRun_Click(object sender, EventArgs e)
        {
            
        }

        private void InputTbx_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.Modifiers == Keys.Control && e.KeyCode == Keys.A)
            {
                InputTbx.SelectAll();
            }
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
            InputTbx.Cut();
        }

        private void toolStripButtonCopy_Click(object sender, EventArgs e)
        {
            InputTbx.Copy();
        }

        private void toolStripButtonPaste_Click(object sender, EventArgs e)
        {
            InputTbx.Paste();
        }

        private void toolStripButtonUndo_Click(object sender, EventArgs e)
        {
            InputTbx.Undo();
        }

        private void exitToolStripMenuItem_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void undoToolStripMenuItem_Click(object sender, EventArgs e)
        {
            InputTbx.Undo();
        }

        private void cutToolStripMenuItem_Click(object sender, EventArgs e)
        {
            InputTbx.Cut();
        }

        private void copyToolStripMenuItem_Click(object sender, EventArgs e)
        {
            InputTbx.Copy();
        }

        private void pasteToolStripMenuItem_Click(object sender, EventArgs e)
        {
            InputTbx.Paste();
        }

        private void selectAllToolStripMenuItem_Click(object sender, EventArgs e)
        {
            InputTbx.Focus();
            InputTbx.SelectAll();
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
                try
                {
                    if ((myStream = openFileDialog1.OpenFile()) != null)
                    {
                        // 读取文件内容至代码框
                        StreamReader sr = new StreamReader(myStream, System.Text.Encoding.GetEncoding("GB2312"));
                        InputTbx.Text = sr.ReadToEnd();
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
                        sr.Write(InputTbx.Text);
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

        private void InputTbx_SelectionChanged(object sender, EventArgs e)
        {
            int row, col=1;
            string text = InputTbx.Text.Substring(0, InputTbx.SelectionStart);
            string[] tokens = text.Split(new string[] { "\n" }, StringSplitOptions.None);
            row = tokens.Length;
            if (tokens.Length - 1 >= 0)
                col = tokens[tokens.Length - 1].Length + 1;
            sl_rowcol.Text = "Row " + row + "  Col " + col;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            TreeFrom f2 = new TreeFrom();
            f2.Show();
        }
    }
}