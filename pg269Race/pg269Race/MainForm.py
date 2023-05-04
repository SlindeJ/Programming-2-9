import System.Drawing
import System.Windows.Forms
import math

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._textBox4 = System.Windows.Forms.TextBox()
		self._textBox5 = System.Windows.Forms.TextBox()
		self._textBox6 = System.Windows.Forms.TextBox()
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Blue
		self._label1.ForeColor = System.Drawing.Color.White
		self._label1.ImageAlign = System.Drawing.ContentAlignment.MiddleRight
		self._label1.Location = System.Drawing.Point(42, 53)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Runner 1:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Blue
		self._label3.ForeColor = System.Drawing.Color.White
		self._label3.ImageAlign = System.Drawing.ContentAlignment.MiddleRight
		self._label3.Location = System.Drawing.Point(42, 125)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 2
		self._label3.Text = "Runner 3:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Blue
		self._label2.ForeColor = System.Drawing.Color.White
		self._label2.ImageAlign = System.Drawing.ContentAlignment.MiddleRight
		self._label2.Location = System.Drawing.Point(42, 90)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 3
		self._label2.Text = "Runner 2:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Chartreuse
		self._label4.ForeColor = System.Drawing.Color.Black
		self._label4.Location = System.Drawing.Point(24, 65)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 6
		self._label4.Text = "2nd Place:"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Chartreuse
		self._label5.ForeColor = System.Drawing.Color.Black
		self._label5.Location = System.Drawing.Point(24, 100)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 5
		self._label5.Text = "3rd Place:"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.Chartreuse
		self._label6.ForeColor = System.Drawing.Color.Black
		self._label6.Location = System.Drawing.Point(24, 26)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 23)
		self._label6.TabIndex = 4
		self._label6.Text = "1st Place:"
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.Yellow
		self._label7.ForeColor = System.Drawing.Color.Black
		self._label7.Location = System.Drawing.Point(194, 26)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(114, 23)
		self._label7.TabIndex = 9
		self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.Silver
		self._label8.Location = System.Drawing.Point(194, 65)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(114, 23)
		self._label8.TabIndex = 8
		self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.Sienna
		self._label9.Location = System.Drawing.Point(194, 100)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(114, 23)
		self._label9.TabIndex = 7
		self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(183, 53)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 10
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(183, 90)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 11
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(183, 125)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 20)
		self._textBox3.TabIndex = 12
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.Red
		self._label10.ForeColor = System.Drawing.Color.Thistle
		self._label10.Location = System.Drawing.Point(183, 9)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(100, 23)
		self._label10.TabIndex = 13
		self._label10.Text = "Runner Name:"
		self._label10.TextAlign = System.Drawing.ContentAlignment.BottomCenter
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.Color.Red
		self._label11.ForeColor = System.Drawing.Color.Thistle
		self._label11.Location = System.Drawing.Point(308, 9)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(100, 23)
		self._label11.TabIndex = 14
		self._label11.Text = "Time is Seconds:"
		self._label11.TextAlign = System.Drawing.ContentAlignment.BottomCenter
		# 
		# textBox4
		# 
		self._textBox4.Location = System.Drawing.Point(308, 53)
		self._textBox4.Name = "textBox4"
		self._textBox4.Size = System.Drawing.Size(100, 20)
		self._textBox4.TabIndex = 17
		# 
		# textBox5
		# 
		self._textBox5.Location = System.Drawing.Point(308, 90)
		self._textBox5.Name = "textBox5"
		self._textBox5.Size = System.Drawing.Size(100, 20)
		self._textBox5.TabIndex = 16
		# 
		# textBox6
		# 
		self._textBox6.Location = System.Drawing.Point(308, 125)
		self._textBox6.Name = "textBox6"
		self._textBox6.Size = System.Drawing.Size(100, 20)
		self._textBox6.TabIndex = 15
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._label7)
		self._groupBox1.Controls.Add(self._label8)
		self._groupBox1.Controls.Add(self._label9)
		self._groupBox1.Controls.Add(self._label4)
		self._groupBox1.Controls.Add(self._label5)
		self._groupBox1.Controls.Add(self._label6)
		self._groupBox1.ForeColor = System.Drawing.Color.White
		self._groupBox1.Location = System.Drawing.Point(58, 171)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(338, 147)
		self._groupBox1.TabIndex = 18
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Race Results"
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Fuchsia
		self._button1.Font = System.Drawing.Font("OCR A Extended", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.DeepSkyBlue
		self._button1.Location = System.Drawing.Point(12, 324)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(118, 36)
		self._button1.TabIndex = 19
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Fuchsia
		self._button2.Font = System.Drawing.Font("OCR A Extended", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.DeepSkyBlue
		self._button2.Location = System.Drawing.Point(174, 324)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(118, 36)
		self._button2.TabIndex = 20
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Fuchsia
		self._button3.Font = System.Drawing.Font("OCR A Extended", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.DeepSkyBlue
		self._button3.Location = System.Drawing.Point(329, 324)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(118, 36)
		self._button3.TabIndex = 21
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Black
		self.ClientSize = System.Drawing.Size(459, 372)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._groupBox1)
		self.Controls.Add(self._textBox4)
		self.Controls.Add(self._textBox5)
		self.Controls.Add(self._textBox6)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "pg269Race"
		self.Load += self.MainFormLoad
		self._groupBox1.ResumeLayout(False)
		self.ResumeLayout(False)
		self.PerformLayout()


	def MainFormLoad(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		t1 = int(self._textBox4.Text)
		t2 = int(self._textBox5.Text)
		t3 = int(self._textBox6.Text)
		r1 = self._textBox1.Text
		r2 = self._textBox2.Text
		r3 = self._textBox3.Text
		first = min(t1, t2, t3)
		second = int(t1 + t2 + t3) - max(t1, t2, t3) - min(t1, t2, t3)
		third = max(t1, t2, t3)
		
		if t1 == first:
			self._label7.Text = str(r1)
		if t1 == second:
			self._label8.Text = str(r1)
		if t1 == third:
			self._label9.Text = str(r1)
			
		if t2 == first:
			self._label7.Text = str(r2)
		if t2 == second:
			self._label8.Text = str(r2)
		if t2 == third:
			self._label9.Text = str(r2)
			
		if t3 == first:
			self._label7.Text = str(r3)
		if t3 == second:
			self._label8.Text = str(r3)
		if t3 == third:
			self._label9.Text = str(r3)
		pass

	def Button2Click(self, sender, e):
		self._textBox4.Text = ""
		self._textBox5.Text = ""
		self._textBox6.Text = ""
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""
		self._label7.Text = ""
		self._label8.Text = ""
		self._label9.Text = ""
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass