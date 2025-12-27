package Game_Theory;

public class Game {

    private final int both_cooperate_points;
    private final int both_defect_points;
    private final int one_defects_points;


    public Game(int both_cooperate_points, int both_defect_points, int one_defects_points) {
        this.both_cooperate_points = both_cooperate_points;
        this.both_defect_points = both_defect_points;
        this.one_defects_points = one_defects_points;
    }

    public int[] playGame(Player player1, Player player2, int rounds) {
        Moves p1Last = null;
        Moves p2Last = null;

        int p1Score = 0;
        int p2Score = 0;

        for (int i = 0; i < rounds; i++) {
            Moves m1 = player1.makeMove(p2Last);
            Moves m2 = player2.makeMove(p1Last);

            if (m1 == Moves.COOPERATE && m2 == Moves.COOPERATE) {
                p1Score += both_cooperate_points;
                p2Score += both_cooperate_points;
            } else if (m1 == Moves.DEFECT && m2 == Moves.DEFECT) {
                p1Score += both_defect_points;
                p2Score += both_defect_points;
            } else if (m1 == Moves.DEFECT && m2 == Moves.COOPERATE) {
                p1Score += one_defects_points;
            } else {
                p2Score += one_defects_points;
            }

            p1Last = m1;
            p2Last = m2;
        }

        return new int[]{p1Score, p2Score};
    }
}
