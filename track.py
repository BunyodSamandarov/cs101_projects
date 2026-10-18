
history = [100]

def record_change(history, amount):
    new_balance = history[-1] + amount

    if new_balance >= 0:
        history.append(new_balance)
        return True
    else:
        return False


def undo_last(history):
    if len(history) > 1:
        history.pop()


def make_forecast(history, days, daily_saving):
    forecast = history.copy()

    for i in range(days):
        record_change(forecast, daily_saving)

    return forecast


n = int(input("Enter whole number: "))
rejected = 0

for i in range(n):
    amount = int(input("Enter change number: "))

    if record_change(history, amount) == False:
        rejected += 1

recorded_history = history.copy()

undo = int(input("Enter number of changes to undo: "))

for i in range(undo):
    undo_last(history)

days = int(input("Enter number of forecast days: "))
saving = int(input("Enter number of daily saving: "))

a = make_forecast(history, days, saving)

print(f"Recorded history: {recorded_history}")
print(f"Rejected changes: {rejected}")
print(f"History after undo: {history}")
print(f"Current balance: {history[-1]}")
print(f"Forecast history: {a}")
print(f"Forecast final balance: {a[-1]}")
