/*
 * Created by SharpDevelop.
 * User: Public Library
 * Date: 5/13/2023
 * Time: 2:16 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;

namespace Lang366bFunctions
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
			listBox1.Items.Clear();
			listBox1.Items.Add("The following numbers generated " + "by the formula x^2 - x + 41 are:");
			
			int x = 1;
			while (true) {
				int number = (int)Math.Pow(x, 2) - x + 41;
				if (IsPrime(number, 2))
					listBox1.Items.Add(number + "   prime");
				else {
					int factor = FindSmallestFactor(number);
					listBox1.Items.Add(number + "   test fails/factors=" + factor);
					return;
				}
				x++;
			}
		}
		
		public bool IsPrime(int n, int f)
		{
			// trial division algorithm
			if (n <= 1) return false;
			if (n == 2 || f * f > n) return true;
			if (n % f == 0) return false;
			return IsPrime(n, f + 1);
		}
		
		public int FindSmallestFactor(int n) 
		{
			for (int lcv = 2; lcv <= Math.Sqrt(n); lcv++)
				if (n % lcv == 0) return lcv;
			return n;
		}
		
		void Button2Click(object sender, EventArgs e)
		{
			Application.Exit();
		}
	}
}
