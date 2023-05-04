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
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Black
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.White
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(465, 29)
		self._label1.TabIndex = 0
		self._label1.Text = "Please Enter A Number You Dislike:"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(368, 12)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 1
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.DarkMagenta
		self._button1.Font = System.Drawing.Font("Papyrus", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.White
		self._button1.Location = System.Drawing.Point(12, 227)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(144, 31)
		self._button1.TabIndex = 2
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.HotPink
		self._button2.Font = System.Drawing.Font("Papyrus", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(174, 227)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(144, 31)
		self._button2.TabIndex = 3
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Fuchsia
		self._button3.Font = System.Drawing.Font("Papyrus", 12, System.Drawing.FontStyle.Bold)
		self._button3.ForeColor = System.Drawing.Color.DarkGray
		self._button3.Location = System.Drawing.Point(333, 227)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(144, 31)
		self._button3.TabIndex = 4
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.RoyalBlue
		self._label2.Font = System.Drawing.Font("OCR A Extended", 54, System.Drawing.FontStyle.Bold)
		self._label2.Location = System.Drawing.Point(12, 48)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(465, 176)
		self._label2.TabIndex = 5
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Crimson
		self.ClientSize = System.Drawing.Size(489, 270)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Lang76a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		if 1 <= int(self._textBox1.Text) <= 9:
			dislike = int(self._textBox1.Text)
			dislike = dislike * 9
			dislike = dislike * 12345679
			self._label2.Text = str(dislike)
		else:
			self._label2.Text = "no"
		pass

	def Button2Click(self, sender, e):
		self._label2.Text = ""
		self._textBox1.Text = ""
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass