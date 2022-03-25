#include <bits/stdc++.h>
using namespace std;
const long long INF = 1LL << 60;

// 二分探索アルゴリズム
bool P(int x) {
    }
int binary_search() {
    int left, right;
    while (right - left > 1) {
        int mid = left + (right - left) / 2;
        int (P(mid)) right = mid;
        else left = mid;
        }
    return right;
    }

// 動的計画法
int main(void) {
    int n;
    cin >> n;
    vactor<long long> h(n);
    for (int i = 0; i < n; ++i) cin >> h[i];    
    vector<long long> dp(n, INF);
    dp[0] = 0
    for (int i = 1; i < n; ++i) {
        if (i == 1) dp[i] = abs(h[i] - h[i - 1]);
        else dp[i] = min(dp[i - 1] + abs(h[i] - h[i - 1]),
            dp[i - 2] + abs(h[i] - h[i - 2]));
        }
    cout << dp[n - 1] << endl;
    }
