/*
Kevin Sun wants to move his precious collection of n cowbells from Naperthrill to Exeter, where there is actually grass instead of corn. Before moving, he must pack his cowbells into k boxes of a fixed size. In order to keep his collection safe during transportation, he won't place more than two cowbells into a single box. Since Kevin wishes to minimize expenses, he is curious about the smallest size box he can use to pack his entire collection.

Kevin is a meticulous cowbell collector and knows that the size of his i-th (1 ≤ i ≤ n) cowbell is an integer si. In fact, he keeps his cowbells sorted by size, so si - 1 ≤ si for any i > 1. Also an expert packer, Kevin can fit one or two cowbells into a box of size s if and only if the sum of their sizes does not exceed s. Given this information, help Kevin determine the smallest s for which it is possible to put all of his cowbells into k boxes of size s.

Input
    
    The first line of the input contains two space-separated integers n and k (1 ≤ n ≤ 2·k ≤ 100 000), denoting the number of cowbells and the number of boxes, respectively.

    The next line contains n space-separated integers s1, s2, ..., sn (1 ≤ s1 ≤ s2 ≤ ... ≤ sn ≤ 1 000 000), the sizes of Kevin's cowbells. It is guaranteed that the sizes si are given in non-decreasing order.

Output

    Print a single integer, the smallest s for which it is possible for Kevin to put all of his cowbells into k boxes of size s.

Examples:
    input
        2 1
        2 5
    output
        7
    
    input
        4 3
        2 3 5 9
    output
        9
    
    input
        3 2
        3 5 7
    output
        8
*/

#include <bits/stdc++.h>
using namespace std;

#define pb		push_back
#define eb		emplace_back
#define mk		make_pair
#define fi		first
#define se		second
#define cc(x)	cout << #x << " = " << x << endl
#define ok		cout << "ok" << endl
#define endl	'\n'

typedef long long ll;
typedef pair<int,int> ii;
const int INF = 0x3f3f3f3f;
const double PI = acos(-1.0);
 
const int N = 1e5 + 10;
int sizes[N];

int solve(int mid, int k, int n){
	int left = 0;
	int right = n - 1;
	
	while(left < right){
		if(sizes[left] + sizes[right] <= mid){
			left++;
			right--;
			k--;
		} else if(sizes[right] <= mid) {
			right--;
			k--;
		}
	}
	
	if(left == right){
		if(sizes[left] <= mid) k--;
		else return 0;
	}
	
	if(k < 0) return 0;
	return 1;
}

int main() {
    ios_base::sync_with_stdio(false);

	int n, k;
	cin >> n >> k;
	
	for(int i = 0; i < n; i++)
		cin >> sizes[i];
	
	int low = sizes[n-1];
	int high = sizes[n-1] + sizes[n-2];
	
	while(low < high){
		int mid = (low + high)/2;
		if(solve(mid, k, n)){
			high = mid;	
		} else {
			low = mid + 1;	
		}
	}
	
	cout << low << endl;
    return 0;
}