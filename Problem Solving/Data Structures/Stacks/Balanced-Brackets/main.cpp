#include <bits/stdc++.h>

using namespace std;
bool isempty(int t){
    if(t==-1){
        return true;
    }
    else{
        return false;
    }
}
// Complete the isBalanced function below.
string isBalanced(string s) {
    int top=-1;
    char d[s.size()];
    int flag=0,i;
    for(int i=0;i<s.size();i++){
        if((s[i]=='(') || (s[i]=='[') || (s[i]=='{')){
            top=top+1;
            d[top]=s[i];
        }
        else if(s[i]==')'){
            if(isempty(top)){
                flag=1;
                return "NO";
            }
            else if(d[top]=='('){
                top=top-1;
            }
            else{
                flag=1;
                return "NO";
            }
        }
        else if(s[i]==']'){
            if(isempty(top)){
                flag=1;
                return "NO";
            }
            else if(d[top]=='['){
                top=top-1;
            }
            else{
                flag=1;
                return "NO";
            }
        }
        else if(s[i]=='}'){
            if(isempty(top)){
                flag=1;
                return "NO";
            }
            else if(d[top]=='{'){
                top=top-1;
            }
            else{
                flag=1;
                return "NO";
            }
        }
    }
    if(flag!=1){
        if(isempty(top)){
            return "YES";
        }
        else{
            return "NO";
        }
    }
    return "a";
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int t;
    cin >> t;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for (int t_itr = 0; t_itr < t; t_itr++) {
        string s;
        getline(cin, s);

        string result = isBalanced(s);

        fout << result << "\n";
    }

    fout.close();

    return 0;
}
