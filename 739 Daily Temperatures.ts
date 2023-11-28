/*
739. Daily Temperatures
https://leetcode.com/problems/daily-temperatures/

Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]

Constraints:
    1 <= temperatures.length <= 105
    30 <= temperatures[i] <= 100
*/
function dailyTemperatures(temperatures: number[]): number[] {
    const result = new Array(temperatures.length).fill(0);
    const stack: number[] = []; // indexes of previous temperatures
    for (let i = 0; i < temperatures.length; i++) {
        const currentTemp = temperatures[i];
        while (stack.length && currentTemp > temperatures[stack.at(-1)]!) {
            const lastTempIndex = stack.pop();
            result[lastTempIndex] = i - lastTempIndex;
        }
        stack.push(i);
    }
    return result;
};

// A O(N) method without stack
function dailyTemperatures(temperatures: number[]): number[] {
    const result = new Array(temperatures.length).fill(0);
    let hottestTemp = temperatures.at(-1)!;
    for (let day = temperatures.length - 1; day > -1; day--) {
        const currentTemp = temperatures[day];
        if (currentTemp >= hottestTemp) {
            // If current temp is the hottest from now on, there is no answer on i.
            hottestTemp = currentTemp;
        } else {
            // Keep finding the higher temp day on right, using existing results.
            // As the lookup is jumping, total lookup time won't exceed N
            // No need to check boundary of higherDay as current temp is not hottest
            let higherDay = day + 1;
            while (temperatures[higherDay] <= currentTemp) {
                higherDay = higherDay + result[higherDay];
            }
            result[day] = higherDay - day;
        }
    }
    return result;
}
