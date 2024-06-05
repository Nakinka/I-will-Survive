#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <string>
using namespace std;

struct Tree {
	bool sign = 0;
	char param;
	Tree* left = NULL, * right = NULL, * parent = NULL;
}

*root;

Tree* create_tree(Tree*& node, char str[], set <char>& operands)
{
	Tree* root = node;
	vector <int> binary_bracket = { -1 };
	vector <int> unar_bracket = { -1 };
	for (int i = 0; str[i] != '\0'; i++)
	{
		switch (str[i])
		{
		case '!':
		{
			node->sign = !(node->sign);
			break;
		}
		case '(':
		{
			if (str[i + 1] == '!') {
				unar_bracket.push_back(i);
				continue;
			}
			else
				binary_bracket.push_back(i);
			Tree* left_node = new Tree;
			node->left = left_node;
			left_node->parent = node;
			node = left_node;
			break;
		}
		case '-':
			i++;
		case '&':
		case '|':
		case '~': {
			if (node->right != NULL)
				throw std::exception("Incorrect formulа!");
			node->param = str[i];
			Tree* right_node = new Tree;
			node->right = right_node;
			right_node->parent = node;
			node = right_node;
			break;
		}
		case ')': {
			if (binary_bracket[binary_bracket.size() - 1] > unar_bracket[unar_bracket.size() - 1]) {
				node = node->parent;
				binary_bracket.pop_back();
				if (node == NULL)
					int a = 4;
			}
			else {
				unar_bracket.pop_back();
			}

			break;
		}
		case ' ':
			break;
		default:
		{
			operands.insert(str[i]);
			node->param = str[i];
			node = node->parent;
			break;
		}
		}
	}
	if (unar_bracket.size() != 1 || binary_bracket.size() != 1)
		throw std::exception("Incorrect formulа!");
	return root;
}


int solve_logic_function(map <char, int> interpretation, Tree* node)
{
	int left_value, right_value, value;
	if (node->left != NULL)
	{
		left_value = solve_logic_function(interpretation, node->left);
	}
	if (node->right != NULL)
	{
		right_value = solve_logic_function(interpretation, node->right);
	}
	if (node->left == NULL && node->right == NULL) {
		value = interpretation.at(node->param);
	}
	else
	{
		switch (node->param)
		{
		case '&':
		{
			if (left_value && right_value)
				value = 1;
			else value = 0;
			break;
		}
		case '|':
		{
			if (left_value || right_value)
				value = 1;
			else value = 0;
			break;
		}
		case '>':
		{
			if (left_value && !right_value)
				value = 0;
			else value = 1;
			break;
		}
		case '~':
		{
			if (left_value == right_value)
				value = 1;
			else value = 0;
			break;
		}
		}
	}

	if (node->sign == 0)
		return value;
	else if (value == 0)
		return 1;
	else
		return 0;
}

void generateCombinations(vector<vector<int>>& result, vector<int>& current, int n, int pos) {
	if (pos == n) {
		result.push_back(current);
		return;
	}

	current[pos] = 0;
	generateCombinations(result, current, n, pos + 1);

	current[pos] = 1;
	generateCombinations(result, current, n, pos + 1);
}

vector<vector<int>> generateCombinations(int n) {
	vector<vector<int>> result;
	vector<int> current(n, 0);
	generateCombinations(result, current, n, 0);
	return result;
}

void Del_Tree(Tree* t) {
	if (t) {
		Del_Tree(t->left);
		Del_Tree(t->right);
		delete t;
	}
}

int main()
{
	setlocale(LC_ALL, "ru");

	cout << "Выберите Логическую функцию" << endl;
	cout << "1. ((a | b) & (!c))" << endl;
	cout << "2. (!(((!a)|c)&(!((!b)&d))))" << endl;
	cout << "3. (!((S->((!R)|(P&Q)))~(P&(!(Q->R)))))" << endl;
	cout << "4. (((!P)->(Q&R))~((!(!(P|Q)))->S))" << endl;
	cout << "5. ( (((a|b)|c)&((a|b)|(!c)))&((a|(!b))|c) )" << endl;


	int swich;
	cout << "Ваш выбор: ";
	cin >> swich;

	char str[100] = ""; 

	switch (swich) {
	case 1:
		strcpy_s(str, "((a|b)&(!c))");
		break;
	case 2:
		strcpy_s(str, "(!(((!a)|c)&(!((!b)&d))))");
		break;
	case 3:
		strcpy_s(str, "(!((S->((!R)|(P&Q)))~(P&(!(Q->R)))))");
		break;
	case 4:
		strcpy_s(str, "(((!P)->(Q&R))~((!(!(P|Q)))->S))");
		break;
	case 5:
		strcpy_s(str, "((!a)->(b|c))");
		break;
	case 6: 
		strcpy_s(str, "((!a)->(b|c))");
		break;
	default:
		cout << "Error" << endl;
		return 0;
	}

	system("cls");

	root = new Tree;
	set <char>operands;

	root = create_tree(root, str, operands);

	vector<vector<int>> interpretations = generateCombinations(operands.size());

	vector<int> solutions;

	for (int i = 0; i < interpretations.size(); i++)
	{
		map <char, int> current_interpretation;
		int number_of_operands = 0;
		for (auto& element : operands)
		{
			current_interpretation.insert(make_pair(element, interpretations[i][number_of_operands++]));
		}
		try {
			solutions.push_back(solve_logic_function(current_interpretation, root));
		}
		catch (const std::exception& e) {
			std::cout << "Поймано исключение: " << e.what() << std::endl;
		}
	}

	cout << "Логическая функция: ";
	for (int i = 0; str[i] != '\0'; i++)
	{
		cout << str[i];
	}

	cout << "\n\nТаблица истинности: \n\n";
	for (const auto& element : operands) {
		cout << element << " ";
	}
	cout << "  Результат\n";
	for (int i = 0; i < interpretations.size(); i++)
	{
		for (size_t j = 0; j < interpretations[i].size(); j++)
		{
			cout << interpretations[i][j] << " ";
		}
		cout << "  " << solutions[i] << "\n";
	}

	cout << endl << "СКНФ: ";
	vector <char>SKNF;
	for (size_t i = 0; i < interpretations.size(); i++)
	{
		if (solutions[i] == 0)
		{
			SKNF.push_back('(');
			int j = 0;
			for (auto& element : operands)
			{
				if (interpretations[i][j] == 0)
				{
				}
				else
				{
					SKNF.push_back('!');
				}
				SKNF.push_back(element);
				SKNF.push_back('|');
				j++;
			}
			SKNF.pop_back();
			SKNF.push_back(')');
			SKNF.push_back('&');
		}
	}
	if (SKNF.size() != 0)
		SKNF.pop_back();
	for (auto& ch : SKNF) {
		std::cout << ch;
	}

	cout << endl << "СДНФ: ";
	vector <char>SDNF;
	for (size_t i = 0; i < interpretations.size(); i++)
	{
		if (solutions[i] == 1)
		{
			SDNF.push_back('(');
			int j = 0;
			for (auto& element : operands)
			{
				if (interpretations[i][j] == 1)
				{
				}
				else
				{
					SDNF.push_back('!');
				}
				SDNF.push_back(element);
				SDNF.push_back('&');
				j++;
			}
			SDNF.pop_back();
			SDNF.push_back(')');
			SDNF.push_back('|');
		}
	}
	if (SDNF.size() != 0)
		SDNF.pop_back();
	for (auto& ch : SDNF) {
		std::cout << ch;
	}

	cout << "\n\nЧисловые формы:\n";
	string form = "(";
	for (size_t i = 0; i < solutions.size(); i++)
	{
		if (solutions[i] == 0)
		{
			form += to_string(i) + ", ";
		}
	}
	if (form.size() > 1) {
		form.pop_back();
		form.pop_back();
	}
	form += ") &";
	cout << form << endl;

	form = "(";
	for (size_t i = 0; i < solutions.size(); i++)
	{
		if (solutions[i] == 1)
		{
			form += to_string(i) + ", ";
		}
	}
	if (form.size() > 1) {
		form.pop_back();
		form.pop_back();
	}
	form += ") |";
	cout << form << endl;

	cout << "Индексная форма:\n";
	int decimal = 0;
	int powerOfTwo = 1;

	for (int i = solutions.size() - 1; i >= 0; --i) {
		decimal += solutions[i] * powerOfTwo;
		powerOfTwo *= 2;
	}
	cout << decimal;
	Del_Tree(root);
	return 0;
}
