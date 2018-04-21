import math 

def matrix_transpose():

	print("Enter your matrix row size : ")
	size1 = int(input())

	print("Enter your matrix column size : ")
	size2 = int(input())

	matrix = [[0 for x in range(size1)] for y in range(size2)]
	result = [[ matrix for x in range(size2)] for y in range(size1)]

	for i in range(len(matrix)):
		print("Enter your number for matrix row : ", i )
		for j in range(len(matrix[0])):
			print("matrix col: ")
			matrix[i][j] = input()

	print("Original Matrix: \n")
	for row in matrix:
		print(*row)

	print("\n")

	for i in range(len(matrix)):
  		for j in range(len(matrix[0])):
     			result[j][i] = matrix[i][j]

	for row in result:
		print(*row)

	return result

def matrix_det():

	print("Enter your matrix row size : ")
	size1 = int(input())

	print("Enter your matrix column size : ")
	size2 = int(input())

	det = 0
	
	if(size1 != size2):
		print("Cannot calculate determinant for a non square matrix")
		return
	else:
		dimension = size1

	matrix = [[0 for x in range(size1)] for y in range(size2)]
	
	for i in range(len(matrix)):
		print("Enter your number for matrix row : ", i )
		for j in range(len(matrix[0])):
			print("matrix col: ")
			matrix[i][j] = input()

	print("Original Matrix: \n")
	for row in matrix:
		print(*row)
	

	if( dimension == 1 ):
		for i in range(len(matrix)):
			for j in range(len(matrix[0])):
				det = matrix[i][j] 
	elif( dimension == 2):
		det_a = int(matrix[0][0])
		det_b = int(matrix[0][1])
		det_c = int(matrix[1][0]) 
		det_d = int(matrix[1][1])
		det = (det_a * det_d) - (det_b * det_c)
	else:
		print("The dimension of your matrix is too high to calculate ")
		return

	print("The determinant of you matrix is : " , det )


def add_matrix():

	print("Enter row size of Matrix A : ")
	s1 = int(input())	
	print("\nEnter col size of Matrix A : ")
	s2 = int(input())
	print("\nEnter row size of Matrix B : ")
	s3 = int(input())
	print("\nEnter col size of Matrix B : ")
	s4 = int(input())
	if( (s1 == s3) and s2 == s4):
		print("Matrix can be added\n")

		matrix1 = [[0 for x in range(s1)] for y in range(s2)]
		matrix2 = [[0 for x in range(s3)] for y in range(s4)]

		for i in range(len(matrix1)):
			print("Enter your number for matrix A row : ", i )
			for j in range(len(matrix1[0])):
				print("matrix col: ")
				matrix1[i][j] = input()

		for i in range(len(matrix2)):
			print("Enter your number for matrix B row : ", i )
			for j in range(len(matrix2[0])):
				print("matrix col: ")
				matrix2[i][j] = input()

	else:
		print("Matrix A of dimension ", s1 , " x " , s2 , " is not equal to Matrix B of dimension of " , s3 , " x " , s4 ) 
		return

	result = [[0 for x in range(len(matrix1))] for y in range(len(matrix1[0]))]

	for i in range(len(matrix1)):
			for j in range(len(matrix1[0])):
				result[i][j] = int(matrix1[i][j]) + int(matrix2[i][j])

	print("\nmatrix A: \n")
	for row in matrix1:
		print(*row)

	print("\nmatrix B: \n")
	for row in matrix2:
		print(*row)

	print("\nFinal added matrix \n")
	for row in result:
		print(*row)
	
	

def mul_matrix():

	print("Enter row size of Matrix A : ")
	s1 = int(input())	
	print("\nEnter col size of Matrix A : ")
	s2 = int(input())
	print("\nEnter row size of Matrix B : ")
	s3 = int(input())
	print("\nEnter col size of Matrix B : ")
	s4 = int(input())

	if( (s2 == s3) ) :
		print("Matrix can be multiplied\n")

		matrix1 = [[0 for x in range(s1)] for y in range(s2)]
		matrix2 = [[0 for x in range(s3)] for y in range(s4)]

		print(matrix2)

		for i in range(len(matrix1)):
			print("Enter your number for matrix A row : ", i )
			for j in range(len(matrix1[0])):
				print("matrix col: ")
				matrix1[i][j] = input()

		for i in range(len(matrix2)):
			print("Enter your number for matrix B row : ", i )
			for j in range(len(matrix2[0])):
				print("matrix col: ")
				matrix2[i][j] = input()

	else:
		print("Matrix A of dimension ", s1 , " x " , s2 , " is not equal to Matrix B of dimension of " , s3 , " x " , s4 ) 
		return

	result = [[0 for x in range(s1)] for y in range(s4)]


	print("\n\n")
	for row in result:
		print(*row)
	print("\n\n")

	for i in range(len(matrix1)):
		sum = 0
		for j in range(len(matrix2[0])):
			for k in range(len(matrix2)):
				result[i][j] += int(matrix1[i][k]) * int(matrix2[k][j])


	print("\nmatrix A: \n")
	for row in matrix1:
		print(*row)

	print("\nmatrix B: \n")
	for row in matrix2:
		print(*row)

	print("\nFinal multiplied matrix \n")
	for row in result:
		print(*row)
	



def inverse_matrix():

	print("Enter row size of Matrix A : ")
	s1 = int(input())	
	print("\nEnter col size of Matrix A : ")
	s2 = int(input())

	if( (s1 == s2) ) :
		print("Matrix can be inversed\n")

	matrix = [[0 for x in range(s1)] for y in range(s2)]
	inverse = [[1 if i == j else 0 for j in range(s2) ] for i in range(s1)]

	if( s1 == 1):

		for i in range(len(matrix)):
			print("Enter your number for matrix A row : ", i )
			for j in range(len(matrix[0])):
				print("matrix col: ")
				matrix[i][j] = input()

		det = int(matrix[0][0])
		inv_det = (1/det)
	
	elif( s1 == 2):



		for i in range(len(matrix)):
			print("Enter your number for matrix A row : ", i )
			for j in range(len(matrix[0])):
				print("matrix col: ")
				matrix[i][j] = input()

		
		det_a = float(matrix[0][0])
		det_b = float(matrix[0][1])
		det_c = float(matrix[1][0]) 
		det_d = float(matrix[1][1])
		det = (det_a * det_d) - (det_b * det_c)
		inv_det = (1/det)
	
	
	elif( s1 > 2):
		print("Matrix dimension too big to multiply")
		return
	
	else:
		print("Matrix A of dimension ", s1 , " x " , s2 , " is not equal to Matrix B of dimension of " , s3 , " x " , s4 ) 
		return

	
	
	result = [[0 for x in range(len(matrix))] for y in range(len(matrix))]

	temp = matrix[0][0]
	matrix[0][0] = matrix[1][1]
	matrix[1][1] = temp

	for i in range(len(matrix)):
			for j in range(len(matrix[0])):
					if(i == j):
						result[i][j] +=  (round(float(matrix[i][j]) * inv_det,2) )
					else:
						result[i][j] += - (round(float(matrix[i][j]) * inv_det,2) )

	

	print("\nOriginal Matrix: \n")
	for row in matrix:
		print(*row)


	print("\nInverse matrix \n")
	for row in result:
		print(*row)
	


	
	 
#matrix_transpose()

#matrix_det()

#add_matrix()

#mul_matrix()

inverse_matrix()
