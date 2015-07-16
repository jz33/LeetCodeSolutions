/*
Second Highest Salary
https://leetcode.com/problems/second-highest-salary/
*/
Select MAX(Salary) From Employee
Where Salary < (Select MAX(Salary) From Employee)
