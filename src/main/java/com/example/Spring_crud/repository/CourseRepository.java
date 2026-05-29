package com.example.Spring_crud.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.example.Spring_crud.entity.Course;

public interface CourseRepository extends JpaRepository<Course, Integer>{

}
