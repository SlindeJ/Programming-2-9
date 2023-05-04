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
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.BlueViolet
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 14)
		self._label1.ForeColor = System.Drawing.Color.Cornsilk
		self._label1.Location = System.Drawing.Point(133, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(236, 300)
		self._label1.TabIndex = 0
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label1.Click += self.Label1Click
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Crimson
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 18)
		self._button1.Location = System.Drawing.Point(375, 9)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(343, 90)
		self._button1.TabIndex = 1
		self._button1.Text = "Show"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.CornflowerBlue
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 10)
		self._button2.ForeColor = System.Drawing.Color.Crimson
		self._button2.Location = System.Drawing.Point(542, 105)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(23, 105)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.SystemColors.ControlText
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 18)
		self._button3.ForeColor = System.Drawing.Color.DarkOliveGreen
		self._button3.Location = System.Drawing.Point(375, 216)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(343, 90)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 12)
		self._label2.ForeColor = System.Drawing.Color.DarkCyan
		self._label2.Location = System.Drawing.Point(12, 9)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 43)
		self._label2.TabIndex = 4
		self._label2.Text = "Fuji Steakhouse"
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 12)
		self._label3.ForeColor = System.Drawing.Color.Cyan
		self._label3.Location = System.Drawing.Point(13, 67)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 43)
		self._label3.TabIndex = 5
		self._label3.Text = "Don't Call"
		# 
		# label4
		# 
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 12)
		self._label4.ForeColor = System.Drawing.Color.DarkGreen
		self._label4.Location = System.Drawing.Point(12, 127)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 43)
		self._label4.TabIndex = 6
		self._label4.Text = "Don't Call"
		# 
		# label5
		# 
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 12)
		self._label5.ForeColor = System.Drawing.Color.Chartreuse
		self._label5.Location = System.Drawing.Point(13, 194)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 43)
		self._label5.TabIndex = 7
		self._label5.Text = "Don't Call"
		# 
		# label6
		# 
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 12)
		self._label6.ForeColor = System.Drawing.Color.OrangeRed
		self._label6.Location = System.Drawing.Point(13, 266)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 43)
		self._label6.TabIndex = 8
		self._label6.Text = "Don't Call"
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Coral
		self.ClientSize = System.Drawing.Size(730, 318)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "PhoneNumbers"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)


	def Label1Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		self._label1.Text = " (608) 754-3388\n\n\n (608) 832-9384\n\n\n (608) 927-9912\n\n\n (608) 837-2871\n\n\n (608) 121-9015"
		pass

	def Button2Click(self, sender, e):
		self._label1.Text = ""
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass

	def MainFormLoad(self, sender, e):
		pass