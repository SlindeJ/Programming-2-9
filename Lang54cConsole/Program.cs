/*
 * Created by SharpDevelop.
 * User: Public Library
 * Date: 4/22/2023
 * Time: 1:52 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;

namespace Lang54cConsole
{
	class Program
	{
		public static void Main(string[] args)
		{
			Console.WriteLine("The radius of the circle:");
			float rad = float.Parse(Console.ReadLine());
			double pii = 3.14159;
			double area1 = pii * rad * rad;
			double circum = 2 * pii * rad;
			area1 = Math.Round(area1, 2);
			circum = Math.Round(circum, 2);
			Console.WriteLine("Area: " + area1);
			Console.WriteLine("Circumference: " + circum);
			Console.ReadKey();
			
		}
	}
}