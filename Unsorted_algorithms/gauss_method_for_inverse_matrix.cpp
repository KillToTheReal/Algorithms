
#include <iostream>
#include <cmath>
 
using namespace std;
 
int Gauss(double **matrix_a, int n, double *massiv_b, double *x)
{
    int i, j, k, r;
    double c, M, max, s, **a, *b;
    a = new double *[n];
    for (i = 0; i<n; i++) 
        a[i] = new double[n];
        
    b = new double[n]; 
    for (i = 0; i<n; i++)
        for (j = 0; j<n; j++) 
            a[i][j] = matrix_a[i][j];
            
    for (i = 0; i<n; i++)
        b[i] = massiv_b[i];
        
    for (k = 0; k<n; k++){
        max = fabs(a[k][k]);
        r = k;
        for (i = k + 1; i<n; i++)
            if (fabs(a[i][k])>max)
            {
                max = fabs(a[i][k]);
                r = i;
            }
        for (j = 0; j<n; j++)
        {
            c = a[k][j];
            a[k][j] = a[r][j];
            a[r][j] = c;
        }
        
        c = b[k]; b[k] = b[r];
        b[r] = c;
        for (i = k + 1; i<n; i++)
        {
            for (M = a[i][k] / a[k][k], j = k; j<n; j++)
                a[i][j] -= M * a[k][j]; b[i] -= M * b[k];
        }
 
    }
    if (a[n - 1][n - 1] == 0) 
        if (b[n - 1] == 0)
            return-1; 
        else 
            return-2;
    else 
    {
        for (i = n - 1; i >= 0; i--)
        {
            for (s = 0, j = i + 1; j<n; j++)
                s += a[i][j] * x[j]; x[i] = (b[i] - s) / a[i][i];
        }
        return 0;
    } 
    for (i = 0; i<n; i++) 
        delete[] a[i];
        
    delete[] a;
    delete[] b;
}
 
int INVERSE (double **a, int n, double **y)
{
    int i, j, res;
    double *b, *x; 
    b = new double[n];
    x = new double[n]; 
    for (i = 0; i<n; i++)
    {
        for (j = 0; j<n; j++)
            if (j == i)
                b[j] = 1;
            else 
                b[j] = 0;
                
            res = Gauss(a, n, b, x);
            if (res != 0) 
                break; 
            else 
            for (j = 0; j < n; j++) 
            {
                y[j][i] = x[j];
            }
    } 
    
    delete[] x;
    delete[] b;
    if (res != 0) 
        return -1;
    else 
        return 0;
}
 
 // Получение матрицы без i-й строки и j-го столбца
void GetMatr(double **mas, double **p, int i, int j, int m) {
  int ki, kj, di, dj;
  di = 0;
  for (ki = 0; ki<m - 1; ki++) { // проверка индекса строки
    if (ki == i) di = 1;
    dj = 0;
    for (kj = 0; kj<m - 1; kj++) { // проверка индекса столбца
      if (kj == j) dj = 1;
      p[ki][kj] = mas[ki + di][kj + dj];
    }
  }
}
// Рекурсивное вычисление определителя
double determinant(double **mas, int m) {
  int i, j, k, n;
  double d;
  double **p;
  p = new double*[m];
  for (i = 0; i<m; i++)
    p[i] = new double[m];
  j = 0; d = 0;
  k = 1; //(-1) в степени i
  n = m - 1;
  if (m<1) cout << "Определитель вычислить невозможно!";
  if (m == 1) {
    d = mas[0][0];
    return(d);
  }
  if (m == 2) {
    d = mas[0][0] * mas[1][1] - (mas[1][0] * mas[0][1]);
    return(d);
  }
  if (m>2) {
    for (i = 0; i<m; i++)
    {
      GetMatr(mas, p, i, 0, m);
      cout << mas[i][j] << endl;
      //PrintMatr(p, n);
      d = d + k * mas[i][0] * determinant(p, n);
      k = -k;
    }
  }
  return(d);
}

int main()
{
    int result, i, j, N;
    double **a, **b;
    cout << "Matrix size : ";
    cin >> N; 
    if (N < 0)
    {
        N *= -1;
    } 
    a = new double *[N];
    
    for (i = 0; i < N; i++)
        a[i] = new double[N]; 
        
        b = new double *[N];
        
    for (i = 0; i<N; i++)
        b[i] = new double[N]; 
        
        cout << "Input Matrix: " << endl;
        
    for (i = 0; i<N; i++)
        for (j = 0; j < N; j++) 
        {
            cin >> a[i][j];
        }
        
    cout << "Your matrix: " << endl; 
    for (i = 0; i<N; cout << endl, i++)
        for (j = 0; j<N; j++)
            cout << a[i][j] << "\t";
        
    cout << "Determinant: " << determinant(a, N) << endl;
    if (determinant(a, N) != 0)
    {
        INVERSE(a,N,b);
        cout << "Inverse matrix: " << endl; 
        for (i = 0; i<N; cout << endl, i++)
            for (j = 0; j<N; j++)
                cout << b[i][j] << "\t";
    }
    else cout << "No Inverse matrix" << endl; 
    
    return 0;
}
