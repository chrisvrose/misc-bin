using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    class Program
    {
        private int num;
        public Program(int n)
        {
            num = n;
        }
        public string Binarize()
        {
            string returnable="";
            while (num != 0)
            {
                returnable =  num%2 + returnable;
                num /= 2;
            }
            return returnable;
        }



        static void Main(string[] args)
        {
            #region Length Input
            Console.WriteLine("Enter array length");
            int a_length;
            if (int.TryParse(Console.ReadLine(), out a_length));
            else a_length = 5;
            #endregion

            int[] a = new int[a_length];

            #region Array init and input
            Console.WriteLine("Enter "+a_length+" numbers");
            for(int i=0;i<a_length;i++)
            {
                if (int.TryParse(Console.ReadLine(), out a[i]));
                else a[i] = 0;
            }
            #endregion

            #region Array output
            Console.WriteLine("Output:");
            foreach(int x in a)
            {
                Program obj = new Program(x);
                Console.WriteLine(obj.Binarize());
            }
            #endregion
            Console.ReadKey();
        }
    }
}
