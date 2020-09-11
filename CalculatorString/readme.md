# Calculator String

____

# Requirements
1. This code run on C#, myself use .NET Core 3.1 as engine.
2. You can run it on .NET Core or other engine, easily on [https://dotnetfiddle.net/](https://dotnetfiddle.net/)
3. If use dotnetfiddle.net, just copy the all code under class `Program {}` in `Program.cs` and run it on compiler `.NET Core 3.1`. 
4. If use .NET Core, just run `dotnet run`

___

## About Code

1. This code only created with 1 function : `calculate(string input)`
2. I use Debug.Assert() for testing
   ```csharp
        static void Main(string[] args)
        {
            string x = "5 + 2 + 1";
            int x_expected = 8;
            string x2 = "-10 + 10";
            int x2_expected = 0;
            
            // Test with Assert
            try 
            {
                System.Diagnostics.Debug.Assert(calculate(x) == x_expected, "Error");
                System.Diagnostics.Debug.Assert(calculate(x2) == x2_expected, "Error");

                System.Console.WriteLine("Semua berjalan lancar, tidak ada error");
            } 
            catch (System.Exception ex)
            {
                System.Console.WriteLine(ex.Message);
            }
        }

   ```