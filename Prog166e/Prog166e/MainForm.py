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
		self._listBox1.BackColor = System.Drawing.Color.PaleVioletRed
		self._listBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._listBox1.ForeColor = System.Drawing.Color.WhiteSmoke
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 20
		self._listBox1.Location = System.Drawing.Point(12, 12)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(308, 184)
		self._listBox1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Beige
		self._button1.Font = System.Drawing.Font("OCR A Extended", 27.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 204)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(308, 54)
		self._button1.TabIndex = 1
		self._button1.Text = "Show"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.OrangeRed
		self._button2.Font = System.Drawing.Font("Papyrus", 27.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(12, 264)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(214, 76)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Gold
		self._button3.Font = System.Drawing.Font("Times New Roman", 21.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(232, 264)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(88, 76)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.RosyBrown
		self.ClientSize = System.Drawing.Size(332, 352)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "Prog166e"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		self._listBox1.Items.Clear()
		num = 1
		den = 2
		while den <= 15:
			while num < den:
				frac = float(num)/float(den)
				self._listBox1.Items.Add(str(num) + "/" + str(den) + " = " + str(round(frac, 5)))
				num += 1
			num = 1
			den += 1
		pass
	
	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()
		pass
	
	def Button3Click(self, sender, e):
		Application.Exit()
		pass

