#include <vector>
#include <string>

using namespace std;

//208 leetcode problem
class Trie {
public:
    Trie() : head() {
    }
    
    void insert(string word) {
        TrieNode* tn = &head;
        for (const char c : word) {
            TrieNode::It it = tn->push(c);
            tn = &(*it);
        }
    }
    
    bool search(string word) {
        TrieNode* tn = &head;
        for (const char c : word) {
            TrieNode::It it = tn->find(c);
            if (it == tn->children.end()) {
                return false;
            }
        }

        return true;
    }
    
    bool startsWith(string prefix) {
        return search(prefix);
    }

private:
    struct TrieNode {
        char val;
        vector<TrieNode> children;

        TrieNode(const char c = '\0') : val(c) {};

        using It = vector<TrieNode>::iterator;
        It find(const char c) {
            for (auto it = children.begin(); it != children.end(); ++it) {
                if (it->val == c) {
                    return it;
                }
            }

            return children.end();
        }

        It push(char c) {
            if (find(c) == children.end()) {
                return children.insert(children.end(), TrieNode(c));
            } else {
                return children.end();
            }
        }
    };

    TrieNode head;
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */