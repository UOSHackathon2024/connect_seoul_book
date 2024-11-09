package com.example.hackathon_server.bookconnected.controller;

import com.example.hackathon_server.bookconnected.entity.Library;
import com.example.hackathon_server.bookconnected.service.LibraryService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;

@RestController
@RequestMapping("/library")
public class LibraryController {

    @Autowired
    private LibraryService libraryService;

    @GetMapping("/all")
    public ResponseEntity<?> getLibraryAll() {
        ResponseEntity<?> response = libraryService.getLibraryAll();
        return response;
    }

    @GetMapping("/{id}")
    public ResponseEntity<?> getLibraryById(@PathVariable(name = "id") Long id) {
        ResponseEntity<?> response = libraryService.getLibraryById(id);
        return response;
    }

}
