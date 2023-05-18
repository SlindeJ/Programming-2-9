/*
 * Created by SharpDevelop.
 * User: Public Library
 * Date: 5/13/2023
 * Time: 3:20 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;
using Microsoft.VisualBasic;

namespace Pg344LoanCalculator
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
		
		void Button1Click(object sender, EventArgs e)
		{
			int MIN_MONTHS = 6;
			int MAX_MONTHS = 48;
			float sngMONTHS_YEAR = 12.0f; // months per year
			double dblNEW_RATE = 0.089;
			double dblUSED_RATE = 0.095;
			double dblANNUAL_RATE = dblNEW_RATE;
			
		}
		
		void Button2Click(object sender, EventArgs e)
		{
			listBox1.Items.Clear();
		}
		
		void Button3Click(object sender, EventArgs e)
		{
			Application.Exit();
		}
	}
}
