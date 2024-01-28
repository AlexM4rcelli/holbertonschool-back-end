import uploadPhoto from './5-photo-reject';
import signUpUser from './4-user-promise';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const promise1 = uploadPhoto(fileName);
  const promise2 = signUpUser(firstName, lastName, fileName);

  return Promise.all([promise1, promise2])
    .then((results) => results.map((result) => ({ status: 'fulfilled', value: result })))
    .catch((error) => ({ status: 'rejected', value: error.toString() }));
}
