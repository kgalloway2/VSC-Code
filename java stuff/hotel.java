/*
Hotel Management System is another beginner level Java project that has many functionalities in it. 
This system merges a man and a computer into a single entity to give an automated hotel management system. 
In the current scenarios, every activity inside a hotel takes place manually which is very tedious and time-consuming.
This system can handle all the activities automatically without manual labor. These activities include hotel inquiry, 
check booking status, room booking, food order, Bill generation, inventory management, and other necessary hotel management features.
The hotel manager now does not need to sit and give time to manage such activities on paper and registers. 
The customers can view and book the hotel rooms online and also can use the other hotel services by requesting them, 
the admin then approves or rejects the customers booking request.

The hotel has a capcity of 100 with 25 rooms. Up to 4 people from a single party can fit into a room.
Currently, the hotel can do the following:
1. Accept bookings which would not overfill the hotel (> 100 guests or > 25 rooms).
2. Return info on a booking based on the name of the party who booked rooms.
3. Return the total bill for a booking based on the name of the party.
4. Checkout a party (vacate their rooms and return the bill).
5. add room service charges (which are added to the bill when it is calculated).
*/

import java.util.ArrayList;

public class hotel{
    int hotelCapacity;
    int roomCapacity;
    ArrayList<String> bookedParties;
    ArrayList<Integer> bookedPartySize;
    ArrayList<Integer> bookedPartyNights;
    ArrayList<Double> extraCharges;

    public hotel(int currentHotelCapacity, int currentRoomCapacity) {
        hotelCapacity = currentHotelCapacity;
        roomCapacity = currentRoomCapacity;
        bookedParties = new ArrayList<String>();
        bookedPartySize = new ArrayList<Integer>();
        bookedPartyNights = new ArrayList<Integer>();
        extraCharges = new ArrayList<Double>();
    }

    public int checkHotelCapacity() {
        return hotelCapacity;
    }

    public int checkRoomCapacity() {
        return roomCapacity;
    }

    public void bookAParty(String nameOfParty, int numberOfGuests, int numberOfNights) {
        int neededRooms = numberOfGuests / 4;
        if (checkHotelCapacity() + numberOfGuests < 100 && checkRoomCapacity() + neededRooms < 25) {
            if (numberOfGuests < 5) {
            hotelCapacity += numberOfGuests;
            roomCapacity += 1;
            bookedParties.add(nameOfParty);
            bookedPartySize.add(numberOfGuests);
            bookedPartyNights.add(numberOfNights);
            extraCharges.add(0.0);
            System.out.println("Your room has been booked for " + numberOfNights + " night(s).");
            } else {
                hotelCapacity += numberOfGuests;
                roomCapacity += neededRooms;
                bookedParties.add(nameOfParty);
                bookedPartySize.add(numberOfGuests);
                bookedPartyNights.add(numberOfNights);
                extraCharges.add(0.0);
                System.out.println("Your party is too large for a single room. Your " + neededRooms + " rooms have been booked for " + numberOfNights + " night(s).");
            }
        } else {
            System.out.println("We do not currently have space for your party.");
        }
    }

    public void checkBooking(String nameOfParty) {
        int partyIndex = bookedParties.indexOf(nameOfParty);
        if (partyIndex != -1) {
            System.out.println("The " + nameOfParty + " party has booked " + bookedPartySize.get(partyIndex) / 4 + " rooms for " + bookedPartyNights.get(partyIndex) + " nights.");
        } else {
            System.out.println("There are no bookings under that name.");
        }
    }

    public double calculateBill(String nameOfParty) {
        int partyIndex = bookedParties.indexOf(nameOfParty);
        if (partyIndex != -1) {
            double totalBill = 89.99 * bookedPartySize.get(partyIndex) * bookedPartyNights.get(partyIndex);
            totalBill += extraCharges.get(partyIndex);
            return totalBill;
        } else {
            System.out.println("There are no bookings under that name.");
            return -1;
        }
    }

    public void checkOut(String nameOfParty) {
        int partyIndex = bookedParties.indexOf(nameOfParty);
        double tempBill = calculateBill(nameOfParty);
        hotelCapacity -= bookedPartySize.get(partyIndex);
        roomCapacity -= Math.max(bookedPartySize.get(partyIndex) / 4, 1);
        bookedParties.remove(partyIndex);
        bookedPartySize.remove(partyIndex);
        bookedPartyNights.remove(partyIndex);
        extraCharges.remove(partyIndex);
        System.out.println("You have been successfuly checked out. Your bill is $" + tempBill + ".");
    }

    public void roomService(String nameOfParty, double roomServiceBill) {
        int partyIndex = bookedParties.indexOf(nameOfParty);
        extraCharges.set(partyIndex, extraCharges.get(partyIndex) + roomServiceBill);
    }

    public static void main(String[] args) {
        hotel hotel1 = new hotel(0,0);
        System.out.println("The hotel currently has " + hotel1.checkHotelCapacity() + " guests in " + hotel1.checkRoomCapacity() + " rooms.");
        hotel1.bookAParty("Smith", 45, 2);
        System.out.println("The hotel currently has " + hotel1.checkHotelCapacity() + " guests in " + hotel1.checkRoomCapacity() + " rooms.");
        hotel1.bookAParty("Doe", 3, 4);
        System.out.println("The hotel currently has " + hotel1.checkHotelCapacity() + " guests in " + hotel1.checkRoomCapacity() + " rooms.");
        hotel1.bookAParty("Kunthala", 22, 6);
        System.out.println("The hotel currently has " + hotel1.checkHotelCapacity() + " guests in " + hotel1.checkRoomCapacity() + " rooms.");
        hotel1.checkBooking("Kunthala");
        hotel1.roomService("Doe", 59.99);
        hotel1.checkOut("Doe");
        System.out.println("The hotel currently has " + hotel1.checkHotelCapacity() + " guests in " + hotel1.checkRoomCapacity() + " rooms.");
    }
}