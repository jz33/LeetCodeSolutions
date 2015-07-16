/*
Combine Two Tables
https://leetcode.com/problems/combine-two-tables/
*/
Select Person.FirstName, Person.LastName, Address.City, Address.State
From Person left join Address on Person.PersonId = Address.PersonId
