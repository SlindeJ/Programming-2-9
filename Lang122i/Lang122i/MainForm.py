import math
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._listBox1 = System.Windows.Forms.ListBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# listBox1
		# 
		self._listBox1.BackColor = System.Drawing.Color.Black
		self._listBox1.ForeColor = System.Drawing.Color.White
		self._listBox1.FormattingEnabled = True
		self._listBox1.Location = System.Drawing.Point(12, 25)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(335, 277)
		self._listBox1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Maroon
		self._button1.Font = System.Drawing.Font("Perpetua Titling MT", 14)
		self._button1.ForeColor = System.Drawing.Color.White
		self._button1.Location = System.Drawing.Point(353, 12)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(132, 93)
		self._button1.TabIndex = 1
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Red
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 22)
		self._button2.ForeColor = System.Drawing.Color.White
		self._button2.Location = System.Drawing.Point(353, 111)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(132, 92)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Firebrick
		self._button3.Font = System.Drawing.Font("OCR A Extended", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.White
		self._button3.Location = System.Drawing.Point(353, 209)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(132, 93)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Aquamarine
		self._label1.Font = System.Drawing.Font("OCR A Extended", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 3)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(92, 19)
		self._label1.TabIndex = 4
		self._label1.Text = "Number:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.MediumSpringGreen
		self._label2.Font = System.Drawing.Font("OCR A Extended", 11)
		self._label2.Location = System.Drawing.Point(110, 3)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 19)
		self._label2.TabIndex = 5
		self._label2.Text = "Cube Root:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.SpringGreen
		self._label3.Font = System.Drawing.Font("OCR A Extended", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(216, 3)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(131, 19)
		self._label3.TabIndex = 6
		self._label3.Text = "Cubed:"
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.CadetBlue
		self.ClientSize = System.Drawing.Size(497, 307)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "Lang122i"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		for num in range(-25, 25 + 1):
			numcubert = math.sqrt(abs(num))
			numcubertt = math.sqrt(numcubert)
			numcubertt = round(numcubertt, 5)
			numcubed = num**3
			self._listBox1.Items.Add(str(num) + "\t\t" + str(numcubertt) + "\t\t" + str(numcubed))
		pass

	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass