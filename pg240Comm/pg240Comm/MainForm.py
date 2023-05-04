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
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
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
		self._label1.BackColor = System.Drawing.Color.Black
		self._label1.Font = System.Drawing.Font("Eras Medium ITC", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.White
		self._label1.Location = System.Drawing.Point(1, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(206, 38)
		self._label1.TabIndex = 0
		self._label1.Text = "Sales for the Month:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Black
		self._label2.Font = System.Drawing.Font("Eras Medium ITC", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.White
		self._label2.Location = System.Drawing.Point(1, 84)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(206, 38)
		self._label2.TabIndex = 1
		self._label2.Text = "Advanced Pay:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.Linen
		self._textBox1.Font = System.Drawing.Font("Eras Medium ITC", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(1, 50)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(206, 31)
		self._textBox1.TabIndex = 2
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.Linen
		self._textBox2.Font = System.Drawing.Font("Eras Medium ITC", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(1, 125)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(206, 31)
		self._textBox2.TabIndex = 3
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Lime
		self._label3.Font = System.Drawing.Font("OCR A Extended", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(1, 166)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(140, 59)
		self._label3.TabIndex = 4
		self._label3.Text = "Commision Rate:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Cyan
		self._label4.Font = System.Drawing.Font("OCR A Extended", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(1, 225)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(140, 59)
		self._label4.TabIndex = 5
		self._label4.Text = "Commision:"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Blue
		self._label5.Font = System.Drawing.Font("OCR A Extended", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ForeColor = System.Drawing.Color.White
		self._label5.Location = System.Drawing.Point(1, 284)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(140, 59)
		self._label5.TabIndex = 7
		self._label5.Text = "Net Pay:"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.Blue
		self._label6.Font = System.Drawing.Font("OCR A Extended", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.ForeColor = System.Drawing.Color.White
		self._label6.Location = System.Drawing.Point(150, 166)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(140, 59)
		self._label6.TabIndex = 6
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.Cyan
		self._label7.Font = System.Drawing.Font("OCR A Extended", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(150, 225)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(140, 59)
		self._label7.TabIndex = 9
		self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.Lime
		self._label8.Font = System.Drawing.Font("OCR A Extended", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.Location = System.Drawing.Point(150, 284)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(140, 59)
		self._label8.TabIndex = 8
		self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.DodgerBlue
		self._button1.Font = System.Drawing.Font("Microsoft Uighur", 15, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.Maroon
		self._button1.Location = System.Drawing.Point(213, 9)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(77, 35)
		self._button1.TabIndex = 10
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Red
		self._button2.Font = System.Drawing.Font("Wide Latin", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.DarkBlue
		self._button2.Location = System.Drawing.Point(213, 50)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(77, 31)
		self._button2.TabIndex = 11
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Orchid
		self._button3.Font = System.Drawing.Font("Papyrus", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.GhostWhite
		self._button3.Location = System.Drawing.Point(213, 84)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(77, 72)
		self._button3.TabIndex = 12
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DarkBlue
		self.ClientSize = System.Drawing.Size(291, 352)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "pg240Comm"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		sales = float(self._textBox1.Text)
		advpay = float(self._textBox2.Text)
		commrate = 0.05
		if 10000 <= sales < 14999:
			commrate = 0.10
		elif 15000 <= sales < 17999:
			commrate = 0.12
		elif 18000 <= sales < 21999:
			commrate = 0.14
		elif 22000 <= sales:
			commrate = 0.16
		comm = sales * commrate
		npay = comm - advpay
		comm = round(comm, 2)
		npay = round(npay,2)
		self._label6.Text = str(commrate * 100) + "%"
		self._label7.Text = "$" + str(comm)
		self._label8.Text = "$" + str(npay)
		pass

	def Button2Click(self, sender, e):
		self._label6.Text = ""
		self._label7.Text = ""
		self._label8.Text = ""
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass