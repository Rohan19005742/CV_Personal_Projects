package Game_Theory;

public abstract class Player {
    private final String name;
    private final float good_percentage;

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

    public abstract Moves makeMove(Moves opponent_last_move);
}