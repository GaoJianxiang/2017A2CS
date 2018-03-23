factorial(0, 1).
factorial(N, F) :-
	X is N - 1,
	factorial(X, Y),
	F is N * Y.


bunnyEars(0,0).
bunnyEars(A,B) :-
	X is A - 1,
	bunnyEars(X, Y),
	B is Y+2.

fibonacci(0,0).
fibonacci(1,1).
fibonacci(A,B):-
	X is A-1,
	Y is A-2,
	fibonacci(X, Z),
	fibonacci(Y, W),
	B is Z+W


bunnyears2(0,0).
bunnyears2(A, B):-
    Z is A-1,
    bunnyears2(Z,W),
    X is Z mod 2,
    B is W+2+X.

triangle(0,0).
triangle(1,1).
triangle(X,Y):-
    Z is X-1,
    triangle(Z,T),
    Y is T+X.

sumdigits(0,0).
sumdigits(X,Y):-
    Z is X//10,
    sumdigits(Z, S),
    Y is S+X mod 10.

count7(0,0).
count7(X,Y):-
    Z is X//10,
    B is X mod 10,
    count7(Z, S),
    Y is S+ B//7-B//8.
