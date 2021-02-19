# AverageScore
### Aim: Get average score from a table in pdf for a lesson

Some tables in the pdf file do not what seems. For instance:

Student ID | Score
------:|------
xxxxxx | 50
xxxxxx | 35,5
xxxxxx | 53
xxxxxx | 100

This table seems pretty well, but you will see some problems if you will check the CSV file;

1. Student ID,Score
2. xxxxxx,50
3. xxxxxx,"35,5"
4. xxxxxx,53
5. xxxxxx,100
6. "" 👈

**Did you see the sixth line? That is not correct, so you should check the CSV file for the correct average score. 
Then, only delete that line and restart the code.**
