package Skill_or_Luck;

import java.util.List;

public class Main {
    
    public static void main(String[] args) {
        List<Player> players = new java.util.ArrayList<>();
        int numPlayers = 100000;

        for (int x = 0; x < numPlayers; x++) {
            players.add(new Player(x+1));
        }

        double skillWeight = 0.9; // Weight for skill
        double luckWeight = 1 - skillWeight;  // Weight for luck

        System.out.println("Player Performance Rankings (Skill Weight: " + skillWeight + ", Luck Weight: " + luckWeight + "):");

        List<Player> Top10Players =   players.stream()
               .sorted((p1, p2) -> Double.compare(
                   p2.getOverallPerformance(skillWeight, luckWeight),
                   p1.getOverallPerformance(skillWeight, luckWeight)))
               .limit(10)
               .toList();

        List<Player> Top10SkillPlayers =   players.stream()
               .sorted((p1, p2) -> Double.compare(p2.getSkillLevel(), p1.getSkillLevel()))
               .limit(10)
               .toList();

        long count = Top10Players.stream()
                .filter(player -> !Top10SkillPlayers.contains(player))
                .count();

        System.out.println("Number of Players in Top 10 Overall Performance but not in Top 10 Skill: " + count);
        System.err.println("Percentage: " + ((double) count / Top10Players.size()) * 100 + "%");

    }
}