package com.example.hackathon_server.program.repository;


import com.example.hackathon_server.program.entity.Program;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.ArrayList;

public interface ProgramRepository extends JpaRepository<Program,Long> {
    ArrayList<Program> getByCategoryContaining(String category);

    ArrayList<Program> findAll();
}
