#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <map>

using namespace std;

vector<string> solution(vector<string> players, vector<string> callings) {
    vector<string> answer;
    string tmp;
    int current_rank;
    int front, rear;
    
    map<string,int> rank;
    
    for(int i =0;i<players.size();i++){
        rank[players[i]] = i;
    }
    
    
    for(int idx=0;idx<callings.size();idx++){
        
        rear = rank[callings[idx]];
        front = rear - 1;
        rank[players[rear]]--;
        rank[players[front]]++;
        
        tmp = players[rear];
        players[rear] = players[front];
        players[front]= tmp;
    }
    
    answer=players;
    return answer;
}