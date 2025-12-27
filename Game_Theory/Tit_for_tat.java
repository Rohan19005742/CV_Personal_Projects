package Game_Theory;

public class Tit_for_tat extends Player {
    public Tit_for_tat(String name) {
        super(name, 0f);
    }

    @Override
    public Moves makeMove(Moves opponentLastMove) {
        if (opponentLastMove == null) {
            return Moves.COOPERATE;
        }
        return opponentLastMove;
    }

    @Override
    public String getStrategy(){
        return "Tit for Tat";
    }
}