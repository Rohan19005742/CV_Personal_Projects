package Skill_or_Luck;

public class Player {
    private double skillLevel; // 0.0 (no skill) to 1.0 (maximum skill)
    private double luckLevel;  // 0.0 (no luck) to 1.0 (maximum luck)
    private int id;

    public Player(int id) {
        this.id = id;
        this.skillLevel = Math.random();
        this.luckLevel = Math.random();
    }

    public double getSkillLevel() {
        return skillLevel;
    }

    public double getLuckLevel() {
        return luckLevel;
    }

    public double getOverallPerformance(double skillWeight, double luckWeight) {
        return (skillLevel * skillWeight + luckLevel * luckWeight) / (skillWeight + luckWeight);
    }

    public int getId() {
        return id;
    }

    public Boolean CompareTo(Player other) {
        return this.id == other.id;
    }
}
