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
		self._listBox1.BackColor = System.Drawing.SystemColors.HotTrack
		self._listBox1.ForeColor = System.Drawing.Color.White
		self._listBox1.FormattingEnabled = True
		self._listBox1.Location = System.Drawing.Point(148, 12)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(545, 225)
		self._listBox1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.BlueViolet
		self._button1.Font = System.Drawing.Font("OCR A Extended", 14)
		self._button1.ForeColor = System.Drawing.Color.Cornsilk
		self._button1.Location = System.Drawing.Point(12, 12)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(130, 225)
		self._button1.TabIndex = 1
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Crimson
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 26)
		self._button2.ForeColor = System.Drawing.Color.DarkCyan
		self._button2.Location = System.Drawing.Point(12, 243)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(296, 60)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.SystemColors.ControlText
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 5, System.Drawing.FontStyle.Bold)
		self._button3.ForeColor = System.Drawing.SystemColors.Control
		self._button3.Location = System.Drawing.Point(314, 243)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(379, 60)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DarkOliveGreen
		self.ClientSize = System.Drawing.Size(705, 315)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "Lang122c"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		for num in range(1, 5 + 1):
			firstrow = int(num * 2)
			secondrow = int(num * 2 + 1)
			thirdrow = int(num * 4)
			fourthrow = int(num * (4 * num))
			self._listBox1.Items.Add("\t" + str(firstrow) + "\t" + str(secondrow) + "\t" + str(thirdrow) + "\t" + str(fourthrow))
		pass

	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass