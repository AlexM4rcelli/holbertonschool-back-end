export default function updateStudentGradeByCity(students, city, newGrades) {
  return students
    .filter((student) => student.location === city)
    .map((studentObj) => {
      const data = newGrades.find((student) => studentObj.id === student.studentId);
      if (data) {
        return {...studentObj, grade: data.grade};
      } else {
        return {...studentObj, grade: 'N/A'};
      }
    });
}
