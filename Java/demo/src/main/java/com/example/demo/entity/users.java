package com.example.demo.entity;

public class users {
    private int id;
    private String username;
    private String passwd;
    private String birthday;
    // Constructors

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getPasswd() {
        return passwd;
    }

    public void setPasswd(String passwd) {
        this.passwd = passwd;
    }

    public String getBirthday() {
        return birthday;
    }

    public void setBirthday(String birthday) {
        this.birthday = birthday;
    }

    @Override
    public String toString() {
        return "users{" +
                "id=" + id +
                ", username='" + username + '\'' +
                ", password='" + passwd + '\'' +
                ", birthday='" + birthday + '\'' +
                '}';
    }
}
