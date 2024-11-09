package com.example.hackathon_server.bookconnected.entity;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import java.sql.Time;

@Entity
@Setter
@Getter
@NoArgsConstructor
@AllArgsConstructor
public class Library {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long libraryId;

    @Column
    private String libraryName;

//    @Column
//    private String libraryLocation;

    @Column
    private Boolean isConnected;

    @Column
    private Double longitude;

    @Column
    private Double latitude;

    @Column
    private Time startTimeDay;

    @Column
    private Time endTimeDay;

    @Column
    private Time startTimeWeekend;

    @Column
    private Time endTimeWeekend;

    @Column
    private Time startTimeHoliday;

    @Column
    private Time endTimeHoliday;
}
