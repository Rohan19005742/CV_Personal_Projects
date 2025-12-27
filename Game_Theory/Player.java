package Game_Theory;

public abstract class Player {
    private final String name;
    private final float good_percentage;

    int totalScore = 0;
    int wins = 0;
    int games = 0;

    public Player(String name, float good_percentage) {
        this.name = name;
        this.good_percentage = good_percentage;
    }

    public String getName() {
        return name;
    }

    public float getGoodPercentage() {
        return good_percentage;
    }

    public abstract Moves makeMove(Moves opponentLastMove);

    public void recordGame(int myScore, int opponentScore) {
        totalScore += myScore;
        games++;
        if (myScore > opponentScore) {
            wins++;
        }
    }

    public double winPercentage() {
        return games == 0 ? 0 : (wins * 100.0 / games);
    }

    public String displayName() {
        return String.format("%s (%.1f%%)", name, winPercentage());
    }
}
