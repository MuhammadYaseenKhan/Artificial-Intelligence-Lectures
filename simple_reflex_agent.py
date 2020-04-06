def simple_reflex_agent(percept, rules):
	state = get_state_from_percept(percept)
	action = rules[state]
	return action
