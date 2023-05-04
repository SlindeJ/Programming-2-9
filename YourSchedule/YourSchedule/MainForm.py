import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label2 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.CadetBlue
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.Cornsilk
		self._label1.Location = System.Drawing.Point(13, 13)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(214, 291)
		self._label1.TabIndex = 0
		self._label1.TextAlign = System.Drawing.ContentAlignment.TopCenter
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Green
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(480, 13)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(228, 65)
		self._button1.TabIndex = 1
		self._button1.Text = "Show"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Yellow
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(480, 120)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(228, 65)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Red
		self._button3.Font = System.Drawing.Font("MS Gothic", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(480, 236)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(228, 65)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.CadetBlue
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 9)
		self._label2.ForeColor = System.Drawing.Color.Cornsilk
		self._label2.Location = System.Drawing.Point(225, 13)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(249, 291)
		self._label2.TabIndex = 4
		self._label2.TextAlign = System.Drawing.ContentAlignment.TopCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Blue
		self.ClientSize = System.Drawing.Size(720, 313)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "YourSchedule"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		self._label1.Text = "\n1st hour is English 11 Honors\n\n\n\n\n\n 2nd hour is TC Physics\n\n\n\n\n\n 3rd hour is Symphonic Band\n\n\n\n\n\n 4th hour is AP Chemistry"
		self._label2.Text = "\n5th hour is World Civilizations\n\n\n\n\n\n 6th hour is Precalculus Honors\n\n\n\n\n\n 7th hour isComputer Programming\n\n\n\n\n\n 8th hour Personal Finance"
		pass

	def Button2Click(self, sender, e):
		self._label1.Text = ""
		self._label2.Text = ""
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass