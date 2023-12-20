def alignment(x, y, scoring_matrix):
    n = len(x)
    m = len(y)


    score_matrix = [[0] * (m + 1) for _ in range(n + 1)]

   
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            match = score_matrix[i - 1][j - 1] + scoring_matrix[x[i - 1]][y[j - 1]]
            delete = score_matrix[i - 1][j] + scoring_matrix[x[i - 1]]['-']
            insert = score_matrix[i][j - 1] + scoring_matrix['-'][y[j - 1]]

           
            score_matrix[i][j] = max(match, delete, insert)

   
    alignment_x = []
    alignment_y = []
    i, j = n, m
    while i > 0 or j > 0:
        if i > 0 and j > 0 and score_matrix[i][j] == score_matrix[i - 1][j - 1] + scoring_matrix[x[i - 1]][y[j - 1]]:
            alignment_x.append(x[i - 1])
            alignment_y.append(y[j - 1])
            i -= 1
            j -= 1
        elif i > 0 and score_matrix[i][j] == score_matrix[i - 1][j] + scoring_matrix[x[i - 1]]['-']:
            alignment_x.append(x[i - 1])
            alignment_y.append('-')
            i -= 1
        else:
            alignment_x.append('-')
            alignment_y.append(y[j - 1])
            j -= 1

    alignment_x.reverse()
    alignment_y.reverse()

    return ''.join(alignment_x), ''.join(alignment_y)


x = "ATGCC"
y = "TACGCA"
#x = "TCCCAGTTATGTCAGGGGACACGAGCATGCAGAGAC"
#y = "AATTGCCGCCGTCGTTTTCAGCAGTTATGTCAGATC"
scoring_matrix = {
    'A': {'A': 1, 'C': -2.3, 'G': -0.8, 'T': -0.2, '-': -0.6},
    'C': {'A': -2.3, 'C': 1, 'G': -0.7, 'T': -0.5, '-': -1},
    'G': {'A': -0.8, 'C': -0.7, 'G': 1, 'T': -1.1, '-': -1.5},
    'T': {'A': -0.2, 'C': -0.5, 'G': -1.1, 'T': 1, '-': -0.9},
    '-': {'A': -0.6, 'C': -1, 'G': -1.5, 'T': -0.9}
}

result = alignment(x, y, scoring_matrix)
print("Alignment:")
print(result[0])
print(result[1])
