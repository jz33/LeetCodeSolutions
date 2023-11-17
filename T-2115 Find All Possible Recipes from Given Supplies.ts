/*
2115. Find All Possible Recipes from Given Supplies
https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

You have information about n different recipes. You are given a string array recipes and a 2D string array ingredients.
The ith recipe has the name recipes[i], and you can create it if you have all the needed ingredients from ingredients[i].
Ingredients to a recipe may need to be created from other recipes, i.e., ingredients[i] may contain a string that is in recipes.

You are also given a string array supplies containing all the ingredients that you initially have, and you have an infinite supply of all of them.

Return a list of all the recipes that you can create. You may return the answer in any order.

Note that two recipes may contain each other in their ingredients.

 

Example 1:

Input: recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]
Output: ["bread"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".

Example 2:

Input: recipes = ["bread","sandwich"], ingredients = [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"]
Output: ["bread","sandwich"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".

Example 3:

Input: recipes = ["bread","sandwich","burger"], ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies = ["yeast","flour","meat"]
Output: ["bread","sandwich","burger"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".
We can create "burger" since we have the ingredient "meat" and can create the ingredients "bread" and "sandwich".

 

Constraints:

    n == recipes.length == ingredients.length
    1 <= n <= 100
    1 <= ingredients[i].length, supplies.length <= 100
    1 <= recipes[i].length, ingredients[i][j].length, supplies[k].length <= 10
    recipes[i], ingredients[i][j], and supplies[k] consist only of lowercase English letters.
    All the values of recipes and supplies combined are unique.
    Each ingredients[i] does not contain any duplicate values.


*/
function findAllRecipes(
    recipes: string[],
    ingredients: string[][],
    supplies: string[]
): string[] {
    const graph = new Map<string, Set<string>>(); // {food : [foods]}
    const inEdges = new Map<string, number>(); // {food: income edge count}
    for (let i = 0; i < recipes.length; i++) {
        const recipe = recipes[i];
        for (const ing of ingredients[i]) {
            const togo = graph.get(ing);
            if (!togo) {
                graph.set(ing, new Set([recipe]));
            } else {
                togo.add(recipe);
                graph.set(ing, togo);
            }
            inEdges.set(recipe, (inEdges.get(recipe) ?? 0) + 1);
        }
    }

    const result = new Set<string>();
    const recipeSet = new Set(recipes);
    let row = supplies;
    while (row.length) {
        const newRow: string[] = [];
        for (const start of row) {
            if (recipeSet.has(start)) {
                result.add(start);
            }
            for (const togo of graph.get(start) ?? []) {
                const edgeCount = inEdges.get(togo);
                if (edgeCount !== undefined) {
                    const newEdgeCount = edgeCount - 1;
                    if (newEdgeCount === 0) {
                        newRow.push(togo);
                    }
                    inEdges.set(togo, newEdgeCount);
                }
            }
        }
        row = newRow;
    }

    return Array.from(result);
}
