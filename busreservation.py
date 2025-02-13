class BusTicketReservation:
    def __init__(self):
        self.seats = [False] * 40  # Assuming a bus with 40 seats

    def display_seats(self):
        print("Bus Seat Layout:")
        for i in range(0, 40, 4):
            row = self.seats[i:i+4]
            print(" ".join(['X' if seat else 'o' for seat in row]))
        print("O: Available, X: Reserved")

    def reserve_seat(self, seat_number):
        if seat_number < 1 or seat_number > 40:
            print("Invalid seat number. Please choose a seat between 1 and 40.")
            return False
        if self.seats[seat_number - 1]:
            print(f"Seat {seat_number} is already reserved.")
            return False
        self.seats[seat_number - 1] = True
        print(f"Seat {seat_number} has been successfully reserved.")
        return True

    def cancel_reservation(self, seat_number):
        if seat_number < 1 or seat_number > 40:
            print("Invalid seat number. Please choose a seat between 1 and 40.")
            return False
        if not self.seats[seat_number - 1]:
            print(f"Seat {seat_number} is not reserved.")
            return False
        self.seats[seat_number - 1] = False
        print(f"Reservation for seat {seat_number} has been successfully canceled.")
        return True

def main():
    reservation_system = BusTicketReservation()
    print("Welcome to the Bus Ticket Reservation System! Type 'exit' to end the session.")
    while True:
        print("\nOptions: display, reserve <seat_number>, cancel <seat_number>, exit")
        user_input = input("You: ").strip().lower()
        if user_input == 'exit':
            print("Goodbye!")
            break
        elif user_input == 'display':
            reservation_system.display_seats()
        elif user_input.startswith('reserve'):
            try:
                seat_number = int(user_input.split()[1])
                reservation_system.reserve_seat(seat_number)
            except (IndexError, ValueError):
                print("Please provide a valid seat number to reserve.")
        elif user_input.startswith('cancel'):
            try:
                seat_number = int(user_input.split()[1])
                reservation_system.cancel_reservation(seat_number)
            except (IndexError, ValueError):
                print("Please provide a valid seat number to cancel.")
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()