package com.example.hackathon_server.bookconnected.service;

import com.example.hackathon_server.bookconnected.entity.Library;
import com.example.hackathon_server.bookconnected.repository.LibraryRepository;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.RequestBody;

import java.util.ArrayList;

@Slf4j
@Service
public class LibraryService {

    @Autowired
    private LibraryRepository libraryRepository;

    public ResponseEntity<?> getLibraryAll() {
        ArrayList<Library> libraries = libraryRepository.findAll();
        log.info("도서관 개수: "+String.valueOf(libraries.size()));
        return ResponseEntity.ok(libraries);

    }

    public ResponseEntity<?> getLibraryById(Long id) {
        Library library = libraryRepository.findById(id).orElse(null);
        if(library==null) {
            return new ResponseEntity<>("없음", HttpStatus.valueOf(400));
        }
        else {
            return ResponseEntity.ok(library);
        }
    }
}
