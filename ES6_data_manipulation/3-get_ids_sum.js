export default function getStudentIdsSum(students) {
  return students.reduce((count, student) => count + student.id, 0);
}
