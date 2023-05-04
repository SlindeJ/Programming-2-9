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
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label12 = System.Windows.Forms.Label()
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._groupBox2 = System.Windows.Forms.GroupBox()
		self._groupBox1.SuspendLayout()
		self._groupBox2.SuspendLayout()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Turquoise
		self._label1.ForeColor = System.Drawing.Color.Red
		self._label1.Location = System.Drawing.Point(0, 60)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Class A:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Crimson
		self._label2.ForeColor = System.Drawing.Color.Blue
		self._label2.Location = System.Drawing.Point(0, 88)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 1
		self._label2.Text = "Class B:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.DarkOrange
		self._label3.ForeColor = System.Drawing.Color.Green
		self._label3.Location = System.Drawing.Point(0, 117)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 2
		self._label3.Text = "Class C:"
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(106, 60)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 3
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(106, 85)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 4
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(106, 114)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 20)
		self._textBox3.TabIndex = 5
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Pink
		self._label4.Location = System.Drawing.Point(6, 16)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 8
		self._label4.Text = "Class A Revinue:"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Magenta
		self._label5.Location = System.Drawing.Point(6, 44)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 7
		self._label5.Text = "Class B Revinue:"
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.DarkOrchid
		self._label6.Location = System.Drawing.Point(6, 76)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 23)
		self._label6.TabIndex = 6
		self._label6.Text = "Class C Revinue:"
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.Black
		self._label7.ForeColor = System.Drawing.Color.White
		self._label7.Location = System.Drawing.Point(6, 105)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(100, 23)
		self._label7.TabIndex = 11
		self._label7.Text = "Total Revinue:"
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.Red
		self._label8.ForeColor = System.Drawing.Color.Black
		self._label8.Location = System.Drawing.Point(134, 16)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(100, 23)
		self._label8.TabIndex = 10
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.Blue
		self._label9.ForeColor = System.Drawing.Color.Ivory
		self._label9.Location = System.Drawing.Point(134, 44)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(100, 23)
		self._label9.TabIndex = 9
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.FromArgb(255, 128, 0)
		self._label10.ForeColor = System.Drawing.Color.Black
		self._label10.Location = System.Drawing.Point(134, 76)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(100, 23)
		self._label10.TabIndex = 12
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.Color.Black
		self._label11.ForeColor = System.Drawing.Color.White
		self._label11.Location = System.Drawing.Point(134, 105)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(100, 23)
		self._label11.TabIndex = 13
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.MediumPurple
		self._button1.FlatAppearance.BorderColor = System.Drawing.Color.Black
		self._button1.FlatAppearance.BorderSize = 200
		self._button1.FlatStyle = System.Windows.Forms.FlatStyle.Popup
		self._button1.Font = System.Drawing.Font("Ink Free", 15.749999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.PaleVioletRed
		self._button1.Location = System.Drawing.Point(12, 161)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(212, 43)
		self._button1.TabIndex = 14
		self._button1.Text = "Calculate Revinue"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Cyan
		self._button2.Font = System.Drawing.Font("Bell MT", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.SeaGreen
		self._button2.Location = System.Drawing.Point(265, 161)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(106, 43)
		self._button2.TabIndex = 15
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Wheat
		self._button3.Font = System.Drawing.Font("OCR A Extended", 15.75, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.Olive
		self._button3.Location = System.Drawing.Point(399, 161)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(100, 43)
		self._button3.TabIndex = 16
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label12
		# 
		self._label12.BackColor = System.Drawing.SystemColors.ControlText
		self._label12.Font = System.Drawing.Font("Leelawadee", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label12.Location = System.Drawing.Point(0, 16)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(206, 31)
		self._label12.TabIndex = 17
		self._label12.Text = "Enter the Number of Tickets Sold for Each Class of Seat:"
		self._label12.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._label12)
		self._groupBox1.Controls.Add(self._label1)
		self._groupBox1.Controls.Add(self._label2)
		self._groupBox1.Controls.Add(self._label3)
		self._groupBox1.Controls.Add(self._textBox1)
		self._groupBox1.Controls.Add(self._textBox2)
		self._groupBox1.Controls.Add(self._textBox3)
		self._groupBox1.ForeColor = System.Drawing.Color.SpringGreen
		self._groupBox1.Location = System.Drawing.Point(12, 12)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(212, 143)
		self._groupBox1.TabIndex = 18
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Tickets Sold"
		# 
		# groupBox2
		# 
		self._groupBox2.Controls.Add(self._label10)
		self._groupBox2.Controls.Add(self._label6)
		self._groupBox2.Controls.Add(self._label5)
		self._groupBox2.Controls.Add(self._label4)
		self._groupBox2.Controls.Add(self._label9)
		self._groupBox2.Controls.Add(self._label11)
		self._groupBox2.Controls.Add(self._label8)
		self._groupBox2.Controls.Add(self._label7)
		self._groupBox2.ForeColor = System.Drawing.Color.Coral
		self._groupBox2.Location = System.Drawing.Point(265, 12)
		self._groupBox2.Name = "groupBox2"
		self._groupBox2.Size = System.Drawing.Size(241, 143)
		self._groupBox2.TabIndex = 19
		self._groupBox2.TabStop = False
		self._groupBox2.Text = "Revinue Generated"
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Purple
		self.ClientSize = System.Drawing.Size(519, 216)
		self.Controls.Add(self._groupBox2)
		self.Controls.Add(self._groupBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "pg186StadiumSeating"
		self._groupBox1.ResumeLayout(False)
		self._groupBox1.PerformLayout()
		self._groupBox2.ResumeLayout(False)
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		classa = int(self._textBox1.Text) * 15
		classb = int(self._textBox2.Text) * 12
		classc = int(self._textBox3.Text) * 9
		revinue = classa + classb + classc
		self._label8.Text = "$" + str(classa)
		self._label9.Text = "$" + str(classb)
		self._label10.Text = "$" + str(classc)
		self._label11.Text = "$" + str(revinue)
		pass

	def Button2Click(self, sender, e):
		self._label11.Text = ""
		self._label10.Text = ""
		self._label9.Text = ""
		self._label8.Text = ""
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass