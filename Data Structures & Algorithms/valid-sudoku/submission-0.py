class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def get_box_ind(row_ind, col_ind):
            box_ind = (row_ind//3)*3 + (col_ind//3)
            return box_ind

        # {dig: {r: {rows}, c: {cols}, b: {box}}}
        occur = {}

        for curr_row_ind, curr_row_val in enumerate(board):
            for curr_col_ind, curr_cell_val in enumerate(curr_row_val):
                if curr_cell_val == ".":
                    continue
                curr_box_ind = get_box_ind(curr_row_ind, curr_col_ind)
                curr_occur_of_dig = occur.get(curr_cell_val, {})
                if curr_occur_of_dig:
                    if curr_row_ind in curr_occur_of_dig.get("r") or curr_col_ind in curr_occur_of_dig.get("c") or curr_box_ind in curr_occur_of_dig.get("b"):
                        return False
                else:
                    occur[curr_cell_val] = {"r": set(), "c": set(), "b": set()}
                occur[curr_cell_val]["r"].add(curr_row_ind)
                occur[curr_cell_val]["c"].add(curr_col_ind)
                occur[curr_cell_val]["b"].add(curr_box_ind)
        return True

        