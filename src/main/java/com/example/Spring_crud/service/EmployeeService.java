package com.example.Spring_crud.service;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.example.Spring_crud.entity.Employee;
import com.example.Spring_crud.repository.EmployeeRepository;

@Service
public class EmployeeService {

	
	@Autowired
	EmployeeRepository employeeRepository;
	
	public Employee insertEmp(Employee employee) {
		return employeeRepository.save(employee);
	}
	
	public List<Employee> insertAllEmp(List<Employee> employee){
		return employeeRepository.saveAll(employee);
	}
	
	public Employee fetchById(int id) {
		Optional<Employee> byId=employeeRepository.findById(id);
		if(byId.isPresent()) {
			return byId.get();
		}
		else {
			return null;
		}
	}

	public List<Employee> fetchAllEmp() {
		return employeeRepository.findAll();
	}
	
	public Employee deleteById(int id) {
		Optional<Employee> byId = employeeRepository.findById(id);
		if (byId.isPresent()) {
			employeeRepository.deleteById(id);
			return byId.get();
		} else {
			return null;
		}
	}
	
	public Employee updateEmp(Employee employee) {
		Optional<Employee> byId = employeeRepository.findById(employee.getId());
		if (byId.isPresent()) {
			return employeeRepository.save(employee);
		} else {
			return null;
		}
	}
       
	
	
}
