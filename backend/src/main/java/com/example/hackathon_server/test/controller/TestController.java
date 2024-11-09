package com.example.hackathon_server.test.controller;

import com.example.hackathon_server.test.Rpository.TestRepository;
import com.example.hackathon_server.test.entity.TestEntity;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class TestController {

    @Autowired
    private TestRepository testRepository;

    @GetMapping("/test")
    public String test() {
        return "hello world";
    }

    @PostMapping("/test/add")
    public void testAdd() {
        TestEntity testEntity = new TestEntity();
        testEntity.setName("세영");

        testRepository.save(testEntity);
    }
}
