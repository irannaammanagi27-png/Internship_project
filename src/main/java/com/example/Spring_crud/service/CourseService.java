package com.example.Spring_crud.service;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.example.Spring_crud.entity.Course;
import com.example.Spring_crud.repository.CourseRepository;

@Service
public class CourseService {

    @Autowired
    CourseRepository courseRepository;

    public Course insertCourse(Course course) {

        return courseRepository.save(course);
    }

    public List<Course> insertAllEmp(List<Course> course) {

        return courseRepository.saveAll(course);
    }

    public Course fetchById(int id) {

        Optional<Course> byId =
                courseRepository.findById(id);

        if (byId.isPresent()) {
            return byId.get();
        } else {
            return null;
        }
    }

    public List<Course> fetchAllEmp() {

        return courseRepository.findAll();
    }

    public Course deleteById(int id) {

        Optional<Course> byId =
                courseRepository.findById(id);

        if (byId.isPresent()) {

            courseRepository.deleteById(id);

            return byId.get();
        } else {
            return null;
        }
    }

    public Course updateEmp(Course course) {

        Optional<Course> byId =
                courseRepository.findById(course.getId());

        if (byId.isPresent()) {

            return courseRepository.save(course);

        } else {
            return null;
        }
    }
}