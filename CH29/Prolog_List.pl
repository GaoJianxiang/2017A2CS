member(I,[I|_]).
member(I,[_|T]):-
	member(I,T).

myappend([],X,X).
myappend([H|T],L,[H|R]):-
	myappend(T,L,R).


mylast(H,[H]).
mylast(L,[_|X]):-
	mylast(L,X).

mylast2(X,[X,_]).
mylast2(L,[_|X]):-
	mylast2(L,X).

element_at(H,[H|_],1).
element_at(L,[_|T],X):-
	Z is X-1,\
	element_at(L,T,Z).

len([],0).\
len([_|T],L):-
	len(T,X),
	L is X+1.