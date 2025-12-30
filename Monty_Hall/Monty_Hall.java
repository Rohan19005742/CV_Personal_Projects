package Monty_Hall;

import java.util.HashSet;
import java.util.Random;
import java.util.Set;

public class Monty_Hall {

    public static void main(String[] args) {

        int totalGames = 10000;
        int numberOfDoors = 10;

        int switchWins = 0;
        int stayWins = 0;

        Random rand = new Random();

        for (int i = 0; i < totalGames; i++) {

            int carDoor = rand.nextInt(numberOfDoors);
            int contestantChoice = rand.nextInt(numberOfDoors);

            // Host opens all losing doors except one
            Set<Integer> openedDoors = new HashSet<>();

            for (int d = 0; d < numberOfDoors; d++) {
                if (d != contestantChoice && d != carDoor) {
                    openedDoors.add(d);
                }
            }

            // Find the one remaining unopened door (other than contestant choice)
            int switchDoor = -1;
            for (int d = 0; d < numberOfDoors; d++) {
                if (d != contestantChoice && !openedDoors.contains(d)) {
                    switchDoor = d;
                    break;
                }
            }

            // Staying
            if (contestantChoice == carDoor) {
                stayWins++;
            }

            // Switching
            if (switchDoor == carDoor) {
                switchWins++;
            }
        }

        System.out.println("Total games: " + totalGames);
        System.out.println("Switch wins: " + switchWins +
                " (" + (100.0 * switchWins / totalGames) + "%)");
        System.out.println("Stay wins: " + stayWins +
                " (" + (100.0 * stayWins / totalGames) + "%)");
    }
}
