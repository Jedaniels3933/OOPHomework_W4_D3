class BudgetCategory:
    def __init__(self, __category_name, __allocated_budget,):
        self.__category_name = __category_name
        self.__allocated_budget = __allocated_budget
        self.expenses = []

    def set_category_name(self, new_category_name):
        self.__category_name = new_category_name
    def set_allocated_budget(self, new_allocated_budget):
        self.__allocated_budget = new_allocated_budget
    def get_category_name(self):
        return
    def get_allocated_budget(self):
        return
    def __repr__(self):
        return f"<BudgetCategory: {self.__category_name}, ${self.__allocated_budget: .2f}>"
    def add_expense(self, expense):
        self.expenses.append(expense)
        if self.get_total_expenses() > self.__allocated_budget:
            print("Warning: Expenses exceed budgeted amount")
        elif self.get_total_expenses() == self.__allocated_budget:
            print("Warning: Expenses equal budgeted amount")
        else:
            print("Expenses are within budget")
    
    def get_total_expenses(self):
        total = 0
        for expense in self.expenses:
            total += expense.amount
        return total
    def display_category_summary(self):
        print(f"Category: {self.__category_name}")
        print(f"Budgeted: ${self.__allocated_budget: .2f}")
        print(f"Spent: ${self.get_total_expenses(): .2f}")
        print(f"Remaining: ${self.__allocated_budget - self.get_total_expenses(): .2f}")
        print("Expenses:")
        for expense in self.expenses:
            print(f"  {expense}")
    
   

food_category = BudgetCategory("Food", 1000)
#food_category.add_expense(100)                Everything but this works
food_category.display_category_summary()

    
        

      