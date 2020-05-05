#include <iostream>
#include <algorithm>
#include <vector>
#include <unordered_map>

using namespace std;

enum Type {
    PRINT,
    PRINTLN,
    LET,
    IF_GOTO
};

struct Command {
    // Print vs Println vs Let vs If_Goto
    Type type;

    // Number (id)
    int label;

    // var index for prints
    // var index for if_Goto
    // number literal for if_goto
    // var index for let
    // number literal for let
    int a;

    // var index for if_Goto
    // number literal for if_goto
    // var index for let (if binary)
    // number literal for let (if binary)
    int b;

    // Compare function for if_goto
    // Math operation for let
    int (*op)(int, int);

    // goto label for if_goto
    // lhs variable for let
    int _goto;

    // check if a is var for print
    // check if a is var for if_goto
    // check if a is var for let
    bool a_isvar;

    // check if b is var for if_goto
    // check if b is var for let (if binary)
    bool b_isvar;

    // String literal for prints
    string str;

    Command(std::string line) {
        int start = 0, end = line.find(' ');
        this->label = stoi(line.substr(start, end - start));

        start = end + 1;
        end = line.find(' ', start);
        if (line[start] == 'L') {
            this->type = Type::LET;
        } else if (line[start] == 'I') {
            this->type = Type::IF_GOTO;
        } else if (line[end-1] == 'N') {
            this->type = Type::PRINTLN;
        } else {
            this->type = Type::PRINT;
        }
        start = end + 1;

        if (this->type == Type::PRINT || this->type == Type::PRINTLN) {
            if (line[start] == '"') {
                this->str = line.substr(start + 1, line.size() - start - 2);
                this->a_isvar = false;
            } else {
                this->a = (int)line[start]-65;
                this->a_isvar = true;
            }
        } else if (this->type == Type::IF_GOTO) {
            end = line.find(' ', start);
            if (line[start] >= 'A' && line[start] <= 'Z') {
                this->a = (int)line[start]-65;
                this->a_isvar = true;
            } else {
                this->a = stoi(line.substr(start, end - start));
                this->a_isvar = false;
            }
            start = end+1;
            end = line.find(' ', start);

            string ostr = line.substr(start, end - start);
            if (ostr == "=") {
                this->op = [](int x, int y) { return x==y ? 1 : 0; };
            } else if (ostr == ">") {
                this->op = [](int x, int y) { return x>y ? 1 : 0; };
            } else if (ostr == "<") {
                this->op = [](int x, int y) { return x<y ? 1 : 0; };
            } else if (ostr == "<>") {
                this->op = [](int x, int y) { return x!=y ? 1 : 0; };
            } else if (ostr == "<=") {
                this->op = [](int x, int y) { return x<=y ? 1 : 0; };
            } else {
                this->op = [](int x, int y) { return x>=y ? 1 : 0; };
            }
            start = end+1;
            end = line.find(' ', start);

            if (line[start] >= 'A' && line[start] <= 'Z') {
                this->b = (int)line[start]-65;
                this->b_isvar = true;
            } else {
                this->b = stoi(line.substr(start, end - start));
                this->b_isvar = false;
            }
            for (int i = 0; i < 3; i++) {
                start = end+1;
                end = line.find(' ', start);
            }
            this->_goto = stoi(line.substr(start, end-start));
        } else {
            this->_goto = (int)line[start]-65;
            start += 4;
            end = line.find(' ', start);
            // Single rhs
            if (end == string::npos) {
                if (line[start] >= 'A' and line[start] <= 'Z') {
                    this->a = (int)line[start]-65;
                    this->a_isvar = true;
                } else {
                    this->a = stoi(line.substr(start, line.size()-start));
                    this->a_isvar = false;
                }
                this->op = [](int x, int y) { return x; };
            } else {
                if (line[start] >= 'A' and line[start] <= 'Z') {
                    this->a = (int)line[start]-65;
                    this->a_isvar = true;
                } else {
                    this->a = stoi(line.substr(start, end-start));
                    this->a_isvar = false;
                }
                start = end+1;
                end = line.find(' ', start);

                if (line[start] == '+') {
                    this->op = [](int x, int y) { return x+y; };
                } else if (line[start] == '-') {
                    this->op = [](int x, int y) { return x-y; };
                } else if (line[start] == '*') {
                    this->op = [](int x, int y) { return x*y; };
                } else {
                    this->op = [](int x, int y) { return x/y; };
                }
                start = end+1;
                end = line.find(' ', start);

                if (line[start] >= 'A' and line[start] <= 'Z') {
                    this->b = (int)line[start]-65;
                    this->b_isvar = true;
                } else {
                    this->b = stoi(line.substr(start, end-start));
                    this->b_isvar = false;
                }
            }
        }
    }

    int exec(int i, vector<int>& variables, unordered_map<int,int>& label_to_index) {
        if (this->type == Type::LET) {
            int _a = this->a_isvar ? variables[this->a] : this->a;
            int _b = this->b_isvar ? variables[this->b] : this->b;
            variables[this->_goto] = this->op(_a,_b);
        } else if (this->type == Type::IF_GOTO) {
            int _a = this->a_isvar ? variables[this->a] : this->a;
            int _b = this->b_isvar ? variables[this->b] : this->b;
            if (this->op(_a,_b)) return label_to_index[this->_goto];
        } else {
            if (this->a_isvar) {
                cout << variables[this->a];
            } else {
                cout << this->str;
            }
            if (this->type == Type::PRINTLN) cout << '\n';
        }
        return i+1;
    }
};

bool compare_cmd(const Command& lhs, const Command& rhs) {
    return lhs.label < rhs.label;
}

int main() {

    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    vector<Command> commands;
    string line;
    while (getline(cin, line)) {
        commands.push_back(Command(line));
    }

    sort(commands.begin(), commands.end(), compare_cmd);

    unordered_map<int, int> label_to_index((commands.size() * 4)/3);
    vector<int> variables(26, 0);
    int index = 0;
    for (vector<Command>::iterator it = commands.begin(); it != commands.end(); ++it) {
        label_to_index[it->label] = index++;
    }
    index = 0;

    while (index < commands.size()) {
        index = commands[index].exec(index, variables, label_to_index);
    }

    return 0;
}