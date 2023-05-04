import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.DarkGoldenrod
		self._label1.Font = System.Drawing.Font("OCR A Extended", 9, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "First Name:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.DarkTurquoise
		self._label2.Font = System.Drawing.Font("OCR A Extended", 9, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 68)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 1
		self._label2.Text = "Last Name:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.SlateBlue
		self._label3.Font = System.Drawing.Font("Microsoft YaHei", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.White
		self._label3.Location = System.Drawing.Point(12, 112)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 2
		self._label3.Text = "Full Name:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(123, 12)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 18)
		self._textBox1.TabIndex = 3
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(123, 71)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 18)
		self._textBox2.TabIndex = 4
		# 
		# textBox3
		# 
		self._textBox3.BackColor = System.Drawing.Color.Red
		self._textBox3.Font = System.Drawing.Font("Modern No. 20", 11.999999, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox3.ForeColor = System.Drawing.Color.Blue
		self._textBox3.Location = System.Drawing.Point(12, 138)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(211, 25)
		self._textBox3.TabIndex = 5
		self._textBox3.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.ForestGreen
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 164)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(211, 23)
		self._button1.TabIndex = 6
		self._button1.Text = "Show Name"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Yellow
		self._button2.Font = System.Drawing.Font("Papyrus", 9, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(12, 193)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 7
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.DeepSkyBlue
		self._button3.Font = System.Drawing.Font("Papyrus", 7, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic)
		self._button3.Location = System.Drawing.Point(148, 193)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 8
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Olive
		self.ClientSize = System.Drawing.Size(231, 222)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Font = System.Drawing.Font("Microsoft Sans Serif", 6.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self.Name = "MainForm"
		self.Text = "pg119FullName"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		firstn = self._textBox1.Text
		lastn = self._textBox2.Text
		fulln = firstn + " " + lastn
		self._textBox3.Text = fulln
		pass

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass