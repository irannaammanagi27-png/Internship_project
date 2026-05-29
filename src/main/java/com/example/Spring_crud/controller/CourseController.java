package com.example.Spring_crud.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import com.example.Spring_crud.entity.Course;
import com.example.Spring_crud.service.CourseService;

@RestController
@RequestMapping("/course")
public class CourseController {

    @Autowired
    CourseService cs;

    @PostMapping("/save")
    public String insert(@RequestBody Course c) {
        cs.insertCourse(c);
        return "data inserted";
    }

    @PostMapping("/saveAll")
    public String insertAllCourse(@RequestBody List<Course> c) {
        cs.insertAllEmp(c);
        return "data inserted";
    }

    @GetMapping("/fetch/{id}")
    public Course fetchById(@PathVariable int id) {
        return cs.fetchById(id);
    }

    @GetMapping("/fetchAll")
    public List<Course> fetchAllCourse() {
        return cs.fetchAllEmp();
    }

    @DeleteMapping("/delete/{id}")
    public String deleteById(@PathVariable int id) {

        Course c = cs.deleteById(id);

        return "data deleted";
    }

    @PutMapping("/update")
    public String updateCourse(@RequestBody Course c) {

        Course course = cs.updateEmp(c);

        return "data updated";
    }
}