// 13.6. З префіксного у інфіксне (100%)

// буду писати на С++, бо на python за часом не проходить тести, не на 100%

#include <iostream>
#include <stack>
#include <string>

using namespace std;

struct Element {
    string value;
    int precedence;
};

string convertToInfix(const string& expression) {
    // string& – це передача рядка (string) за посиланням (&), що дозволяє уникнути зайвого копіювання даних
    stack<Element> stk;
    // stk – це ім'я змінної, яка є об'єктом цього стеку

    for (int i = (int)expression.size() - 1; i >= 0; --i) {
        // (int)expression.size() - 1 означає, що i починається з останнього індексу рядка (тобто рухаємося з кінця рядка на початок)
        // на кожній ітерації i зменшується на 1 (рухаємось у зворотному напрямку)

        char symbol = expression[i];
        // char (скорочено від character) — це тип даних у C++, який використовується для зберігання одного символу
        if (isalpha(symbol)) {
            stk.push({string(1, symbol), 3});
            // літери мають найвищий пріоритет у виразі

        } else {

            int currentPrecedence = (symbol == '+' || symbol == '-') ? 1 : 2;
            // якщо умова істинна (true), виконується перше значення (1 у цьому випадку)
            // якщо умова хибна (false), виконується друге значення (2 у цьому випадку)

            Element leftOperand = stk.top(); stk.pop();
            Element rightOperand = stk.top(); stk.pop();

            string leftStr = leftOperand.value;
            string rightStr = rightOperand.value;

            if (leftOperand.precedence < currentPrecedence) { 
                leftStr = "(" + leftStr + ")";
            }
            if (rightOperand.precedence < currentPrecedence ||
                (rightOperand.precedence == currentPrecedence && (symbol == '-' || symbol == '/'))) {
                rightStr = "(" + rightStr + ")";
                // && - логічне "і"
            }

            stk.push({leftStr + symbol + rightStr, currentPrecedence});
        }
    }
    return stk.empty() ? "" : stk.top().value;
    // тернарний оператор (?:), який є скороченою формою if-else
}

int main() {
    string input;
    cin >> input;
    cout << convertToInfix(input);
    cout.flush(); // очищення буфера вручну
}