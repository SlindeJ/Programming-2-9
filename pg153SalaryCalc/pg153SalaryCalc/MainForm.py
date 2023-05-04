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
		self._label4 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.DeepSkyBlue
		self._label1.ForeColor = System.Drawing.Color.ForestGreen
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Annual Salary"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Blue
		self._label2.ForeColor = System.Drawing.Color.PaleGreen
		self._label2.Location = System.Drawing.Point(118, 9)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(130, 23)
		self._label2.TabIndex = 1
		self._label2.Text = "Pay Periods Per Year"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Gold
		self._label4.Location = System.Drawing.Point(254, 35)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(117, 20)
		self._label4.TabIndex = 3
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.ControlLight
		self._label3.ForeColor = System.Drawing.Color.Black
		self._label3.Location = System.Drawing.Point(254, 9)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(117, 23)
		self._label3.TabIndex = 4
		self._label3.Text = "Salary Per Pay Period"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(12, 35)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 5
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(118, 35)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(130, 20)
		self._textBox2.TabIndex = 6
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Crimson
		self._button1.ForeColor = System.Drawing.Color.LightSteelBlue
		self._button1.Location = System.Drawing.Point(118, 56)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(130, 34)
		self._button1.TabIndex = 7
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Thistle
		self.ClientSize = System.Drawing.Size(383, 91)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "pg153SalaryCalc"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		annual = 0.0
		paypers = 0.0
		salpaypers = 0.0
		try:
			annual = float(self._textBox1.Text)
			paypers = float(self._textBox2.Text)
		except:
			MessageBox.Show("The Input Files Must Contain Nonzero Numeric Values.", "Error")
		salpaypers = annual / paypers
		salpaypers = round(salpaypers, 2)
		self._label4.Text = "$" + str(salpaypers)
		pass