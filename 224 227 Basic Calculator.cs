/*
https://leetcode.com/problems/basic-calculator-i
https://leetcode.com/problems/basic-calculator-ii
The solution works both I & II
*/
public int Calculate(string s)
{
    int i = 0;
    return Execute(s, ref i);
}

// called right after "right" is updated
private void Combine(ref int result, ref int left, int right, char sign)
{
    // do calculation right after number parse
    switch (sign)
    {
        case '+':
            result += left;
            left = right;
            break;
        case '-':
            result += left;
            left = -right;
            break;
        case '*':
            left = left * right;
            break;
        case '/':
            left = left / right;
            break;
        default:
            throw new ArgumentException();
    }
}

private int ParseInt(string s, ref int i)
{
    int r = 0;
    char c = s[i];
    for (; i < s.Length; i++)
    {
        c = s[i];
        if (char.IsDigit(c))
        {
            r = r * 10 + c - '0';
        }
        else
        {
            i--; // why?
            return r;
        }
    }
    return r;
}

// Used for double input case
private double ParseDouble(string s, ref int i)
{
    double r = 0D;
    int deci = 0; // decimal digit count
    char c = s[i];
    for (; i < s.Length; i++)
    {
        c = s[i];
        if (char.IsDigit(c))
        {
            if (deci == 0)
            {
                r = r * 10 + c - '0';
            }
            else
            {
                r += (c - '0') / Math.Pow(10, deci);
                deci++;
            }
        }
        else if (c == '.')
        {
            if (deci == 0)
            {
                deci = 1;
            }
            else
            {
                // double '.'
                throw new ArgumentException();
            }
        }
        else
        {
            i--; // why?
            return r;
        }
    }
    return r;
}
        
private int Execute(string s, ref int i)
{
    int result = 0;
    int left = 0;
    int right = 0; // used for number passing
    char sign = '+';
    for (; i < s.Length; i++)
    {
        char c = s[i];
        switch (c)
        {
            case ' ':
                // ignore spaces
                continue;
            case '(':
                // goto sub branch
                i++; // why?
                right = Execute(s, ref i);
                Combine(ref result, ref left, right, sign);
                break;
            case ')':
                // return to higher branch
                // NOT i++ why?
                return result + left;
            case '+':
            case '-':
            case '*':
            case '/':
                // sign
                sign = c;
                break;
            default:
                if (char.IsDigit(c))
                // Double: if (char.IsDigit(c) || c == '.')
                {
                    right = ParseInt(s, ref i);
                    Combine(ref result, ref left, right, sign);
                }
                else
                {
                    throw new ArgumentException();
                }
                break;
        }
    }
    return result + left;
}
