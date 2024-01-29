export default function cleanSet(set, startString) {
  return Array.from(set)
  .filter(value => value.startsWith(startString) && startString)
  .map(value => {
    return value.slice(startString.length)
  })
  .join('-');
}
