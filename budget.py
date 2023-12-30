class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, payee):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {payee.name}")
            payee.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"*{self.name.center(28)}*"
        ledger_strings = [f"{item['description'][:23]:<23}{item['amount']:>7.2f}" for item in self.ledger]
        total = self.get_balance()
        ledger_strings.append(f"Total: {total:>7.2f}")
        return "\n".join([title] + ledger_strings)


def create_spend_chart(categories):
    percentages = [round(category.get_balance() / category.get_balance() * 100, 2) for category in categories]
    total_height = round(max(percentages), -1)
    chart = []
    for i in range(0, int(total_height), -10):
        line = []
        for category, percentage in zip(categories, percentages):
            if percentage >= i:
                line.append("o" * (percentage - i))
            else:
                line.append(" " * (100 - i))
        chart.append("|".join(line))
    bottom_line = []
    for category in categories:
        bottom_line.append(category.name[:3].center(10))
    chart.append("-" * len(bottom_line[0]))
    chart.append("   ".join(bottom_line))
    chart.append("Percentage spent by category")
    return "\n".join(chart[::-1])