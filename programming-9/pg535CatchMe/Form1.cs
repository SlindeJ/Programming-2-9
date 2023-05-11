using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;



namespace pg535CatchMe
{
    public partial class Form1 : Form
    {
        private string[] strCaption = { "Click here", "Try harder!", "Try again", "So close", "Hello?", "Over here!", "Too slow", "Gotta go!", "Missed me!", "Faster!", "Do it again!"};
        private Random rand = new Random();
        public Form1() {
            
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
              MessageBox.Show("You got me!", "", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
            Application.Exit();
        }

        private void btnCatch_MouseEnter_1(object sender, EventArgs e)
        {
            // randomly choose a caption
            int intIndex = rand.Next(strCaption.Length);
            btnCatch.Text = strCaption[intIndex];
            // move to a new horizontal position
            btnCatch.Left = rand.Next(this.Width - btnCatch.Width);
            // move to a new vertical position
            btnCatch.Top = rand.Next(this.Height - btnCatch.Height - 30);
        }
    }
}
