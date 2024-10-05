class PayoutCalculator:
    def __init__(self):
        self.calculate_payout()

    def calculate_payout(self) -> None:
        work_hours: int = int(input("Enter work hours: "))

        if work_hours <= 140:
            payout: int = work_hours * 30_000
        elif work_hours > 140:
            extra_hours = work_hours - 140

            if extra_hours > 50:
                extra_hours = 50

            payout: int = (work_hours * 30_000) + (extra_hours * 50_000)

        print(f"Payout: {payout:,}")

if __name__ == '__main__':
    app = PayoutCalculator()