#include <iostream>
#include <vector>
#include <string>
#include <tuple>


using namespace std;

struct Rect {
    int frow;
    int fcol;
    int lrow;
    int lcol;

    bool operator!=(const Rect& r2) {
        return tie(frow, fcol, lrow, lcol) != tie(r2.frow, r2.fcol, r2.lrow, r2.lcol);
    }
};
const Rect NONE = {-1, -1, -1, -1};
using Sector = Rect;

bool isInside(int row, int col, Rect r) {
    return r.frow <= row && row <= r.lrow &&
        r.fcol <= col && col <= r.lcol;
}

Rect rectInSector(const vector<string>& picture, const Sector& s) {
    Rect r = NONE;
    for (int row = s.frow; row <= s.lrow; ++row) {
        for (int col = s.fcol; col <= s.lcol; ++col) {
            if (picture[row][col] == '#' && !isInside(row, col, r)) {
                if (r != NONE) {
                    return NONE;
                }
                r.frow = r.lrow = row; r.fcol = r.lcol = col;
                
                while (r.lrow + 1 <= s.lrow && picture[r.lrow + 1][col] == '#') {
                    r.lrow++;
                }

                while (r.lcol + 1 <= s.lcol && picture[row][r.lcol + 1] == '#') {
                    r.lcol++;
                }
            }
        }
    }

    for (int row = r.frow + 1; row <= r.lrow; ++row) {
        for (int col = r.fcol + 1; col <= r.lcol; ++col) {
            if (picture[row][col] != '#') {
                return NONE;
            }
        }
    }

    return r;
}

void fillRectangle(vector<string>& picture, const Rect& r, char c) {
    for (int row = r.frow; row <= r.lrow; ++row) {
        for (int col = r.fcol; col <= r.lcol; ++col) {
            picture[row][col] = c;
        }
    }
}

bool checkSectors(int m, int n, vector<string>& picture, const Sector& s1, const Sector& s2) {
    Rect r1 = rectInSector(picture, s1);
    Rect r2 = rectInSector(picture, s2);

    if (r1 != NONE && r2 != NONE) {
        fillRectangle(picture, r1, 'a');
        fillRectangle(picture, r2, 'b');
        return true;
    } else {
        return false;
    }
}

bool isTwoRect(int m, int n, vector<string>& picture) {
    for (int row = 0; row + 1 < m; ++row) {
        Sector s1 = {0, 0, row, n - 1};
        Sector s2 = {row + 1, 0, m - 1, n - 1};
        if (checkSectors(m, n, picture, s1, s2)) {
            return true;
        }
    }

    for (int col = 0; col + 1 < n; ++col) {
        Sector s1 = {0, 0, m - 1, col};
        Sector s2 = {0, col + 1, m - 1, n - 1};
        if (checkSectors(m, n, picture, s1, s2)) {
            return true;
        }
    }

    return false;
}

int main() {
    int m, n;
    cin >> m >> n;
    vector<string> picture(m);
    for (string& line : picture) {
        cin >> line;
    }

    if (isTwoRect(m, n, picture)) {
        cout << "YES\n";
        for (const string& line : picture) {
            cout << line << "\n";
        }
    } else {
        cout << "NO\n";
    }

    return 0;
}