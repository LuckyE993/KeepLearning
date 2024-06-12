package com.example.demo.controller;
import com.example.demo.entity.prize;
import com.example.demo.entity.rule;
import java.util.List;

public class RuleAndPrizesRequest {

    private rule rule;
    private List<prize> prizes;

    // Getters and Setters
    public rule getRule() {
        return rule;
    }

    public void setRule(rule rule) {
        this.rule = rule;
    }

    public List<prize> getPrizes() {
        return prizes;
    }

    public void setPrizes(List<prize> prizes) {
        this.prizes = prizes;
    }
}
