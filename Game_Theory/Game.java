package Game_Theory;

public class Game {

    private int reward;      // R: both cooperate
    private int temptation; // T: you defect, opponent cooperates
    private int punishment; // P: both defect
    private int sucker;     // S: you cooperate, opponent defects
    private String name;


    public static Builder builder() {
        return new Builder();
    }

    public static class Builder {
        private int reward;      // R: both cooperate
        private int temptation; // T: you defect, opponent cooperates
        private int punishment; // P: both defect
        private int sucker;     // S: you cooperate, opponent defects
        private String name;


        public Builder setReward(int reward) {
            this.reward = reward;
            return this;
        }

        public Builder setName(String name) {
            this.name = name;
            return this;
        }

        public Builder setTemptation(int temptation) {
            this.temptation = temptation;
            return this;
        }

        public Builder setPunishment(int punishment) {
            this.punishment = punishment;
            return this;
        }

        public Builder setSucker(int sucker) {
            this.sucker = sucker;
            return this;
        }

        public Game build() {
            return new Game(reward, temptation, punishment, sucker, name);
        }
    }

    private Game(int reward, int temptation, int punishment, int sucker, String name) {
        this.reward = reward;
        this.temptation = temptation;
        this.punishment = punishment;
        this.sucker = sucker;
        this.name = name;
    }

    public String getName() {
        return name;
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
                p1Score += reward;
                p2Score += reward;
            } else if (m1 == Moves.DEFECT && m2 == Moves.DEFECT) {
                p1Score += punishment;
                p2Score += punishment;
            } else if (m1 == Moves.DEFECT && m2 == Moves.COOPERATE) {
                p1Score += temptation;
                p2Score += sucker;
            } else {
                p2Score += temptation;
                p1Score += sucker;
            }

            p1Last = m1;
            p2Last = m2;
        }

        return new int[]{p1Score, p2Score};
    }
}
