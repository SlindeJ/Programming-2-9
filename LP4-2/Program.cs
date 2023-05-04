/*
 * Created by SharpDevelop.
 * User: Public Library
 * Date: 4/22/2023
 * Time: 2:35 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;

namespace LP4_2
{
	class Program
	{
		public static void Main(string[] args)
		{
			Console.Write("Enter weight: ");
			int weight = int.Parse(Console.ReadLine());
			Console.Write("Enter length: ");
			int length = int.Parse(Console.ReadLine());
			Console.Write("Enter width: ");
			int width = int.Parse(Console.ReadLine());
			Console.Write("Enter height: ");
			int height = int.Parse(Console.ReadLine());
			
			
			int volume = length * width * height;
			
			if (weight > 27 && volume > 100000) {
				Console.WriteLine("Package is too heavy and too large");
			} else if (weight > 27) {
				Console.WriteLine("Package is too heavy");
			} else if (volume > 100000) {
				Console.WriteLine("Package is too large");
			} else {
				Console.WriteLine("Package is okay:");
			}
			
			
			
			Console.ReadKey();
		}
	}
}