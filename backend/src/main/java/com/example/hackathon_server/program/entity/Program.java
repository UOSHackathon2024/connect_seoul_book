package com.example.hackathon_server.program.entity;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import org.springframework.web.bind.annotation.GetMapping;

import java.util.Date;

@Setter
@Getter
@AllArgsConstructor
@NoArgsConstructor
@Entity
public class Program {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long programId;

    @Column
    private String programName;

    @Column
    private String libraryName;

    @Column
    private Date startProgram;

    @Column
    private Date endProgram;

    @Column
    private Date acceptProgram;

    @Column
    private Date acceptEnd;

    @Column
    private String category;

    @Column
    private String days;

    @Column
    private String clientType;

    @Column
    private String programPlace;

    @Column
    private String programInstructor;

    @Column
    private String imageUrl;
}
