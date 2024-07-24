# resource_optimizer.py
import pulp

def optimize_resources(tasks, resources):
    # 创建问题
    prob = pulp.LpProblem("Resource Allocation", pulp.LpMaximize)

    # 决策变量
    x = pulp.LpVariable.dicts("task", 
                              ((i, j) for i in tasks for j in resources), 
                              lowBound=0,
                              cat='Integer')

    # 目标函数：最大化完成的任务数
    prob += pulp.lpSum([x[i, j] for i in tasks for j in resources])

    # 约束条件
    for j in resources:
        prob += pulp.lpSum([x[i, j] for i in tasks]) <= resources[j]['capacity']

    for i in tasks:
        prob += pulp.lpSum([x[i, j] for j in resources]) <= 1

    # 求解问题
    prob.solve()

    # 返回结果
    results = {}
    for i in tasks:
        for j in resources:
            if x[i, j].value() > 0:
                results[i] = j

    return results

# 使用示例
tasks = ['Task1', 'Task2', 'Task3', 'Task4']
resources = {
    'Resource1': {'capacity': 2},
    'Resource2': {'capacity': 3}
}

allocation = optimize_resources(tasks, resources)
print(allocation)
