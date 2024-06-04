#pragma once
#include "Integer.h"
#include <iostream>
#include<vector>#include <sstream>
using namespace std;

typedef vector<int>::iterator iter;

class Integer;

class Float {
public:
    float float_form;
    int sign;
    vector<int> exponent;
    int exponent_decimal;
    vector<int> mantisse;

    Float(float number) {
        float_form = number;
        if (number >= 0) {
            sign = 0;
        }
        else sign = 1;

        int integerPart = static_cast<int>(number);
        float fractionalPart = number - integerPart;
        integerPart = abs(integerPart);
        fractionalPart = fabs(fractionalPart);
        vector<int> binaryIntegerPart;
        if (integerPart == 0) binaryIntegerPart.push_back(0);
        while (integerPart > 0) {
            binaryIntegerPart.push_back(integerPart % 2);
            integerPart = integerPart / 2;
        }

        vector<int>  binaryFractionalPart;
        const int maxIterations = 10 - binaryIntegerPart.size();
        int iteration = 0;
        while (fractionalPart > 0 || iteration < maxIterations) {
            fractionalPart *= 2;
            if (fractionalPart >= 1) {
                binaryFractionalPart.push_back(1);
                fractionalPart -= 1;
            }
            else {
                binaryFractionalPart.push_back(0);
            }
            iteration++;
        }

        vector<int> binaryFull;
        for (int i = binaryIntegerPart.size() - 1; i >= 0; i--) {
            binaryFull.push_back(binaryIntegerPart[i]);
        }
        binaryFull.insert(binaryFull.end(), binaryFractionalPart.begin(), binaryFractionalPart.end());

        int current_position_of_dot = binaryIntegerPart.size();
        int wanted_position_of_dot = 1;
        for (; (wanted_position_of_dot < binaryFull.size()) && (binaryFull[wanted_position_of_dot - 1] != 1); wanted_position_of_dot++)
        {
            if (wanted_position_of_dot == 22)
                int p = 0;
        }
        exponent_decimal = current_position_of_dot - wanted_position_of_dot;
        iter it1 = binaryFull.begin();
        for (int i = 0; i < wanted_position_of_dot; i++, it1++);
        binaryFull.erase(binaryFull.begin(), it1);

        vector<int> binaryNew;
        for (int i = binaryFull.size() - 1; i >= 0; i--) {
            binaryNew.push_back(binaryFull[i]);
        }
        if (binaryNew.size() == 0)
        {
            binaryNew.push_back(0);
            exponent_decimal = -127;
        }
        mantisse = binaryNew;

        vector<int>direct_code;
        int numb = 127 + exponent_decimal;
        while (numb > 0) {
            direct_code.push_back(numb % 2);
            numb = numb / 2;
        }
        if (direct_code.size() == 0)
            direct_code.push_back(0);

        vector<int>binaryExponent = direct_code;
        exponent = binaryExponent;
    }
    Float operator+(Float& other)
    {
        Float result(this->float_form + other.float_form);
        vector<int>mantisse1 = this->mantisse;
        vector<int>mantisse2 = other.mantisse;
        mantisse1.insert(mantisse1.end(), 1);
        mantisse2.insert(mantisse2.end(), 1);
        int exp1 = this->exponent_decimal;
        int exp2 = other.exponent_decimal;
        if (exp1 > exp2)
        {
            for (int i = 0; i < exp1 - exp2; i++)
            {
                mantisse2.insert(mantisse2.end(), 0);
            }
            exp2 = exp1;
        }
        else if (exp1 < exp2)
        {
            for (int i = 0; i < exp2 - exp1; i++)
            {
                mantisse1.insert(mantisse1.end(), 0);
            }
            exp1 = exp2;
        }
        mantisse1.push_back(this->sign);
        mantisse2.push_back(other.sign);
        mantisse1.push_back(this->sign);
        mantisse2.push_back(other.sign);
        vector <int> Sum;
        if (this->sign == 0 && other.sign == 0)
        {
            Sum = sum_of_mantisse(mantisse1, mantisse2);
            Sum.pop_back();
            if (Sum[Sum.size() - 1] == 1)
            {
                if (exp1 > 0) exp1++;
                else exp1--;
            }
            else Sum.pop_back();
            result.sign = 0;
        }
        else if ((this->sign == 1 && other.sign == 0 && abs(this->float_form) > other.float_form) || (this->sign == 0 && other.sign == 1 && abs(this->float_form) < abs(other.float_form)))
        {
            if (this->sign == 1) {
                invert(mantisse1);
                plus1(mantisse1);
            }
            else
            {
                invert(mantisse2);
                plus1(mantisse2);
            }
            Sum = sum_of_mantisse(mantisse1, mantisse2);
            invert(Sum);
            plus1(Sum);
            Sum.pop_back();
            Sum.pop_back();
            result.sign = 1;
        }
        else if ((this->sign == 1 && other.sign == 0 && abs(this->float_form) < other.float_form) || (this->sign == 0 && other.sign == 1 && this->float_form > abs(other.float_form)))
        {
            if (this->sign == 1) {
                invert(mantisse1);
                plus1(mantisse1);
            }
            else
            {
                invert(mantisse2);
                plus1(mantisse2);
            }

            Sum = sum_of_mantisse(mantisse1, mantisse2);
            Sum.pop_back();
            Sum.pop_back();
            result.sign = 0;
        }
        else if (this->sign == 1 && other.sign == 1)
        {
            invert(mantisse1);
            plus1(mantisse1);
            invert(mantisse2);
            plus1(mantisse2);
            Sum = sum_of_mantisse(mantisse1, mantisse2);
            invert(Sum);
            plus1(Sum);
            if (Sum[Sum.size() - 2] == 0)
            {
                if (exp1 > 0) exp1++;
                else exp1--;
                Sum.pop_back();
                Sum.pop_back();
                Sum.push_back(1);
            }
            else
            {
                Sum.pop_back();
                Sum.pop_back();
            }
            result.sign = 1;
        }

        int n = Sum.size();
        for (int i = 0; Sum[n - 1 - i] != 1; i++)
        {
            exp1--;
            Sum.pop_back();
        }

        result.exponent_decimal = exp1;
        vector<int>direct_code;
        int numb = 127 + exp1;
        while (numb > 0) {
            direct_code.push_back(numb % 2);
            numb = numb / 2;
        }

        vector<int>binaryExponent = direct_code;

        result.exponent = binaryExponent;
        Sum.pop_back();
        if (Sum.size() > 23)
        {
            int elementsToRemove = Sum.size() - 23;
            Sum.erase(Sum.begin(), Sum.begin() + elementsToRemove);
        }

        result.mantisse = Sum;


        return result;
    }

    void invert(vector<int>& Sum)
    {
        iter it = Sum.begin();
        for (; it != Sum.end() - 2; it++)
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
        if (carry > 0)
            Sum.insert(Sum.end(), carry);
    }

    vector <int> sum_of_mantisse(vector <int> first, vector <int> second)
    {
        vector <int> sum;
        if (first.size() > second.size())
        {
            int dif = first.size() - second.size();
            if (second[second.size() - 1] == 0) {
                for (int i = 0; i < dif; i++)
                    second.insert(second.begin(), 0);
            }
            else
                for (int i = 0; i < dif; i++)
                    second.insert(second.begin(), 1);
        }
        else if (first.size() < second.size())
        {
            int dif = second.size() - first.size();
            if (first[first.size() - 1] == 0) {
                for (int i = 0; i < dif; i++)
                    first.insert(first.begin(), 0);
            }
            else
                for (int i = 0; i < dif; i++)
                    first.insert(first.begin(), 1);
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
        return sum;
    }

    void print() {
        cout << "Number in decimal form: " << float_form << endl;
        cout << "Number in floating-point form: ";
        cout << sign << '.';
        for (int i = exponent.size() - 1; i >= 0; --i) {
            cout << exponent[i];
        }
        cout << '.';
        for (int i = mantisse.size() - 1; i >= 0; --i) {
            cout << mantisse[i];
        }
        cout << endl << "Exponent: " << exponent_decimal;
        cout << endl << endl;
    }

    Float() {};
};
