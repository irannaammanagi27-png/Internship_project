package com.example.Spring_crud.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import com.example.Spring_crud.entity.Employee;
import com.example.Spring_crud.service.EmployeeService;

@RestController
public class EmployeeController {

    @Autowired
    EmployeeService es;

    @PostMapping("/save")
    public String insert(@RequestBody Employee e) {
        es.insertEmp(e);
        return "data inserted";
    }

    @PostMapping("/saveAll")
    public String insertAllEmp(@RequestBody List<Employee> e) {
        es.insertAllEmp(e);
        return "data inserted";
    }

    @GetMapping("/fetch/{id}")
    public Employee fetchById(@PathVariable int id) {
        return es.fetchById(id);
    }
 
    @GetMapping("/fetchAll")
	public List<Employee> fetchAllEmp() {
		return es.fetchAllEmp();
	}
    @DeleteMapping("/delete/{id}")
	public String deleteById(@PathVariable int id) {
    	Employee e=es.deleteById(id);
		return "data deleted";
	}
    
    @PutMapping("/update")
        public String updateEmp(@RequestBody Employee e) {
    	Employee emp=es.updateEmp(e);
    
        return "data updated";
    }
}