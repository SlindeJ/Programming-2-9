﻿import System.Drawing
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
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Thistle
		self._button1.Font = System.Drawing.Font("OCR A Extended", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(87, 155)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(86, 46)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Maroon
		self._button2.Font = System.Drawing.Font("OCR A Extended", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.SteelBlue
		self._button2.Location = System.Drawing.Point(87, 207)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(86, 46)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
		self._button3.Font = System.Drawing.Font("OCR A Extended", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(87, 259)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(86, 46)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.FromArgb(255, 255, 128)
		self._label1.Font = System.Drawing.Font("Microsoft Tai Le", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.Red
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(125, 23)
		self._label1.TabIndex = 3
		self._label1.Text = "Radius of the circle is: "
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(143, 9)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 22)
		self._textBox1.TabIndex = 4
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Teal
		self._label2.Font = System.Drawing.Font("Georgia", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(14, 54)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 33)
		self._label2.TabIndex = 5
		self._label2.Text = "Area of the circle is: "
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.FromArgb(0, 192, 0)
		self._label3.Font = System.Drawing.Font("Georgia", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(14, 115)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 33)
		self._label3.TabIndex = 6
		self._label3.Text = "Circumference of the circle is: "
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.FromArgb(192, 0, 192)
		self._label4.Font = System.Drawing.Font("Georgia", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(143, 54)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 33)
		self._label4.TabIndex = 7
		self._label4.TextAlign = System.Drawing.ContentAlignment.TopCenter
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.FromArgb(255, 128, 0)
		self._label5.Font = System.Drawing.Font("Georgia", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(143, 115)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 33)
		self._label5.TabIndex = 8
		self._label5.TextAlign = System.Drawing.ContentAlignment.TopCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(128, 255, 255)
		self.ClientSize = System.Drawing.Size(261, 317)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "prog54cfunctions"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		pi = float(3.14159)
		radius = float(self._textBox1.Text)
		cir = 2 * pi * radius
		area = pi * radius ** 2
		self._label4.Text = str(round(area, 3))
		self._label5.Text = str(round(cir, 3))
		pass

	def Button2Click(self, sender, e):
		self._label4.Text = ""
		self._label5.Text = ""
		self._textBox1.Text = ""
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass