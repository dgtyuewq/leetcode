class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        cell=[cells]

        rank = 0
        for i in range(N):
            k=[None]*8
            k[0] = 0
            k[-1] = 0
            for j in range (1,7):
                if cell[i][j-1]==cell[i][j+1]:
                    k[j]=1
                else:
                    k[j]=0
            cell.append(k)
            rank = rank + 1
            if i>1  and cell[1] == k:
                if cell[1] == k :
                    rank_1 = N%(rank-1)  #幾個循環取餘數
                else:
                    rank_1 = N
                if rank_1 != 0:
                    return cell[rank_1]
                else:
                    return cell[rank-1]
        return cell[rank]
