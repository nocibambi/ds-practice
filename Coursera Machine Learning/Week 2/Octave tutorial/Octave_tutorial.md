# Whos
Shows all the defined values and their dimensions

# [A B] or [A, B]
Concatenates two matrices.

# [A; B]
Puts matrix B under matrix A

# A(:)
Prints all the values of matrix A in one single column.

# keyboard
Command (usually at the end of the function), making the program to exit to the debugger.

# A * B
Matrix multiplication
(m * n) * (n * o)

# A .* B
Elementwise multiplication
(m * n) * (m * n)

# A .^ n
Elementwise squaring

# 1 ./ v
Elementwise reciprocal

# v + ones(length(v), 1)
Incrementing each element in a vector by 1.
Same as v + 1

# max(a)
* Gives the maximum value of a vector OR
* the columwise maximum of a matrix

# [x, y] = max(a)
* Gives the maximum value of a vector/columwise maximum of a matrix AND
* the index of the value/column

# a < 3 VS find(a < 3)
1. a < 3 returns the truth values of each element
2. find(a < 3) returns the values satisfying the critera

# [r, c] = find(A >= 7)
* The column index of elements satisfying the criteria
* the row index of the same elements

# max(rand(3), rand(3)
Returns a 3x3 matrix filled with the maximum values of

# max(A, [], 1)
Columnwise maximum

# max(A, [], 2)
Rowwise maximum

# sum(sum(A.*eye(length(A))))
Diagnoalwise maximum

# sum(sum(A.*flipud(eye(length(A)))))
Diagnoalwise maximum

# pinv(A)
Pseudo inverse of the matrix

# plot(a, b)
Generates a plot with values of a vector and b vector on the two axes.

# hold on
keeps the plot and puts new changes on top of it

# print -dpng 'filename.png'
saves the plot in png format.

# close
closes the plot window

# clf
clears a plot

# imagesc(A)
Creates a heatmap of a matrix
