typedef std::vector<int> VEC;
typedef std::vector<VEC> MAT;

VEC findDiagonalOrder(MAT& mat) {
    VEC res;
    if (mat.size() == 0 || mat[0].size() == 0) return res;
    
    auto row_max = mat.size() - 1;
    auto col_max = mat[0].size() - 1;
    bool go_up_right = true;
    size_t x = 0;
    size_t y = 0;
    
    while(!(x == row_max && y == col_max)) {
        res.push_back(mat[x][y]);
        
        if(go_up_right) { // go up right
            if(x > 0 && y < col_max) {                   
                x -= 1;
                y += 1;
            } else if (y < col_max) {
                y += 1;
                go_up_right = false;
            } else if (x < row_max) {
                x += 1;
                go_up_right = false;
            } else {
                break;
            }
        } else { // go down left
            if(y > 0 && x < row_max) {                   
                x += 1;
                y -= 1;
            } else if (x < row_max) {
                x += 1;
                go_up_right = true;
            } else if (y < col_max) {
                y += 1;
                go_up_right = true;
            } else {
                break;
            }
        }
    }
    res.push_back(mat[x][y]);
    return res;
}
