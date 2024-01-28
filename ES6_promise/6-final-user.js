import uploadPhoto from './5-photo-reject';
import signUpUser from './4-user-promise';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const promise1 = signUpUser(firstName, lastName, fileName);
  const promise2 = uploadPhoto(fileName);

  return Promise.allSettled([promise1, promise2])
    .then((results) => results.map((res) => ({
      status: res.status,
      value: res.value || res.reason.toString(),
    })));
}
