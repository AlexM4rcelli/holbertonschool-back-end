export default function cleanSet(set, startString) {
  if (!startString || !startString.length) return '';
  return Array.from(set)
  .filter(value => value.startsWith(startString))
  .map(value => {
    return value.slice(startString.length)
  })
  .join('-');
}
