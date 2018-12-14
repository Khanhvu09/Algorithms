const grid = 20;
var path = 1;

for (i = 0; i < grid; i++) {
   path *= (2 * grid) - i;
   path /= i + 1;
}
console.log(path);

