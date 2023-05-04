import math
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._listBox1 = System.Windows.Forms.ListBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# listBox1
		# 
		self._listBox1.BackColor = System.Drawing.Color.Black
		self._listBox1.ForeColor = System.Drawing.Color.White
		self._listBox1.FormattingEnabled = True
		self._listBox1.Location = System.Drawing.Point(12, 12)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(437, 186)
		self._listBox1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Lime
		self._button1.ForeColor = System.Drawing.Color.Red
		self._button1.Location = System.Drawing.Point(12, 204)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(141, 43)
		self._button1.TabIndex = 1
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.FromArgb(128, 255, 128)
		self._button2.ForeColor = System.Drawing.Color.FromArgb(255, 128, 128)
		self._button2.Location = System.Drawing.Point(136, 253)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(141, 43)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
		self._button3.ForeColor = System.Drawing.Color.FromArgb(255, 192, 192)
		self._button3.Location = System.Drawing.Point(295, 219)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(141, 43)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Crimson
		self.ClientSize = System.Drawing.Size(502, 316)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "Lang122a"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		# range(start, stop, stepsize) -- iterate on even 0-10: range(0 11, 2)
		for num in range(1, 50 + 1):
			numSqd = num**2
			numSqrt = math.sqrt(num)
			numSqrt = round(math.sqrt(num), 4)
			self._listBox1.Items.Add(str(num) + "\t" + str(numSqd) + "\t" + str(numSqrt))
		pass

	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass