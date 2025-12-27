package Game_Theory;

public class Evil_tit_for_tat extends Player{

    public Evil_tit_for_tat(String name, float good_percentage) {
        super(name, good_percentage);
    }

    @Override
    public Moves makeMove(Moves opponentLastMove) {
        if (opponentLastMove == null) {
            return Moves.COOPERATE;
        }
        if (Math.random() < super.getGoodPercentage()) {
            return Moves.DEFECT;
        }
        return opponentLastMove;
    }

    @Override
    public String getStrategy(){
        return "Evil Tit for Tat";
    }
}
