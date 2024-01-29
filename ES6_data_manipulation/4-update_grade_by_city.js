export default function updateStudentGradeByCity(students, city, newGrades) {
  return students.filter(student => student.location === city).map(
    studentObj => {
      const data = newGrades.find(student => studentObj.id === student.studentId);
      if (data) {
        studentObj.grade = data.grade;
      } else {
        studentObj.grade = 'N/A';
      }
      return studentObj
    }
  )
}
