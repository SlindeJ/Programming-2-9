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
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._groupBox2 = System.Windows.Forms.GroupBox()
		self._groupBox3 = System.Windows.Forms.GroupBox()
		self._groupBox4 = System.Windows.Forms.GroupBox()
		self._radioButton1 = System.Windows.Forms.RadioButton()
		self._radioButton2 = System.Windows.Forms.RadioButton()
		self._radioButton3 = System.Windows.Forms.RadioButton()
		self._radioButton4 = System.Windows.Forms.RadioButton()
		self._checkBox1 = System.Windows.Forms.CheckBox()
		self._checkBox2 = System.Windows.Forms.CheckBox()
		self._checkBox3 = System.Windows.Forms.CheckBox()
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._groupBox1.SuspendLayout()
		self._groupBox2.SuspendLayout()
		self._groupBox3.SuspendLayout()
		self._groupBox4.SuspendLayout()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(23, 280)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(200, 67)
		self._button1.TabIndex = 0
		self._button1.Text = "button1"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(252, 280)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(127, 67)
		self._button2.TabIndex = 1
		self._button2.Text = "button2"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(393, 280)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(127, 67)
		self._button3.TabIndex = 2
		self._button3.Text = "button3"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._radioButton4)
		self._groupBox1.Controls.Add(self._radioButton3)
		self._groupBox1.Controls.Add(self._radioButton2)
		self._groupBox1.Controls.Add(self._radioButton1)
		self._groupBox1.Location = System.Drawing.Point(23, 15)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(130, 151)
		self._groupBox1.TabIndex = 3
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Type of Membership"
		# 
		# groupBox2
		# 
		self._groupBox2.Controls.Add(self._textBox1)
		self._groupBox2.Controls.Add(self._label1)
		self._groupBox2.Location = System.Drawing.Point(23, 182)
		self._groupBox2.Name = "groupBox2"
		self._groupBox2.Size = System.Drawing.Size(200, 92)
		self._groupBox2.TabIndex = 4
		self._groupBox2.TabStop = False
		self._groupBox2.Text = "Membership Length"
		# 
		# groupBox3
		# 
		self._groupBox3.Controls.Add(self._checkBox3)
		self._groupBox3.Controls.Add(self._checkBox2)
		self._groupBox3.Controls.Add(self._checkBox1)
		self._groupBox3.Location = System.Drawing.Point(305, 15)
		self._groupBox3.Name = "groupBox3"
		self._groupBox3.Size = System.Drawing.Size(164, 143)
		self._groupBox3.TabIndex = 5
		self._groupBox3.TabStop = False
		self._groupBox3.Text = "Options"
		# 
		# groupBox4
		# 
		self._groupBox4.Controls.Add(self._textBox3)
		self._groupBox4.Controls.Add(self._textBox2)
		self._groupBox4.Controls.Add(self._label3)
		self._groupBox4.Controls.Add(self._label2)
		self._groupBox4.Location = System.Drawing.Point(252, 174)
		self._groupBox4.Name = "groupBox4"
		self._groupBox4.Size = System.Drawing.Size(268, 100)
		self._groupBox4.TabIndex = 6
		self._groupBox4.TabStop = False
		self._groupBox4.Text = "Membership Fees"
		# 
		# radioButton1
		# 
		self._radioButton1.BackColor = System.Drawing.SystemColors.ControlDark
		self._radioButton1.Location = System.Drawing.Point(11, 23)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(104, 24)
		self._radioButton1.TabIndex = 0
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "radioButton1"
		self._radioButton1.UseVisualStyleBackColor = False
		# 
		# radioButton2
		# 
		self._radioButton2.BackColor = System.Drawing.SystemColors.ControlDark
		self._radioButton2.Location = System.Drawing.Point(11, 53)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(104, 24)
		self._radioButton2.TabIndex = 1
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "radioButton2"
		self._radioButton2.UseVisualStyleBackColor = False
		# 
		# radioButton3
		# 
		self._radioButton3.BackColor = System.Drawing.SystemColors.ControlDark
		self._radioButton3.Location = System.Drawing.Point(11, 83)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(104, 24)
		self._radioButton3.TabIndex = 2
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "radioButton3"
		self._radioButton3.UseVisualStyleBackColor = False
		# 
		# radioButton4
		# 
		self._radioButton4.BackColor = System.Drawing.SystemColors.ControlDark
		self._radioButton4.Location = System.Drawing.Point(11, 113)
		self._radioButton4.Name = "radioButton4"
		self._radioButton4.Size = System.Drawing.Size(104, 24)
		self._radioButton4.TabIndex = 3
		self._radioButton4.TabStop = True
		self._radioButton4.Text = "radioButton4"
		self._radioButton4.UseVisualStyleBackColor = False
		# 
		# checkBox1
		# 
		self._checkBox1.BackColor = System.Drawing.SystemColors.ControlDark
		self._checkBox1.Location = System.Drawing.Point(6, 17)
		self._checkBox1.Name = "checkBox1"
		self._checkBox1.Size = System.Drawing.Size(152, 36)
		self._checkBox1.TabIndex = 0
		self._checkBox1.Text = "checkBox1"
		self._checkBox1.UseVisualStyleBackColor = False
		# 
		# checkBox2
		# 
		self._checkBox2.BackColor = System.Drawing.SystemColors.ControlDark
		self._checkBox2.Location = System.Drawing.Point(6, 59)
		self._checkBox2.Name = "checkBox2"
		self._checkBox2.Size = System.Drawing.Size(152, 36)
		self._checkBox2.TabIndex = 1
		self._checkBox2.Text = "checkBox2"
		self._checkBox2.UseVisualStyleBackColor = False
		# 
		# checkBox3
		# 
		self._checkBox3.BackColor = System.Drawing.SystemColors.ControlDark
		self._checkBox3.Location = System.Drawing.Point(6, 101)
		self._checkBox3.Name = "checkBox3"
		self._checkBox3.Size = System.Drawing.Size(152, 36)
		self._checkBox3.TabIndex = 2
		self._checkBox3.Text = "checkBox3"
		self._checkBox3.UseVisualStyleBackColor = False
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ControlDark
		self._label1.Location = System.Drawing.Point(11, 26)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(183, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "label1"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(11, 57)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(183, 20)
		self._textBox1.TabIndex = 1
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.ControlDark
		self._label2.Location = System.Drawing.Point(19, 30)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 0
		self._label2.Text = "label2"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.ControlDark
		self._label3.Location = System.Drawing.Point(18, 64)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 1
		self._label3.Text = "label3"
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(158, 30)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 2
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(158, 64)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 20)
		self._textBox3.TabIndex = 3
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(647, 359)
		self.Controls.Add(self._groupBox4)
		self.Controls.Add(self._groupBox3)
		self.Controls.Add(self._groupBox2)
		self.Controls.Add(self._groupBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "pg250MembershipFee"
		self._groupBox1.ResumeLayout(False)
		self._groupBox2.ResumeLayout(False)
		self._groupBox2.PerformLayout()
		self._groupBox3.ResumeLayout(False)
		self._groupBox4.ResumeLayout(False)
		self._groupBox4.PerformLayout()
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		pass

	def Button2Click(self, sender, e):
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass