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
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._label12 = System.Windows.Forms.Label()
		self._label13 = System.Windows.Forms.Label()
		self._label14 = System.Windows.Forms.Label()
		self._label15 = System.Windows.Forms.Label()
		self._label16 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.MediumVioletRed
		self._label1.Location = System.Drawing.Point(128, 8)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 20)
		self._label1.TabIndex = 0
		self._label1.Text = "Number1"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.MediumVioletRed
		self._label2.Location = System.Drawing.Point(128, 37)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 19)
		self._label2.TabIndex = 1
		self._label2.Text = "Number2"
		self._label2.Click += self.Label2Click
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(243, 8)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(199, 20)
		self._textBox1.TabIndex = 2
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(243, 37)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(199, 20)
		self._textBox2.TabIndex = 3
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.FromArgb(0, 192, 0)
		self._button1.Location = System.Drawing.Point(448, 6)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(146, 23)
		self._button1.TabIndex = 4
		self._button1.Text = "Clear"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.FromArgb(0, 192, 0)
		self._button2.Location = System.Drawing.Point(448, 35)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(146, 23)
		self._button2.TabIndex = 6
		self._button2.Text = "Exit"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.RoyalBlue
		self._button3.Location = System.Drawing.Point(104, 87)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(490, 55)
		self._button3.TabIndex = 7
		self._button3.Text = "Calculate"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.ControlText
		self._label3.ForeColor = System.Drawing.Color.Chartreuse
		self._label3.Location = System.Drawing.Point(104, 154)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(242, 23)
		self._label3.TabIndex = 8
		self._label3.Text = "Sum:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.ControlText
		self._label4.ForeColor = System.Drawing.Color.Chartreuse
		self._label4.Location = System.Drawing.Point(104, 177)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(242, 23)
		self._label4.TabIndex = 9
		self._label4.Text = "Difference:"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.SystemColors.ControlText
		self._label5.ForeColor = System.Drawing.Color.Chartreuse
		self._label5.Location = System.Drawing.Point(104, 200)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(242, 23)
		self._label5.TabIndex = 10
		self._label5.Text = "Product:"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.SystemColors.ControlText
		self._label6.ForeColor = System.Drawing.Color.Chartreuse
		self._label6.Location = System.Drawing.Point(104, 223)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(242, 23)
		self._label6.TabIndex = 11
		self._label6.Text = "Average:"
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.SystemColors.ControlText
		self._label7.ForeColor = System.Drawing.Color.Chartreuse
		self._label7.Location = System.Drawing.Point(104, 246)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(242, 23)
		self._label7.TabIndex = 12
		self._label7.Text = "Abs. Value"
		self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.SystemColors.ControlText
		self._label8.ForeColor = System.Drawing.Color.Chartreuse
		self._label8.Location = System.Drawing.Point(104, 269)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(242, 23)
		self._label8.TabIndex = 13
		self._label8.Text = "Maximum:"
		self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.SystemColors.ControlText
		self._label9.ForeColor = System.Drawing.Color.Chartreuse
		self._label9.Location = System.Drawing.Point(104, 292)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(242, 23)
		self._label9.TabIndex = 14
		self._label9.Text = "Minimum:"
		self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.Crimson
		self._label10.Font = System.Drawing.Font("Tahoma", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label10.Location = System.Drawing.Point(352, 292)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(242, 23)
		self._label10.TabIndex = 21
		self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.Color.Crimson
		self._label11.Font = System.Drawing.Font("Tahoma", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label11.Location = System.Drawing.Point(352, 269)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(242, 23)
		self._label11.TabIndex = 20
		self._label11.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label12
		# 
		self._label12.BackColor = System.Drawing.Color.Crimson
		self._label12.Font = System.Drawing.Font("Tahoma", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label12.Location = System.Drawing.Point(352, 246)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(242, 23)
		self._label12.TabIndex = 19
		self._label12.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label13
		# 
		self._label13.BackColor = System.Drawing.Color.Crimson
		self._label13.Font = System.Drawing.Font("Tahoma", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label13.Location = System.Drawing.Point(352, 223)
		self._label13.Name = "label13"
		self._label13.Size = System.Drawing.Size(242, 23)
		self._label13.TabIndex = 18
		self._label13.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label14
		# 
		self._label14.BackColor = System.Drawing.Color.Crimson
		self._label14.Font = System.Drawing.Font("Tahoma", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label14.Location = System.Drawing.Point(352, 200)
		self._label14.Name = "label14"
		self._label14.Size = System.Drawing.Size(242, 23)
		self._label14.TabIndex = 17
		self._label14.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label15
		# 
		self._label15.BackColor = System.Drawing.Color.Crimson
		self._label15.Font = System.Drawing.Font("Tahoma", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label15.Location = System.Drawing.Point(352, 177)
		self._label15.Name = "label15"
		self._label15.Size = System.Drawing.Size(242, 23)
		self._label15.TabIndex = 16
		self._label15.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label16
		# 
		self._label16.BackColor = System.Drawing.Color.Crimson
		self._label16.Font = System.Drawing.Font("Tahoma", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label16.Location = System.Drawing.Point(352, 154)
		self._label16.Name = "label16"
		self._label16.Size = System.Drawing.Size(242, 23)
		self._label16.TabIndex = 15
		self._label16.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.MediumTurquoise
		self.ClientSize = System.Drawing.Size(710, 321)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label12)
		self.Controls.Add(self._label13)
		self.Controls.Add(self._label14)
		self.Controls.Add(self._label15)
		self.Controls.Add(self._label16)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Lang88a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button3Click(self, sender, e):
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		Sum = num1 + num2
		diff = num1 - num2
		if (num1 - num2) < 0:
			diff = num1 - num2 
		else:
			diff = num2 - num1
		if (num1 - num2) > 0:
			Abs = num1 - num2 
		else:
			Abs = num2 - num1
		Product = num1 * num2
		if num1 >= num2:
			Max = num1
		else:
			Max = num2
		if Max == num1:
			Min = num2
		else:
			Min = num1
		
		self._label11.Text = str(Max)
		self._label10.Text = str(Min)
		self._label12.Text = str(Abs)
		self._label13.Text = str(Sum/2.0)
		self._label14.Text = str(Product)
		self._label15.Text = str(diff)
		self._label16.Text = str(Sum)
		
		
		
		Max = 0
		Min = 0
		pass

	def Button2Click(self, sender, e):
		Application.Exit()
		pass

	def Button1Click(self, sender, e):		#Clear button
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label11.Text = ""
		self._label10.Text = ""
		self._label12.Text = ""
		self._label13.Text = ""
		self._label14.Text = ""
		self._label15.Text = ""
		self._label16.Text = ""
		pass

	def Label2Click(self, sender, e):
		pass