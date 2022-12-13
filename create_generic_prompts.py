for i in range(3):
    with open(f"survey_problems/problem{i+1}.txt", 'r') as f:
        problem = f.read()
        print(f'--------Problem {i+1}---------')
        print(problem)
        print('--------------------------')
        problem = problem.replace('clear', 'pred1')
        problem = problem.replace('ontable', 'pred2')
        problem = problem.replace('on', 'pred3')
        problem = problem.replace('handempty', 'pred4')

        problem = problem.replace('unstack', 'op1')
        problem = problem.replace('put-down', 'op2')
        problem = problem.replace('stack', 'op3')
        problem = problem.replace('pick-up', 'op4')

        problem = problem.replace('block', 'object')
        print(f'--------Problem {i+4}---------')
        print(problem)
        print('--------------------------')
