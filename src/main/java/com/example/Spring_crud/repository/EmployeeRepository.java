package com.example.Spring_crud.repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.example.Spring_crud.entity.Employee;

public interface EmployeeRepository extends JpaRepository<Employee, Integer>{

}
