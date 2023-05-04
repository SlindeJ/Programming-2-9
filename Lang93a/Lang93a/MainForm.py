import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Red
		self._label1.Font = System.Drawing.Font("OCR A Extended", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.MidnightBlue
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(183, 49)
		self._label1.TabIndex = 0
		self._label1.Text = "Total Kilowatts Used:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label1.Click += self.Label1Click
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(201, 24)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 1
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.White
		self._button1.Font = System.Drawing.Font("OCR A Extended", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.Red
		self._button1.Location = System.Drawing.Point(201, 58)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(19, 250)
		self._button1.TabIndex = 2
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.ForestGreen
		self._button2.Font = System.Drawing.Font("Bradley Hand ITC", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.SeaShell
		self._button2.Location = System.Drawing.Point(467, 42)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(175, 61)
		self._button2.TabIndex = 3
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(415, 109)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(272, 195)
		self._button3.TabIndex = 4
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Fuchsia
		self._label2.Font = System.Drawing.Font("Microsoft Uighur", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.White
		self._label2.Location = System.Drawing.Point(12, 58)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(183, 41)
		self._label2.TabIndex = 5
		self._label2.Text = "Base Cost:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Blue
		self._label3.Font = System.Drawing.Font("Microsoft Uighur", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.Tomato
		self._label3.Location = System.Drawing.Point(12, 109)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(183, 41)
		self._label3.TabIndex = 6
		self._label3.Text = "Surcharge:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Cyan
		self._label4.Font = System.Drawing.Font("Microsoft Uighur", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(12, 158)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(183, 41)
		self._label4.TabIndex = 7
		self._label4.Text = "City Tax:"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Lime
		self._label5.Font = System.Drawing.Font("Microsoft Uighur", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(12, 209)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(183, 41)
		self._label5.TabIndex = 8
		self._label5.Text = "Amount to Pay:"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.Yellow
		self._label6.Font = System.Drawing.Font("Microsoft Uighur", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(12, 266)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(183, 41)
		self._label6.TabIndex = 9
		self._label6.Text = "Late Pay:"
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.Fuchsia
		self._label7.ForeColor = System.Drawing.Color.White
		self._label7.Location = System.Drawing.Point(226, 58)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(183, 41)
		self._label7.TabIndex = 10
		self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.Blue
		self._label8.ForeColor = System.Drawing.Color.Tomato
		self._label8.Location = System.Drawing.Point(226, 109)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(183, 41)
		self._label8.TabIndex = 11
		self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.Cyan
		self._label9.Location = System.Drawing.Point(226, 158)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(183, 41)
		self._label9.TabIndex = 12
		self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.Lime
		self._label10.Location = System.Drawing.Point(226, 209)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(183, 41)
		self._label10.TabIndex = 13
		self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.Color.Yellow
		self._label11.Location = System.Drawing.Point(226, 266)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(183, 41)
		self._label11.TabIndex = 14
		self._label11.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(255, 128, 0)
		self.ClientSize = System.Drawing.Size(699, 316)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Lang93a"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		kwatts = float(self._textBox1.Text)
		basekwatts = float(kwatts * 0.0475)
		basekwatts = round(basekwatts, 2)
		skwatts = float(basekwatts * 0.10)
		skwatts = round(skwatts, 2)
		ctytax = float(basekwatts * 0.03)
		ctytax = round(ctytax, 2)
		kwattpay = float(basekwatts + skwatts + ctytax)
		kwattpay =round(kwattpay, 2)
		latekwattpay = float(kwattpay * 1.04)
		latekwattpay = round(latekwattpay, 2)
		self._label7.Text = str(basekwatts)
		self._label8.Text = str(skwatts)
		self._label9.Text = str(ctytax)
		self._label10.Text = str(kwattpay)
		self._label11.Text = str(latekwattpay)
		pass

	def Button2Click(self, sender, e):
		self._label7.Text = ""
		self._label8.Text = ""
		self._label9.Text = ""
		self._label10.Text = ""
		self._label11.Text = ""
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass

	def Label1Click(self, sender, e):
		pass

	def MainFormLoad(self, sender, e):
		pass