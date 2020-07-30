/*
36. Valid Sudoku
https://leetcode.com/problems/valid-sudoku/submissions/
*/
import (
    "strconv"
)

func isValidPoint(point byte, bitmap int) (int, bool) {
    if val, err := strconv.Atoi(string(point)); err == nil {
        bitmap = bitmap ^ (1 << val)
        if (bitmap & (1 << val)) == 0 {
            return bitmap, false
        }
    }
    return bitmap, true
}

func isValidSudoku(board [][]byte) bool {
    isValid := true
    
    // Row
    for i := 0; i < 9; i++ {
        bitmap := 0
        for j := 0; j < 9; j++ {
            if bitmap, isValid = isValidPoint(board[i][j], bitmap); !isValid {
                return false
            }
        }
    }
    
    // Column
    for i := 0; i < 9; i++ {
        bitmap := 0
        for j := 0; j < 9; j++ {
            if bitmap, isValid = isValidPoint(board[j][i], bitmap); !isValid {
                return false
            }
        }
    }
    
    // Cell
    for i := 0; i < 3; i++ {
        for j := 0; j < 3; j++ {
            bitmap := 0
            for x := i * 3; x < (i + 1) * 3; x++ {
                for y := j * 3; y < (j + 1) * 3; y++ {
                    if bitmap, isValid = isValidPoint(board[x][y], bitmap); !isValid {
                        return false
                    }
                }
            }
        }
    }
    
    return true
}
