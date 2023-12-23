#include <iostream>
#include <vector>
#include <string>

using namespace std;

struct CellPrefSuf {
    int prefLeft = 0;
    int prefTop = 0;
    int sufRight = 0;
    int sufBottom = 0;
};


vector<vector<CellPrefSuf>> buildPrefSuf(const int n, const int m, const vector<string>& field) {
    vector<vector<CellPrefSuf>> prefSufField(n, vector<CellPrefSuf>(m));
    for (int i = 0; i < n; ++i) {
        prefSufField[i][0].prefLeft = (field[i][0] == '#');
        prefSufField[i][m - 1].sufRight = (field[i][m - 1] == '#');
    }
    for (int j = 0; j < m; ++j) {
        prefSufField[0][j].prefTop = (field[0][j] == '#');
        prefSufField[n - 1][j].sufBottom = (field[n - 1][j] == '#');
    }
    
    for (int i = 1; i + 1 < n; ++i) {
        for (int j = 1; j + 1 < m; ++j) {
            if (field[i][j] == '#') {
                prefSufField[i][j].prefLeft = prefSufField[i][j - 1].prefLeft + 1;
                prefSufField[i][j].prefTop = prefSufField[i - 1][j].prefTop + 1;
            }

            if (field[n - 1 - i][m - 1 - j] == '#') {
                prefSufField[n - 1 - i][m - 1 - j].sufRight = prefSufField[n - 1 - i][m - j].sufRight + 1;
                prefSufField[n - 1 - i][m - 1 - j].sufBottom = prefSufField[n - i][m - 1 - j].sufBottom + 1;
            }
        }
    }
    return prefSufField;
}

bool canBuildRowCol(const int i, const int j, const int step, const int k, 
        const vector<vector<CellPrefSuf>>& prefSufField) {
    // if (i == 3 && j == 6 && k == 3) {
    //     cout << "Step " << step << "\n"
    //         << "left" << prefSufField[i + step][j].prefLeft << "\n"
    //         << "right " << prefSufField[i + step][j].sufRight << "\n"
    //         << "top " << prefSufField[i][j + step].prefTop << "\nbottom " 
    //         << prefSufField[i][j + step].sufBottom << "\n";
    // }
    return prefSufField[i + step][j].prefLeft >= k + 1 && 
        prefSufField[i + step][j].sufRight >= 2 * k &&
        prefSufField[i][j + step].prefTop >= k + 1 &&
        prefSufField[i][j + step].sufBottom >= 2 * k;
}

bool canBuild(const int n, const int m, const int k,
        const vector<string>& field, const vector<vector<CellPrefSuf>>& prefSufField) {
    for (int i = k; i < n - 2 * k + 1; ++i) {
        for (int j = k; j < m - 2 * k + 1; ++j) {
            bool canBeBuild = true;
            for (int step = 0; step < k; ++step) {
                if (!canBuildRowCol(i, j, step, k, prefSufField)) {
                    canBeBuild = false;
                    break;
                }
            }

            if (canBeBuild) {
                return true;
            }
        }
    }

    return false;
}

int minOfficeSize(const int n, const int m, const vector<string>& field) {
    vector<vector<CellPrefSuf>> prefSufField = buildPrefSuf(n, m, field);

    int l = 1;
    int r = min(n, m) / 3;
    while (l < r) {
        int mid = (l + r + 1) / 2;
        if (canBuild(n, m, mid, field, prefSufField)) {
            l = mid;
        } else {
            r = mid - 1;
        }
    }

    return l;
}

int main() {
    int n, m;
    cin >> n >> m;
    vector<string> field(n);
    for (string& row : field) {
        cin >> row;
    }
    cout << minOfficeSize(n, m, field) << "\n";
    return 0;
}