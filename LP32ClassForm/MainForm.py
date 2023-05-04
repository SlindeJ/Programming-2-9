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
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.FromArgb(255, 128, 0)
		self._label1.Font = System.Drawing.Font("OCR A Extended", 10.5)
		self._label1.ForeColor = System.Drawing.Color.Blue
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(371, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Enter the diameter of the pizza in inches:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Brown
		self._label2.Font = System.Drawing.Font("OCR A Extended", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.Lime
		self._label2.Location = System.Drawing.Point(12, 71)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(265, 18)
		self._label2.TabIndex = 1
		self._label2.Text = "The cost of making the pizza is: "
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.DarkSeaGreen
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.Magenta
		self._label3.Location = System.Drawing.Point(283, 71)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 44)
		self._label3.TabIndex = 2
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(136, 35)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(112, 20)
		self._textBox1.TabIndex = 3
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.PaleTurquoise
		self._button1.Font = System.Drawing.Font("Felix Titling", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 92)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(103, 23)
		self._button1.TabIndex = 4
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.DodgerBlue
		self._button2.Font = System.Drawing.Font("Felix Titling", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(121, 92)
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
		self._button3.Font = System.Drawing.Font("Felix Titling", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.White
		self._button3.Location = System.Drawing.Point(202, 92)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 6
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.CadetBlue
		self.ClientSize = System.Drawing.Size(395, 124)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "LP32ClassForm"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		inches = int(self._textBox1.Text)
		
		from pizza23 import *
		obj1 = pizza23(inches)
		obj1.calcmaterials()
		self._label3.Text = str(obj1.getcost())
		pass

	def Button2Click(self, sender, e):
		self._label3.Text = ""
		self._textBox1.Text = ""
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass