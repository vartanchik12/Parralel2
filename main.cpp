#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <stdexcept>
#include <omp.h>

using Matrix = std::vector<std::vector<double>>;


Matrix readMatrix(const std::string filename) {
    std::ifstream file(filename);
    if (!file) {
        throw std::runtime_error("�� ������� ������� ���� ");
    }

    Matrix matrix;
    std::string line;
    while (std::getline(file, line)) {
        std::istringstream iss(line);
        std::vector<double> row;
        double value;
        while (iss >> value) {
            row.push_back(value);
        }
        if (!row.empty()) {
            matrix.push_back(row);
        }
    }
    return matrix;
}


void writeMatrixToFile(const Matrix& matrix, const std::string filename) {
    std::ofstream file(filename);
    if (!file) {
        throw std::runtime_error("�� ������� ������� ���� ��� ������ ");
    }

    for (const auto& row : matrix) {
        for (size_t i = 0; i < row.size(); ++i) {
            file << row[i];
            if (i < row.size() - 1) {
                file << " ";
            }
        }
        file << "\n";
    }
}


Matrix multiplyMatrices(const Matrix& A, const Matrix& B) {

    size_t rows_A = A.size();
    size_t cols_A = A[0].size();
    size_t cols_B = B[0].size();

    Matrix result(rows_A, std::vector<double>(cols_B, 0.0));

    #pragma omp parallel for shared(A, B, result) 
    for (size_t i = 0; i < rows_A; ++i) {
        for (size_t j = 0; j < cols_B; ++j) {
            for (size_t k = 0; k < cols_A; ++k) {
                result[i][j] += A[i][k] * B[k][j];
            }
        }
    }

    return result;
}


int main() {
    std::string matrix_A_file, matrix_B_file, result_file;


    matrix_A_file = "matrixA.txt";
    matrix_B_file = "matrixB.txt";
    result_file = "matrix_result.txt";


    int num_threads = omp_get_max_threads();
    omp_set_num_threads(num_threads);
    
    printf("Используется %d потоков OpenMP\n", num_threads);

    Matrix A = readMatrix(matrix_A_file);
    Matrix B = readMatrix(matrix_B_file);

    if (A.empty() || B.empty()) {
        throw std::runtime_error("Matrices are empty");
    }

    double start_time = omp_get_wtime();
    Matrix result = multiplyMatrices(A, B);
    double end_time = omp_get_wtime();

    printf("Время выполнения: %.4f секунд\n", end_time - start_time);

    writeMatrixToFile(result, result_file);

    return 0;
}