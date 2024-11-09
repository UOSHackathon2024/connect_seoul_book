package com.example.hackathon_server.program.dto;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import java.util.ArrayList;

@Setter
@Getter
@NoArgsConstructor
@AllArgsConstructor
public class CategoryRequestFrom {

    private ArrayList<String> categorys;
}
