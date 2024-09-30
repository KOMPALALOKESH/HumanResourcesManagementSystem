# Database Schema and Design Decisions for HRMS

## Overview
The HRMS (Human Resource Management System) application utilizes a straightforward database schema consisting of two primary tables: **Employee** and **Attendance**. This design aims to efficiently manage employee information and attendance records while ensuring flexibility for future enhancements.

## Employee Table
The **Employee** table is designed to store essential information about each employee in the organization. It includes the following fields:

- **name**: The name of the employee.
- **designation**: The job title or role of the employee.
- **department**: The department in which the employee works.
- **date_of_joining**: The date on which the employee joined the organization.

### Design Decisions
- The Employee table is structured to provide a clear representation of employee details, facilitating easy retrieval and management of employee data.
- Each field is chosen to capture relevant information that can be used for various HR functions, such as reporting and analytics.

## Attendance Table
The **Attendance** table is responsible for tracking the attendance records of employees. It contains the following fields:

- **employee**: A foreign key that references the Employee table, indicating which employee is marked for attendance.
- **date**: The date for which the attendance is recorded.
- **status**: The status of the attendance, which can be 'Present', 'Absent', or any other custom status.

### Design Decisions
- The use of a foreign key in the Attendance table ensures that each attendance record is directly linked to a specific employee, allowing for straightforward data retrieval and management.
- The **status** field is designed to be flexible, accommodating various attendance scenarios, such as different types of leaves or special cases.

## Overall Design Philosophy
The database schema is intentionally kept simple and clear, with a focus on separation of concerns. The Employee table handles employee information, while the Attendance table manages attendance records. This design approach not only simplifies data management but also allows for future scalability and enhancements as the HRMS application evolves.

By maintaining a straightforward schema, the HRMS application can efficiently support its core functionalities while providing a solid foundation for potential future features.
