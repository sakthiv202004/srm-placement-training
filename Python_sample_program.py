# ==================== Right-Angled Triangle Star Pattern ====================
n=int(input())
for row in range(1,n+1):
    for col in range(1,row+1):
        print("*",end="")
    print()

*
**
***
****


# ==================== Square Star Pattern ====================
n=int(input())
for row in range(1,n+1):
    for col in range(1,n+1):
        print("*",end="")
    print()

****
****
****
****


# ==================== Alternating 0-1 Pattern ====================
n=int(input())
for row in range (1,n+1):
    for col in range(1,n+1):
        print(int(not(row+col)%2),end="")
    print()

10101
01010
10101
01010
10101


# ==================== Left-Aligned Inverted Square Pattern ====================
n = int(input())
for i in range(n):
    print(" " * (n - i - 1) + "*" * n)
    print()

    *****
   *****
  *****
 *****
*****


# ==================== Odd Number Triangle Pattern ====================
n=int(input())
val=1
for row in range(1,n+1):
    if row%2==1:
        val=1
    else:
        val=2
    for col in range(1,row+1):
        print(val,end="")
        val=val+2
    print()

1
24
135
2468
13579


# ==================== Hollow Square Star Pattern ====================
n=int(input())
for row in range(1,n+1):
    for col in range(1,n+1):
        if row==1 or row==n or col==1 or col==n:
            print("*",end="")
        else:
            print(" ",end="")
    print()

*****
*   *
*   *
*   *
*****


# ==================== Square with Diagonal Star Pattern ====================
n = int(input())
size = 2 * n - 1
for i in range(size):
    for j in range(size):
        if i == 0 or i == size - 1 or j == 0 or j == size - 1 or i == j or i + j == size - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

*******
**   **
* * * *
*  *  *
* * * *
**   **
*******


# ==================== Inverted Pyramid Star Pattern ====================
n = int(input())
for i in range(n):
    print(" " * i + "*" * (2 * (n - i) - 1))

*******
 *****
  ***
   *


# ==================== Pyramid Star Pattern ====================
n = int(input())
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))

   *
  ***
 *****
*******


# ==================== Diamond Outline Star Pattern ====================
n = int(input())

for i in range(2 * n - 1):
    x = i if i < n else 2 * n - 2 - i
    
    if x == n - 1:
        print(" " * x + "*")
    else:
        print(" " * x + "*" + " " * (2 * (n - x - 1) - 1) + "*")
*     *
 *   * 
  * *  
   *   
  * *  
 *   * 
*     *
