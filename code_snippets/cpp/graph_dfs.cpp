#include<iostream>
#include<map>
#include<set>

void dfs(std::map<int, std::set<int>>& graph, int start, std::set<int>& visited) {
    visited.insert(start);
    for (int next : graph[start]) {
        if (visited.find(next) == visited.end())
            dfs(graph, next, visited);
    }
}
