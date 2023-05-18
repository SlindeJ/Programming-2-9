/*
 * Created by SharpDevelop.
 * User: Public Library
 * Date: 5/13/2023
 * Time: 3:41 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;

namespace Lang122dFor
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
			for (int x = -12; x < 17; x++) {
				double y = Math.Pow(x, 6) - 3 * Math.Pow(x, 5) - 93 * Math.Pow(x, 4) + 87 * Math.Pow(x, 3) + 1596 * Math.Pow(x, 2) - 1380 * x - 2800;
				string bigg = String.Format("{0}\t\t{1}", x, y);
				listBox1.Items.Add(bigg);
			}
			
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
