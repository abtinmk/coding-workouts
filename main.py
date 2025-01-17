class DFA:
    def __init__(self, states, sigmas, enteghal, start_state, final_state):
        self.states = states
        self.sigmas = sigmas
        self.enteghal = enteghal
        self.start_state = start_state
        self.final_state = final_state
        self.current_state = self.start_state

    def reset(self):
        self.current_state = self.start_state

    def process(self, input_string):
        self.reset()
        for alphabet in input_string:
            if alphabet not in self.sigmas:
                raise ValueError(f'invalid: {alphabet}')
            self.current_state = self.enteghal[self.current_state][alphabet]
        return self.current_state in self.final_state

    def produce_strings(self,maxdepth=20):
        def dfs(state, current_string, result):
            if len(result)>maxdepth:
                return
            if state in self.final_state:
                result.append(current_string)
            for char in self.sigmas:
                next_state = self.enteghal.get(state, {}).get(char)
                if next_state :
                    dfs(next_state, current_string + char, result)
           

        results = []
        dfs(self.start_state, '', results)

        if not results:
         return [], [], '', ''  # وقتی رشته‌ای وجود ندارد

        min_string = min(results, key=len)
        max_string = max(results, key=len)
        return results, results[:20], min_string, max_string
    #فاز 3
    def minimize(self):
        partition=[set(self.final_state),set(self.states)-set(self.final_state)]
        updated=True
        while updated:
            updated=False
            new_partitions=[]

state = input('states:')
while state == "\n":
    state = input()
states = state.split()

n = True
first_state = input('first state:')
fstate = []
while n:
    final_state = input('finals:')
    fstate = final_state.split()
    for i in fstate:
        if i in states:
            n = False
        else:
            print(f'{i} not in states')
            break

sigma = input("alphabet:")
while sigma == "\n":
    sigma = input()
sigmas = sigma.split()

enteghal = {}
for i in states:
    moves = {}
    for j in sigmas:
        one_move = input(f'{i} with {j} move to:')
        moves[j] = one_move
    enteghal[i] = moves

dfa = DFA(states, sigmas, enteghal, first_state, fstate)
string_to_process = input('string to process:')
result_accept = dfa.process(string_to_process)
print(f'string {string_to_process} is {"accepted" if result_accept else "unaccepted"}')

result = dfa.produce_strings()
if len(result) == 4:
    strings1, strings2, smallest, biggest = result
    print('accepted strings:', strings2,"and",strings1)
    print(biggest, 'is the biggest')
    if len(smallest)==0:
        print("landa is the smallest")
    else:
        print(smallest, 'is the smallest')
else:
    print("No valid strings produced.")
x=int(input('string with much len you want: '))
wanted='nothing'
for i in strings1:
    if len(i)==x:
        wanted=i
        break

print(wanted)
