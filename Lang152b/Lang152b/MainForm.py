import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._listBox1 = System.Windows.Forms.ListBox()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# listBox1
		# 
		self._listBox1.BackColor = System.Drawing.Color.DarkGoldenrod
		self._listBox1.Font = System.Drawing.Font("OCR A Extended", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._listBox1.ForeColor = System.Drawing.Color.LightPink
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 17
		self._listBox1.Location = System.Drawing.Point(12, 37)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(233, 259)
		self._listBox1.TabIndex = 0
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(225, 12)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 1
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Black
		self._button1.Font = System.Drawing.Font("OCR A Extended", 6.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.White
		self._button1.Location = System.Drawing.Point(251, 37)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 44)
		self._button1.TabIndex = 2
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.SlateBlue
		self._button2.Font = System.Drawing.Font("Microsoft PhagsPa", 13.25, System.Drawing.FontStyle.Bold)
		self._button2.ForeColor = System.Drawing.Color.ForestGreen
		self._button2.Location = System.Drawing.Point(251, 87)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 104)
		self._button2.TabIndex = 3
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.WhiteSmoke
		self._button3.Font = System.Drawing.Font("Microsoft JhengHei", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.Turquoise
		self._button3.Location = System.Drawing.Point(251, 197)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 104)
		self._button3.TabIndex = 4
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.DodgerBlue
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 12)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 5
		self._label1.Text = "Even Interger:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.BottomLeft
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.SteelBlue
		self._label2.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(119, 12)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 6
		self._label2.Text = "Total Sum:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.BottomLeft
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Violet
		self.ClientSize = System.Drawing.Size(337, 312)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "Lang152b"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		Sum = 0
		input = int(self._textBox1.Text)
		for num in range(0, input, 2):
			Sum = Sum + num
			self._listBox1.Items.Add(str(num) + "\t   " + str(Sum))
		pass

	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()
		self._textBox1.Text = ""
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass

	def MainFormLoad(self, sender, e):
		pass