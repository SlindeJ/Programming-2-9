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
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.MediumPurple
		self._button1.Font = System.Drawing.Font("OCR A Extended", 8.5)
		self._button1.Location = System.Drawing.Point(293, 14)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(79, 23)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.MediumPurple
		self._button2.Font = System.Drawing.Font("OCR A Extended", 8.5)
		self._button2.Location = System.Drawing.Point(334, 52)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(79, 23)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.MediumPurple
		self._button3.Font = System.Drawing.Font("OCR A Extended", 8.5)
		self._button3.Location = System.Drawing.Point(312, 99)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(79, 23)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.DarkSeaGreen
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 12)
		self._label1.Location = System.Drawing.Point(22, 29)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 3
		self._label1.Text = "Speed Limit:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.TopRight
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.DarkSalmon
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 12)
		self._label2.Location = System.Drawing.Point(22, 79)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 4
		self._label2.Text = "Car Speed:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.TopRight
		self._label2.Click += self.Label2Click
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(162, 29)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 5
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(162, 77)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 6
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.LightBlue
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 12)
		self._label3.Location = System.Drawing.Point(22, 134)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 7
		self._label3.Text = "Fine Cost:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.TopRight
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.DarkRed
		self._label4.Font = System.Drawing.Font("Symbol", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 2)
		self._label4.Location = System.Drawing.Point(162, 134)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 8
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.MediumOrchid
		self.ClientSize = System.Drawing.Size(423, 185)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Lang82a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Label2Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		spdlimit = float(self._textBox1.Text)
		spdcar = float(self._textBox2.Text)
		spdover = float(spdcar - spdlimit) * 5.00
		spdover = round(spdover, 3)
		total = float(20.00 + spdover)
		total = round(total, 3)
		self._label4.Text = str(total)
		pass

	def Button2Click(self, sender, e):
		self._label4.Text = ""
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass