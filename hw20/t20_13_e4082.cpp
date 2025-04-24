// Дерево відрізків.
// Завдання для самостійної роботи
// 20.13. Добуток на відрізку
// Вказівка. У кожному завданні має бути побудоване та використане дерево відрізків.

#include <iostream>
#include <vector>
#include <string>

using namespace std;

int sign(int x) {
    if (x > 0) return 1;
    if (x < 0) return -1;
    return 0;
}

class SegmentTree {
    vector<int> tree;
    int n;

public:
    SegmentTree(const vector<int>& data) {
        n = data.size();
        tree.resize(4 * n); 
        build(1, 0, n - 1, data);
    }

    void build(int node, int l, int r, const vector<int>& data) {
        if (l == r) {
            tree[node] = sign(data[l]);
            return;
        }
        int mid = (l + r) / 2;
        build(2 * node, l, mid, data);
        build(2 * node + 1, mid + 1, r, data);
        tree[node] = tree[2 * node] * tree[2 * node + 1]; // зберіг знак добутку
    }

    // оновлення значення у позиції pos на val
    void update(int node, int l, int r, int pos, int val) {
        if (l == r) {
            tree[node] = sign(val);
            return;
        }
        int mid = (l + r) / 2;
        if (pos <= mid)
            update(2 * node, l, mid, pos, val);
        else
            update(2 * node + 1, mid + 1, r, pos, val);
        tree[node] = tree[2 * node] * tree[2 * node + 1]; 
    }

    // добуток знаків [ql, qr]
    int query(int node, int l, int r, int ql, int qr) {
        if (qr < l || r < ql) return 1; // нейтрал елем
        if (ql <= l && r <= qr) return tree[node];
        int mid = (l + r) / 2;
        int left = query(2 * node, l, mid, ql, qr);
        int right = query(2 * node + 1, mid + 1, r, ql, qr);
        return left * right;
    }

    void update(int pos, int val) {
        update(1, 0, n - 1, pos, val);
    }

    int query(int l, int r) {
        return query(1, 0, n - 1, l, r);
    }
};

int main() {

    ios::sync_with_stdio(false); 
    cin.tie(nullptr);            

    int n, k;
    while (cin >> n >> k) {
        vector<int> data(n);
        for (int i = 0; i < n; ++i) {
            cin >> data[i];
        }

        SegmentTree seg(data);
        string result;

        for (int i = 0; i < k; ++i) {
            char cmd;  // збереження команди з вхідних даних
            int a, b;
            cin >> cmd >> a >> b;
            if (cmd == 'C') {
                seg.update(a - 1, b); // a-1
            } else if (cmd == 'P') {
                int res = seg.query(a - 1, b - 1); // [a-1, b-1]
                if (res > 0) result += '+';
                else if (res < 0) result += '-';
                else result += '0';
            }
        }

        cout << result << '\n';
    }
    return 0;
}