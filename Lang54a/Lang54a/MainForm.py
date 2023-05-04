import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._comboBox1 = System.Windows.Forms.ComboBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Black
		self._label1.Font = System.Drawing.Font("Sitka Small", 28)
		self._label1.ForeColor = System.Drawing.Color.White
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(166, 82)
		self._label1.TabIndex = 0
		self._label1.Text = "Car:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.TopRight
		# 
		# comboBox1
		# 
		self._comboBox1.FormattingEnabled = True
		self._comboBox1.Items.AddRange(System.Array[System.Object](
			["1970 VW Bug",
			"1979 Firebird",
			"1980 Subaru",
			"1975 Cutlass"]))
		self._comboBox1.Location = System.Drawing.Point(184, 32)
		self._comboBox1.Name = "comboBox1"
		self._comboBox1.Size = System.Drawing.Size(162, 21)
		self._comboBox1.TabIndex = 1
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.FromArgb(255, 128, 255)
		self._button1.Font = System.Drawing.Font("Papyrus", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(101, 99)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(490, 49)
		self._button1.TabIndex = 2
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.DodgerBlue
		self._button2.Font = System.Drawing.Font("Tempus Sans ITC", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.Maroon
		self._button2.Location = System.Drawing.Point(378, 9)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(158, 64)
		self._button2.TabIndex = 3
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.FromArgb(128, 255, 255)
		self._button3.Font = System.Drawing.Font("Tempus Sans ITC", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.Maroon
		self._button3.Location = System.Drawing.Point(542, 9)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(156, 79)
		self._button3.TabIndex = 4
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Red
		self._label2.Font = System.Drawing.Font("Times New Roman", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.Blue
		self._label2.Location = System.Drawing.Point(101, 151)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(177, 46)
		self._label2.TabIndex = 5
		self._label2.Text = "Miles:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.TopRight
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.FromArgb(255, 128, 0)
		self._label3.Font = System.Drawing.Font("Times New Roman", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.Red
		self._label3.Location = System.Drawing.Point(101, 207)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(177, 46)
		self._label3.TabIndex = 6
		self._label3.Text = "Gallons:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Yellow
		self._label4.Font = System.Drawing.Font("Times New Roman", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.DarkGreen
		self._label4.Location = System.Drawing.Point(101, 264)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(177, 46)
		self._label4.TabIndex = 7
		self._label4.Text = "MPG:"
		self._label4.TextAlign = System.Drawing.ContentAlignment.BottomRight
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Red
		self._label5.Font = System.Drawing.Font("Yu Gothic", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ForeColor = System.Drawing.Color.Blue
		self._label5.Location = System.Drawing.Point(357, 151)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(234, 46)
		self._label5.TabIndex = 8
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.FromArgb(255, 128, 0)
		self._label6.Font = System.Drawing.Font("Yu Gothic", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.ForeColor = System.Drawing.Color.Red
		self._label6.Location = System.Drawing.Point(357, 207)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(234, 46)
		self._label6.TabIndex = 9
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.Yellow
		self._label7.Font = System.Drawing.Font("Yu Gothic", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.ForeColor = System.Drawing.Color.DarkGreen
		self._label7.Location = System.Drawing.Point(357, 262)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(234, 46)
		self._label7.TabIndex = 10
		self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Blue
		self.ClientSize = System.Drawing.Size(710, 317)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._comboBox1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Lang54a"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)


	def MainFormLoad(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		miles = 0
		gallons = 0
		mpg = 0
		car = self._comboBox1.Text
		if car == "1970 VW Bug":
			miles = 286
			gallons = 9
		if car == "1980 Subaru":
			miles = 361
			gallons = 18
		if car == "1979 Firebird":
			miles = 412
			gallons = 40
		if car == "1975 Cutlass":
			miles = 161
			gallons = 11
		#cast one varaible as float to get real division
		mpg = miles / float(gallons)
		mpg = round(mpg, 10)
		self._label7.Text = str(mpg)
		self._label6.Text = str(gallons)
		self._label5.Text = str(miles)
		pass

	def Button2Click(self, sender, e):
		self._label7.Text = ""
		self._label6.Text = ""
		self._label5.Text = ""
		self._comboBox1.Text = ""
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass