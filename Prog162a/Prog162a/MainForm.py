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
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label3 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Maroon
		self._button1.ForeColor = System.Drawing.Color.White
		self._button1.Location = System.Drawing.Point(12, 69)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(206, 23)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Navy
		self._button2.ForeColor = System.Drawing.Color.White
		self._button2.Location = System.Drawing.Point(12, 96)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(100, 26)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.DodgerBlue
		self._button3.Location = System.Drawing.Point(118, 96)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(100, 26)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Khaki
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 10)
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 34)
		self._label1.TabIndex = 3
		self._label1.Text = "Enter Factorial Number:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Chartreuse
		self._label2.Location = System.Drawing.Point(12, 43)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 4
		self._label2.Text = "Factorial Value:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(118, 9)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 6
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.MediumSeaGreen
		self._label3.Location = System.Drawing.Point(118, 43)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 7
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.RosyBrown
		self.ClientSize = System.Drawing.Size(232, 134)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Prog162a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button3Click(self, sender, e):
		Application.Exit()
		pass

	def Button1Click(self, sender, e):
		number = int(self._textBox1.Text)
		value = 1
		for num in range(1, number + 1, 1):
			value = value * num
			self._label3.Text = str(value)
		pass

	def Button2Click(self, sender, e):
		self._label3.Text = ""
		self._textBox1.Text = ""
		pass