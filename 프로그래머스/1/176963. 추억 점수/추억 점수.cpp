#include <string>
#include <vector>
#include <map>
#include <iostream>
using namespace std;

vector<int> solution(vector<string> name, vector<int> yearning, vector<vector<string>> photo) {
    vector<int> answer;
    map<string, int> score_map;
    
    for(int i =0; i<name.size();i++){
        score_map[name[i]] = yearning[i];
        
    }
    answer.assign(photo.size(),0);
    for(int i=0;i<photo.size();i++){
        for(int j =0; j<photo[i].size();j++){
            
            if(score_map[photo[i][j]]){
                
                answer[i] += score_map[photo[i][j]];
            }
            else{
                continue;
            }
        }
    }
    return answer;
}