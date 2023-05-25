/*
 * Created by SharpDevelop.
 * User: slinde.j
 * Date: 5/25/2023
 * Time: 3:58 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;
using Microsoft.VisualBasic;

namespace Pg498Payroll3
{
	/// <summary>
	/// Description of MainForm.
	/// </summary>
	public partial class MainForm : Form
	{
		public MainForm()
		{
			//
			// The InitializeComponent() call is required for Windows Forms designer support.
			//
			InitializeComponent();
			
			//
			// TODO: Add constructor code after the InitializeComponent() call.
			//
		}
		const decimal decHOURLY_PAY_RATE = 6.0m;
		const int intMAX_EMPLOYEES = 5;
		// "const" prevents us from ever changing the value
		void Button1Click(object sender, EventArgs e) {
			int[] intHours = new int[intMAX_EMPLOYEES];
			int intCount = 0;			// Loop counter
			int intEmpHours = 0;		// Employee hours
			decimal decEmpPay = 0.0m;	//Employee gross pay
			
			// Get the hours worked by the employees
			for (intCount = 0; intCount < intMAX_EMPLOYEES; intCount++) {
				while (int.Parse(
					Interaction.InputBox("Enter the number of hours worked by employee #" + (intCount+1).ToString(), "Need Hours Worked"),
					out intEmpHours) == false) {
					MessageBox.Show("Please enter an integer for hours worked");
				}
				intHours[intCount] = intEmpHours;
			}
			
			// Calculate and display each employee's gross pay
			listBox1.Items.Clear();
			for (intCount = 0; intCount < intMAX_EMPLOYEES; intCount++) {
				decEmpPay = intHours[intCount] * decHOURLY_PAY_RATE;
				listBox1.Items.Add("Employee") + (intCount+1).ToString() + " earned " + decEmpPay.ToString("$.00");
				
			}
		}
		
		void Button2Click(object sender, EventArgs e)
		{
			Application.Exit();
		}
	}
}
