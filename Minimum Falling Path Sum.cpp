#include <iostream>
#include <vector>
#include <climits>
using namespace std;

class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& matrix) {
        int n = matrix.size();
        vector<vector<int>> dp(n + 1, vector<int>(n + 1));

        // Initialize last row
        for (int j = 0; j < n; ++j)
            dp[n - 1][j] = matrix[n - 1][j];

        // Fill DP table from bottom to top
        for (int i = n - 2; i >= 0; --i) {
            for (int j = 0; j < n; ++j) {
                int ans = dp[i + 1][j]; // Below

                if (j > 0) // Below-left
                    ans = min(ans, dp[i + 1][j - 1]);

                if (j < n - 1) // Below-right
                    ans = min(ans, dp[i + 1][j + 1]);

                dp[i][j] = ans + matrix[i][j];
            }
        }

        int ans = INT_MAX;
        for (int j = 0; j < n; ++j)
            ans = min(ans, dp[0][j]);

        return ans;
    }
};

int main() {
    int n;
    cout << "Enter the size of the square matrix: ";
    cin >> n;

    vector<vector<int>> matrix(n, vector<int>(n));

    cout << "Enter the matrix elements:\n";
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> matrix[i][j];
        }
    }

    Solution sol;
    cout << "Minimum Falling Path Sum: " << sol.minFallingPathSum(matrix) << endl;

    return 0;
}