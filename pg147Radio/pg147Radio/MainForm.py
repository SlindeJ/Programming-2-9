import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._radioButton1 = System.Windows.Forms.RadioButton()
		self._radioButton2 = System.Windows.Forms.RadioButton()
		self._radioButton3 = System.Windows.Forms.RadioButton()
		self._checkBox1 = System.Windows.Forms.CheckBox()
		self._checkBox2 = System.Windows.Forms.CheckBox()
		self._checkBox3 = System.Windows.Forms.CheckBox()
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._groupBox2 = System.Windows.Forms.GroupBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._groupBox1.SuspendLayout()
		self._groupBox2.SuspendLayout()
		self.SuspendLayout()
		# 
		# radioButton1
		# 
		self._radioButton1.BackColor = System.Drawing.Color.Red
		self._radioButton1.Location = System.Drawing.Point(6, 19)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(104, 24)
		self._radioButton1.TabIndex = 0
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "Button1"
		self._radioButton1.UseVisualStyleBackColor = False
		# 
		# radioButton2
		# 
		self._radioButton2.BackColor = System.Drawing.Color.FromArgb(255, 128, 0)
		self._radioButton2.Location = System.Drawing.Point(6, 56)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(104, 24)
		self._radioButton2.TabIndex = 1
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "Button2"
		self._radioButton2.UseVisualStyleBackColor = False
		# 
		# radioButton3
		# 
		self._radioButton3.BackColor = System.Drawing.Color.Yellow
		self._radioButton3.Location = System.Drawing.Point(6, 93)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(104, 24)
		self._radioButton3.TabIndex = 2
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "Button3"
		self._radioButton3.UseVisualStyleBackColor = False
		# 
		# checkBox1
		# 
		self._checkBox1.BackColor = System.Drawing.Color.Lime
		self._checkBox1.Location = System.Drawing.Point(7, 19)
		self._checkBox1.Name = "checkBox1"
		self._checkBox1.Size = System.Drawing.Size(104, 24)
		self._checkBox1.TabIndex = 3
		self._checkBox1.Text = "Box4"
		self._checkBox1.UseVisualStyleBackColor = False
		# 
		# checkBox2
		# 
		self._checkBox2.BackColor = System.Drawing.Color.Cyan
		self._checkBox2.Location = System.Drawing.Point(7, 55)
		self._checkBox2.Name = "checkBox2"
		self._checkBox2.Size = System.Drawing.Size(104, 24)
		self._checkBox2.TabIndex = 4
		self._checkBox2.Text = "Box5"
		self._checkBox2.UseVisualStyleBackColor = False
		# 
		# checkBox3
		# 
		self._checkBox3.BackColor = System.Drawing.Color.Fuchsia
		self._checkBox3.Location = System.Drawing.Point(7, 92)
		self._checkBox3.Name = "checkBox3"
		self._checkBox3.Size = System.Drawing.Size(104, 24)
		self._checkBox3.TabIndex = 5
		self._checkBox3.Text = "Box6"
		self._checkBox3.UseVisualStyleBackColor = False
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._radioButton3)
		self._groupBox1.Controls.Add(self._radioButton2)
		self._groupBox1.Controls.Add(self._radioButton1)
		self._groupBox1.Font = System.Drawing.Font("Gill Sans MT", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox1.Location = System.Drawing.Point(12, 12)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(117, 126)
		self._groupBox1.TabIndex = 6
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Radio Buttons"
		# 
		# groupBox2
		# 
		self._groupBox2.Controls.Add(self._checkBox3)
		self._groupBox2.Controls.Add(self._checkBox2)
		self._groupBox2.Controls.Add(self._checkBox1)
		self._groupBox2.Font = System.Drawing.Font("OCR A Extended", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox2.Location = System.Drawing.Point(175, 12)
		self._groupBox2.Name = "groupBox2"
		self._groupBox2.Size = System.Drawing.Size(117, 126)
		self._groupBox2.TabIndex = 7
		self._groupBox2.TabStop = False
		self._groupBox2.Text = "Check Boxes"
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.RoyalBlue
		self._button1.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 144)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(117, 23)
		self._button1.TabIndex = 8
		self._button1.Text = "Ok"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Crimson
		self._button2.Font = System.Drawing.Font("OCR A Extended", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(175, 144)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(117, 23)
		self._button2.TabIndex = 9
		self._button2.Text = "Exit"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Orchid
		self.ClientSize = System.Drawing.Size(304, 173)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._groupBox2)
		self.Controls.Add(self._groupBox1)
		self.Name = "MainForm"
		self.Text = "pg147Radio"
		self._groupBox1.ResumeLayout(False)
		self._groupBox2.ResumeLayout(False)
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		if self._radioButton1.Checked == True:
			strMessage = "You selected Button 1"
		elif self._radioButton2.Checked == True:
			strMessage = "You selected Button 2"
		elif self._radioButton3.Checked == True:
			strMessage = "You selected Button 3"
		
		if self._checkBox1.Checked == True:
			strMessage += " and Box 4"
		if self._checkBox2.Checked == True:
			strMessage += " and Box 5"
		if self._checkBox3.Checked == True:
			strMessage += " and Box 6"
		MessageBox.Show(strMessage)
		pass

	def Button2Click(self, sender, e):
		Application.Exit()
		pass