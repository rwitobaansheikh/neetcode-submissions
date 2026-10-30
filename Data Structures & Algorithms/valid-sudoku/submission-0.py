class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=collections.defaultdict(set)
        cols=collections.defaultdict(set)
        squares=collections.defaultdict(set)
        for r_i, row in enumerate(board):
            for c_i, element in enumerate(row):
                if element == '.':
                    continue
                if (element in rows[r_i] 
                    or element in cols[c_i] 
                    or element in squares[(r_i//3,c_i//3)]):
                    return False
                
                else:
                    rows[r_i].add(element)
                    cols[c_i].add(element)
                    squares[(r_i//3 , c_i//3)].add(element)

        return True

        
        