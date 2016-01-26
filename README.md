[![build monitor](https://travis-ci.org/tomviner/chess.svg "build monitor")](https://travis-ci.org/tomviner/chess)
[![Coverage Status](https://coveralls.io/repos/tomviner/chess/badge.png?branch=master)](https://coveralls.io/r/tomviner/chess?branch=master)

Chess
=====

My friend Rich and I have been playing chess for about a quater century.
We used to play in each other's houses, but now he lives 600 miles away.
So my aim is to make an online chess board we can play on again.
I plan to use Python and TDD.

Planning
========

To get to the end goal of _two way web chess_ I need to progress through these milestones:

Stage 1
-------

- A **board** that can
    - place pieces
    - display itself
    - move pieces
- A **game** that can
    - initialise a board
    - take input from a player
        - ultimately from the web interface
        - from raw_input for now
- Using **chess notation**
    - [Algebraic chess notation](http://en.wikipedia.org/wiki/Algebraic_chess_notation)
    - Validating input in terms of boundries

Stage 2
-------
- The **game** now can:
    - alternate between two users
    - follow basic rules of taking

Further Stages
==============

Normal Moves
------------

- The ways each Piece can move
- Pawn's initial move
- Pawn taking

Special Moves
-------------

- (Rule - knowledge requirement)
- Castling - past moves of king & rook
- En passant - previous move of pawn
- Pawn promotion - user choice of piece or assume queen
- Stalemate - last 50 moves

End of the Game
---------------

- (Check)
- Checkmate
- Stalemate
- Resignation

User Stories
============

- As a **chess player** I want **to view a chess board** so that **I can play chess**

- As a **chess player** I want **to submit a move** so that **I can attempt to checkmate my friend**

- As a **chess player** I want **to see the other player's moves** so that **I can defend against my friend's moves**

- As a **chess player** I want **the rules of chess to be enforced** so that **my friend doesn't cheat - or me make an illegal move accidentally**

- As a **chess player** I want **to see who's turn it is** so that **I know when to move**

- As a **chess player** I want **a win/lose/draw to be displayed** so that **my friend and I know who's won**

Scenarios
=========

Initial Board from Players' perspective
---------------------------------------

**GIVEN** I'm playing as White
**WHEN** I start a game of chess
**THEN** I should see a chess board in the standard initial layout, with White in the lower half

**GIVEN** I'm playing as Black
**WHEN** I start a game of chess
**THEN** I should see a chess board in the standard initial layout, with Black in the lower half

Moving a piece
--------------

**GIVEN** We have just started a game of chess
**AND** I'm White
**WHEN** I advance my Queen's pawn two squares
**THEN** My friend should see my move

Taking a piece
--------------

**GIVEN** A game has advanced to just one Rook each
**AND** It's my turn, and the Rooks share a rank
**WHEN** I take my friend's Rook
**THEN** His piece is removed from the board, and mine is placed there

Rules of Chess enforced
-----------------------

See who's turn it is
--------------------

Detect endgame state
--------------------

