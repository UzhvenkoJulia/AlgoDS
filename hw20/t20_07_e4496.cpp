// Дерево відрізків.
// Завдання для самостійної роботи
// 20.7. Пригоди Незнайки та його друзів
// Вказівка. У кожному завданні має бути побудоване та використане дерево відрізків.

#include <iostream>
#include <vector>

using namespace std;

// дерево відрізків для підтримки сум на відрізках і оновлень окремих елементів
class SegmentTree {
private:
    vector <long long> tree;
    int size;

    void build(const vector<int>& weights, int node, int l, int r) {
        if (l == r) {
            tree[node] = weights[l]; // вузол листок
        } else {
            int mid = (l + r) / 2;
            build(weights, 2 * node, l, mid);
            build(weights, 2 * node + 1, mid + 1, r);
            tree[node] = tree[2 * node] + tree[2 * node + 1]; // внутрішній вузол
        }
    }

    void update(int node, int l, int r, int index, int value) {
        if (l == r) {
            tree[node] = value;
        } else {
            int mid = (l + r) / 2;
            if (index <= mid) update(2 * node, l, mid, index, value);
            else update(2 * node + 1, mid + 1, r, index, value);
            tree[node] = tree[2 * node] + tree[2 * node + 1];
        }
    }

    // бінарний пошук
    int upperBound(int node, int l, int r, long long capacity) {
        if (tree[node] <= capacity) return r + 1; // всі в цьому піддереві можуть сісти
        if (l == r) return l; // вже на одному елементі - далі не можна

        int mid = (l + r) / 2;
        if (tree[2 * node] > capacity) {
            return upperBound(2 * node, l, mid, capacity);
        } else {
            return upperBound(2 * node + 1, mid + 1, r, capacity - tree[2 * node]);
        }
    }


public:
    SegmentTree(const vector<int>& weights) {
        size = weights.size();
        tree.resize(4 * size);
        build(weights, 1, 0, size - 1);
    }

    void update(int index, int value) {
        update(1, 0, size - 1, index, value);
    }

    int countFit(long long capacity) {
        int idx = upperBound(1, 0, size - 1, capacity);
        return idx; // повертає позицію, до якої влізли чоловічки
    }
};

int main() {
    ios::sync_with_stdio(false);  // scanf/printf = cin і cout
    cin.tie(nullptr);  // відв'язує cin від cout
    // перед кожним cin автоматично викликається cout.flush()
    // cin більше не чекає, поки cout завершить вивід

    // використовуюється для оптимізації швидкості вводу-виводу

    int n;
    cin >> n;
    vector<int> weights(n);
    for (int i = 0; i < n; ++i) {
        cin >> weights[i];
    }

    SegmentTree seg(weights);

    int m;
    cin >> m;
    while (m--) {  // постфіксний декремент -> зменшення значення змінної m на 1
        int t;
        cin >> t;
        if (t == 1) {
            long long v;
            cin >> v;
            int result = seg.countFit(v);
            cout << result << "\n";
        } else if (t == 2) {
            int x, y;
            cin >> x >> y;
            seg.update(x - 1, y); // індексація з 0
        }
    }
    return 0;
}