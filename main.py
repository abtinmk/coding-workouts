class DFA:
    def __init__(self,states,sigmas,enteghal,start_state,final_state):
        self.states=states
        self.sigmas=sigmas
        self.enteghal=enteghal
        self.start_state=start_state
        self.final_state=final_state
        self.current_state=self.start_state
    def reset(self):
        self.current_state=self.start_state
    def process(self,input_string):
        self.reset()
        for alphabet in input_string:
            if alphabet not in self.sigmas:
                raise ValueError(f'invalid:{alphabet}')
            self.current_state=self.enteghal[self.current_state][alphabet]
        return self.current_state in self.final_state
    def produce_strings(self):
        def dfs(state,current_string,moshahede,result):
            if state in self.final_state:
                result.append(current_string)
            moshahede.append(state)
            for char in self.sigmas:
                next_state=self.enteghal.get(state,{}).get(char)
                if next_state and next_state not in moshahede:
                    if dfs(next_state,current_string+char,moshahede,result):
                        return True
            moshahede.pop()
            return False
        results=[]
        dfs(self.start_state,'',[],results)
        if len(results)<2:
            return results[0]
        min_string=min(results,key=len)
        max_string=max(results,key=len)
        return results,results[:2],min_string,max_string
state=input('states:')
while(state=="\n"):
    state=input()
states=state.split()
n=True
first_state=input('first state:')
fstate=[]
while(n):
    final_state=input('finals:')
    fstate=final_state.split()
    for i in fstate:
        if i in states:
            n=False
        else:
            print(f'{i} not in states')
            break
sigma=input("alphabet:")
while(sigma=="\n"):
    sigma=input()
sigmas=sigma.split()
enteghal={}
for i in states:
    moves={}
    for j in sigmas:
        one_move=input(f'{i} with {j} move to:')
        moves[j]=one_move
    enteghal[i]=moves
dfa=DFA(states,sigmas,enteghal,first_state,fstate)
string_to_process=input('string to process:')
result_accept=dfa.process(string_to_process)
print(f'string {string_to_process} is {"accepted" if result_accept else "unaccepted"}')
strings1,strings2,smallest,biggest=dfa.produce_strings()
print('accepted strings:',strings1,',',strings2)
print(biggest,'is the biggest')
print(smallest,'is the smallest')
