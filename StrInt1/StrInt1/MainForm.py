import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label3 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.White
		self._label3.Location = System.Drawing.Point(12, 28)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(216, 125)
		self._label3.TabIndex = 2
		self._label3.TextAlign = System.Drawing.ContentAlignment.TopCenter
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(68, 5)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 3
		self._textBox1.TextChanged += self.TextBox1TextChanged
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Black
		self._button1.ForeColor = System.Drawing.Color.FromArgb(0, 192, 0)
		self._button1.Location = System.Drawing.Point(12, 165)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 4
		self._button1.Text = "Formulate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Black
		self._button2.ForeColor = System.Drawing.Color.White
		self._button2.Location = System.Drawing.Point(152, 165)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 5
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.DarkOrchid
		self._button3.Font = System.Drawing.Font("Javanese Text", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.White
		self._button3.Location = System.Drawing.Point(84, 188)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 29)
		self._button3.TabIndex = 6
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DarkTurquoise
		self.ClientSize = System.Drawing.Size(239, 221)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label3)
		self.Name = "MainForm"
		self.Text = "StrInt1"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)
		self.PerformLayout()





	def Button3Click(self, sender, e):
		Application.Exit()
		pass

	def Button2Click(self, sender, e):
		self._label3.Text = ""
		self._textBox1.Text = ""
		pass

	def Button1Click(self, sender, e):
		self._label3.Text = ""
		myStr = self._textBox1.Text
		for lcv in range(len(myStr)):
			for lcv2 in range(lcv + 1, len(myStr)):
				letter1 = myStr[lcv]
				letter2 = myStr[lcv2]
				if letter1 == letter2:
					self._label3.Text += letter2 + " "
		pass

	def TextBox1TextChanged(self, sender, e):
		pass

	def MainFormLoad(self, sender, e):
		pass