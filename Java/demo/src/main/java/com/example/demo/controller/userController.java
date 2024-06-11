package com.example.demo.controller;

import com.example.demo.entity.users;
import com.example.demo.mapper.UserMapper;
import com.example.demo.utils.JwtUtils;
import com.example.demo.utils.Results;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/user")
@CrossOrigin
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
    @PostMapping("/login")
    public Results login(@RequestBody users user){
        String token = JwtUtils.generateToken(user.getUsername());
        return Results.ok().data("token",token);
    }

    @GetMapping("/info")
    public Results info(String token){
       String username = JwtUtils.getClaimsByToken(token).getSubject();
       String url = "https://img2.baidu.com/it/u=1325995315,4158780794&fm=26&fmt=auto&gp=0.jpg";
       return Results.ok().data("username",username).data("avatar",url);
    }
    @PostMapping("/logout")
    public Results logout(){
        return Results.ok();
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
