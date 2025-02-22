# first start by searching for all the file in level00 that belongs to the flag00 user.
``
find / -user flag00
``
ignore the one with the permission issue. then you'll find a file called /usr/sbin/john.
in that file you'll find an encrypted string.
I used an online tool to discover how it is encrypted. (affine cipher).
since it is a weak method of encryption. you'll crack it easily.x24ti5gi3x0ol2eh4esiuxias