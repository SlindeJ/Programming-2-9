﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace HelloWorld
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

        private void button1_Click(object sender, EventArgs e)
        {
            label1.Text = "Hello, World!";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            label1.Text = "";
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}
