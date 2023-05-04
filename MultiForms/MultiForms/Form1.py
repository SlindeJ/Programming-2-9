
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form1(Form):
	def __init__(self, parent, msg):
		self.InitializeComponent()
		self.parent = parent
		self.msg = msg
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ControlDark
		self._label1.Location = System.Drawing.Point(99, 41)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "label1"
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(73, 142)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(160, 60)
		self._button1.TabIndex = 1
		self._button1.Text = "Show Home Form"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# Form1
		# 
		self.ClientSize = System.Drawing.Size(321, 319)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Name = "Form1"
		self.Text = "Form1"
		self.FormClosing += self.Form1FormClosing
		self.Load += self.Form1Load
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		self.Close()
		self.parent.Show()
		pass

	def Form1Load(self, sender, e):
		self._label1.Text = self.msg
		pass

	def Form1FormClosing(self, sender, e):
		self.parent.Show()
		pass