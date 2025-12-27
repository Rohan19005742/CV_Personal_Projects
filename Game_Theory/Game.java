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

    public void playGame(Player player1, Player player2, int rounds) {
        Moves player1_last_move = null;
        Moves player2_last_move = null;

        int player1_score = 0;
        int player2_score = 0;

        for (int i = 0; i < rounds; i++) {
            Moves move1 = player1.makeMove(player2_last_move);
            Moves move2 = player2.makeMove(player1_last_move);

            if (move1 == Moves.COOPERATE && move2 == Moves.COOPERATE) {
                player1_score += both_cooperate_points;
                player2_score += both_cooperate_points;
            } else if (move1 == Moves.DEFECT && move2 == Moves.DEFECT) {
                player1_score += both_defect_points;
                player2_score += both_defect_points;
            } else if (move1 == Moves.DEFECT && move2 == Moves.COOPERATE) {
                player1_score += one_defects_points;
            } else if (move1 == Moves.COOPERATE && move2 == Moves.DEFECT) {
                player2_score += one_defects_points;
            }

            player1_last_move = move1;
            player2_last_move = move2;
        }

        System.out.println(player1.getName() + " Score: " + player1_score);
        System.out.println(player2.getName() + " Score: " + player2_score);
    }

    public static void main(String[] args) {
        RandomPlayer player1 = new RandomPlayer("Alice", 0.7f);
        RandomPlayer player2 = new RandomPlayer("Bob", 0.4f);
        Game game = new Game(3, 1, 5);
        game.playGame(player1, player2, 100000);
    }
}
