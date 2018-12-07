#include <cstdio>
#include <iostream>
#include <algorithm>
#include <queue>
#include <cstring>
using namespace std;
const int maxn = 100 + 7, N = 26;
struct Edge {
	int to, nxt;
}e[maxn];
int tot, head[N], d[N];
bool vis[N];
void init() {
	tot = 0;
	memset(d, 0, sizeof d);
	memset(vis, 0, sizeof vis);
	memset(head, -1, sizeof head);
}
void add(int u, int v) {
	e[tot].to = v;
	e[tot].nxt = head[u];
	head[u] = tot++;
}

string work() {
	string res = "";
	priority_queue<int, vector<int>, greater<int> > pq;
	for (int i = 0; i < N; ++i) if(vis[i] && d[i] == 0) {
		pq.push(i);
	}
	while(!pq.empty()) {
		int u = pq.top(); pq.pop();
		res += (u + 'A');
		for (int i = head[u]; ~i; i = e[i].nxt) {
			int v = e[i].to;
			if (--d[v] == 0) pq.push(v);
		}
	}
	return res;
}

int main()
{
	freopen("tmp.txt", "rt", stdin);
	init();
	string line;
	while(getline(cin, line)) {
		int u = line[5] - 'A', v = line[36] - 'A';
		add(u, v);
		d[v]++;
		vis[u] = vis[v] = true;
	}
	cout << work() << endl;

	return 0;
}
