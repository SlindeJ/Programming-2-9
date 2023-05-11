using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace pg273MassAndWeight
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            double mass = double.Parse(textBox1.Text);
            double weight = mass * 9.8;
            if (weight > 1000)
            {
                label2.Text = "Object is too heavy";
            }
            else if (weight < 10)
            {
                label2.Text = "Object is too light";
            }
            else
            {
                label2.Text = "Object weight valid";
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            label2.Text = "";
            textBox1.Text = "";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
