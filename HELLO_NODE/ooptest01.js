var Animal = require('./animal.js')
var Human = require('./Human.js')
console.log(Animal)
const ani = new Animal();
ani.named("멍멍이");
console.log(ani.name);

const hum=new Human();
hum.named("전청조");
hum.goldspoon();
console.log(hum.name);
console.log(hum.asset);
