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
		self._listBox1.Size = System.Drawing.Size(291, 290)
		self._listBox1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.FromArgb(192, 64, 0)
		self._button1.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._button1.Location = System.Drawing.Point(309, 12)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 88)
		self._button1.TabIndex = 1
		self._button1.Text = "Show"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.FromArgb(255, 128, 0)
		self._button2.ForeColor = System.Drawing.Color.Blue
		self._button2.Location = System.Drawing.Point(309, 106)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 102)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
		self._button3.ForeColor = System.Drawing.Color.Crimson
		self._button3.Location = System.Drawing.Point(309, 214)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 88)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.LightGreen
		self.ClientSize = System.Drawing.Size(397, 318)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "Lang122h"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		for num in range(1, 20 + 1):
			sqr = num**2
			sqroot = math.sqrt(num)
			sqroot2 = round(sqroot, 4)
			cube = num**3
			cuberoot = math.sqrt(sqroot)
			cuberoot = round(cuberoot, 4)
			self._listBox1.Items.Add("\t" + str(num) + "\t" + str(sqr) + "\t" + str(sqroot2) + "\t" + str(cube) + "\t" + str(cuberoot))
		pass

	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass