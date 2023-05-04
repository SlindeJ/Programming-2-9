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
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._button4 = System.Windows.Forms.Button()
		self._button5 = System.Windows.Forms.Button()
		self._button6 = System.Windows.Forms.Button()
		self._button7 = System.Windows.Forms.Button()
		self._button8 = System.Windows.Forms.Button()
		self._button9 = System.Windows.Forms.Button()
		self._textBox3 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Blue
		self._label1.Font = System.Drawing.Font("Maiandra GD", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.Orange
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "First Number:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Lime
		self._label2.Font = System.Drawing.Font("Maiandra GD", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 52)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 1
		self._label2.Text = "Operation:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.FromArgb(255, 128, 0)
		self._label3.Font = System.Drawing.Font("Maiandra GD", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.SlateBlue
		self._label3.Location = System.Drawing.Point(12, 95)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 2
		self._label3.Text = "Second Number:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Red
		self._label4.Font = System.Drawing.Font("Maiandra GD", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.White
		self._label4.Location = System.Drawing.Point(12, 140)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 3
		self._label4.Text = "Output:"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Black
		self._label5.Font = System.Drawing.Font("OCR A Extended", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ForeColor = System.Drawing.Color.White
		self._label5.Location = System.Drawing.Point(170, 52)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 4
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.SystemColors.ScrollBar
		self._textBox1.Location = System.Drawing.Point(170, 9)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 5
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.SystemColors.ScrollBar
		self._textBox2.Location = System.Drawing.Point(170, 95)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 6
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Black
		self._button1.Font = System.Drawing.Font("OCR A Extended", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.White
		self._button1.Location = System.Drawing.Point(100, 311)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(82, 60)
		self._button1.TabIndex = 8
		self._button1.Text = "MOD"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Green
		self._button2.ForeColor = System.Drawing.Color.HotPink
		self._button2.Location = System.Drawing.Point(12, 339)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(82, 23)
		self._button2.TabIndex = 9
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Maroon
		self._button3.ForeColor = System.Drawing.Color.RoyalBlue
		self._button3.Location = System.Drawing.Point(188, 339)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(82, 23)
		self._button3.TabIndex = 10
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# button4
		# 
		self._button4.BackColor = System.Drawing.Color.Black
		self._button4.Font = System.Drawing.Font("OCR A Extended", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button4.ForeColor = System.Drawing.Color.White
		self._button4.Location = System.Drawing.Point(12, 183)
		self._button4.Name = "button4"
		self._button4.Size = System.Drawing.Size(82, 54)
		self._button4.TabIndex = 11
		self._button4.Text = "+"
		self._button4.UseVisualStyleBackColor = False
		self._button4.Click += self.Button4Click
		# 
		# button5
		# 
		self._button5.BackColor = System.Drawing.Color.Black
		self._button5.Font = System.Drawing.Font("OCR A Extended", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button5.ForeColor = System.Drawing.Color.White
		self._button5.Location = System.Drawing.Point(12, 251)
		self._button5.Name = "button5"
		self._button5.Size = System.Drawing.Size(82, 54)
		self._button5.TabIndex = 12
		self._button5.Text = "^"
		self._button5.UseVisualStyleBackColor = False
		self._button5.Click += self.Button5Click
		# 
		# button6
		# 
		self._button6.BackColor = System.Drawing.Color.Black
		self._button6.Font = System.Drawing.Font("OCR A Extended", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button6.ForeColor = System.Drawing.Color.White
		self._button6.Location = System.Drawing.Point(100, 183)
		self._button6.Name = "button6"
		self._button6.Size = System.Drawing.Size(82, 54)
		self._button6.TabIndex = 14
		self._button6.Text = "-"
		self._button6.UseVisualStyleBackColor = False
		self._button6.Click += self.Button6Click
		# 
		# button7
		# 
		self._button7.BackColor = System.Drawing.Color.Black
		self._button7.Font = System.Drawing.Font("OCR A Extended", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button7.ForeColor = System.Drawing.Color.White
		self._button7.Location = System.Drawing.Point(100, 251)
		self._button7.Name = "button7"
		self._button7.Size = System.Drawing.Size(82, 54)
		self._button7.TabIndex = 13
		self._button7.Text = "/"
		self._button7.UseVisualStyleBackColor = False
		self._button7.Click += self.Button7Click
		# 
		# button8
		# 
		self._button8.BackColor = System.Drawing.Color.Black
		self._button8.Font = System.Drawing.Font("OCR A Extended", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button8.ForeColor = System.Drawing.Color.White
		self._button8.Location = System.Drawing.Point(188, 183)
		self._button8.Name = "button8"
		self._button8.Size = System.Drawing.Size(82, 54)
		self._button8.TabIndex = 16
		self._button8.Text = "*"
		self._button8.UseVisualStyleBackColor = False
		self._button8.Click += self.Button8Click
		# 
		# button9
		# 
		self._button9.BackColor = System.Drawing.Color.Black
		self._button9.Font = System.Drawing.Font("OCR A Extended", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button9.ForeColor = System.Drawing.Color.White
		self._button9.Location = System.Drawing.Point(188, 251)
		self._button9.Name = "button9"
		self._button9.Size = System.Drawing.Size(82, 54)
		self._button9.TabIndex = 15
		self._button9.Text = "//"
		self._button9.UseVisualStyleBackColor = False
		self._button9.Click += self.Button9Click
		# 
		# textBox3
		# 
		self._textBox3.BackColor = System.Drawing.Color.FromArgb(255, 128, 0)
		self._textBox3.Font = System.Drawing.Font("Rockwell", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox3.ForeColor = System.Drawing.Color.Blue
		self._textBox3.Location = System.Drawing.Point(149, 140)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(121, 23)
		self._textBox3.TabIndex = 17
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.White
		self.ClientSize = System.Drawing.Size(283, 374)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._button8)
		self.Controls.Add(self._button9)
		self.Controls.Add(self._button6)
		self.Controls.Add(self._button7)
		self.Controls.Add(self._button5)
		self.Controls.Add(self._button4)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "pg140SimpleCalc"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		#MOD
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		self._label5.Text = "MOD"
		divinitial = num1 // num2
		divafter = divinitial * num2
		output = num1 - divafter
		self._textBox3.Text = str(output)
		pass

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""
		self._label5.Text = ""
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass

	def Button4Click(self, sender, e):
		#addition
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		self._label5.Text = "+"
		output = num1 + num2
		self._textBox3.Text = str(output)
		pass

	def Button5Click(self, sender, e):
		#exponent
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		self._label5.Text = "^"
		output = num1 ** num2
		self._textBox3.Text = str(output)
		pass

	def Button6Click(self, sender, e):
		#subtraction
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		self._label5.Text = "-"
		output = num1 - num2
		self._textBox3.Text = str(output)
		pass

	def Button7Click(self, sender, e):
		#normal division
		num1 = float(self._textBox1.Text)
		num2 = float(self._textBox2.Text)
		self._label5.Text = "/"
		output = num1 / num2
		output = round(output, 2)
		self._textBox3.Text = str(output)
		pass

	def Button8Click(self, sender, e):
		#multiplication
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		self._label5.Text = "*"
		output = num1 * num2
		self._textBox3.Text = str(output)
		pass

	def Button9Click(self, sender, e):
		#floor division
		num1 = float(self._textBox1.Text)
		num2 = float(self._textBox2.Text)
		self._label5.Text = "//"
		output = num1 // num2
		output = round(output, 2)
		self._textBox3.Text = str(output)
		pass