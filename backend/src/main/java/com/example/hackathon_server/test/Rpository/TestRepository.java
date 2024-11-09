package com.example.hackathon_server.test.Rpository;

import com.example.hackathon_server.test.entity.TestEntity;
import org.springframework.data.jpa.repository.JpaRepository;

public interface TestRepository extends JpaRepository<TestEntity,Long> {

}
