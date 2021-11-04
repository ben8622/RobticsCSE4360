#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#ifndef M_PI
#define M_PI 3.1415927
#endif

/* ROBOT CONSTANT LENGTHS */
const double l0 = 0.25;
const double l1 = 0.2;
const double l2 = 0.2;
const double l3 = 0.15;
const double d1 = -0.04;
const double d2 = 0.04;
const double d3 = -0.04;
const double d4 = -0.04;

/* FUNCTION DEFS */
double** create_Rx(double theta);
double** create_Ry(double theta);
double** create_Rz(double theta);
double** create_Dx(double length);
double** create_Dy(double length);
double** create_Dz(double length);
double** multiply_matrices(double** M1, double** M2);
double** create_matrix();
void print_matrix(double** M);

fwd_kin(theta, x)
double *theta;
double x[3];
{
	/* Create matrices in order of equation from left to right */
	double** Rz_theta0 = create_Rz(theta[0]);
	double** Dz_l0 = create_Dz(l0);
	double** Dy_d1 = create_Dy(d1);
	double** Ry_theta1 = create_Ry(theta[1]);
	double** Dx_l1 = create_Dx(l1);
	double** Dy_d2 = create_Dy(d2);
	double** Ry_theta2 = create_Ry(theta[2]);
	double** Dx_l2 = create_Dx(l2);
	double** Dy_d3 = create_Dy(d3);
	double** Ry_theta3 = create_Ry(theta[3]);
	double** Dz_d4 = create_Dz(d4);
	double** Dx_l3 = create_Dx(l3);

	/* Rz(t0)Dz(l0)Ry(t1)Dy(d1)Dx(l1)Ry(t2)Dy(d2)Dx(l2)Ry(t3)Dy(d3)Dz(d4)Dx(l3) */
	double** T0 = multiply_matrices(Rz_theta0, Dz_l0);
	/* T()Ry(t1)Dy(d1)Dx(l1)Ry(t2)Dy(d2)Dx(l2)Ry(t3)Dy(d3)Dz(d4)Dx(l3) */
	double** T1 = multiply_matrices(T0, Ry_theta1);
	/* T()Dy(d1)Dx(l1)Ry(t2)Dy(d2)Dx(l2)Ry(t3)Dy(d3)Dz(d4)Dx(l3) */
	double** T2 = multiply_matrices(T1, Dy_d1);
	/* T()Dx(l1)Ry(t2)Dy(d2)Dx(l2)Ry(t3)Dy(d3)Dz(d4)Dx(l3) */
	double** T3 = multiply_matrices(T2, Dx_l1);
	/* T()Ry(t2)Dy(d2)Dx(l2)Ry(t3)Dy(d3)Dz(d4)Dx(l3) */
	double** T4 = multiply_matrices(T3, Ry_theta2);
	/* T()Dy(d2)Dx(l2)Ry(t3)Dy(d3)Dz(d4)Dx(l3) */
	double** T5 = multiply_matrices(T4, Dy_d2);
	/* T()Dx(l2)Ry(t3)Dy(d3)Dz(d4)Dx(l3) */
	double** T6 = multiply_matrices(T5, Dx_l2);
	/* T()Ry(t3)Dy(d3)Dz(d4)Dx(l3) */
	double** T7 = multiply_matrices(T6, Ry_theta3);
	/* T()Dy(d3)Dz(d4)Dx(l3) */
	double** T8 = multiply_matrices(T7, Dy_d3);
	/* T()Dz(d4)Dx(l3) */
	double** T9 = multiply_matrices(T8, Dz_d4);
	/* T()Dx(l3) */
	double** T10 = multiply_matrices(T9, Dx_l3);

	x[0] = T10[0][3];
	x[1] = T10[1][3];
	x[2] = T10[2][3];

	free(Rz_theta0);
	free(Dz_l0);
	free(Dy_d1);
	free(Ry_theta1);
	free(Dx_l1);
	free(Dy_d2);
	free(Ry_theta2);
	free(Dx_l2);
	free(Dy_d3);
	free(Ry_theta3);
	free(Dx_l3);
	free(T0);
	free(T1);
	free(T2);
	free(T3);
	free(T4);
	free(T5);
	free(T6);
	free(T7);
	free(T8);
	free(T9);
	free(T10);
}

inv_kin(x, theta)
double *x;
double theta[6];
{

}

/*
 ********** END OF KINEMATIC FUNCTIONS *********
*/


double** create_Rx(double theta)
{
  int i = 0;
  int j = 0;
  double R[4][4] = {
	  {1, 0, 0, 0},
	  {0, cos(theta), -1*sin(theta), 0},
	  {0, sin(theta), cos(theta), 0},
	  {0, 0, 0, 1}
  };
  double** M = create_matrix();
  for(i=0; i<4; i++)
  {
    for(j=0; j<4; j++)
    {
      M[i][j] = R[i][j];
    }
  }
  return M;
}
double** create_Ry(double theta)
{
  int i = 0;
  int j = 0;
  double R[4][4] = {
	  {cos(theta), 0, sin(theta), 0},
	  {0, 1, 0, 0},
	  {-1*sin(theta), 0, cos(theta), 0},
	  {0, 0, 0, 1}
  };
  double** M = create_matrix();
  for(i=0; i<4; i++)
  {
    for(j=0; j<4; j++)
    {
      M[i][j] = R[i][j];
    }
  }
  return M;
}
double** create_Rz(double theta)
{
  int i = 0;
  int j = 0;
  double R[4][4] = {
	  {cos(theta), -1*sin(theta), 0, 0},
	  {sin(theta), cos(theta), 0, 0},
	  {0, 0, 1, 0},
	  {0, 0, 0, 1}
  };
  double** M = create_matrix();
  for(i=0; i<4; i++)
  {
    for(j=0; j<4; j++)
    {
      M[i][j] = R[i][j];
    }
  }
  return M;
}
double** create_Dx(double length)
{
  int i = 0;
  int j = 0;
  double D[4][4] = {
	  {1, 0, 0, length},
	  {0, 1, 0, 0},
	  {0, 0, 1, 0},
	  {0, 0, 0, 1}
  };
  double** M = create_matrix();
  for(i=0; i<4; i++)
  {
    for(j=0; j<4; j++)
    {
      M[i][j] = D[i][j];
    }
  }
  return M;
}
double** create_Dy(double length)
{
  int i = 0;
  int j = 0;
  double D[4][4] = {
	  {1, 0, 0, 0},
	  {0, 1, 0, length},
	  {0, 0, 1, 0},
	  {0, 0, 0, 1}
  };
  double** M = create_matrix();
  for(i=0; i<4; i++)
  {
    for(j=0; j<4; j++)
    {
      M[i][j] = D[i][j];
    }
  }
  return M;
}
double** create_Dz(double length)
{
  int i = 0;
  int j = 0;
  double D[4][4] = {
	  {1, 0, 0, 0},
	  {0, 1, 0, 0},
	  {0, 0, 1, length},
	  {0, 0, 0, 1}
  };
  double** M = create_matrix();
  for(i=0; i<4; i++)
  {
    for(j=0; j<4; j++)
    {
      M[i][j] = D[i][j];
    }
  }
  return M;
}

double** multiply_matrices(double** M1, double** M2)
{
	double** M = create_matrix();
	int i, j, k = 0;
	for(i=0; i<4; i++)
	{
		for(j=0; j<4; j++)
		{
			for(k=0; k<4; k++)
			{
				M[i][j] = M[i][j] + (M1[i][k] * M2[k][j]);
			}
		}
	}
	return M;
}
double** create_matrix()
{
  double** matrix = malloc(4*sizeof(double*));
  int i = 0;
  for(i=0; i<4; i++)
  {
    matrix[i] = calloc(4,sizeof(double));
  }
  return matrix;
}
void print_matrix(double** M)
{
  printf("printing matrix: \n");
  int i = 0;
  int j = 0;
  for(i=0; i<4; i++)
  {
    for(j=0; j<4; j++)
    {
	printf("%f ", M[i][j]);
    }
    printf("\n");
  }
}



