﻿/*
 * Created by SharpDevelop.
 * User: Public Library
 * Date: 4/22/2023
 * Time: 2:09 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;

namespace LP4_5Console
{
	class Program
	{
		public static void Main(string[] args)
		{
			Console.Write("Enter the percentage: ");
			double grade = double.Parse(Console.ReadLine());
			char letgrade = ' ';
			if (grade >= 90){
				letgrade = 'A';
			} else if (grade >= 80){
				letgrade = 'B';
			} else if (grade >= 70){
				letgrade = 'C';
			} else if (grade >= 60){
				letgrade = 'D';
			} else {
				letgrade = 'F';
			}
			Console.WriteLine("The corresponding letter grade is: " + letgrade);
			Console.ReadKey();
			
		}
	}
}