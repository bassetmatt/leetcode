#include <vector>
#include <fmt/base.h>

class Solution {
public:

};

struct TestCase {};

int test() {
    Solution solution;
    TestCase test_cases[] = {};
    int error_found = 0;
    for (auto& test_case : test_cases) {
        if (false) {
            fmt::print(stderr,
                "Test failed"
            );
            ++error_found;
        }
    }
    return error_found;
}

int main([[maybe_unused]] int argc, [[maybe_unused]] char* argv[]) {
    int errors = test();
    if (errors == 0) {
        fmt::print(stderr, "All test cases passed!\n");
    } else {
        fmt::print(stderr, "{} test case(s) failed.\n", errors);
        return 1;
    }
    return 0;
}
