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
	/// Description of GeneralForm.
	/// </summary>
	public partial class GeneralForm : Form
	{
		private Form myParent;
		private int Nou = 0;
		public decimal PriceEachTicket() {
			if RadioButton1CheckedChanged
		}
		public GeneralForm(Form prt)
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
		
		void GeneralFormFormClosing(object sender, FormClosingEventArgs e)
		{
			this.myParent.Show();
		}
		void Button2Click(object sender, EventArgs e)
		{
			if (Nou = 1) {
				decimal PriceEachTicket = 20.0;
			} else if (Nou = 2) {
				decimal PriceEachTicket = 15.0;
			} else if (Nou = 3) {
				decimal PriceEachTicket = 10.0;
			} else {
				decimal PriceEachTicket = 0.0;
			}
			int intNumTickets = 0;
			decimal decTicketCost = 0.0m;
			decimal decSalesTax = 0.0m;
			decimal decTotal = 0.0m;
			
			intNumTickets = int.Parse(textBox1.Text);
			decTicketCost = intNumTickets * PriceEachTicket;
			decSalesTax = CalcTax(decTicketCost); 
			decTotal = decTicketCost + decSalesTax;
			
			label2.Text = decTicketCost.ToString("$.00");
			label3.Text = decSalesTax.ToString("$.00");
			label4.Text = decTotal.ToString("$.00");
		}
		
		void RadioButton1CheckedChanged(object sender, EventArgs e)
		{
			Nou = 1;
		}
		
		void RadioButton2CheckedChanged(object sender, EventArgs e)
		{
			Nou = 2;
		}
		
		void RadioButton3CheckedChanged(object sender, EventArgs e)
		{
			Nou = 3;
		}
	}
}