/*
Limak is an old brown bear. He often plays poker with his friends. Today they went to a casino. There are n players (including Limak himself) and right now all of them have bids on the table. i-th of them has bid with size ai dollars.

Each player can double his bid any number of times and triple his bid any number of times. The casino has a great jackpot for making all bids equal. Is it possible that Limak and his friends will win a jackpot?

Input
    
    First line of input contains an integer n (2 ≤ n ≤ 105), the number of players.

    The second line contains n integer numbers a1, a2, ..., an (1 ≤ ai ≤ 109) — the bids of players.

Output

    Print "Yes" (without the quotes) if players can make their bids become equal, or "No" otherwise.

Examples:
    input
        4
        75 150 75 50
    output
        Yes
    
    input
        3
        100 150 250
    output
        No
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
 
ll solve(ll num){
	while(num % 2 == 0) num /= 2;
	while(num % 3 == 0) num /= 3;

	return num;
}

int main() {
    ios_base::sync_with_stdio(false);

	const int N = 2e5 + 10;
	int n, v[N]; cin >> n;
	for(int i = 0; i < n; i++)
		cin >> v[i];
	
	int ans[N];
	for(int i = 0; i < n; i++)
		ans[i] = solve(v[i]);
	
	for(int i = 0; i < n; i++){
		int pattern = ans[0];
		if(ans[i] != pattern){
			cout << "No" << endl;
			return 0;
		}
	}
	
	cout << "Yes" << endl;
    return 0;
}