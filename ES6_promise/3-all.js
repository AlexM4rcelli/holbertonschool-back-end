import { uploadPhoto, createUser } from './utils.js';
export default function handleProfileSignup() {
  const promise1 = uploadPhoto();
  const promise2 = createUser();
  Promise.all([promise1, promise2])
    .then((results) => {
      let [result1, result2] = results;
      console.log(`${result1.body} ${result2.firstName} ${result2.lastName}`);
    })
}