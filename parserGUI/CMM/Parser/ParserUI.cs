using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using Eto.Drawing;
using Eto.Forms;

namespace ParserUI
{
    partial class MainForm
    {
        private void InitializeComponent()
        {
            var layout_left = new DynamicLayout { Padding = new Padding(10, 5, 5, 5), Spacing = new Size(5, 5), ClientSize = new Size(345, 426), MinimumSize = new Size(345, 426) };
            var layout_right = new DynamicLayout { Padding = new Padding(5, 5, 5, 5), Spacing = new Size(5, 5), ClientSize = new Size(180, 426), MinimumSize = new Size(180, 426) };

            var layout_serialPort = new DynamicLayout { Padding = new Padding(5, 15, 5, 5), Spacing = new Size(5, 5) };


            _textAreaIn = new TextArea() { BackgroundColor = Colors.Black, TextColor = Colors.SpringGreen, };
            _textAreaOut = new TextArea() { BackgroundColor = Colors.Black, TextColor = Colors.SpringGreen, };
            layout_left.AddAutoSized(new Label() { Text = "接收区" });
            layout_left.AddSeparateRow(new Panel() { Content = _textAreaIn, MinimumSize = new Size(345, 240), ClientSize = new Size(345, 240) });
            layout_left.AddAutoSized(new Label() { Text = "发送区" });
            layout_left.AddSeparateRow(new Panel() { Content = _textAreaOut, MinimumSize = new Size(345, 165), ClientSize = new Size(345, 165) });

            _comboBoxSerialPortName = new ComboBox();
            _comboBoxSerialBaudRate = new ComboBox();
            _comboBoxSerialDataBits = new ComboBox();
            _comboBoxSerialParity = new ComboBox();
            _comboBoxSerialStopBits = new ComboBox();

            _btnClear = new Button { Text = "清空收区" };
            _btnOpen = new Button { Text = "打开串口" };
            _btnSend = new Button { Text = "串口发送" };
            _checkBoxHex = new CheckBox { Text = "是否Hex" };
            label7 = new Label();

            layout_serialPort.BeginVertical();
            layout_serialPort.BeginHorizontal();
            layout_serialPort.AddAutoSized(new Label() { Text = "端口号：" }, new Padding(0, 3));
            layout_serialPort.AddAutoSized(_comboBoxSerialPortName);
            layout_serialPort.EndBeginHorizontal();
            layout_serialPort.BeginHorizontal();
            layout_serialPort.AddAutoSized(new Label() { Text = "波特率：" }, new Padding(0, 3));
            layout_serialPort.AddAutoSized(_comboBoxSerialBaudRate);
            layout_serialPort.EndBeginHorizontal();
            layout_serialPort.BeginHorizontal();
            layout_serialPort.AddAutoSized(new Label() { Text = "数据位：" }, new Padding(0, 3));
            layout_serialPort.AddAutoSized(_comboBoxSerialDataBits);
            layout_serialPort.EndBeginHorizontal();
            layout_serialPort.BeginHorizontal();
            layout_serialPort.AddAutoSized(new Label() { Text = "效验位：" }, new Padding(0, 3));
            layout_serialPort.AddAutoSized(_comboBoxSerialParity);
            layout_serialPort.EndBeginHorizontal();
            layout_serialPort.BeginHorizontal();
            layout_serialPort.AddAutoSized(new Label() { Text = "停止位：" }, new Padding(0, 3));
            layout_serialPort.AddAutoSized(_comboBoxSerialStopBits);
            layout_serialPort.EndBeginHorizontal();
            //layout_serialPort.AddColumn();
            //layout_serialPort.AddColumn();

            layout_serialPort.EndBeginVertical();

            layout_right.AddAutoSized(layout_serialPort);
            layout_right.AddCentered(new Panel() { Content = _btnClear, ClientSize = new Size(164, 37), MinimumSize = new Size(164, 37) }, null, null, true);
            layout_right.AddCentered(new Panel() { Content = _btnOpen, ClientSize = new Size(164, 37), MinimumSize = new Size(164, 37) }, new Padding(0, 80, 0, 0), null, true);
            layout_right.AddCentered(new Panel() { Content = _btnSend, ClientSize = new Size(164, 37), MinimumSize = new Size(164, 37) }, new Padding(0, 10), null, true);
            layout_right.AddCentered(_checkBoxHex);
            layout_right.AddAutoSized(label7);

            var layout = new Splitter()
            {
                Panel1 = layout_left,
                Panel2 = layout_right,
                Orientation = SplitterOrientation.Horizontal
            };
        }





        private TextArea _textAreaIn;
        private TextArea _textAreaOut;

        private ComboBox _comboBoxSerialPortName;
        private ComboBox _comboBoxSerialBaudRate;
        private ComboBox _comboBoxSerialDataBits;
        private ComboBox _comboBoxSerialParity;
        private ComboBox _comboBoxSerialStopBits;

        private Button _btnClear;
        private Button _btnOpen;
        private Button _btnSend;
        private CheckBox _checkBoxHex;
        private Label label7;
    }
}
