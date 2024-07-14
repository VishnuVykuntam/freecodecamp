def arithmetic_arranger(problems, show_answers=False):

    before,op,after=[],[],[]
    items=[p.split() for p in problems]
    l=len(items)
    if l>5:
        return 'Error: Too many problems.'
    for i in items:
        
        for j in i:
            if j.isalpha():
                return ('Error: Numbers must only contain digits.')
            
        if i[1] not in ['+','-']:
            return ("Error: Operator must be '+' or '-'.")
        if len(i[0])>4 or len(i[2])>4:
            return ('Error: Numbers cannot be more than four digits.')
        before.append((i[0]))
        op.append(i[1])
        after.append((i[2]))
    operand1=[int(before[i]) for i in range(len(before))]
    operand2=[int(after[i]) for i in range(len(after))]
    string1=""
    string2=""
    string3=""
    for i in range(l):
        k=len(before[i])-len(after[i])
        m=max(len(before[i]),len(after[i]))
        string3+="-"*(int(m))
        string3+='--'
        items[i].insert(2,' ')
        if k>0:
            items[i].insert(2,' '*(k))
        elif k<0:
            items[i].insert(0,' '*(-k))
        items[i].insert(0,'  ')
        for j in range(len(items[i])):
            if items[i][j] not in ['+','-']:
                string1+=items[i][j]
                
            else:
                
                for k in range(j,len(items[i])):
                    string2+=items[i][k]
                break
        string1+='    '
        string2+='    '
        string3+='    '
        list1=list(string1)
        for k in list1:
            if k.isalpha():
                return 'Error: Numbers must only contain digits.'
        list2=list(string2)
        for k in list2:
            if k.isalpha():
                return 'Error: Numbers must only contain digits.'

    
    string=string1.rstrip()+'\n'+string2.rstrip()+'\n'+string3.rstrip()
    
    answers=[]
    print(operand1,op,operand2,answers)
    if show_answers:
        for i in range(len(op)):
            if op[i]=='+':
                answers.append(operand1[i]+operand2[i])
            else:
                answers.append(operand1[i]-operand2[i])
        ans=string3.split()
        string4=""
        for i in range(len(ans)):
            length=len(str(answers[i]))
            hyphens=len(ans[i])
            for j in range(hyphens-length):
                string4+=' '
                
            string4+=str(answers[i])
            string4+='    '
        string+='\n'+string4

    return string


print(f'{arithmetic_arranger(["3 + 855", "988 + 40"], True)}')
