export default function createReportObject(employeesList) {
  return {
    'allEmployees': {...employeesList},

    getNumberOfDepartments() {
      let count = 0;
      for (let key in this){
        count += 1;
      }
      return count
    }
  };
}