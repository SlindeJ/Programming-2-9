﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Red
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 24)
		self._label1.Location = System.Drawing.Point(80, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(564, 75)
		self._label1.TabIndex = 0
		self._label1.Text = "Hello, World"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Black
		self._button1.Location = System.Drawing.Point(80, 151)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(261, 71)
		self._button1.TabIndex = 1
		self._button1.Text = "Show"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Black
		self._button2.Location = System.Drawing.Point(383, 151)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(261, 71)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Black
		self._button3.Location = System.Drawing.Point(80, 234)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(564, 71)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Blue
		self.ClientSize = System.Drawing.Size(718, 317)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.ForeColor = System.Drawing.Color.White
		self.Name = "MainForm"
		self.Text = "HelloWorld3"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		"""Show Button"""
		self._label1.Text = "Hello, World"
		pass

	def Button2Click(self, sender, e):
		"""Clear Button"""
		self._label1.Text = ""
		pass

	def Button3Click(self, sender, e):
		"""Exit Button"""
		Application.Exit()
		pass