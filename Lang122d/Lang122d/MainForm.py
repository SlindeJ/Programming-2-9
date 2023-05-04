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
		self._listBox1.BackColor = System.Drawing.Color.ForestGreen
		self._listBox1.ForeColor = System.Drawing.Color.Gold
		self._listBox1.FormattingEnabled = True
		self._listBox1.Location = System.Drawing.Point(12, 12)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(243, 290)
		self._listBox1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.SlateBlue
		self._button1.Font = System.Drawing.Font("OCR A Extended", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(261, 12)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(21, 290)
		self._button1.TabIndex = 1
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.BlueViolet
		self._button2.Font = System.Drawing.Font("Malgun Gothic", 18, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(288, 12)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(21, 290)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.MediumOrchid
		self._button3.Font = System.Drawing.Font("Bell MT", 14, System.Drawing.FontStyle.Bold)
		self._button3.Location = System.Drawing.Point(315, 12)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(21, 290)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Plum
		self.ClientSize = System.Drawing.Size(347, 320)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "Lang122d"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		for num in range(-12, 16 + 1):
			numy = int(num**6 - 3 * num**5 - 93 * num**4 + 87 * num**3 + 1596 * num**2 - 1380 * num - 2800)
			self._listBox1.Items.Add(str(num) + "\t" + str(numy))
		pass

	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass