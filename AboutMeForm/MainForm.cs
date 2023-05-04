/*
 * Created by SharpDevelop.
 * User: Public Library
 * Date: 4/22/2023
 * Time: 3:15 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;

namespace AboutMeForm
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
			label1.Text = ("My name is Jacob Slinde \n My favorite sport is Swimming \n My favorite quote is: \n Everything in this world is either a potato or not a potato");
		}
		
		void Button2Click(object sender, EventArgs e)
		{
			label1.Text = "";
		}
		
		void Button3Click(object sender, EventArgs e)
		{
			Application.Exit();
		}
	}
}
