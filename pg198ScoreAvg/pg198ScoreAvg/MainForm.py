import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._label6 = System.Windows.Forms.Label()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Khaki
		self._button1.Font = System.Drawing.Font("Palatino Linotype", 12, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 186)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(158, 37)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate Average"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.ForestGreen
		self._button2.Font = System.Drawing.Font("Myanmar Text", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.Navy
		self._button2.Location = System.Drawing.Point(127, 229)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(158, 37)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.FromArgb(192, 0, 0)
		self._button3.Font = System.Drawing.Font("OCR A Extended", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.White
		self._button3.Location = System.Drawing.Point(12, 272)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(158, 37)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.RoyalBlue
		self._label1.ForeColor = System.Drawing.Color.Black
		self._label1.Location = System.Drawing.Point(21, 19)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 3
		self._label1.Text = "Score 1:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.SteelBlue
		self._label2.ForeColor = System.Drawing.Color.Black
		self._label2.Location = System.Drawing.Point(21, 57)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 4
		self._label2.Text = "Score 2:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.DeepSkyBlue
		self._label3.ForeColor = System.Drawing.Color.Black
		self._label3.Location = System.Drawing.Point(21, 92)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 5
		self._label3.Text = "Score 3:"
		self._label3.Click += self.Label3Click
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.DarkTurquoise
		self._label4.ForeColor = System.Drawing.Color.Black
		self._label4.Location = System.Drawing.Point(21, 131)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 6
		self._label4.Text = "Average:"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.LimeGreen
		self._label5.ForeColor = System.Drawing.Color.FromArgb(64, 64, 64)
		self._label5.Location = System.Drawing.Point(152, 131)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 7
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(152, 19)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 8
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(152, 57)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 9
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(152, 92)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 20)
		self._textBox3.TabIndex = 10
		# 
		# groupBox1
		# 
		self._groupBox1.BackColor = System.Drawing.Color.SlateBlue
		self._groupBox1.Controls.Add(self._textBox3)
		self._groupBox1.Controls.Add(self._textBox2)
		self._groupBox1.Controls.Add(self._textBox1)
		self._groupBox1.Controls.Add(self._label5)
		self._groupBox1.Controls.Add(self._label4)
		self._groupBox1.Controls.Add(self._label3)
		self._groupBox1.Controls.Add(self._label2)
		self._groupBox1.Controls.Add(self._label1)
		self._groupBox1.ForeColor = System.Drawing.Color.White
		self._groupBox1.Location = System.Drawing.Point(12, 12)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(273, 166)
		self._groupBox1.TabIndex = 11
		self._groupBox1.TabStop = False
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.Red
		self._label6.Font = System.Drawing.Font("Arial Narrow", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.ForeColor = System.Drawing.Color.MidnightBlue
		self._label6.Location = System.Drawing.Point(176, 186)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(109, 37)
		self._label6.TabIndex = 12
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Red
		self.ClientSize = System.Drawing.Size(303, 321)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._groupBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "pg198ScoreAvg"
		self._groupBox1.ResumeLayout(False)
		self._groupBox1.PerformLayout()
		self.ResumeLayout(False)


	def Label3Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		s1 = float(self._textBox1.Text)
		s2 = float(self._textBox2.Text)
		s3 = float(self._textBox3.Text)
		average = float((s1 + s2 + s3) / 3)
		average = round(average, 2)
		self._label5.Text = str(average)
		if float(average) >= 95:
			self._label6.Text = "Congradulations! Great Job!"
		pass

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""
		self._label5.Text = ""
		self._label6.Text = ""
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass