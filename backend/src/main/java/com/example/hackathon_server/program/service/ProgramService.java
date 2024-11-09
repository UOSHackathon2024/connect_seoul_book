package com.example.hackathon_server.program.service;

import com.example.hackathon_server.program.dto.CategoryRequestFrom;
import com.example.hackathon_server.program.entity.Program;
import com.example.hackathon_server.program.repository.ProgramRepository;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatusCode;
import org.springframework.http.RequestEntity;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.ZoneId;
import java.time.ZonedDateTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Objects;

@Service
@Slf4j
public class ProgramService {

    @Autowired
    private ProgramRepository programRepository;

    public ResponseEntity<?> getProgramByCategory(CategoryRequestFrom form) {
        ArrayList<String> categoryList = form.getCategorys();
        ArrayList<Program> programsList = new ArrayList<>();
        ArrayList<Map<String, Object>> data = new ArrayList<>();

        //프로그램 카테고리 별로 다 추가
        for(int i=0; i< categoryList.size();i++) {
            ArrayList<Program> programs = programRepository.getByCategoryContaining(categoryList.get(i));
            if(programs==null) {
                continue;
            }
            else {
                for(int j=0; j<programs.size();j++) {
                    programsList.add(programs.get(j));
                }
            }
        }

        for(int i=0;i < programsList.size();i++) {
            Map<String,Object> programInfo = new HashMap<>();
            Program program = programsList.get(i);
            programInfo.put("program",program);

            ZonedDateTime nowInKST = ZonedDateTime.now(ZoneId.of("Asia/Seoul"));
            LocalDate today = nowInKST.toLocalDate();

            LocalDate startDate = program.getStartProgram().toInstant()
                    .atZone(ZoneId.of("Asia/Seoul"))
                    .toLocalDate();

            LocalDate endDate = program.getEndProgram().toInstant()
                    .atZone(ZoneId.of("Asia/Seoul"))
                    .toLocalDate();

            if (today.isBefore(startDate)) {
                programInfo.put("status","모임전");
            }
            else if(today.isAfter(endDate)) {
                programInfo.put("status","모임후");
            }
            else {
                programInfo.put("status","모임중");
            }

            data.add(programInfo);
        }

        return ResponseEntity.ok(data);
    }

    public ResponseEntity<?> getProgramById(Long id) {
        Program program = programRepository.findById(id).orElse(null);
        if(program==null) {
            return new ResponseEntity<>("프로그램 없음", HttpStatusCode.valueOf(400));
        }

        return ResponseEntity.ok(program);
    }

    public ResponseEntity<?> getAllProgram() {
        ArrayList<Program> programs = programRepository.findAll();
        return ResponseEntity.ok(programs);
    }
}
