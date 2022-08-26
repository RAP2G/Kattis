# Kattis

Hello World!
Input
There is no input for this problem.

Output
Output should contain one line, containing the string “Hello World!”.


FizzBuzz
Image by chris morgan cc by
According to Wikipedia, FizzBuzz is a group word game for children to teach them about division. This may or may not be true, but this question is generally used to torture screen young computer science graduates during programming interviews.
Basically, this is how it works: you print the integers from  to , replacing any of them divisible by  with Fizz or, if they are divisible by , with Buzz. If the number is divisible by both  and , you print FizzBuzz instead.

Check the samples for further clarification.

Input
Input contains a single test case. Each test case contains three integers on a single line, ,  and  ().

Output
Print integers from  to  in order, each on its own line, replacing the ones divisible by  with Fizz, the ones divisible by  with Buzz and ones divisible by both  and  with FizzBuzz.


Hissing Microphone
A known problem with some microphones is the “hissing s”. That is, sometimes the sound of the letter s is particularly pronounced; it stands out from the rest of the word in an unpleasant way.

Of particular annoyance are words that contain the letter s twice in a row. Words like amiss, kiss, mississippi and even hiss itself.

Input
The input contains a single string on a single line. This string consists of only lowercase letters (no spaces) and has between  and  characters.

Output
Output a single line. If the input string contains two consecutive occurrences of the letter s, then output hiss. Otherwise, output no hiss.


Oddities
Some numbers are just, well, odd. For example, the number  is odd, because it is not a multiple of two. Numbers that are a multiple of two are not odd, they are even. More precisely, if a number  can be expressed as  for some integer , then  is even. For example,  is even.

Some people get confused about whether numbers are odd or even. To see a common example, do an internet search for the query “is zero even or odd?” (Don’t search for this now! You have a problem to solve!)

Write a program to help these confused people.

Input
Input begins with an integer  on a line by itself, indicating the number of test cases that follow. Each of the following  lines contain a test case consisting of a single integer .

Output
For each , print either ‘ is odd’ or ‘ is even’ depending on whether  is odd or even.