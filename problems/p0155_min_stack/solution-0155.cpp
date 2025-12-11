#include <vector>
#include <fmt/base.h>

struct StackNode {
    int value;
    int stack_min;
};

class MinStack {
private:
    std::vector<StackNode> stack;
    int stack_min;

public:
    MinStack() {
        stack = std::vector<StackNode>();
        stack_min = __INT32_MAX__;
    }

    void push(int val) {
        StackNode node = StackNode(val, stack_min);
        stack.push_back(node);
        stack_min = (val < stack_min) ? val : stack_min;
    }

    void pop() {
        stack_min = stack.back().stack_min;
        stack.pop_back();
    }

    int top() {
        return stack.back().value;
    }

    int getMin() {
        return stack_min;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */

int main([[maybe_unused]] int argc, [[maybe_unused]] char* argv[]) {
    fmt::println("No test for this problem");
    return 0;
}
