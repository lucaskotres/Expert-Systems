
def gps(initial_states, goal_states, operators):

    prefix = 'Executando '
    for operator in operators:
        operator['add'].append(prefix + operator['action'])

    final_states = achieve_all(initial_states, operators, goal_states, [])
    if not final_states:
        return None
    return [state for state in final_states if state.startswith(prefix)]


def achieve_all(states, ops, goals, goal_stack):

    for goal in goals:
        states = achieve(states, ops, goal, goal_stack)
        if not states:
            return None

    for goal in goals:
        if goal not in states:
            return None

    return states


def achieve(states, operators, goal, goal_stack):

    debug(len(goal_stack), 'Achieving: %s' % goal)
   
    if goal in states:
        return states

    if goal in goal_stack:
        return None

    for op in operators:
        
        if goal not in op['add']:
            continue

        result = apply_operator(op, states, operators, goal, goal_stack)
        if result:
            return result

def apply_operator(operator, states, ops, goal, goal_stack):

    debug(len(goal_stack), 'Consider: %s' % operator['action'])

    result = achieve_all(states, ops, operator['preconds'], [goal] + goal_stack)
    if not result:
        return None

    debug(len(goal_stack), 'Action: %s' % operator['action'])

    add_list, delete_list = operator['add'], operator['delete']
    return [state for state in result if state not in delete_list] + add_list

import logging

def debug(level, msg):
    logging.debug(' %s %s' % (level * '  ', msg))