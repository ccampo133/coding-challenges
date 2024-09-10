package valid_sudoku

type set map[byte]bool

func isValidSudoku(board [][]byte) bool {
	rowSets := make(map[int]set)
	colSets := make(map[int]set)
	type key struct{ i, j int }
	subSets := make(map[key]set)

	for i := 0; i < 9; i++ {
		rowSet, ok := rowSets[i]
		if !ok {
			rowSet = make(set)
			rowSets[i] = rowSet
		}
		for j := 0; j < 9; j++ {
			val := board[i][j]
			if val == '.' {
				continue
			}
			if val < '1' || val > '9' {
				return false
			}
			colSet, ok := colSets[j]
			if !ok {
				colSet = make(set)
				colSets[j] = colSet
			}
			k := key{i: i / 3, j: j / 3}
			subSet, ok := subSets[k]
			if !ok {
				subSet = make(set)
				subSets[k] = subSet
			}
			if rowSet[val] || colSet[val] || subSet[val] {
				return false
			}
			rowSet[val] = true
			colSet[val] = true
			subSet[val] = true
		}
	}
	return true
}
