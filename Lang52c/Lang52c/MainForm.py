import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(41, 13)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Radius"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(41, 40)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 1
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(12, 114)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(271, 60)
		self._button1.TabIndex = 2
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(12, 180)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(271, 60)
		self._button2.TabIndex = 3
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(12, 246)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(271, 60)
		self._button3.TabIndex = 4
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.ControlDark
		self._label2.Location = System.Drawing.Point(468, 71)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 5
		self._label2.Text = "Area"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.ControlDark
		self._label3.Location = System.Drawing.Point(575, 71)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 6
		self._label3.Text = "Circumference"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.ControlDarkDark
		self._label4.Location = System.Drawing.Point(468, 98)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 7
		self._label4.Text = "label4"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.SystemColors.ControlDarkDark
		self._label5.Location = System.Drawing.Point(575, 98)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 8
		self._label5.Text = "label5"
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(747, 318)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Lang52c"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		Pi = 3.14159
		Radius = float(self._textBox1.Text)
		Area = Pi * Radius**2
		Round(area, 3)
		Circumference = 2 * Pi * Radius
		Round(Circumference, 3)
		self._label4.Text = str(Area)
		self._label5.Text = str(Circumference)
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass

	def Button2Click(self, sender, e):
		self._label4.Text = ""
		self._label5.Text = ""
		pass