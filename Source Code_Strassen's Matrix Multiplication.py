import numpy as np

def algoritma_strassen(x, y):
    if x.size == 1 or y.size == 1:
        return x * y

    n = x.shape[0]

    if n % 2 == 1:
        x = np.pad(x, (0, 1), mode='constant')
        y = np.pad(y, (0, 1), mode='constant')

    m = int(np.ceil(n / 2))
    a = x[: m, : m]
    b = x[: m, m:]
    c = x[m:, : m]
    d = x[m:, m:]
    e = y[: m, : m]
    f = y[: m, m:]
    g = y[m:, : m]
    h = y[m:, m:]
    p1 = algoritma_strassen (a, f - h)
    p2 = algoritma_strassen (a + b, h)
    p3 = algoritma_strassen (c + d, e)
    p4 = algoritma_strassen (d, g - e)
    p5 = algoritma_strassen (a + d, e + h)
    p6 = algoritma_strassen (b - d, g + h)
    p7 = algoritma_strassen (a - c, e + f)
    hasil = np.zeros((2 * m, 2 * m), dtype=np.int32)
    hasil[: m, : m] = p5 + p4 - p2 + p6
    hasil[: m, m:] = p1 + p2
    hasil[m:, : m] = p3 + p4
    hasil[m:, m:] = p1 + p5 - p3 - p7

    return hasil[: n, : n]

if __name__ == "__main__":

    x = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    y = np.array([[-1, 0, 0], [0, -1, 0], [0, 0, -1]])
    print('Hasil Perkalian Matriks: ')
    print(algoritma_strassen(x, y))
