export default function getStudentIdsSum(students) {
  return students.reduce((count, student) => {
    return count += student.id;
  }, 0);
}
