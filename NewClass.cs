using System;

namespace ConsoleApp
{
    class Program
    {
        static void Main(string[] args)
        {
        
            char add, subtr, multi, divi, modulo;
            add = '+';
            subtr = '-';
            multi = '*';
            divi = '/';
            modulo = '%';

        Console.Write("Enter a number ");
        float num1= float.Parse(Console.ReadLine());
        Console.Write("Enter a second number ");
        float num2=float.Parse(Console.ReadLine());

        
        Console.Write("Enter an operation");
        char action= char.Parse(Console.ReadLine());

        try{
            switch(action){
                case '+':
                float subtr2=num1+num2;
                 Console.WriteLine(Math.Abs(subtr2));
                 Console.WriteLine("The Actual result is {0}",subtr2);
                 break;

                 case '-':
                subtr2=num1-num2;
                 Console.WriteLine(Math.Abs(subtr2));
                 Console.WriteLine("The Actual result is {0}",subtr2);
                 break;

                 case '*':
                subtr2=num1*num2;
                 Console.WriteLine(Math.Abs(subtr2));
                 Console.WriteLine("The Actual result is {0}",subtr2);
                 break;

                 case '/':
                 if (num2 == 0)
    {
        Console.WriteLine("Cannot Divide by zero!");
        break;
    }
                else{
                subtr2=num1/num2;
                
                 Console.WriteLine("The Actual result is {0}",subtr2);
                 
                 break;
                }
                 case '%':
                subtr2=num1%num2;
                 
                 Console.WriteLine("The Actual result is {0}",subtr2);
                 break;

                default:
                Console.WriteLine("Invalid Operation!");
                break;

            }
        return;
        }
        catch(DivideByZeroException){
            Console.WriteLine("Cannot Divide by zero!");
        }
        
    }
}
}