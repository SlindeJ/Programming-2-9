/*
 * Created by SharpDevelop.
 * User: Public Library
 * Date: 4/22/2023
 * Time: 3:31 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;

namespace Lang54bForm
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
			int num1 = int.Parse(textBox1.Text);
			int num2 = int.Parse(textBox2.Text);
			int num3 = int.Parse(textBox3.Text);
			int num4 = int.Parse(textBox4.Text);
			
			int summ = num1 + num2 + num3 + num4;
			double avg = (double)summ / 4;
			avg = Math.Round(avg, 2);
			label5.Text = "The sum of the four numbers is " + summ.ToString();
			label6.Text = "The average of the four numbers is " + avg.ToString();
			
		}
		
		void Button2Click(object sender, EventArgs e)
		{
			label5.Text = "";
			label6.Text = "";
			textBox1.Text = "";
			textBox2.Text = "";
			textBox3.Text = "";
			textBox4.Text = "";
		}
		
		void Button3Click(object sender, EventArgs e)
		{
			Application.Exit();
		}
	}
}
