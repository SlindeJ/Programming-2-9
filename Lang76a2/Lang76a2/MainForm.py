import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._radioButton1 = System.Windows.Forms.RadioButton()
		self._radioButton2 = System.Windows.Forms.RadioButton()
		self._radioButton3 = System.Windows.Forms.RadioButton()
		self._radioButton4 = System.Windows.Forms.RadioButton()
		self._radioButton5 = System.Windows.Forms.RadioButton()
		self._radioButton6 = System.Windows.Forms.RadioButton()
		self._radioButton7 = System.Windows.Forms.RadioButton()
		self._radioButton8 = System.Windows.Forms.RadioButton()
		self._radioButton9 = System.Windows.Forms.RadioButton()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.DarkOrange
		self._label1.Font = System.Drawing.Font("Papyrus", 15.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(336, 70)
		self._label1.TabIndex = 0
		self._label1.Text = "Choose A Number You Dislike:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.BottomCenter
		# 
		# radioButton1
		# 
		self._radioButton1.BackColor = System.Drawing.SystemColors.ControlDarkDark
		self._radioButton1.Location = System.Drawing.Point(12, 82)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(102, 58)
		self._radioButton1.TabIndex = 1
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "1"
		self._radioButton1.UseVisualStyleBackColor = False
		self._radioButton1.CheckedChanged += self.RadioButton1CheckedChanged
		# 
		# radioButton2
		# 
		self._radioButton2.BackColor = System.Drawing.SystemColors.ControlDarkDark
		self._radioButton2.Location = System.Drawing.Point(12, 146)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(102, 58)
		self._radioButton2.TabIndex = 2
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "2"
		self._radioButton2.UseVisualStyleBackColor = False
		self._radioButton2.CheckedChanged += self.RadioButton2CheckedChanged
		# 
		# radioButton3
		# 
		self._radioButton3.BackColor = System.Drawing.SystemColors.ControlDarkDark
		self._radioButton3.Location = System.Drawing.Point(13, 210)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(102, 58)
		self._radioButton3.TabIndex = 3
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "3"
		self._radioButton3.UseVisualStyleBackColor = False
		self._radioButton3.CheckedChanged += self.RadioButton3CheckedChanged
		# 
		# radioButton4
		# 
		self._radioButton4.BackColor = System.Drawing.SystemColors.ControlDarkDark
		self._radioButton4.Location = System.Drawing.Point(121, 82)
		self._radioButton4.Name = "radioButton4"
		self._radioButton4.Size = System.Drawing.Size(119, 58)
		self._radioButton4.TabIndex = 4
		self._radioButton4.TabStop = True
		self._radioButton4.Text = "4"
		self._radioButton4.UseVisualStyleBackColor = False
		self._radioButton4.CheckedChanged += self.RadioButton4CheckedChanged
		# 
		# radioButton5
		# 
		self._radioButton5.BackColor = System.Drawing.SystemColors.ControlDarkDark
		self._radioButton5.Location = System.Drawing.Point(121, 146)
		self._radioButton5.Name = "radioButton5"
		self._radioButton5.Size = System.Drawing.Size(119, 58)
		self._radioButton5.TabIndex = 5
		self._radioButton5.TabStop = True
		self._radioButton5.Text = "5"
		self._radioButton5.UseVisualStyleBackColor = False
		self._radioButton5.CheckedChanged += self.RadioButton5CheckedChanged
		# 
		# radioButton6
		# 
		self._radioButton6.BackColor = System.Drawing.SystemColors.ControlDarkDark
		self._radioButton6.Location = System.Drawing.Point(121, 210)
		self._radioButton6.Name = "radioButton6"
		self._radioButton6.Size = System.Drawing.Size(119, 58)
		self._radioButton6.TabIndex = 6
		self._radioButton6.TabStop = True
		self._radioButton6.Text = "6"
		self._radioButton6.UseVisualStyleBackColor = False
		self._radioButton6.CheckedChanged += self.RadioButton6CheckedChanged
		# 
		# radioButton7
		# 
		self._radioButton7.BackColor = System.Drawing.SystemColors.ControlDarkDark
		self._radioButton7.Location = System.Drawing.Point(246, 82)
		self._radioButton7.Name = "radioButton7"
		self._radioButton7.Size = System.Drawing.Size(102, 58)
		self._radioButton7.TabIndex = 7
		self._radioButton7.TabStop = True
		self._radioButton7.Text = "7"
		self._radioButton7.UseVisualStyleBackColor = False
		self._radioButton7.CheckedChanged += self.RadioButton7CheckedChanged
		# 
		# radioButton8
		# 
		self._radioButton8.BackColor = System.Drawing.SystemColors.ControlDarkDark
		self._radioButton8.Location = System.Drawing.Point(246, 146)
		self._radioButton8.Name = "radioButton8"
		self._radioButton8.Size = System.Drawing.Size(102, 58)
		self._radioButton8.TabIndex = 8
		self._radioButton8.TabStop = True
		self._radioButton8.Text = "8"
		self._radioButton8.UseVisualStyleBackColor = False
		self._radioButton8.CheckedChanged += self.RadioButton8CheckedChanged
		# 
		# radioButton9
		# 
		self._radioButton9.BackColor = System.Drawing.SystemColors.ControlDarkDark
		self._radioButton9.Location = System.Drawing.Point(246, 210)
		self._radioButton9.Name = "radioButton9"
		self._radioButton9.Size = System.Drawing.Size(102, 58)
		self._radioButton9.TabIndex = 9
		self._radioButton9.TabStop = True
		self._radioButton9.Text = "9"
		self._radioButton9.UseVisualStyleBackColor = False
		self._radioButton9.CheckedChanged += self.RadioButton9CheckedChanged
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Red
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(484, 42)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(171, 36)
		self._label2.TabIndex = 10
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.FromArgb(255, 128, 0)
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(484, 78)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(171, 36)
		self._label3.TabIndex = 11
		self._label3.Text = "X 9"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Black
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(484, 114)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(171, 10)
		self._label4.TabIndex = 12
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Yellow
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(484, 124)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(171, 36)
		self._label5.TabIndex = 13
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.Lime
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(484, 160)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(171, 36)
		self._label6.TabIndex = 14
		self._label6.Text = "X 12345679"
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.Black
		self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(484, 196)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(171, 11)
		self._label7.TabIndex = 15
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.Cyan
		self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.Location = System.Drawing.Point(484, 207)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(171, 36)
		self._label8.TabIndex = 16
		self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(371, 9)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(90, 55)
		self._button1.TabIndex = 17
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(371, 105)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(90, 55)
		self._button2.TabIndex = 18
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(371, 212)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(90, 55)
		self._button3.TabIndex = 19
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.PaleGoldenrod
		self.ClientSize = System.Drawing.Size(672, 281)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._radioButton9)
		self.Controls.Add(self._radioButton8)
		self.Controls.Add(self._radioButton7)
		self.Controls.Add(self._radioButton6)
		self.Controls.Add(self._radioButton5)
		self.Controls.Add(self._radioButton4)
		self.Controls.Add(self._radioButton3)
		self.Controls.Add(self._radioButton2)
		self.Controls.Add(self._radioButton1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Lang76a2"
		self.ResumeLayout(False)


	def RadioButton1CheckedChanged(self, sender, e):
		pass

	def RadioButton2CheckedChanged(self, sender, e):
		pass

	def RadioButton3CheckedChanged(self, sender, e):
		pass
	
	def RadioButton4CheckedChanged(self, sender, e):
		pass

	def RadioButton5CheckedChanged(self, sender, e):
		pass

	def RadioButton6CheckedChanged(self, sender, e):
		pass

	def RadioButton7CheckedChanged(self, sender, e):
		pass

	def RadioButton8CheckedChanged(self, sender, e):
		pass

	def RadioButton9CheckedChanged(self, sender, e):
		pass

		# CALCULATE BUTTON HERE
	def Button1Click(self, sender, e):
		oneten = 0
		if self._radioButton1.Checked == True:
			oneten = 1
		if self._radioButton2.Checked == True:
			oneten = 2
		if self._radioButton3.Checked == True:
			oneten = 3
		if self._radioButton4.Checked == True:
			oneten = 4
		if self._radioButton5.Checked == True:
			oneten = 5
		if self._radioButton6.Checked == True:
			oneten = 6
		if self._radioButton7.Checked == True:
			oneten = 7
		if self._radioButton8.Checked == True:
			oneten = 8
		if self._radioButton9.Checked == True:
			oneten = 9
		xoneten = oneten * 9
		foneten = xoneten * 12345679
		self._label8.Text = str(foneten)
		self._label2.Text = str(oneten)
		self._label5.Text = str(xoneten)
		self._label3.Text = "X 9"
		self._label6.Text = "X 12345679"
		pass

	def Button2Click(self, sender, e):
		self._label2.Text = ""
		self._label3.Text = ""
		self._label5.Text = ""
		self._label6.Text = ""
		self._label8.Text = ""
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass