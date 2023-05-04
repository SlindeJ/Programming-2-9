import System.Drawing
import System.Windows.Forms
import time
from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._lblDateToday = System.Windows.Forms.Label()
		self._lblTimeToday = System.Windows.Forms.Label()
		self._groupBox2 = System.Windows.Forms.GroupBox()
		self._groupBox3 = System.Windows.Forms.GroupBox()
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._btnCalculate = System.Windows.Forms.Button()
		self._btnClear = System.Windows.Forms.Button()
		self._btnExit = System.Windows.Forms.Button()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._txtNights = System.Windows.Forms.TextBox()
		self._txtNightlyCharge = System.Windows.Forms.TextBox()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._txtRoomService = System.Windows.Forms.TextBox()
		self._txtTelephone = System.Windows.Forms.TextBox()
		self._txtMisc = System.Windows.Forms.TextBox()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._label12 = System.Windows.Forms.Label()
		self._label13 = System.Windows.Forms.Label()
		self._lblTotal = System.Windows.Forms.Label()
		self._lblTax = System.Windows.Forms.Label()
		self._lblSubtotal = System.Windows.Forms.Label()
		self._lblAddCharges = System.Windows.Forms.Label()
		self._lblRoomCharges = System.Windows.Forms.Label()
		self._groupBox2.SuspendLayout()
		self._groupBox3.SuspendLayout()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.FromArgb(255, 128, 0)
		self._label1.Font = System.Drawing.Font("Verdana", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.White
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(462, 43)
		self._label1.TabIndex = 0
		self._label1.Text = "Highlander Hotel"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Crimson
		self._label2.Font = System.Drawing.Font("MS Gothic", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.Aqua
		self._label2.Location = System.Drawing.Point(12, 61)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 1
		self._label2.Text = "Todays Date:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Crimson
		self._label3.Font = System.Drawing.Font("MS Gothic", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.Aqua
		self._label3.Location = System.Drawing.Point(12, 95)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 3
		self._label3.Text = "Time:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# lblDateToday
		# 
		self._lblDateToday.BackColor = System.Drawing.Color.Black
		self._lblDateToday.Font = System.Drawing.Font("MS Gothic", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._lblDateToday.ForeColor = System.Drawing.Color.White
		self._lblDateToday.Location = System.Drawing.Point(137, 61)
		self._lblDateToday.Name = "lblDateToday"
		self._lblDateToday.Size = System.Drawing.Size(149, 23)
		self._lblDateToday.TabIndex = 2
		# 
		# lblTimeToday
		# 
		self._lblTimeToday.BackColor = System.Drawing.Color.Black
		self._lblTimeToday.Font = System.Drawing.Font("MS Gothic", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._lblTimeToday.ForeColor = System.Drawing.Color.White
		self._lblTimeToday.Location = System.Drawing.Point(137, 95)
		self._lblTimeToday.Name = "lblTimeToday"
		self._lblTimeToday.Size = System.Drawing.Size(149, 23)
		self._lblTimeToday.TabIndex = 4
		# 
		# groupBox2
		# 
		self._groupBox2.Controls.Add(self._txtMisc)
		self._groupBox2.Controls.Add(self._txtTelephone)
		self._groupBox2.Controls.Add(self._txtRoomService)
		self._groupBox2.Controls.Add(self._label8)
		self._groupBox2.Controls.Add(self._label7)
		self._groupBox2.Controls.Add(self._label6)
		self._groupBox2.Font = System.Drawing.Font("Microsoft PhagsPa", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox2.Location = System.Drawing.Point(12, 246)
		self._groupBox2.Name = "groupBox2"
		self._groupBox2.Size = System.Drawing.Size(239, 110)
		self._groupBox2.TabIndex = 6
		self._groupBox2.TabStop = False
		self._groupBox2.Text = "Additional Charges"
		# 
		# groupBox3
		# 
		self._groupBox3.Controls.Add(self._lblTotal)
		self._groupBox3.Controls.Add(self._label13)
		self._groupBox3.Controls.Add(self._lblTax)
		self._groupBox3.Controls.Add(self._label12)
		self._groupBox3.Controls.Add(self._lblSubtotal)
		self._groupBox3.Controls.Add(self._label11)
		self._groupBox3.Controls.Add(self._lblAddCharges)
		self._groupBox3.Controls.Add(self._label10)
		self._groupBox3.Controls.Add(self._lblRoomCharges)
		self._groupBox3.Controls.Add(self._label9)
		self._groupBox3.Font = System.Drawing.Font("Microsoft PhagsPa", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox3.Location = System.Drawing.Point(257, 137)
		self._groupBox3.Name = "groupBox3"
		self._groupBox3.Size = System.Drawing.Size(218, 219)
		self._groupBox3.TabIndex = 7
		self._groupBox3.TabStop = False
		self._groupBox3.Text = "Total Charges"
		# 
		# groupBox1
		# 
		self._groupBox1.Controls.Add(self._txtNightlyCharge)
		self._groupBox1.Controls.Add(self._txtNights)
		self._groupBox1.Controls.Add(self._label5)
		self._groupBox1.Controls.Add(self._label4)
		self._groupBox1.Font = System.Drawing.Font("Microsoft PhagsPa", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._groupBox1.Location = System.Drawing.Point(12, 137)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(239, 95)
		self._groupBox1.TabIndex = 8
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Room Information"
		# 
		# btnCalculate
		# 
		self._btnCalculate.BackColor = System.Drawing.Color.Lime
		self._btnCalculate.Font = System.Drawing.Font("OCR A Extended", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._btnCalculate.Location = System.Drawing.Point(301, 61)
		self._btnCalculate.Name = "btnCalculate"
		self._btnCalculate.Size = System.Drawing.Size(173, 43)
		self._btnCalculate.TabIndex = 9
		self._btnCalculate.Text = "Calculate Charge"
		self._btnCalculate.UseVisualStyleBackColor = False
		self._btnCalculate.Click += self.BtnCalculateClick
		# 
		# btnClear
		# 
		self._btnClear.BackColor = System.Drawing.Color.Yellow
		self._btnClear.Font = System.Drawing.Font("OCR A Extended", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._btnClear.Location = System.Drawing.Point(301, 110)
		self._btnClear.Name = "btnClear"
		self._btnClear.Size = System.Drawing.Size(89, 23)
		self._btnClear.TabIndex = 10
		self._btnClear.Text = "Clear"
		self._btnClear.UseVisualStyleBackColor = False
		self._btnClear.Click += self.BtnClearClick
		# 
		# btnExit
		# 
		self._btnExit.BackColor = System.Drawing.Color.Cyan
		self._btnExit.Font = System.Drawing.Font("OCR A Extended", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._btnExit.Location = System.Drawing.Point(385, 110)
		self._btnExit.Name = "btnExit"
		self._btnExit.Size = System.Drawing.Size(89, 23)
		self._btnExit.TabIndex = 11
		self._btnExit.Text = "Exit"
		self._btnExit.UseVisualStyleBackColor = False
		self._btnExit.Click += self.BtnExitClick
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.DarkGreen
		self._label4.ForeColor = System.Drawing.Color.Orange
		self._label4.Location = System.Drawing.Point(12, 24)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 0
		self._label4.Text = "Nights:"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.PaleGreen
		self._label5.ForeColor = System.Drawing.Color.Black
		self._label5.Location = System.Drawing.Point(12, 64)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 1
		self._label5.Text = "Nightly Charge:"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# txtNights
		# 
		self._txtNights.Location = System.Drawing.Point(126, 24)
		self._txtNights.Name = "txtNights"
		self._txtNights.Size = System.Drawing.Size(100, 22)
		self._txtNights.TabIndex = 2
		# 
		# txtNightlyCharge
		# 
		self._txtNightlyCharge.Location = System.Drawing.Point(126, 64)
		self._txtNightlyCharge.Name = "txtNightlyCharge"
		self._txtNightlyCharge.Size = System.Drawing.Size(100, 22)
		self._txtNightlyCharge.TabIndex = 3
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.DeepSkyBlue
		self._label6.Location = System.Drawing.Point(4, 16)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 23)
		self._label6.TabIndex = 0
		self._label6.Text = "Room Service:"
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.SkyBlue
		self._label7.Location = System.Drawing.Point(4, 49)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(100, 23)
		self._label7.TabIndex = 1
		self._label7.Text = "Telephone:"
		self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.LightSkyBlue
		self._label8.Location = System.Drawing.Point(4, 84)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(100, 23)
		self._label8.TabIndex = 2
		self._label8.Text = "Misc:"
		self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# txtRoomService
		# 
		self._txtRoomService.Location = System.Drawing.Point(129, 16)
		self._txtRoomService.Name = "txtRoomService"
		self._txtRoomService.Size = System.Drawing.Size(100, 22)
		self._txtRoomService.TabIndex = 3
		# 
		# txtTelephone
		# 
		self._txtTelephone.Location = System.Drawing.Point(129, 49)
		self._txtTelephone.Name = "txtTelephone"
		self._txtTelephone.Size = System.Drawing.Size(100, 22)
		self._txtTelephone.TabIndex = 4
		# 
		# txtMisc
		# 
		self._txtMisc.Location = System.Drawing.Point(129, 84)
		self._txtMisc.Name = "txtMisc"
		self._txtMisc.Size = System.Drawing.Size(100, 22)
		self._txtMisc.TabIndex = 5
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.LightSeaGreen
		self._label9.Font = System.Drawing.Font("Microsoft Tai Le", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.Location = System.Drawing.Point(6, 27)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(100, 23)
		self._label9.TabIndex = 0
		self._label9.Text = "Room Charges:"
		self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.PaleTurquoise
		self._label10.Font = System.Drawing.Font("Microsoft Tai Le", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label10.Location = System.Drawing.Point(6, 63)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(100, 23)
		self._label10.TabIndex = 1
		self._label10.Text = "Additional Charges:"
		self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.Color.Teal
		self._label11.Font = System.Drawing.Font("Microsoft Tai Le", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label11.Location = System.Drawing.Point(6, 103)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(100, 23)
		self._label11.TabIndex = 2
		self._label11.Text = "Subtotal:"
		self._label11.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		self._label11.Click += self.Label11Click
		# 
		# label12
		# 
		self._label12.BackColor = System.Drawing.Color.CornflowerBlue
		self._label12.Font = System.Drawing.Font("Microsoft Tai Le", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label12.Location = System.Drawing.Point(6, 143)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(100, 23)
		self._label12.TabIndex = 3
		self._label12.Text = "Tax:"
		self._label12.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# label13
		# 
		self._label13.BackColor = System.Drawing.Color.Orchid
		self._label13.Font = System.Drawing.Font("Microsoft Tai Le", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label13.Location = System.Drawing.Point(6, 178)
		self._label13.Name = "label13"
		self._label13.Size = System.Drawing.Size(100, 23)
		self._label13.TabIndex = 4
		self._label13.Text = "Total Charges:"
		self._label13.TextAlign = System.Drawing.ContentAlignment.MiddleRight
		# 
		# lblTotal
		# 
		self._lblTotal.BackColor = System.Drawing.Color.Orchid
		self._lblTotal.Location = System.Drawing.Point(112, 178)
		self._lblTotal.Name = "lblTotal"
		self._lblTotal.Size = System.Drawing.Size(100, 23)
		self._lblTotal.TabIndex = 16
		# 
		# lblTax
		# 
		self._lblTax.BackColor = System.Drawing.Color.CornflowerBlue
		self._lblTax.Location = System.Drawing.Point(112, 143)
		self._lblTax.Name = "lblTax"
		self._lblTax.Size = System.Drawing.Size(100, 23)
		self._lblTax.TabIndex = 15
		# 
		# lblSubtotal
		# 
		self._lblSubtotal.BackColor = System.Drawing.Color.Teal
		self._lblSubtotal.Location = System.Drawing.Point(112, 103)
		self._lblSubtotal.Name = "lblSubtotal"
		self._lblSubtotal.Size = System.Drawing.Size(100, 23)
		self._lblSubtotal.TabIndex = 14
		# 
		# lblAddCharges
		# 
		self._lblAddCharges.BackColor = System.Drawing.Color.PaleTurquoise
		self._lblAddCharges.Location = System.Drawing.Point(112, 63)
		self._lblAddCharges.Name = "lblAddCharges"
		self._lblAddCharges.Size = System.Drawing.Size(100, 23)
		self._lblAddCharges.TabIndex = 13
		# 
		# lblRoomCharges
		# 
		self._lblRoomCharges.BackColor = System.Drawing.Color.LightSeaGreen
		self._lblRoomCharges.Location = System.Drawing.Point(112, 27)
		self._lblRoomCharges.Name = "lblRoomCharges"
		self._lblRoomCharges.Size = System.Drawing.Size(100, 23)
		self._lblRoomCharges.TabIndex = 12
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.OrangeRed
		self.ClientSize = System.Drawing.Size(486, 360)
		self.Controls.Add(self._btnExit)
		self.Controls.Add(self._btnClear)
		self.Controls.Add(self._btnCalculate)
		self.Controls.Add(self._groupBox1)
		self.Controls.Add(self._groupBox3)
		self.Controls.Add(self._groupBox2)
		self.Controls.Add(self._lblTimeToday)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._lblDateToday)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "pg162RoomCharge"
		self.Load += self.MainFormLoad
		self._groupBox2.ResumeLayout(False)
		self._groupBox2.PerformLayout()
		self._groupBox3.ResumeLayout(False)
		self._groupBox1.ResumeLayout(False)
		self._groupBox1.PerformLayout()
		self.ResumeLayout(False)


	def MainFormLoad(self, sender, e):
		#Get today's date from the system and display it 
		from datetime import date
		self._lblDateToday.Text = date.today().strftime("%A, %B, %d, %Y")
		#Get current time from System and display it
		import time
		self._lblTimeToday.Text = time.strftime("%I:%M:%S %p")
		
		pass

	def BtnCalculateClick(self, sender, e):
		decRoomCharges = 0.0 #room chalculations
		decAddCharges = 0.0 #additional charges
		decSubtotal = 0.0 #subtotal
		decTax = 0.0
		decTotal = 0.0
		decTAX_RATE = 0.08
		
		
		try:
			decAddCharges = float(self._txtRoomService.Text) + \
				float(self._txtTelephone.Text) + \
				float(self._txtMisc.Text)
			self._lblAddCharges.Text = str(round(decAddCharges, 2))
		except:
			MessageBox.Show("Room service, Telephone, and Misc. must be numbers", "Error")
			
			
		try:
			decRoomCharges = float(self._txtNights.Text) * \
				float(self._txtNightlyCharge.Text)
			self._lblRoomCharges.Text = str(round(decRoomCharges, 2))
		except:
			MessageBox.Show("Nights and Nightly Charge must be numbers", "Error") 
			
		decSubtotal = decRoomCharges + decAddCharges 
		self._lblSubtotal.Text = str(round(decSubtotal, 2))
		
		decTax = decSubtotal * decTAX_RATE
		self._lblTax.Text = str(round(decTax, 2))
		
		decTotal = decSubtotal + decTax
		self._lblTotal.Text = str(round(decTotal, 2))
		pass

	def BtnClearClick(self, sender, e):
		self._txtNights.Clear()
		self._txtNightlyCharge.Clear()
		self._txtRoomService.Clear()
		self._txtMisc.Clear()
		self._txtTelephone.Clear()
		
		self._lblRoomCharges.Text = ""
		self._lblAddCharges.Text = ""
		self._lblSubtotal.Text = ""
		self._lblTax.Text = ""
		self._lblTotal.Text = ""
		
		from datetime import date
		self._lblDateToday.Text = date.today().strftime("%A, %B, %d, %Y")
		
		import time
		self._lblTimeToday.Text = time.strftime("%I:%M:%S %p")
		self._txtNights.Focus()
		pass

	def BtnExitClick(self, sender, e):
		Application.Exit()
		pass

	def Label11Click(self, sender, e):
		pass