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
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Olive
		self._label1.ForeColor = System.Drawing.Color.SpringGreen
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(169, 40)
		self._label1.TabIndex = 0
		self._label1.Text = "Radius"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.SystemColors.Window
		self._textBox1.Location = System.Drawing.Point(200, 21)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 1
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.DarkGreen
		self._label2.Font = System.Drawing.Font("Yu Gothic", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 164)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(209, 57)
		self._label2.TabIndex = 2
		self._label2.Text = "Area"
		self._label2.TextAlign = System.Drawing.ContentAlignment.BottomCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.DarkGreen
		self._label3.Font = System.Drawing.Font("Yu Gothic", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(269, 164)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(209, 57)
		self._label3.TabIndex = 3
		self._label3.Text = "Circumference"
		self._label3.TextAlign = System.Drawing.ContentAlignment.BottomCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.LightPink
		self._label4.Font = System.Drawing.Font("Arial", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(12, 249)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(209, 57)
		self._label4.TabIndex = 4
		self._label4.TextAlign = System.Drawing.ContentAlignment.TopCenter
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.LightPink
		self._label5.Font = System.Drawing.Font("Arial", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(269, 249)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(209, 57)
		self._label5.TabIndex = 5
		self._label5.TextAlign = System.Drawing.ContentAlignment.TopCenter
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Red
		self._button1.Font = System.Drawing.Font("OCR A Extended", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.LightSeaGreen
		self._button1.Location = System.Drawing.Point(12, 65)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(466, 96)
		self._button1.TabIndex = 6
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.LightYellow
		self._button2.Font = System.Drawing.Font("Ink Free", 15.749999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.DarkMagenta
		self._button2.Location = System.Drawing.Point(485, 9)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(219, 139)
		self._button2.TabIndex = 7
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.GreenYellow
		self._button3.Font = System.Drawing.Font("Microsoft Uighur", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.DeepPink
		self._button3.Location = System.Drawing.Point(485, 164)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(219, 139)
		self._button3.TabIndex = 9
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.LightCyan
		self.ClientSize = System.Drawing.Size(716, 315)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Lang54c2"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		Pi = 3.14159
		Radius = float(self._textBox1.Text)
		Area = float(Pi * Radius**2)
		Area = round(Area, 3)
		Circumference = float(2 * Pi * Radius)
		Circumference = round(Circumference, 3)
		self._label4.Text = str(Area)
		self._label5.Text = str(Circumference)
		pass

	def Button2Click(self, sender, e):
		self._label4.Text = ""
		self._label5.Text = ""
		self._textBox1.Text = ""
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass