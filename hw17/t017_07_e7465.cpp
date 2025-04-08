// Бінарні дерева. Бінарні дерева пошуку.
// Завдання для самостійної роботи
// 17.7. Однакові дерева (100%)
// Вказівка 1. У кожному завданні має бути реалізоване та використане бінарне дерево.
// Вказівка 2. Дерево має бути реалізоване як рекурсивна структура.


#include <iostream>

using namespace std;


class TreeNode {
public:
    int val;         // у поточному вузлі
    TreeNode *left;  // вказівник 
    TreeNode *right; 

    // конструктор для ініціалізації значення вузла
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Tree {
public:
    TreeNode *head; 

    // порожнє дерево
    Tree() : head(NULL) {}

    // метод для вставки значення
    void Insert(int val) {
        // якщо дерево порожнє, створюємо корінь
        if (head == NULL) {
            head = new TreeNode(val);
        } else {
            InsertRecursive(head, val); 
        }
    }

    void InsertRecursive(TreeNode* node, int val) {
        // якщо значення менше за поточне, йдемо в ліве піддерево
        if (val < node->val) {
            if (node->left == NULL) {
                node->left = new TreeNode(val);
            } else {
                InsertRecursive(node->left, val);
            }
        }
        // якщо значення більше або рівне поточному, йдемо в праве піддерево
        else {
            if (node->right == NULL) {
                node->right = new TreeNode(val);
            } else {
                InsertRecursive(node->right, val);
            }
        }
    }

    // метод для перевірки, чи є два дерева однаковими
    int IsSameTree(Tree *p) {
        return IsSameRecursive(this->head, p->head);
    }

    int IsSameRecursive(TreeNode* node1, TreeNode* node2) {
        // якщо обидва дерева порожні, вони однакові
        if (node1 == NULL && node2 == NULL) {
            return 1;
        }
        // якщо лише одне дерево порожнє або значення не збігаються, дерева не однакові
        if (node1 == NULL || node2 == NULL || node1->val != node2->val) {
            return 0;
        }
        return IsSameRecursive(node1->left, node2->left) && IsSameRecursive(node1->right, node2->right);
    }
};

int main() {

    int n, m;
    cin >> n;  // читання елем преш

    int arr1[n];  // оголош масив

    for (int i = 0; i < n; i++) {
        cin >> arr1[i];
    }

    cin >> m;

    int arr2[m];

    for (int i = 0; i < m; i++) {
        cin >> arr2[i];
    }

    Tree tree1, tree2;

    // вставл знач з масивів в два дерева
    for (int i = 0; i < n; i++) {
        tree1.Insert(arr1[i]);
    }

    for (int i = 0; i < m; i++) {
        tree2.Insert(arr2[i]);
    }

    if (tree1.IsSameTree(&tree2)) {
        cout << 1 << endl; 
    } else {
        cout << 0 << endl; 
    }

    return 0;
}