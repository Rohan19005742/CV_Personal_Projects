package Game_Theory;

import java.util.Random;

public class RandomPlayer extends Player {
    public RandomPlayer(String name, float good_percentage) {
        super(name, good_percentage);
    }

    @Override
    public Moves makeMove(Moves opponent_last_move) {
        Random r= new Random();
        if (r.nextDouble() < super.getGoodPercentage()) {
            return Moves.COOPERATE;
        } else {
            return Moves.DEFECT;
        }
    }
    
}
