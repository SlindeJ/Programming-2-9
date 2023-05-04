import math
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Black
		self._label1.ForeColor = System.Drawing.Color.Cornsilk
		self._label1.Location = System.Drawing.Point(12, 12)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Enter A:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Black
		self._label2.ForeColor = System.Drawing.Color.Cornsilk
		self._label2.Location = System.Drawing.Point(12, 35)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 1
		self._label2.Text = "Enter B:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Black
		self._label3.ForeColor = System.Drawing.Color.Cornsilk
		self._label3.Location = System.Drawing.Point(12, 54)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 2
		self._label3.Text = "Enter C:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(118, 12)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 3
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(118, 36)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 4
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(118, 59)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 20)
		self._textBox3.TabIndex = 5
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.BlueViolet
		self._button1.Font = System.Drawing.Font("Microsoft YaHei", 22.25)
		self._button1.Location = System.Drawing.Point(12, 108)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(206, 84)
		self._button1.TabIndex = 6
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Beige
		self._button2.Font = System.Drawing.Font("Microsoft YaHei", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(40, 198)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(158, 82)
		self._button2.TabIndex = 7
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Cyan
		self._button3.Font = System.Drawing.Font("OCR A Extended", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(527, 12)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(158, 291)
		self._button3.TabIndex = 8
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Maroon
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.Silver
		self._label4.Location = System.Drawing.Point(279, 192)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(206, 88)
		self._label4.TabIndex = 9
		self._label4.TextAlign = System.Drawing.ContentAlignment.TopCenter
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Maroon
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ForeColor = System.Drawing.Color.Silver
		self._label5.Location = System.Drawing.Point(279, 95)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(206, 82)
		self._label5.TabIndex = 10
		self._label5.TextAlign = System.Drawing.ContentAlignment.TopCenter
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.BurlyWood
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(279, 12)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(206, 65)
		self._label6.TabIndex = 11
		self._label6.Text = "Square Roots:"
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.BlueViolet
		self._label7.ForeColor = System.Drawing.Color.Cornsilk
		self._label7.Location = System.Drawing.Point(279, 77)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(206, 18)
		self._label7.TabIndex = 12
		self._label7.Text = "Negative Root:"
		self._label7.TextAlign = System.Drawing.ContentAlignment.BottomCenter
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.BlueViolet
		self._label8.ForeColor = System.Drawing.Color.Cornsilk
		self._label8.Location = System.Drawing.Point(279, 177)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(206, 15)
		self._label8.TabIndex = 13
		self._label8.Text = "Positive Root:"
		self._label8.TextAlign = System.Drawing.ContentAlignment.BottomCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Blue
		self.ClientSize = System.Drawing.Size(697, 315)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Prog58b"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		A = float(self._textBox1.Text)
		B = float(self._textBox2.Text)
		C = float(self._textBox3.Text)
		Proot = float(( -B + math.sqrt(B ** 2 - 4 * A * C)) / 2 * A)
		round(Proot, 3)
		Nroot = float(( -B - math.sqrt(B ** 2 - 4 * A * C)) / 2 * A)
		round(Nroot, 3)
		self._label4.Text = str(Proot)
		self._label5.Text = str(Nroot)
		pass

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""
		self._label4.Text = ""
		self._label5.Text = ""
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass

	def MainFormLoad(self, sender, e):
		pass