package com.example.hackathon_server.bookconnected.repository;

import com.example.hackathon_server.bookconnected.entity.Library;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.ArrayList;

public interface LibraryRepository extends JpaRepository<Library,Long> {
    ArrayList<Library> findAll();


}
