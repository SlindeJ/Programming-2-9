/*
 * Created by SharpDevelop.
 * User: Public Library
 * Date: 4/22/2023
 * Time: 3:54 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;

namespace Lang85cForm
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
			label2.Text = "1. Determine your birth month (January = 1, February = 2, March = 3,...).\n2. Multiply that number by 5.\n3. Add 6 to that number.\n4. Multiply that number by 4.\n5. Add 9 to the number.\n6. Multiply that number by 5.\n7. Add your birth day to the number (ex. if you were born on the 10th, add 10, if born on the 25th add 25, and so on).";
			//
			// TODO: Add constructor code after the InitializeComponent() call.
			//
		}
		
		void Button1Click(object sender, EventArgs e)
		{
			int number = int.Parse(textBox1.Text);
			double num2 = number - 165.0;
			double num3 = num2 / 100;
			double months = Math.Round(num3);
			double day = Math.Round((num3 - months) * 100);
			label4.Text = "Your birthday is: " + months.ToString() + "/" + day.ToString();
		}
		
		void Button2Click(object sender, EventArgs e)
		{
			textBox1.Text = "";
			label4.Text = "";
		}
		
		void Button3Click(object sender, EventArgs e)
		{
			Application.Exit();
		}
	}
}
