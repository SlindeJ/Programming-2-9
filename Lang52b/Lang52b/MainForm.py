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
		self._textBox3 = System.Windows.Forms.TextBox()
		self._textBox4 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.SystemColors.WindowText
		self._textBox1.ForeColor = System.Drawing.SystemColors.Window
		self._textBox1.Location = System.Drawing.Point(12, 89)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(270, 20)
		self._textBox1.TabIndex = 0
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.SystemColors.WindowText
		self._textBox2.ForeColor = System.Drawing.SystemColors.Window
		self._textBox2.Location = System.Drawing.Point(12, 115)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(270, 20)
		self._textBox2.TabIndex = 1
		# 
		# textBox3
		# 
		self._textBox3.BackColor = System.Drawing.SystemColors.WindowText
		self._textBox3.ForeColor = System.Drawing.SystemColors.Window
		self._textBox3.Location = System.Drawing.Point(12, 141)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(270, 20)
		self._textBox3.TabIndex = 2
		# 
		# textBox4
		# 
		self._textBox4.BackColor = System.Drawing.SystemColors.WindowText
		self._textBox4.ForeColor = System.Drawing.SystemColors.Window
		self._textBox4.Location = System.Drawing.Point(12, 167)
		self._textBox4.Name = "textBox4"
		self._textBox4.Size = System.Drawing.Size(270, 20)
		self._textBox4.TabIndex = 3
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.BlueViolet
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.GhostWhite
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(270, 77)
		self._label1.TabIndex = 4
		self._label1.Text = "Please Input Numbers"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._label2.ForeColor = System.Drawing.Color.White
		self._label2.Location = System.Drawing.Point(381, 41)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 5
		self._label2.Text = "Sum"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.ControlDark
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 22)
		self._label3.Location = System.Drawing.Point(381, 64)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 71)
		self._label3.TabIndex = 6
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label3.Click += self.Label3Click
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.ForestGreen
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12)
		self._button1.Location = System.Drawing.Point(12, 193)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(270, 48)
		self._button1.TabIndex = 9
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Goldenrod
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 12)
		self._button2.Location = System.Drawing.Point(12, 257)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(270, 51)
		self._button2.TabIndex = 10
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.RoyalBlue
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 22)
		self._button3.ForeColor = System.Drawing.SystemColors.ButtonShadow
		self._button3.Location = System.Drawing.Point(340, 193)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(359, 115)
		self._button3.TabIndex = 11
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label4
		# 
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._label4.ForeColor = System.Drawing.Color.White
		self._label4.Location = System.Drawing.Point(564, 41)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 12
		self._label4.Text = "Average"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label4.Click += self.Label4Click
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.SystemColors.ControlDark
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 22)
		self._label5.Location = System.Drawing.Point(564, 64)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 71)
		self._label5.TabIndex = 13
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Tomato
		self.ClientSize = System.Drawing.Size(752, 320)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox4)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "Lang52b"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		nbr1 = int(self._textBox1.Text)
		nbr2 = int(self._textBox2.Text)
		nbr3 = int(self._textBox3.Text)
		nbr4 = int(self._textBox4.Text)
		sum = nbr1 + nbr2 + nbr3 + nbr4
		average = (nbr1 + nbr2 + nbr3 + nbr4)/4.0
		self._label3.Text = str(sum)
		self._label5.Text = str(average)
		pass

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""
		self._textBox4.Text = ""
		self._label3.Text = ""
		self._label5.Text = ""
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass

	def Label4Click(self, sender, e):
		pass

	def Label3Click(self, sender, e):
		pass