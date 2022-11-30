#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  function occurs (count, current) {
    return (current === searchElement ? count + 1 : count);
  }
  return list.reduce(occurs, 0);
};
