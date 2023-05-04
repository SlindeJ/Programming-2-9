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
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Red
		self._label1.Font = System.Drawing.Font("OCR A Extended", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(15, 16)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Package A:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.FromArgb(255, 128, 0)
		self._label2.Font = System.Drawing.Font("OCR A Extended", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(15, 51)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 1
		self._label2.Text = "Package B:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Yellow
		self._label3.Font = System.Drawing.Font("OCR A Extended", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(15, 86)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 2
		self._label3.Text = "Package C:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(190, 16)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 3
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(190, 51)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 4
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(190, 86)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 20)
		self._textBox3.TabIndex = 5
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.DarkGreen
		self._label4.Font = System.Drawing.Font("OCR A Extended", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.GhostWhite
		self._label4.Location = System.Drawing.Point(12, 160)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(203, 97)
		self._label4.TabIndex = 6
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Blue
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.GhostWhite
		self._button1.Location = System.Drawing.Point(221, 160)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(94, 39)
		self._button1.TabIndex = 7
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Fuchsia
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(221, 205)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(94, 23)
		self._button2.TabIndex = 8
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Yellow
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 9, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(221, 234)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(94, 23)
		self._button3.TabIndex = 9
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._textBox3)
		self._groupBox1.Controls.Add(self._textBox2)
		self._groupBox1.Controls.Add(self._textBox1)
		self._groupBox1.Controls.Add(self._label3)
		self._groupBox1.Controls.Add(self._label2)
		self._groupBox1.Controls.Add(self._label1)
		self._groupBox1.ForeColor = System.Drawing.Color.Indigo
		self._groupBox1.Location = System.Drawing.Point(12, 12)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(303, 118)
		self._groupBox1.TabIndex = 10
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Quantity Sold"
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Cyan
		self.ClientSize = System.Drawing.Size(327, 279)
		self.Controls.Add(self._groupBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label4)
		self.Name = "MainForm"
		self.Text = "pg269SoftwareSales"
		self.Load += self.MainFormLoad
		self._groupBox1.ResumeLayout(False)
		self._groupBox1.PerformLayout()
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		pka = int(self._textBox1.Text)
		pkb = int(self._textBox2.Text)
		pkc = int(self._textBox3.Text)
		if 10 <= pka < 20:
			discounta = 0.8
		if 20 <= pka < 50:
			discounta = 0.7
		if 50 <= pka < 100:
			discounta = 0.6
		if 100 <= pka:
			discounta = 0.5
		
		if 10 <= pkb < 20:
			discountb = 0.8
		if 20 <= pkb < 50:
			discountb = 0.7
		if 50 <= pkb < 100:
			discountb = 0.6
		if 100 <= pkb:
			discountb = 0.5
			
		if 10 <= pkc < 20:
			discountc = 0.8
		if 20 <= pkc < 50:
			discountc = 0.7
		if 50 <= pkc < 100:
			discountc = 0.6
		if 100 <= pkc:
			discountc = 0.5
		costa = pka * 99 * discounta
		costb = pkb * 199 * discountb
		costc = pkc * 299 * discountc
		total = costa + costb + costc
		self._label4.Text = "Package A: $" + str(costa) + "\n" + "Package B: $" + str(costb) + "\n" + "Package C: $" + str(costc) + "\n" + "Grand Total: $" + str(total)
		
		pass

	def Button2Click(self, sender, e):
		self._label4.Text = ""
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""
		pass

	def Button3Click(self, sender, e):
		Application.Exit()
		pass

	def MainFormLoad(self, sender, e):
		pass