package com.example.demo.controller;

import com.example.demo.entity.users;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import com.example.demo.mapper.UserMapper;

import java.util.List;

@RestController

public class userController {
    @Autowired
    private UserMapper userMapper;

    @GetMapping("/queryUsers")
    public List query(){
        List<users> list = userMapper.selectList(null);
        System.out.println(list);
        return list;
    }
    @PostMapping("/addUser")
    public String addUser(users user){
        int i=userMapper.insert(user);
        if(i>0){
            return "success";
        }else{
            return "fail";
        }
    }
//
//    @GetMapping("/user/{id}")
//    public String getUserById(@PathVariable int id) {
//        System.out.println("id = " + id);
//        return "hello";
//    }
//    @PostMapping("/user")
//    public String addUser(users user) {
//        return "Add ok";
//    }
//    @PutMapping("/user")
//    public String updateUser(users user) {
//        return "Update ok";
//    }
//    @DeleteMapping("/user/{id}")
//    public String deleteUser(@PathVariable int id) {
//        System.out.println("id = " + id);
//        return "delete ok";
//    }
//
//
//


}
