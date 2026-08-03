#include <iostream>
#include <queue>
#include <vector>
#include <sstream>
#include <algorithm>
using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right)
        : val(x), left(left), right(right) {}
};

class Solution {
public:
    pair<int, int> dp(TreeNode* node) {
        if (!node) return {0, 0};  // {robbed, not_robbed}

        auto [leftRobbed, leftNotRobbed] = dp(node->left);
        auto [rightRobbed, rightNotRobbed] = dp(node->right);

        int robbed = node->val + leftNotRobbed + rightNotRobbed;
        int notRobbed = max(leftRobbed, leftNotRobbed) +
                        max(rightRobbed, rightNotRobbed);

        return {robbed, notRobbed};
    }

    int rob(TreeNode* root) {
        auto [robbed, notRobbed] = dp(root);
        return max(robbed, notRobbed);
    }
};

// Function to build tree from level-order input
TreeNode* buildTree(const vector<int>& nodes) {
    if (nodes.empty() || nodes[0] == -1)
        return nullptr;

    TreeNode* root = new TreeNode(nodes[0]);
    queue<TreeNode*> q;
    q.push(root);

    int i = 1;
    while (!q.empty() && i < nodes.size()) {
        TreeNode* curr = q.front();
        q.pop();

        if (i < nodes.size() && nodes[i] != -1) {
            curr->left = new TreeNode(nodes[i]);
            q.push(curr->left);
        }
        i++;

        if (i < nodes.size() && nodes[i] != -1) {
            curr->right = new TreeNode(nodes[i]);
            q.push(curr->right);
        }
        i++;
    }

    return root;
}

int main() {
    cout << "Enter level-order traversal (-1 for null): ";
    string line;
    getline(cin, line);

    stringstream ss(line);
    vector<int> nodes;
    int x;

    while (ss >> x)
        nodes.push_back(x);

    TreeNode* root = buildTree(nodes);

    Solution sol;
    cout << "Maximum amount that can be robbed: " << sol.rob(root) << endl;

    return 0;
}