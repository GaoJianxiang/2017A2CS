﻿#3.1

character(habib).
charcater_type(habib,explorer).
has_skill(habib,timetravel).
pet(habib,fish).

#3.2

onlyPet(C,P) :-
	character(C),animal(P).

#3.3

character(stefan).
character(elena).
animal(cat).
animal(dog).
pet(stefan,cat).
pet(elena,dog).
has_skill(stefan,heal).
has_skill(elana,dance).

#3.4

True.
X = princess.
X = jim.
X = invisibility.
X = jim.

#3.5

pet(jim,X).
has_skill(X,fly).
skill(X).

type_pet(T,P) :-
	character_type(C,T),pet(C,P).

type_pet(princess,X).
