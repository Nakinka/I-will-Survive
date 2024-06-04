#pragma once
#include"Float.h"

class Integer {
public:

    int decimal_form;
    vector<int> direct_code;
    vector<int> reverse_code;
    vector<int> complement_code;

    void convert_to_direct()
    {
        int number = decimal_form;
        int sign = 0;
        if (decimal_form < 0) {
            number *= -1;
            sign = 1;
        }
        while (number > 0) {
            direct_code.push_back(number % 2);
            number = number / 2;
        }
        if (sign == 1)
            direct_code.push_back(1);
        else direct_code.push_back(0);
    }

    vector<int> sum_of_complement(vector<int>& first, vector<int>& second)
    {
        vector <int> sum;
        if (first.size() > second.size())
        {
            int dif = first.size() - second.size();
            if (second[second.size() - 1] == 0) {
                for (int i = 0; i < dif; i++)
                    second.insert(second.end() - 1, 0);
            }
            else
                for (int i = 0; i < dif; i++)
                    second.insert(second.end() - 1, 1);
        }
        else if (first.size() < second.size())
        {
            int dif = second.size() - first.size();
            if (first[first.size() - 1] == 0) {
                for (int i = 0; i < dif; i++)
                    first.insert(first.end() - 1, 0);
            }
            else
                for (int i = 0; i < dif; i++)
                    first.insert(first.end() - 1, 1);
        }
        iter it1 = first.begin();
        iter it2 = second.begin();
        int carry = 0;
        for (; it1 != first.end(); it1++, it2++)
        {
            int bit = carry + *it1 + *it2;
            if (bit < 2)
            {
                sum.push_back(bit);
                carry = 0;
            }
            else if (bit == 2)
            {
                sum.push_back(0);
                carry = 1;
            }
            else if (bit == 3)
            {
                sum.push_back(1);
                carry = 1;
            }
        }
        if (carry > 0)
            sum.insert(sum.end(), 1);
        return sum;
    }
    vector<int> sum_of_direct(vector<int>& first, vector<int>& second)
    {
        vector <int> sum;
        if (first.size() > second.size())
        {
            int dif = first.size() - second.size();
            for (int i = 0; i < dif; i++)
                second.insert(second.end(), 0);
        }
        else if (first.size() < second.size())
        {
            int dif = second.size() - first.size();
            for (int i = 0; i < dif; i++)
                first.insert(first.end(), 0);
        }
        iter it1 = first.begin();
        iter it2 = second.begin();
        int carry = 0;
        for (; it1 != first.end(); it1++, it2++)
        {
            int bit = carry + *it1 + *it2;
            if (bit < 2)
            {
                sum.push_back(bit);
                carry = 0;
            }
            else if (bit == 2)
            {
                sum.push_back(0);
                carry = 1;
            }
            else if (bit == 3)
            {
                sum.push_back(1);
                carry = 1;
            }
        }
        if (carry > 0)
            sum.insert(sum.end(), 1);
        return sum;
    }

    void invert(vector<int>& Sum)
    {
        iter it = Sum.begin();
        for (; it != Sum.end() - 1; it++)
        {
            if (*it == 1)
                *it = 0;
            else
                *it = 1;
        }
    }
    void plus1(vector<int>& Sum)
    {
        int carry = 1;
        for (iter it = Sum.begin(); it != Sum.end() - 1; it++)
        {
            int sum = *it + carry;
            *it = sum % 2;
            carry = sum / 2;
            if (carry == 0) break;
        }
    }

    Integer(int number)
    {
        decimal_form = number;
        convert_to_direct();
        if (number >= 0)
        {
            reverse_code = direct_code;
            complement_code = direct_code;
        }
        else
        {
            vector<int> binary = direct_code;
            invert(binary);
            reverse_code = binary;
            plus1(binary);
            complement_code = binary;
        }
    }
    Integer operator+(Integer& other)
    {
        Integer result(this->decimal_form + other.decimal_form);
        vector <int> Sum = sum_of_complement(this->complement_code, other.complement_code);
        if (this->decimal_form > 0 && other.decimal_form > 0)
        {
            Sum.push_back(0);
            result.direct_code = Sum;
            result.reverse_code = Sum;
            result.complement_code = Sum;
        }
        else if ((this->decimal_form > 0 && other.decimal_form < 0 && abs(other.decimal_form) > this->decimal_form) || (other.decimal_form > 0 && this->decimal_form < 0 && abs(this->decimal_form) > other.decimal_form))
        {
            result.complement_code = Sum;
            invert(Sum);
            plus1(Sum);
            result.direct_code = Sum;
            invert(Sum);
            result.reverse_code = Sum;
        }
        else if ((this->decimal_form > 0 && other.decimal_form < 0 && abs(other.decimal_form) <= this->decimal_form) || (other.decimal_form > 0 && this->decimal_form < 0 && abs(this->decimal_form) <= other.decimal_form))
        {
            Sum.pop_back();
            Sum.push_back(0);
            result.direct_code = Sum;
            result.reverse_code = Sum;
            result.complement_code = Sum;
        }
        else if (this->decimal_form < 0 && other.decimal_form < 0)
        {
            result.complement_code = Sum;
            invert(Sum);
            plus1(Sum);
            result.direct_code = Sum;
            invert(Sum);
            result.reverse_code = Sum;
        }
        return result;
    }
    Integer operator-(Integer& other)
    {
        Integer deducted(other.decimal_form * -1);
        Integer result = *this + deducted;
        return result;
    }
    Integer operator*(Integer& other)
    {
        Integer Composition(this->decimal_form * other.decimal_form);
        vector<int> result(this->direct_code.size() + other.direct_code.size() - 2, 0);
        iter it1 = this->direct_code.begin();
        for (int i = 0; it1 != this->direct_code.end() - 1; i++, it1++)
        {
            vector<int>temp;
            iter it2 = other.direct_code.begin();
            for (int j = i; j > 0; j--)
                temp.push_back(0);
            for (; it2 != other.direct_code.end() - 1; it2++)
            {
                int bit = *it1 * (*it2);
                temp.push_back(bit);
            }
            result = sum_of_direct(result, temp);
        }
        if ((this->decimal_form < 0 && other.decimal_form > 0) || (other.decimal_form < 0 && this->decimal_form > 0))
        {
            result.push_back(1);
            Composition.direct_code = result;
            invert(result);
            Composition.reverse_code = result;
            plus1(result);
            Composition.complement_code = result;
        }
        else {
            result.push_back(0);
            Composition.direct_code = result;
            Composition.reverse_code = result;
            Composition.complement_code = result;
        }
        return Composition;
    }

    void operator/(Integer& other)
    {
        Float quot(1.0 * this->decimal_form / other.decimal_form);
        Float fl(1. / other.decimal_form);
        vector<int> first = fl.mantisse;

        first.push_back(1);

        vector<int> second = this->get_direct_code();
        second.pop_back();

        vector<int> result(second.size() + first.size(), 0);
        iter it1 = second.begin();
        for (int i = 0; it1 != second.end(); i++, it1++)
        {
            vector<int>temp;
            iter it2 = first.begin();
            for (int j = i; j > 0; j--)
                temp.push_back(0);
            for (; it2 != first.end(); it2++)
            {
                int bit = *it1 * (*it2);
                temp.push_back(bit);
            }
            result = sum_of_direct(result, temp);
        }
        int len_of_fractional_part = (first.size() - 1 - fl.exponent_decimal);
        vector<int> fractional_part;
        if (len_of_fractional_part > result.size())
        {
            int n = result.size();
            for (int i = 0; i < len_of_fractional_part - n + 1; i++)
                result.push_back(0);
        }
        for (int i = 0; i < len_of_fractional_part; i++)
            fractional_part.push_back(result[i]);
        result.erase(result.begin(), result.begin() + len_of_fractional_part);

        if ((this->decimal_form < 0 && other.decimal_form>0) || (this->decimal_form > 0 && other.decimal_form < 0))
            result.push_back(1);
        else result.push_back(0);

        int elementsToRemove = fractional_part.size() - 10;
        if (elementsToRemove > 0)
            fractional_part.erase(fractional_part.begin(), fractional_part.begin() + elementsToRemove);

        for (int i = result.size() - 1; i >= 0; cout << result[i--]);
        cout << '.';
        for (int i = fractional_part.size() - 1; i >= 0; cout << fractional_part[i--]);
        cout << endl;
    }

    void print()
    {
        cout << endl << "Number in decimal form: " << decimal_form << endl;
        cout << "Direct code: ";
        for (int i = direct_code.size() - 1; i >= 0; cout << direct_code[i--]);
        cout << endl;
        cout << "Reverse code: ";
        for (int i = reverse_code.size() - 1; i >= 0; cout << reverse_code[i--]);
        cout << endl;
        cout << "Complement code: ";
        for (int i = complement_code.size() - 1; i >= 0; cout << complement_code[i--]);
        cout << endl;
    }


    vector<int> get_direct_code()
    {
        return direct_code;
    }
    vector<int> get_reverse_code()
    {
        return reverse_code;
    }
    vector<int> get_complement_code()
    {
        return complement_code;
    }

    int get_int_form()
    {
        return decimal_form;
    }
};
