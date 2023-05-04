import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._label12 = System.Windows.Forms.Label()
		self._label13 = System.Windows.Forms.Label()
		self._label14 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(175, 12)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 0
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(175, 34)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 1
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Black
		self._label1.ForeColor = System.Drawing.Color.White
		self._label1.Location = System.Drawing.Point(30, 12)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 2
		self._label1.Text = "Amount to be Paid:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		self._label1.Click += self.Label1Click
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Black
		self._label2.ForeColor = System.Drawing.Color.White
		self._label2.Location = System.Drawing.Point(30, 34)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 3
		self._label2.Text = "Amount Recieved:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Black
		self._label3.ForeColor = System.Drawing.Color.White
		self._label3.Location = System.Drawing.Point(30, 57)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 4
		self._label3.Text = "Change:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.LightGreen
		self._label4.Location = System.Drawing.Point(30, 80)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(139, 32)
		self._label4.TabIndex = 5
		self._label4.Text = "Dollars"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.CornflowerBlue
		self._label5.Location = System.Drawing.Point(175, 57)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 6
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Red
		self._button1.Font = System.Drawing.Font("OCR A Extended", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(30, 235)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(245, 78)
		self._button1.TabIndex = 7
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.DarkGoldenrod
		self._button2.Font = System.Drawing.Font("Papyrus", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.SystemColors.ControlLightLight
		self._button2.Location = System.Drawing.Point(293, 14)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(172, 158)
		self._button2.TabIndex = 8
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.DarkGoldenrod
		self._button3.Font = System.Drawing.Font("Papyrus", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.SystemColors.ControlLightLight
		self._button3.Location = System.Drawing.Point(465, 148)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(172, 158)
		self._button3.TabIndex = 9
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.LightGreen
		self._label6.Location = System.Drawing.Point(175, 80)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 32)
		self._label6.TabIndex = 10
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.DodgerBlue
		self._label7.Location = System.Drawing.Point(175, 112)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(100, 30)
		self._label7.TabIndex = 11
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.DarkOrchid
		self._label8.Location = System.Drawing.Point(175, 142)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(100, 30)
		self._label8.TabIndex = 12
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.DeepPink
		self._label9.Location = System.Drawing.Point(175, 172)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(100, 30)
		self._label9.TabIndex = 13
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.Crimson
		self._label10.Location = System.Drawing.Point(175, 202)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(100, 30)
		self._label10.TabIndex = 14
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.Color.DodgerBlue
		self._label11.Location = System.Drawing.Point(30, 112)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(139, 30)
		self._label11.TabIndex = 15
		self._label11.Text = "Quarters"
		# 
		# label12
		# 
		self._label12.BackColor = System.Drawing.Color.DarkOrchid
		self._label12.Location = System.Drawing.Point(30, 142)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(139, 30)
		self._label12.TabIndex = 16
		self._label12.Text = "Dimes"
		# 
		# label13
		# 
		self._label13.BackColor = System.Drawing.Color.DeepPink
		self._label13.Location = System.Drawing.Point(30, 172)
		self._label13.Name = "label13"
		self._label13.Size = System.Drawing.Size(139, 30)
		self._label13.TabIndex = 17
		self._label13.Text = "Nickels"
		# 
		# label14
		# 
		self._label14.BackColor = System.Drawing.Color.Crimson
		self._label14.Location = System.Drawing.Point(30, 202)
		self._label14.Name = "label14"
		self._label14.Size = System.Drawing.Size(139, 30)
		self._label14.TabIndex = 18
		self._label14.Text = "Pennies"
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Silver
		self.ClientSize = System.Drawing.Size(649, 318)
		self.Controls.Add(self._label14)
		self.Controls.Add(self._label13)
		self.Controls.Add(self._label12)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "Lang58t"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)
		self.PerformLayout()


	def Label1Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		Price = float(self._textBox1.Text)
		Payed = float(self._textBox2.Text)
		Change = float(Payed - Price)
		self._label5.Text = str(Change)
		Dollars = float(Change // 1.00)
		Quarters = float((Change - Dollars) // 0.25)
		DollarsQ = Dollars + Quarters * 0.25			#DollarsQ
		Dimes = float((Change - DollarsQ) // 0.10)
		DollarsD = DollarsQ + Dimes * 0.10			#DollarsD
		Nickels = float((Change - DollarsD) // 0.05)
		DollarsN = DollarsD + Nickels * 0.05			#DollarsN
		Pennies = float((Change - DollarsN) / 0.01)
		self._label6.Text = str(Dollars)
		self._label7.Text = str(Quarters)
		self._label8.Text = str(Dimes)
		self._label9.Text = str(Nickels)
		self._label10.Text = str(Pennies)
		pass

	def Button2Click(self, sender, e):
		self._label6.Text = ""
		self._label7.Text = ""
		self._label8.Text = ""
		self._label9.Text = ""
		self._label10.Text = ""
		self._label5.Text = ""
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass

	def MainFormLoad(self, sender, e):
		pass