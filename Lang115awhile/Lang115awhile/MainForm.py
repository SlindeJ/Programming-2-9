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
		self.SuspendLayout()
		# 
		# listBox1
		# 
		self._listBox1.BackColor = System.Drawing.Color.MediumSpringGreen
		self._listBox1.FormattingEnabled = True
		self._listBox1.Location = System.Drawing.Point(24, 15)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(120, 212)
		self._listBox1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.LightBlue
		self._button1.Font = System.Drawing.Font("Maiandra GD", 9, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.HotPink
		self._button1.Location = System.Drawing.Point(24, 242)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(120, 23)
		self._button1.TabIndex = 1
		self._button1.Text = "Show"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Green
		self._button2.Font = System.Drawing.Font("Microsoft YaHei", 9, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.FromArgb(255, 128, 0)
		self._button2.Location = System.Drawing.Point(24, 280)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(120, 23)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Red
		self._button3.Font = System.Drawing.Font("OCR A Extended", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.White
		self._button3.Location = System.Drawing.Point(24, 318)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(120, 23)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.RoyalBlue
		self.ClientSize = System.Drawing.Size(167, 347)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "Lang115awhile"
		self.ResumeLayout(False)



	def Button1Click(self, sender, e):
		self._listBox1.Items.Clear()
		lcv = 2
		while lcv <= 36:
			self._listBox1.Items.Add(str(lcv))
			lcv += 2
		pass

	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass