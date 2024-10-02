#here we will use threads to avoid double booking 
import threading

class SeatBookingSystem:
    def __init__(self, total_seats):
        self.total_seats = total_seats
        self.lock = threading.Lock()
        self.booked_seats = []

    def book_seat(self, seat_number):
        with self.lock:  # Acquire lock
            if seat_number in self.booked_seats:
                print(f"Seat {seat_number} is already booked.")
            elif seat_number > self.total_seats or seat_number < 1:
                print(f"Seat {seat_number} is not valid.")
            else:
                self.booked_seats.append(seat_number)
                print(f"Seat {seat_number} successfully booked.")

# Example usage
if __name__ == "__main__":
    booking_system = SeatBookingSystem(10)

    # Simulating multiple bookings
    def book():
        for i in range(1, 6):
            booking_system.book_seat(i)

    # Creating multiple threads
    t1 = threading.Thread(target=book)
    t2 = threading.Thread(target=book)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
