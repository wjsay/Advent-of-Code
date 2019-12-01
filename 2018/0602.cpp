#include <cstdio>
#include <iostream>
#include <algorithm>
#include <queue>
#include <cstring>
#include <map> 
using namespace std;
const int maxn = 360 + 200, MAXN = 10000, OFFSET = 100;
int a[maxn], b[maxn];
int main()
{
	freopen("data.in", "rt", stdin);
	int n = 0, x, y;
	char ch;
	while(cin >> x >> ch >> y) {
		a[++n] = y + OFFSET;
		b[n] = x + OFFSET;
	}
	int cnt(0);
	for (int i = 0; i < maxn; ++i) {
		for (int j = 0; j < maxn; ++j) {
			int sum = 0;
			for (int k = 1; k <= n; ++k) {
				if(sum < MAXN) sum += abs(a[k] - i) + abs(b[k] - j);
				else break;
			}
			cnt += (sum < MAXN);		
		}
	}
	cout << cnt << endl;

	return 0;
}
// 44667
