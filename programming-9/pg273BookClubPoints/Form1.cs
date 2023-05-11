using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace pg273BookClubPoints
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            textBox1.Text = "";
            label2.Text = "";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int points = 0;
            int books = int.Parse(textBox1.Text);
            if (books == 0)
            {
                points = 0;
            }
            else if (books == 1)
            {
                points = 5;
            }
            else if (books == 2)
            {
                points = 15;
            }
            else if (books >= 3) {
                points = 30;
            }
            else
            {
                label2.Text = "Please enter a valid number of books";
            }
            label2.Text = points.ToString();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}
