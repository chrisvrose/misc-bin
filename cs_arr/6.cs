using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;

namespace ConsoleApp1
{
    class Program
    {
        private char separator;
        private decimal num;

        public Program(decimal n)
        {
            separator = char.Parse(Thread.CurrentThread.CurrentCulture.NumberFormat.NumberDecimalSeparator);
            num = n;
        }

        public Tuple<int,int> GetParts() {
            decimal num_tempcopy = num;
            int lp = (int)num;
            int rp;

            #region Getting the decimal section
            rp = 0;
            num_tempcopy %= 1;
            while (num_tempcopy % 1 != 0)
            {
                num_tempcopy *= 10;
            }
            rp = (int)num_tempcopy;
            #endregion

            string lp_temp = lp.ToString();
            string rp_temp = rp.ToString();
            //Console.WriteLine(rp_temp);
            // Note, reusing lp and rp
            lp = 0;rp = 1;
            #region Calculate Results
            foreach(char x in lp_temp)
            {
                lp += int.Parse(x.ToString());
            }
            foreach (char x in rp_temp)
            {
                rp *= int.Parse(x.ToString());
            }
            #endregion
            
            return new Tuple<int, int>(lp,rp);
        }
        
        static void Main(string[] args)
        {
            decimal number_input;
            Console.WriteLine("Enter number");
            if (decimal.TryParse(Console.ReadLine(), out number_input)) ; else number_input = 0.0m;
            Program obj = new Program(number_input);
            Tuple<int, int> res = obj.GetParts();
            Console.WriteLine("Result 1:" + res.Item1 + "\nResult 2:" + res.Item2);

            Console.ReadKey();
        }
    }
}
