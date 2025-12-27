package Game_Theory;

import java.util.List;

public class Main {
    public static void main(String[] args) {
        runAllGamesTournament();
    }

    public static void runAllGamesTournament() {
        List<Player> players = List.of(
            new RandomPlayer("Alice", 0f),
            new RandomPlayer("Bob", 0.1f),
            new RandomPlayer("Charlie", 0.2f),
            new RandomPlayer("Diana", 0.3f),
            new RandomPlayer("Eve", 0.4f),
            new RandomPlayer("Frank", 0.5f),
            new RandomPlayer("Grace", 0.6f),
            new RandomPlayer("Heidi", 0.7f),
            new RandomPlayer("Ivan", 0.8f),
            new RandomPlayer("Judy", 0.9f),
            new RandomPlayer("Mallory", 1f),
            new Tit_for_tat("TFT"),
            new Forgiving_tit_for_tat("FTFT 0.1", 0.1f),
            new Evil_tit_for_tat("evil 0.3", 0.3f)
        );

        List<Game> games = List.of(
            prisonerDilemmaGame(),
            prisonerDilemma2Game(),
            chickenGame(),
            stagHuntGame(),
            dontdothesameGame(),
            dothesameGame(),
            simpleCooperationGame(),
            harshCooperationGame(),
            splitOrStealGame()
        );

        for (Game game : games) {
            Tournament tournament = new Tournament(players, game, 100_000);

            tournament.run();
            tournament.displayLeaderboard();
            System.out.println();
        }
    }

    //Split or steal style
    public static void randomGoodAlwaysLossesTournament() {
        List<Player> players = List.of(
            new RandomPlayer("Alice", 0f),
            new RandomPlayer("Bob", 0.1f),
            new RandomPlayer("Charlie", 0.2f),
            new RandomPlayer("Diana", 0.3f),
            new RandomPlayer("Eve", 0.4f),
            new RandomPlayer("Frank", 0.5f),
            new RandomPlayer("Grace", 0.6f),
            new RandomPlayer("Heidi", 0.7f),
            new RandomPlayer("Ivan", 0.8f),
            new RandomPlayer("Judy", 0.9f),
            new RandomPlayer("Mallory", 1f),
            new Tit_for_tat("")

        );

        Game game = splitOrStealGame();
        Tournament tournament = new Tournament(players, game, 100_000);

        tournament.run();
        tournament.displayLeaderboard();
    }

    public static Game splitOrStealGame() {
        return Game.builder()
                .setReward(1)
                .setPunishment(0)
                .setTemptation(2)
                .setSucker(0)
                .setName("Split or Steal")
                .build();
    }

    public static Game prisonerDilemmaGame() {
        return Game.builder()
                .setReward(3)
                .setPunishment(1)
                .setTemptation(5)
                .setSucker(0)
                .setName("Prisoner's Dilemma")
                .build();
    }

    public static Game prisonerDilemma2Game() {
        return Game.builder()
                .setReward(-1)
                .setPunishment(-2)
                .setTemptation(0)
                .setSucker(-3)
                .setName("Prisoner's Dilemma 2")
                .build();
    }

    public static Game chickenGame() {
        return Game.builder()
                .setReward(0)
                .setPunishment(-10)
                .setTemptation(1)
                .setSucker(-1)
                .setName("Chicken")
                .build();
    }

    public static Game stagHuntGame() {
        return Game.builder()
                .setReward(4)
                .setPunishment(2)
                .setTemptation(3)
                .setSucker(0)
                .setName("Stag Hunt")
                .build();
    }

    public static Game dontdothesameGame() {
        return Game.builder()
                .setReward(0)
                .setPunishment(0)
                .setTemptation(1)
                .setSucker(1)
                .setName("Don't Do The Same")
                .build();
    }

    public static Game customGame(int reward, int temptation, int punishment, int sucker) {
        return Game.builder()
                .setReward(reward)
                .setTemptation(temptation)
                .setPunishment(punishment)
                .setSucker(sucker)
                .setName("Custom Game")
                .build();
    }

    public static Game dothesameGame() {
        return Game.builder()
                .setReward(1)
                .setPunishment(1)
                .setTemptation(0)
                .setSucker(0)
                .setName("Do The Same")
                .build();
    }

    public static Game simpleCooperationGame() {
        return Game.builder()
                .setReward(2)
                .setPunishment(0)
                .setTemptation(3)
                .setSucker(1)
                .setName("Simple Cooperation")
                .build();
    }

    public static Game harshCooperationGame() {
        return Game.builder()
                .setReward(5)
                .setPunishment(-5)
                .setTemptation(10)
                .setSucker(-10)
                .setName("Harsh Cooperation")
                .build();
    }
}