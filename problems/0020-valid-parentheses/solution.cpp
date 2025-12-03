#include <deque>
#include <string>
#include <vector>

class Solution {
public:
    bool isValid(std::string s) {
        std::deque<char> par_stack = std::deque<char>();

        char open[3] = { '(', '[', '{' };
        char close[3] = { ')', ']', '}' };

        for (char c : s) {
            for (int i = 0; i < 3; ++i) {
                if (c == open[i]) {
                    par_stack.push_back(c);
                    break;
                } else if (c == close[i]) {
                    if (par_stack.empty() || par_stack.back() != open[i]) {
                        return false;
                    }
                    par_stack.pop_back();
                    break;
                } else if (i == 2) {
                    return false;
                }
            }
        }
        return par_stack.empty();
    }
};

int main([[maybe_unused]] int argc, [[maybe_unused]] char* argv[]) {
    return 0;
}
