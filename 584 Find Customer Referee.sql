'''
584. Find Customer Referee
https://leetcode.com/problems/find-customer-referee/
'''
# Write your MySQL query statement below
select name from Customer
where referee_id is null or referee_id != 2;