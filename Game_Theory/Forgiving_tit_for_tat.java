package Game_Theory;

public class Forgiving_tit_for_tat extends Player {
    public Forgiving_tit_for_tat(String name, float good_percentage) {
        super(name, good_percentage);
    }

    @Override
    public Moves makeMove(Moves opponentLastMove) {
        if (opponentLastMove == null || Math.random() < super.getGoodPercentage()) {
            return Moves.COOPERATE;
        }
        return opponentLastMove;
    }

    @Override
    public String getStrategy(){
        return "Forgiving Tit for Tat";
    }
}
