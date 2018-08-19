using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    class Program2
    {
        private int num;
        public Program2(int n)
        {
            num = n;
        }
        public string Addable()
        {
            string returnable = "";
            string num_string = num.ToString();
            foreach(char i in num_string)
                returnable = returnable + (int.Parse(i.ToString()) + 1).ToString();
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
                Program2 obj = new Program2(x);
                Console.WriteLine(obj.Addable());
            }
            #endregion
            Console.ReadKey();
        }
    }
}
