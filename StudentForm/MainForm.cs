/*
 * Created by SharpDevelop.
 * User: Public Library
 * Date: 5/13/2023
 * Time: 2:49 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;

namespace StudentForm
{
	/// <summary>
	/// Description of MainForm.
	/// </summary>
	public partial class MainForm : Form
	{
		private Form myParent;
		public MainForm(Form prt)
		{
			this.myParent = prt;
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
			this.myParent.Show();
			this.Close();
		}
		
		decimal decTAXRATE = 0.06m; // Sales Tax Rate
		private decimal CalcTax(decimal cost) {
			// Returns the sales tax on ticket sales
			return cost * decTAXRATE;
		}
	}
}
