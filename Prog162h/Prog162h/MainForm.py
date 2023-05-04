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
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Orange
		self._button1.Font = System.Drawing.Font("Lucida Fax", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(143, 206)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(100, 78)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Maroon
		self._button2.Font = System.Drawing.Font("Book Antiqua", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.LightSeaGreen
		self._button2.Location = System.Drawing.Point(12, 206)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(125, 36)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.DodgerBlue
		self._button3.Font = System.Drawing.Font("Book Antiqua", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.Navy
		self._button3.Location = System.Drawing.Point(12, 248)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(125, 39)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Red
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 3
		self._label1.Text = "Guests:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.Blue
		self._textBox1.Font = System.Drawing.Font("Tahoma", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.ForeColor = System.Drawing.Color.White
		self._textBox1.Location = System.Drawing.Point(143, 9)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 23)
		self._textBox1.TabIndex = 4
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.FromArgb(255, 128, 0)
		self._label2.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 60)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 5
		self._label2.Text = "Chairs:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.Cyan
		self._textBox2.Font = System.Drawing.Font("Tahoma", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(143, 60)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 23)
		self._textBox2.TabIndex = 6
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.DeepPink
		self._label3.ForeColor = System.Drawing.Color.White
		self._label3.Location = System.Drawing.Point(12, 111)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(231, 33)
		self._label3.TabIndex = 7
		self._label3.TextAlign = System.Drawing.ContentAlignment.TopCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.DarkViolet
		self._label4.ForeColor = System.Drawing.Color.White
		self._label4.Location = System.Drawing.Point(12, 161)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(231, 33)
		self._label4.TabIndex = 8
		self._label4.TextAlign = System.Drawing.ContentAlignment.TopCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Black
		self.ClientSize = System.Drawing.Size(261, 296)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Prog162h"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		guests = int(self._textBox1.Text)
		chairs = int(self._textBox2.Text)
		n = 1
		difference = 1
		for num in range(1, guests + 1, 1):
			n = n * num
		for num2 in range(1, (guests - chairs) + 1, 1):
			difference = difference * num2
		permutations = n / difference
		standing = guests - chairs
		if standing < 0:
			standing = "No Guests Left Standing"
		self._label3.Text = "Permutations: " + str(permutations)
		self._label4.Text = "Guests standing: " + str(standing)
		pass

	def Button2Click(self, sender, e):
		self._label3.Text = ""
		self._label4.Text = ""
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass