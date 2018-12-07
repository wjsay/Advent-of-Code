#include <cstdio>
#include <iostream>
#include <algorithm>
#include <queue>
#include <cstring>
using namespace std;
const int maxn = 100 + 7, N = 27, WORKER_COUNT = 5, SCORE = 60;
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
struct Node {
	int id, time;
	Node(int id, int time):id(id), time(time){}
	Node(){}
	bool operator < (const Node rhd) const {
		return time == rhd.time ? id > rhd.id : time > rhd.time;
	}
};
int work() {
	int timer = 0;
	priority_queue<int, vector<int>, greater<int> > pq;
	priority_queue<Node> worker, tmp;
	for (int i = 1; i < N; ++i) if(vis[i] && d[i] == 0) {
		pq.push(i);
	}
	while(!pq.empty() || !worker.empty()) {
		while(!pq.empty() && worker.size() < WORKER_COUNT) {
			int u = pq.top();
			pq.pop();
			worker.push(Node(u, u + SCORE));
		}
		// start working...
		if (!worker.empty()) {
			Node node = worker.top();
			int minV = node.time;
			timer += minV;
			while(!worker.empty()) {
				node = worker.top();
				int id =  node.id;
				int t = node.time;
				if (t - minV > 0) {
					tmp.push(Node(id, t-minV));
				}else if (t - minV == 0) {
					for (int i = head[id]; ~i; i = e[i].nxt) {
						int v = e[i].to;
						if (--d[v] == 0) {
							pq.push(v);
						}
					}
				}
				worker.pop();
			}
		}
		swap(worker, tmp);
	}
	return timer;
}

int main()
{
	freopen("input.txt", "rt", stdin);
	init();
	string line;
	while(getline(cin, line)) {
		int u = line[5] - '@', v = line[36] - '@';
		add(u, v);
		d[v]++;
		vis[u] = vis[v] = true;
	}
	cout << work() << endl;

	return 0;
}

