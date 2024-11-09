package com.example.hackathon_server.bookconnected.entity;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

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
}
