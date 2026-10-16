
class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({
            'amount': amount,
            'description': description
        })

    def get_balance(self):
        balance = 0

        for transaction in self.ledger:
            balance += transaction['amount']

        return balance

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({
                'amount': -amount,
                'description': description
            })
            return True

        return False

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True

        return False

    def __str__(self):
        title = self.name.center(30, '*') + '\n'
        items = ''

        for transaction in self.ledger:
            description = transaction['description'][:23]
            amount = f"{transaction['amount']:>7.2f}"
            items += f"{description:<23}{amount}\n"

        total = f"Total: {self.get_balance():.2f}"

        return title + items + total


def create_spend_chart(categories):
    if not categories:
        return "Percentage spent by category"

    spent_list = []

    for category in categories:
        spent = 0

        for transaction in category.ledger:
            if transaction['amount'] < 0:
                spent += abs(transaction['amount'])

        spent_list.append(spent)

    total_spent = sum(spent_list)

    if total_spent > 0:
        percentages = []

        for spent in spent_list:
            percentage = (spent / total_spent) * 100
            rounded_percentage = (int(percentage) // 10) * 10
            percentages.append(rounded_percentage)
    else:
        percentages = [0 for _ in categories]

    chart = "Percentage spent by category\n"

    for i in range(100, -1, -10):
        chart += f"{i:>3}| "

        for percentage in percentages:
            if percentage >= i:
                chart += "o  "
            else:
                chart += "   "

        chart += "\n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    max_length = max(len(category.name) for category in categories)
    names = [category.name.ljust(max_length) for category in categories]

    for i in range(max_length):
        chart += "     "

        for name in names:
            chart += f"{name[i]}  "

        if i < max_length - 1:
            chart += "\n"

    return chart
