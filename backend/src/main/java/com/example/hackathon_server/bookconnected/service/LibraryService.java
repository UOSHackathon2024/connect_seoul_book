package com.example.hackathon_server.bookconnected.service;

import com.example.hackathon_server.bookconnected.entity.Library;
import com.example.hackathon_server.bookconnected.repository.LibraryRepository;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.RequestBody;

import java.sql.Time;
import java.time.DayOfWeek;
import java.time.LocalDate;
import java.time.LocalTime;
import java.util.*;

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
            Map<String, Object> data = new HashMap<>();
            data.put("library_info",library);

            LocalDate today = LocalDate.now();
            LocalTime now = LocalTime.now();

            LocalTime startTime;
            LocalTime endTime;

            if(isWeekend(today)) {
                //주말 로직
                startTime = library.getStartTimeWeekend().toLocalTime();
                endTime = library.getEndTimeWeekend().toLocalTime();
            }
            else {
                //평일 로직
                startTime = library.getStartTimeDay().toLocalTime();
                endTime = library.getEndTimeDay().toLocalTime();
            }

            if (!now.isBefore(startTime) && !now.isAfter(endTime)) {
                data.put("isStatus","운영중");
            }
            else {
                data.put("isStatus","운영종료");
            }

            return ResponseEntity.ok(data);
        }
    }

    public boolean isWeekend(LocalDate date) {
        DayOfWeek dayOfWeek = date.getDayOfWeek();
        return dayOfWeek == DayOfWeek.SATURDAY || dayOfWeek == DayOfWeek.SUNDAY;
    }
}
