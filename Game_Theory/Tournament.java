package Game_Theory;

import java.util.*;

public class Tournament {

    private final List<Player> players;
    private final int[][] scoreGrid;
    private final Game game;
    private final int rounds;

    public Tournament(List<Player> players, Game game, int rounds) {
        this.players = players;
        this.game = game;
        this.rounds = rounds;
        this.scoreGrid = new int[players.size()][players.size()];
    }

    public void run() {
        for (int i = 0; i < players.size(); i++) {
            for (int j = i + 1; j < players.size(); j++) {

                Player p1 = players.get(i);
                Player p2 = players.get(j);

                int[] result = game.playGame(p1, p2, rounds);

                scoreGrid[i][j] = result[0];
                scoreGrid[j][i] = result[1];

                p1.recordGame(result[0], result[1]);
                p2.recordGame(result[1], result[0]);
            }
        }
    }

    public void displayLeaderboard() {
        List<Player> sorted = players.stream()
            .sorted(Comparator.comparingInt((Player p) -> p.totalScore).reversed())
            .toList();

        System.out.printf(
            "%-4s %-12s %-12s %-6s %-8s %-6s%n",
            "Pos", "Name", "TotalScore", "Wins", "Win%", "Games"
        );
        System.out.println("--------------------------------------------------");

        for (int i = 0; i < sorted.size(); i++) {
            Player p = sorted.get(i);

            System.out.printf(
                "%-4d %-12s %-12d %-6d %-7.1f %-6d%n",
                i + 1,
                p.getName(),
                p.totalScore,
                p.wins,
                p.winPercentage(),
                p.games
            );
        }
    }


}

