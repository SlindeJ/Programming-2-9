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
		self._label1.BackColor = System.Drawing.SystemColors.HighlightText
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 24)
		self._label1.ForeColor = System.Drawing.Color.Blue
		self._label1.Location = System.Drawing.Point(358, 19)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(315, 73)
		self._label1.TabIndex = 0
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Cyan
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 24)
		self._button1.ForeColor = System.Drawing.Color.DarkBlue
		self._button1.Location = System.Drawing.Point(43, 139)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(297, 69)
		self._button1.TabIndex = 1
		self._button1.Text = "Show"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Cyan
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 24)
		self._button2.ForeColor = System.Drawing.Color.DarkBlue
		self._button2.Location = System.Drawing.Point(381, 139)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(292, 69)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Indigo
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 20)
		self._button3.ForeColor = System.Drawing.Color.Gold
		self._button3.Location = System.Drawing.Point(43, 234)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(630, 69)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.HighlightText
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 26)
		self._label2.ForeColor = System.Drawing.Color.Green
		self._label2.Location = System.Drawing.Point(43, 19)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(316, 73)
		self._label2.TabIndex = 4
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DarkRed
		self.ClientSize = System.Drawing.Size(714, 315)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "CraigRules"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		self._label1.Text = "Cougars!"
		self._label2.Text = "Go"
		pass

	def Button2Click(self, sender, e):
		self._label1.Text = ""
		self._label2.Text = ""
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass