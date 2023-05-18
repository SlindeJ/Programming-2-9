/*
 * Created by SharpDevelop.
 * User: Public Library
 * Date: 5/13/2023
 * Time: 2:43 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;

namespace Pg435TicketSalesCS
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
			GeneralForm frm = new GeneralForm(this);
			// frm = GeneralForm(self)
			frm.Show();
			this.Hide();
		}
		
		void Button2Click(object sender, EventArgs e)
		{
			StudentForm frm = new StudentForm(this);
			// frm = GeneralForm(self)
			frm.Show();
			this.Hide();
		}
		
		void Button3Click(object sender, EventArgs e)
		{
			Application.Exit();
		}
		
		void MainFormFormClosing(object sender, FormClosingEventArgs e)
		{
			
		}
	}
}
