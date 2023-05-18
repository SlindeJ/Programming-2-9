/*
 * Created by SharpDevelop.
 * User: slinde.j
 * Date: 5/15/2023
 * Time: 4:20 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;
using System.Drawing;
using System.Windows.Forms;

namespace Pg435TicketSalesCS
{
	/// <summary>
	/// Description of StudentForm.
	/// </summary>
	public partial class StudentForm : Form
	{
		private Form myParent;
		public StudentForm(Form prt)
		{
			
			//
			// The InitializeComponent() call is required for Windows Forms designer support.
			//
			InitializeComponent();
			myParent = prt;
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
		
		void StudentFormFormClosing(object sender, FormClosingEventArgs e)
		{
			this.myParent.Show();
		}
		
		void Button2Click(object sender, EventArgs e)
		{
			int intNumTickets = 0;
			decimal decTicketCost = 0.0m;
			decimal decSalesTax = 0.0m;
			decimal decTotal = 0.0m;
			
			intNumTickets = int.Parse(textBox1.Text);
			decTicketCost = intNumTickets * 7.0m;
			decSalesTax = CalcTax(decTicketCost); 
			decTotal = decTicketCost + decSalesTax;
			
			label3.Text = decTicketCost.ToString("$.00");
			label4.Text = decSalesTax.ToString("$.00");
			label5.Text = decTotal.ToString("$.00");
			
			
		}
	}
}