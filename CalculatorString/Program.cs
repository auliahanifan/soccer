namespace CalculatorString
{
    class Program
    {
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

        static int calculate(string input) {
            
            int result = 0;
            int tempNumber = 0;
            bool operation = false;
            char lastOperation = ' ';
            bool error = false;
            string errorMessage = "";
            bool space = false;

            foreach (char character in input)
            {
                if (character == '0' | character == '1' | character == '2' | character == '3' | character == '4' |
                    character == '5' | character == '6' | character == '7' | character == '8' | character == '9')
                {
                    if (space == true && tempNumber != 0)
                    {
                        error = true;
                        errorMessage = "Tidak dapat memisahkan angka dengan spasi tanpa operator + atau kurang diantaranya";
                    }
                    else if (tempNumber == 0)
                    {
                        tempNumber = int.Parse(character.ToString());
                        space = false;
                        operation = false;
                    }
                    else if (tempNumber != 0)
                    {
                        tempNumber = tempNumber * 10 + int.Parse(character.ToString());
                        space = false;
                        operation = false;
                    }

                }
                else if (character == ' ')
                {
                    space = true;
                }
                else if (character == '+' | character == '-')
                {
                    if (tempNumber == 0 && lastOperation != ' ')
                    {
                        error = true;
                        errorMessage = "Menambahkan 2 operator tanpa angka";
                    }
                    else
                    {
                        if (lastOperation == '+' | lastOperation == ' ')
                        {
                            result = result + tempNumber;
                        }
                        else if (lastOperation == '-')
                        {
                            result = result - tempNumber;
                        }
                        lastOperation = character;

                        operation = true;
                        tempNumber = 0;
                        space = false;
                    }

                }
                else
                {
                    throw new System.ArgumentException("Menggunakan character yang tidak", "original");
                }
            }

            if (tempNumber != 0)
            {
                if (lastOperation == '-')
                {
                    result = result - tempNumber;
                } else 
                {
                    result = result + tempNumber;
                }
            }

            if (operation)
            {
                error = true;
                errorMessage = "Jangan mengakhiri dengan operasi";
            }

            if (error)
            {
                throw new System.ArgumentException(errorMessage, "string input");
            }
            return result;
        }
    }
}
