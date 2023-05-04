import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label3 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label1 = System.Windows.Forms.Label()
		self._button3 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button1 = System.Windows.Forms.Button()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label4 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(12, 49)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(175, 38)
		self._textBox1.TabIndex = 13
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Black
		self._label3.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.White
		self._label3.Location = System.Drawing.Point(177, 139)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(174, 64)
		self._label3.TabIndex = 12
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 127)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(159, 40)
		self._label2.TabIndex = 11
		self._label2.Text = "Anagram:"
		self._label2.Click += self.Label2Click
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(175, 37)
		self._label1.TabIndex = 10
		self._label1.Text = "Enter Word:"
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.DarkSlateBlue
		self._button3.Font = System.Drawing.Font("OCR A Extended", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.Silver
		self._button3.Location = System.Drawing.Point(247, 256)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(115, 37)
		self._button3.TabIndex = 9
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Red
		self._button2.Font = System.Drawing.Font("Microsoft Tai Le", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.Blue
		self._button2.Location = System.Drawing.Point(135, 225)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(115, 37)
		self._button2.TabIndex = 8
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.DarkGreen
		self._button1.Font = System.Drawing.Font("SimSun", 20.25, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.Fuchsia
		self._button1.Location = System.Drawing.Point(22, 194)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(115, 37)
		self._button1.TabIndex = 7
		self._button1.Text = "Show"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(193, 69)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(187, 38)
		self._textBox2.TabIndex = 15
		# 
		# label4
		# 
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(193, 27)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(187, 39)
		self._label4.TabIndex = 14
		self._label4.Text = "Enter Word 2:"
		self._label4.Click += self.Label4Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(128, 255, 255)
		self.ClientSize = System.Drawing.Size(392, 304)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "StrInt2"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		self._label3.Text = ""
		word = self._textBox1.Text
		anagram = self._textBox2.Text
		word = word.lower()
		anagram = anagram.lower()
		
		if len(word) != len(anagram):
			self._label3.Text = "False"
		else:
			for lcv in range(len(word)):
				c = word[lcv]
				index = anagram.index(c)
				
				if index != -1:
					anagram = anagram[0:index] + anagram[index+1:]
				else:
					self._label3.Text = "False"
		self._label3.Text = str(len(anagram) == 0)

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._label3.Text = ""
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass

	def Label2Click(self, sender, e):
		pass

	def Label4Click(self, sender, e):
		pass