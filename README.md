Guest Dinner Sign Down
======================

Run [this program](../master/signdown.py) in the same folder as a file called `hat.txt` like this:

```
5

Alice
Bob
Charlie

Dave

Evie
Frank
Garry

Harry
Ian
```

and it will produce a file in the same folder called `results.txt` like this:

```
SUCCESSFUL GROUPS:

Alice
Bob
Charlie

Harry
Ian

0 EMPTY SEATS
```

which contains groups selected at random to fill the hall.

The first line in `hat.txt` is the number of seats in the hall, followed by the groups who are balloting together, with one name on each line and a blank line between each group.
