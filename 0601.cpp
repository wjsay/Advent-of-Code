#include <cstdio>
#include <iostream>
#include <algorithm>
#include <queue>
#include <cstring>
#include <map> 
using namespace std;
const int maxn = 360;
int mp[maxn][maxn];
int a[maxn], b[maxn];
int r[4] = {-1, 1, 0, 0};
int c[4] = {0, 0, -1, 1};
int bfs(int x, int y, int val) {
	queue<pair<int, int> > que;
	que.push(pair<int, int>(x, y));
	mp[x][y] = -1;
	int cnt = 0;
	bool fg = false;
	while(!que.empty()) {
		pair<int, int> v = que.front(); que.pop();
		cnt++;
		for (int i = 0; i < 4; ++i) {
			int xx = v.first + r[i], yy = v.second + c[i];
			if (xx < 0 || x >= maxn || yy < 0 || yy >= maxn) {
				fg = true;
			}else if (mp[xx][yy] == val) {
				mp[xx][yy] = -1;//遍历过了 
				que.push(pair<int, int>(xx, yy));
			}
		}
	}
	return fg ? -1 : cnt;
}

int main()
{
	freopen("data.in", "rt", stdin);
	int n = 0, x, y;
	char ch;
	while(cin >> x >> ch >> y) {
		a[++n] = y;
		b[n] = x;
		mp[y][x] = n;
	}
	for (int i = 0; i < maxn; ++i) {
		for (int j = 0; j < maxn; ++j) {
			if (mp[i][j] != 0) continue;
			multimap<int, int> mymap;
			int minV = 0x3f3f3f3f, cnt(0), v(0); 
			for (int k = 1; k <= n; ++k) { // 点(i, j) 到 k点的距离 
				int d = abs(a[k] - i) + abs(b[k] - j);
				if (minV > d) {
					minV = d;
					cnt = 1; 
					v = k;
				}
				else if (minV == d) {
					cnt++;
				} 
			}
			if (cnt == 1) {
				mp[i][j] = v;
			}
		}
	}
	int maxV = 0;
	for (int i = 0; i < maxn; ++i) {
		for (int j = 0; j < maxn; ++j) if (mp[i][j] != -1){
			maxV = max(maxV, bfs(i, j, mp[i][j]));
		} 
	}
	cout << maxV << endl;

	return 0;
}

