package com.example.hackathon_server.program.controller;

import com.example.hackathon_server.program.dto.CategoryRequestFrom;
import com.example.hackathon_server.program.service.ProgramService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.RequestEntity;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/program")
public class ProgramController {

    @Autowired
    private ProgramService programService;


    @GetMapping("/get/all")
    public ResponseEntity<?> getAllProgram() {
        ResponseEntity<?> response = programService.getAllProgram();
        return response;
    }

    @PostMapping("/get/category")
    public ResponseEntity<?> getProgramByCategory(@RequestBody CategoryRequestFrom form) {
        ResponseEntity<?> response = programService.getProgramByCategory(form);
        return response;
    }

    @GetMapping("/{id}")
    public ResponseEntity<?> getProgramById(@PathVariable(name = "id") Long id) {
        ResponseEntity<?> response = programService.getProgramById(id);
        return response;
    }
}
