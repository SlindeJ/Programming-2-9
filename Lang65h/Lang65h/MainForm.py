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
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.DarkOliveGreen
		self._button1.Font = System.Drawing.Font("OCR A Extended", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.Pink
		self._button1.Location = System.Drawing.Point(12, 134)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(151, 81)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.MediumSlateBlue
		self._button2.Font = System.Drawing.Font("OCR A Extended", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.Gold
		self._button2.Location = System.Drawing.Point(173, 134)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(151, 81)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Coral
		self._button3.Font = System.Drawing.Font("Papyrus", 21.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(12, 218)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(312, 82)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Indigo
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.Orange
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 3
		self._label1.Text = "Pound:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Indigo
		self._label2.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.Orange
		self._label2.Location = System.Drawing.Point(118, 9)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 4
		self._label2.Text = "Shilling:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Indigo
		self._label3.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.Orange
		self._label3.Location = System.Drawing.Point(224, 9)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 5
		self._label3.Text = "Pence:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Crimson
		self._label4.Font = System.Drawing.Font("Microsoft Uighur", 17.75)
		self._label4.ForeColor = System.Drawing.Color.DarkTurquoise
		self._label4.Location = System.Drawing.Point(12, 58)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(312, 32)
		self._label4.TabIndex = 6
		self._label4.Text = "Current Pound/Pence Value:"
		self._label4.TextAlign = System.Drawing.ContentAlignment.BottomCenter
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.MidnightBlue
		self._label5.Font = System.Drawing.Font("Microsoft YaHei", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ForeColor = System.Drawing.Color.OldLace
		self._label5.Location = System.Drawing.Point(12, 100)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(312, 31)
		self._label5.TabIndex = 7
		self._label5.Text = "label5"
		self._label5.TextAlign = System.Drawing.ContentAlignment.TopCenter
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(12, 35)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 8
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(118, 35)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 9
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(224, 35)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 20)
		self._textBox3.TabIndex = 10
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.SteelBlue
		self.ClientSize = System.Drawing.Size(337, 312)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Lang65h"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		pound = float(self._textBox1.Text)
		pound = round(pound, 3)
		shilling = float(self._textBox2.Text) / 20
		shilling = round(shilling, 2)
		penence = float(self._textBox3.Text) / 12 / 20
		penence = round(penence, 2)
		newtotal = float(pound + shilling + penence)
		self._label5.Text = str(newtotal)
		pass

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""
		self._label5.Text = ""
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass

	def MainFormLoad(self, sender, e):
		pass