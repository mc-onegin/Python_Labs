import numpy as np

print("1)")
matrix = []
with open("1.txt") as file:
    for i in file:
        matrix.append((list(map(int, i.split(',')))))

np_matrix = np.array(matrix)
print(np.sum(np_matrix), np.max(np_matrix), np.min(np_matrix), sep="\n")

print("2)")
def RLE(mas):
    changes = np.where(np.diff(mas))[0] + 1
    starts = np.concatenate(([0], changes))
    ends = np.concatenate((changes, [len(mas)]))
    values = mas[starts]
    counts = ends - starts
    return values, counts


x = np.array([2, 2, 2, 3, 3, 3, 5])
a, b = RLE(x)
print((a, b))

print("3)")
arr = np.random.normal(size=(10, 4))
mini = np.min(arr)
maxi = np.max(arr)
mean = np.mean(arr)
deviation = np.std(arr)
five_rows = arr[:5]
print(mini, maxi, mean, deviation, five_rows, sep="\n")

print("4)")
x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])
indices = np.flatnonzero(x[:-1] == 0) + 1
selected_values = x[indices]
max_value = selected_values.max()
print(max_value)

print("5)")
def log_normal(X, m, C):
    N, D = X.shape
    inv_C = np.linalg.inv(C)
    det_C = np.linalg.det(C)
    log_det_term = -0.5 * np.log(det_C)
    const_term = -0.5 * D * np.log(2 * np.pi)

    diff = X - m
    quadratic_form = np.einsum('ij,jk,ik->i', diff, inv_C, diff)
    log_pdfs = const_term + log_det_term - 0.5 * quadratic_form
    return log_pdfs


m = np.array([0., 0.])
C = np.array([[1., 0.5], [0.5, 1.]])
X = np.random.randn(5, 2)
print(log_normal(X, m, C))

print("6")
a = np.arange(16).reshape(4, 4)
a[[1, 3]] = a[[3, 1]]
print(a)

print("7)")
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
species_column = iris[:, 4].astype(str)
unique_species, counts = np.unique(species_column, return_counts=True)
for specie, count in zip(unique_species, counts):
    print(f"Вид: {specie}, Кол-во: {count}")

print("8)")
arr_8 = np.array([0, 1, 2, 0, 0, 4, 0, 6, 9])
non_zero_indices = np.nonzero(arr_8)[0]
print(non_zero_indices)


