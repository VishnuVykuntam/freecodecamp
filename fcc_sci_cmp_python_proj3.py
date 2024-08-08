class Category:
    def __init__(self,category_name):
        self.category_name=category_name
        self.ledger=[]
    def __str__(self):
        string=''
        one_side=(30-len(self.category_name))//2
        string+='*'*one_side+self.category_name+'*'*one_side+'\n'
        for item in self.ledger:
            desc_length=len(item['description'])
            if desc_length<23:
                string+=item['description']+' '*(23-desc_length)
            else:
                desc_cut=item['description'][:23]
                string+=desc_cut
            amount_len=len(f"{(float(item['amount'])):.2f}")
            if amount_len<=7:
                string+=' '*(7-amount_len)+f"{(float(item['amount'])):.2f}"+'\n'
            else:
                while(amount_len>7):
                    cash=list(f"{(float(item['amount'])):.2f}")
                    cash.pop()
                    amount_len-=1
                string+=''.join(cash)+'\n'
        string+= "Total: "
        string += f"{self.get_balance():.2f}"
        return string
    def check_funds(self,amount):
        return amount <= sum([item['amount'] for item in self.ledger])
    def deposit(self,amount,description=''):
        self.ledger.append({'amount':amount,'description':description})
    def withdraw(self,amount,description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount':-amount,'description':description})
            return True
        else:
            return False
    def get_balance(self):
        return sum([item['amount'] for item in self.ledger])
    def transfer(self,amount,another_category):
        if self.check_funds(amount):
            self.ledger.append({'amount':-amount,f'description':f'Transfer to {another_category.category_name}'})
            another_category.deposit(amount,f'Transfer from {self.category_name}')
            return True
        else:
            return False

def create_spend_chart(categories):
    bar_chart='Percentage spent by category\n'
    num_categories=len(categories)
    spent=[]
    percent=[]
    names=[]
    total=0
    print(num_categories)
    for i in range(num_categories):
        temp=categories[i]
        names.append(temp.category_name)
        for item in temp.ledger:
            k=item['amount']
            if k<0:
                total+=abs(k)
        spent.append(sum([abs(item['amount']) if item['amount']<0 else 0 for item in temp.ledger]))

    for i in range(num_categories):
        print(spent[i]*100/total)
        try:
            percent.append(10 * (spent[i]*100/total)//10)
        except:
            percent.append(0)
        print(percent)
    print(percent)
    for i in range(10,-1,-1):
        if i==10:
            bar_chart+=f'{i*10}| '
        elif i==0:
            bar_chart+='  0| '
        else:
            bar_chart+=f' {i*10}| '
        for j in range(num_categories):
            if percent[j]<i*10:
                bar_chart+='   '
            else:
                bar_chart+='o  '
        bar_chart+=f'\n'
    bar_chart+='    '+'-'*num_categories*3+'-\n'
    biggest_name_length=max([len(name) for name in names])
    for i in range(biggest_name_length):
        bar_chart+='    '
        for j in range(num_categories):
            try:
                bar_chart+=f' {names[j][i]} '
            except:
                bar_chart+=f'   '
        if i==biggest_name_length-1:
            bar_chart+=' '
        else:
            bar_chart+=' \n'
    print("hi",bar_chart[-1]==' ')
    return bar_chart
Clothing=Category('Clothing')
food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
Clothing.deposit(500,'deposit')
Clothing.withdraw(300,'test')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)
categories=[food,Clothing]
print(create_spend_chart(categories))