public class matrix {

    public static int diagonalSum(int[][] matrix) {

        int n = matrix.length;
        int total = 0;

        for (int i = 0; i < n; i++) {

            total += matrix[i][i];

            if (i != n - 1 - i) {
                total += matrix[i][n - 1 - i];
            }
        }

        return total;
    }

    public static void main(String[] args) {

        int[][] matrix = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };

        System.out.println(diagonalSum(matrix));
    }
}