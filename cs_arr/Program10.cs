using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading;

namespace ConsoleApp1
{
    class Program10
    {
        private string store;
        
        public Program10(string s)
        {
            store = s;
        }

        public string ReplaceAll()
        {
            string tempstring = store;
            foreach(char x in store)
            {
                tempstring = tempstring.Replace(x.ToString(),((int)x).ToString());
                //Console.WriteLine(x.ToString() + " " + ((int)x).ToString());
            }
            //Console.WriteLine(tempstring);
            return tempstring;
        }

        static void Main(string[] args)
        {
            string input_var;
            Console.WriteLine("Input string:");
            input_var = Console.ReadLine();
            Console.WriteLine("Output String: "+ (new Program10(input_var)).ReplaceAll() );
            Console.ReadKey();
        }
    }
}
