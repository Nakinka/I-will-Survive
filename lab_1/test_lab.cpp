#include <gtest/gtest.h>
#include "pch.h"
#include "Integer.h" 
#include "Float.h"

std::ostringstream oss;

TEST(IntegerTest, ConvertToDirectPositive) {
    Integer num(5);
    std::vector<int> expected = { 1, 0, 1, 0 };
    EXPECT_EQ(num.get_direct_code(), expected);
}

TEST(IntegerTest, ConvertToDirectNegative) {
    Integer num(-5);
    std::vector<int> expected = { 1, 0, 1, 1 };
    EXPECT_EQ(num.get_direct_code(), expected);
}

TEST(IntegerTest, SumOfComplementPositive) {
    Integer num1(5), num2(7);
    std::vector<int> result = num1.sum_of_complement(num1.get_complement_code(), num2.get_complement_code());
    std::vector<int> expected = { 0, 0, 1, 1 };
    EXPECT_EQ(result, expected);
}

TEST(IntegerTest, SumOfComplementNegative) {
    Integer num1(-5), num2(-7);
    std::vector<int> result = num1.sum_of_complement(num1.get_complement_code(), num2.get_complement_code());
    std::vector<int> expected = { 0, 0, 1, 0, 1 };
    EXPECT_EQ(result, expected);
}

TEST(IntegerTest, OperatorPlusPositive) {
    Integer num1(5), num2(7);
    Integer result = num1 + num2;
    EXPECT_EQ(result.get_int_form(), 12);
}

TEST(IntegerTest, OperatorPlusNegative) {
    Integer num1(-5), num2(-7);
    Integer result = num1 + num2;
    EXPECT_EQ(result.get_int_form(), -12);
}

TEST(IntegerTest, OperatorMinusPositive) {
    Integer num1(5), num2(7);
    Integer result = num1 - num2;
    EXPECT_EQ(result.get_int_form(), -2);
}

TEST(IntegerTest, OperatorMinusNegative) {
    Integer num1(-5), num2(-7);
    Integer result = num1 - num2;
    EXPECT_EQ(result.get_int_form(), 2);
}

TEST(IntegerTest, OperatorMultiplyPositive) {
    Integer num1(5), num2(7);
    Integer result = num1 * num2;
    EXPECT_EQ(result.get_int_form(), 35);
}

TEST(IntegerTest, OperatorMultiplyNegative) {
    Integer num1(-5), num2(-7);
    Integer result = num1 * num2;
    EXPECT_EQ(result.get_int_form(), 35);
}

TEST(FloatTest, ConstructorPositive) {
    Float f(123.456f);
    EXPECT_FLOAT_EQ(f.float_form, 123.456f);
    EXPECT_EQ(f.sign, 0);
    
}

TEST(FloatTest, ConstructorNegative) {
    Float f(-123.456f);
    EXPECT_FLOAT_EQ(f.float_form, -123.456f);
    EXPECT_EQ(f.sign, 1);
   
}

TEST(FloatTest, AdditionPositiveNumbers) {
    Float f1(5.5f), f2(6.6f);
    Float result = f1 + f2;
    EXPECT_FLOAT_EQ(result.float_form, 12.1f);
}


    TEST(FloatTest, AdditionMixedSigns) {
        Float f1(5.5f), f2(-6.6f);
        Float result = f1 + f2;
        EXPECT_FLOAT_EQ(result.float_form, -1.1f);

    }

    TEST(FloatTest, InvertAndPlusOne) {
        Float f(5.5f);
        vector<int> testMantisse = { 1, 0, 1, 0, 1 };
        f.invert(testMantisse);
        f.plus1(testMantisse);
    }

    TEST(FloatTest, SumOfMantisse) {
        Float f;
        vector<int> mantisse1 = { 1, 0, 1 }, mantisse2 = { 1, 1, 0 };
        vector<int> result = f.sum_of_mantisse(mantisse1, mantisse2);
    }

    TEST(DivisionOperatorTest, PositiveDivision) {
        Integer dividend(15);
        Integer divisor(3);
    }

    void captureCoutOutput() {
        std::streambuf* oldCoutBuffer = std::cout.rdbuf();
        std::cout.rdbuf(oss.rdbuf());
    }

    void restoreCoutOutput(std::streambuf* oldCoutBuffer) {
        std::cout.rdbuf(oldCoutBuffer);
    }

    TEST(PrintFunctionTest, PrintPositiveInteger) {
        Integer num(5);
        std::streambuf* oldCoutBuffer = nullptr;
        captureCoutOutput();
        num.print();
        restoreCoutOutput(oldCoutBuffer);
        std::string expectedOutput = "\nNumber in decimal form: 5\nDirect code: 0101\nReverse code: 0101\nComplement code: 0101\n";
        EXPECT_EQ(oss.str(), expectedOutput);
    }
