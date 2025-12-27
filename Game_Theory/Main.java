package Game_Theory;

import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<Player> players = List.of(
            new RandomPlayer("Alice", 0f),
            new RandomPlayer("Bob", 0.8f),
            new RandomPlayer("Charlie", 0.7f)
        );

        Game game = new Game(3, 1, 5);
        Tournament tournament = new Tournament(players, game, 100_000);

        tournament.run();
        tournament.displayLeaderboard();
    }
}