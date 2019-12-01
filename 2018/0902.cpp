#include <iostream>
#include <malloc.h>
#include <algorithm>
using namespace std;
const int player_count = 432, last_marble = 71019 * 100; # 改数据！
typedef struct CircleNode {
	int val;
	CircleNode * pre;
	CircleNode * nxt;
	CircleNode(){}
	CircleNode(int val, CircleNode* pre, CircleNode*nxt):val(val), pre(pre), nxt(nxt){}
	CircleNode* insert(int value) {
		CircleNode *p = (CircleNode*)malloc(sizeof(CircleNode));
		p->val = value;
		this->pre->nxt = p;
		p->pre = this->pre;
		this->pre = p;
		p->nxt = this;
		return p;
	}
	CircleNode* del() {
		CircleNode *p = this->nxt;
		this->pre->nxt = this->nxt;
		this->nxt->pre = this->pre;
		free(this);
		return p;
	}
}*CircleLink;

void test(CircleLink p) {
	for (int i = 0; i < 25; ++i) {
		cout << p->val << ' ';
		p = p->nxt;
	}
	cout << endl;
	getchar();
}

int main()
{
	CircleLink p = (CircleLink)malloc(sizeof(CircleNode));
	CircleLink T = p;
	p->pre = p->nxt = p; p->val = 0;
	p = p->insert(1);
	int this_marble = 2;
	int this_player = 2;
	long long palyer_score_list[player_count] = { 0 };
	while (this_marble <= last_marble) {
		if (this_marble % 23 == 0) {
			palyer_score_list[this_player] += this_marble;
			p = p->pre->pre->pre->pre->pre->pre->pre;
			palyer_score_list[this_player] += p->val;
			p = p->del();
		}
		else {
			p = p->nxt->nxt;
			p = p->insert(this_marble);
		}
		this_marble += 1;
		this_player = (this_player + 1) % player_count;
	}
	long long maxV = 0;
	for (int i = 0; i < player_count; ++i) {
		maxV = max(maxV, palyer_score_list[i]);
	}
	cout << maxV << endl;

	return 0;
}