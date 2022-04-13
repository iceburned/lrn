mtx = [[int(_) for _ in input().split(", ")] for _ in range(int(input()))]
primary_diag = [mtx[_][_] for _ in range(len(mtx))]
secondary_diag = [mtx[_][-_-1] for _ in range(len(mtx))]
print(f"Primary diagonal: {', '.join([str(_) for _ in primary_diag])}. Sum: {sum(primary_diag)}")
print(f"Secondary diagonal: {', '.join([str(_) for _ in secondary_diag])}. Sum: {sum(secondary_diag)}")